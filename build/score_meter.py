#!/usr/bin/env python3
"""
score_meter.py — render an Application Priority Score "meter" for the tool's UI.

The score is an internal, evidence-based decision aid for the candidate. It is not a
prediction of an employer's ATS score, match category, or interview decision.

Produces:
  1) a PNG gauge (band-colored bar + marker, optional per-dimension breakdown bars), and
  2) an inline text meter printed to stdout (drops straight into the chat / match report).

Input JSON (fit.json):
{
  "score": 80,
  "band": "Strong fit",                       # optional; auto-derived from score if omitted
  "role": "Revenue Operations Manager",        # optional, shown as subtitle
  "breakdown": [                               # optional
    ["Must-have requirements met", 33, 40],
    ["Seniority & scope alignment", 12, 15],
    ["Domain / industry alignment", 13, 15],
    ["Differentiators", 13, 15],
    ["Evidence strength", 9, 15]
  ]
}

Usage:  python3 build/score_meter.py <fit.json> [out.png]
"""
import json, os, sys

# band thresholds -> (label, strong color, pale zone color)
BANDS = [
    (0,  "Likely not a fit", (0.80, 0.22, 0.22), (0.97, 0.90, 0.90)),
    (40, "Long shot",        (0.91, 0.62, 0.10), (0.99, 0.95, 0.86)),
    (60, "Solid stretch",    (0.10, 0.45, 0.75), (0.90, 0.94, 0.99)),
    (80, "Strong fit",       (0.15, 0.62, 0.35), (0.89, 0.96, 0.91)),
]


_SUBS = {"—": "-", "–": "-", "‒": "-", "‐": "-", "‘": "'",
         "’": "'", "“": '"', "”": '"', "•": "*", "…": "...",
         "→": "->", "·": "-", " ": " "}


def _san(s):
    """PyMuPDF base fonts only cover Latin-1; map common unicode punctuation to ASCII
    so em-dashes/bullets/curly-quotes don't render as a fallback dot."""
    s = str(s)
    for k, v in _SUBS.items():
        s = s.replace(k, v)
    return s.encode("latin-1", "replace").decode("latin-1")


def band_for(score):
    b = BANDS[0]
    for t in BANDS:
        if score >= t[0]:
            b = t
    return b  # (threshold, label, color, pale)


def text_meter(score, label):
    emoji = {"Likely not a fit": "🔴", "Long shot": "🟡",
             "Solid stretch": "🔵", "Strong fit": "🟢"}.get(label, "⚪")
    filled = round(score / 5.0)
    bar = "█" * filled + "░" * (20 - filled)
    return ("%s Application Priority Score: %d / 100 — %s\n[%s]  %d%%\nInternal decision aid — not a prediction of any employer's score or decision."
            % (emoji, score, label, bar, score))


def render_png(data, out):
    import fitz
    score = max(0, min(100, int(round(data["score"]))))
    _, auto_label, color, _ = band_for(score)
    label = _san(data.get("band") or auto_label)
    role = _san(data["role"]) if data.get("role") else None
    bd = [(_san(n), v, m) for (n, v, m) in (data.get("breakdown") or [])]

    W = 720
    pad = 36
    bar_x0, bar_x1 = pad, W - pad
    bar_w = bar_x1 - bar_x0
    bar_y0, bar_h = 150, 30
    H = bar_y0 + bar_h + 44 + (len(bd) * 26 + 16 if bd else 0)

    d = fitz.open()
    pg = d.new_page(width=W, height=H)
    pg.draw_rect(fitz.Rect(0, 0, W, H), color=None, fill=(1, 1, 1))

    ink = (0.10, 0.10, 0.10); muted = (0.45, 0.45, 0.45)
    pg.insert_text((pad, 40), "APPLICATION PRIORITY SCORE", fontsize=12, fontname="hebo", color=muted)
    if role:
        pg.insert_text((pad, 58), role, fontsize=10.5, fontname="helv", color=muted)

    # big number + band label
    pg.insert_text((pad, 112), str(score), fontsize=52, fontname="hebo", color=color)
    num_w = fitz.get_text_length(str(score), fontname="hebo", fontsize=52)
    pg.insert_text((pad + num_w + 6, 112), "/100", fontsize=20, fontname="helv", color=muted)
    pg.insert_text((pad + num_w + 70, 112), label, fontsize=22, fontname="hebo", color=color)

    # zones (pale band backgrounds across the track)
    edges = [0, 40, 60, 80, 100]
    for i in range(4):
        x0 = bar_x0 + bar_w * edges[i] / 100.0
        x1 = bar_x0 + bar_w * edges[i + 1] / 100.0
        pale = BANDS[i][3]
        pg.draw_rect(fitz.Rect(x0, bar_y0, x1, bar_y0 + bar_h), color=None, fill=pale)
    # progress fill 0 -> score in band color
    fx = bar_x0 + bar_w * score / 100.0
    pg.draw_rect(fitz.Rect(bar_x0, bar_y0, fx, bar_y0 + bar_h), color=None, fill=color)
    # track border
    pg.draw_rect(fitz.Rect(bar_x0, bar_y0, bar_x1, bar_y0 + bar_h),
                 color=(0.75, 0.75, 0.75), width=0.8)
    # marker at the score
    pg.draw_line(fitz.Point(fx, bar_y0 - 6), fitz.Point(fx, bar_y0 + bar_h + 6),
                 color=(0.12, 0.12, 0.12), width=1.6)
    pg.draw_circle(fitz.Point(fx, bar_y0 - 8), 4, color=(0.12, 0.12, 0.12),
                   fill=(0.12, 0.12, 0.12))
    # tick labels
    for e in edges:
        tx = bar_x0 + bar_w * e / 100.0
        s = str(e)
        tw = fitz.get_text_length(s, fontname="helv", fontsize=8)
        pg.insert_text((tx - tw / 2, bar_y0 + bar_h + 16), s, fontsize=8,
                       fontname="helv", color=muted)

    # optional breakdown bars
    if bd:
        y = bar_y0 + bar_h + 40
        lbl_w = 230
        mb_x0 = pad + lbl_w
        mb_x1 = W - pad - 52
        mb_w = mb_x1 - mb_x0
        for name, val, mx in bd:
            frac = (val / mx) if mx else 0
            pg.insert_text((pad, y + 9), name, fontsize=9.5, fontname="helv", color=ink)
            pg.draw_rect(fitz.Rect(mb_x0, y, mb_x1, y + 11), color=None, fill=(0.91, 0.91, 0.91))
            pg.draw_rect(fitz.Rect(mb_x0, y, mb_x0 + mb_w * frac, y + 11), color=None, fill=color)
            pg.insert_text((mb_x1 + 8, y + 9), "%d/%d" % (val, mx), fontsize=9,
                           fontname="hebo", color=muted)
            y += 26

    pg.get_pixmap(dpi=150).save(out)
    return label


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: score_meter.py <fit.json> [out.png]")
    spec = sys.argv[1]
    data = json.load(open(spec))
    out = sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(spec)[0] + ".png"
    score = max(0, min(100, int(round(data["score"]))))
    label = data.get("band") or band_for(score)[1]
    try:
        label = render_png(data, out)
        print("METER: %s" % out)
    except Exception as e:
        print("PNG render failed: %s" % e)
    print(text_meter(score, label))


if __name__ == "__main__":
    main()
