#!/usr/bin/env python3
"""
render_resume.py — build a professional, ATS-safe, balanced 2-page resume.

Outputs (same dir/basename as the input JSON):
  - <base>.pdf   ReportLab, real selectable text (ATS-safe), EXACT pagination.
  - <base>.docx  python-docx, native editable Word (ATS-preferred submission).

Prints a report the caller uses to enforce the "balanced 2 pages" rule:
  PAGES=<n>  LAST_PAGE_FILL=<0..1>  -> <verdict>

Design (see research/ + ats-playbook.md): single column, standard headings, real
text (no images), clean type hierarchy. Looks professional AND parses cleanly.

JSON schema:
{
  "name": "...", "headline": "...(optional honest self-description)...",
  "contact": {"location":"","phone":"","email":"","linkedin":""},
  "summary": "...",
  "experience": [{"title":"","company":"","location":"","dates":"","bullets":["",""]}],
  "competencies": [{"category":"","items":["",""]}],
  "education": ["..."], "certifications": ["..."]
}

Usage:  python3 build/render_resume.py <resume.json>
"""
import json, os, sys

# ---------- shared style constants -------------------------------------------
FONT_MAIN = "Helvetica"          # ATS-standard, clean, professional
NAVY      = (0x16, 0x3a, 0x5f)
INK       = (0x1a, 0x1a, 0x1a)
MUTED     = (0x55, 0x55, 0x55)
MARGIN_TB_IN = 0.5
MARGIN_LR_IN = 0.6
BODY_PT   = 10.3


def _esc(s):
    """Escape data for ReportLab's mini-XML parser (prevents markup injection,
    entity corruption like 'R&D'->'R&D;', and silent drops of <word> patterns)."""
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# ============================ PDF (ReportLab) ================================
def build_pdf(data, path):
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.units import inch
    from reportlab.lib.colors import Color
    from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                    Spacer, Table, TableStyle, HRFlowable, KeepTogether)

    navy = Color(*[c / 255 for c in NAVY]); ink = Color(*[c / 255 for c in INK])
    muted = Color(*[c / 255 for c in MUTED])
    pw, ph = letter
    ml = MARGIN_LR_IN * inch; mt = MARGIN_TB_IN * inch
    usable = pw - 2 * ml; frameH = ph - 2 * mt

    name_st = ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=21,
                             textColor=navy, alignment=TA_CENTER, spaceAfter=1, leading=24)
    head_st = ParagraphStyle("head", fontName="Helvetica", fontSize=11.5,
                             textColor=muted, alignment=TA_CENTER, spaceAfter=2, leading=14)
    contact_st = ParagraphStyle("contact", fontName="Helvetica", fontSize=9,
                                textColor=muted, alignment=TA_CENTER, spaceAfter=2, leading=12)
    sec_st = ParagraphStyle("sec", fontName="Helvetica-Bold", fontSize=10.5,
                            textColor=navy, spaceBefore=8, spaceAfter=1, leading=13)
    body_st = ParagraphStyle("body", fontName=FONT_MAIN, fontSize=BODY_PT,
                             textColor=ink, leading=BODY_PT + 3, spaceAfter=2, alignment=TA_LEFT)
    role_l = ParagraphStyle("role_l", fontName="Helvetica-Bold", fontSize=10.5,
                            textColor=ink, leading=13)
    role_r = ParagraphStyle("role_r", fontName="Helvetica", fontSize=9,
                            textColor=muted, alignment=TA_RIGHT, leading=13)
    loc_st = ParagraphStyle("loc", fontName="Helvetica-Oblique", fontSize=9,
                            textColor=muted, leading=11, spaceAfter=1)
    bullet_st = ParagraphStyle("bul", fontName=FONT_MAIN, fontSize=BODY_PT, textColor=ink,
                               leading=BODY_PT + 3, leftIndent=11, bulletIndent=0,
                               spaceAfter=1.5)

    def rule():
        return HRFlowable(width="100%", thickness=0.7, color=navy,
                          spaceBefore=1, spaceAfter=3, lineCap="round")

    def section(title):
        return [Paragraph(title.upper(), sec_st), rule()]

    def role_header(job):
        left = Paragraph("<b>%s</b>&nbsp;&nbsp;|&nbsp;&nbsp;<font color='#163a5f'>%s</font>"
                         % (_esc(job["title"]), _esc(job.get("company", ""))), role_l)
        right = Paragraph(_esc(job.get("dates", "")), role_r)
        t = Table([[left, right]], colWidths=[usable * 0.72, usable * 0.28])
        t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                               ("LEFTPADDING", (0, 0), (-1, -1), 0),
                               ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                               ("TOPPADDING", (0, 0), (-1, -1), 0),
                               ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
        return t

    def make_story():
        s = [Paragraph(_esc(data["name"]), name_st)]
        if data.get("headline"):
            s.append(Paragraph(_esc(data["headline"]), head_st))
        c = data.get("contact", {})
        bits = [c.get("location"), c.get("phone"), c.get("email"), c.get("linkedin")]
        s.append(Paragraph("&nbsp;&nbsp;&bull;&nbsp;&nbsp;".join(_esc(b) for b in bits if b), contact_st))

        if data.get("summary"):
            s += section("Summary")
            s.append(Paragraph(_esc(data["summary"]), body_st))

        if data.get("experience"):
            s += section("Professional Experience")
            for job in data["experience"]:
                head = [role_header(job)]
                if job.get("location"):
                    head.append(Paragraph(_esc(job["location"]), loc_st))
                bl = job.get("bullets", [])
                first = [Paragraph(_esc(bl[0]), bullet_st, bulletText="•")] if bl else []
                s.append(KeepTogether(head + first))
                for b in bl[1:]:
                    s.append(Paragraph(_esc(b), bullet_st, bulletText="•"))
                s.append(Spacer(1, 3))

        if data.get("competencies"):
            s += section("Core Competencies")
            for g in data["competencies"]:
                s.append(Paragraph("<b>%s:</b>&nbsp;&nbsp;%s"
                                   % (_esc(g["category"]), ", ".join(_esc(i) for i in g["items"])), body_st))

        if data.get("education"):
            s += section("Education")
            for ln in data["education"]:
                s.append(Paragraph(_esc(ln), body_st))
        if data.get("certifications"):
            s += section("Certifications")
            for ln in data["certifications"]:
                s.append(Paragraph(_esc(ln), body_st))
        return s

    frame_top = mt + frameH

    class _Doc(BaseDocTemplate):
        _last_page = 1
        _last_y = mt
        def afterFlowable(self, flowable):
            self._last_page = self.canv.getPageNumber()
            try:
                self._last_y = self.frame._y      # layout cursor after this flowable
            except Exception:
                pass

    doc = _Doc(path, pagesize=letter, leftMargin=ml, rightMargin=ml,
               topMargin=mt, bottomMargin=mt, title="Resume")
    doc.addPageTemplates([PageTemplate(id="main",
                          frames=[Frame(ml, mt, usable, frameH, id="f",
                                        leftPadding=0, rightPadding=0,
                                        topPadding=0, bottomPadding=0)])])
    doc.build(make_story())
    pages = doc._last_page
    used_last = frame_top - doc._last_y          # height consumed on the final page
    last_fill = used_last / frameH
    return pages, max(0.0, min(1.0, last_fill))


# ============================ DOCX (python-docx) =============================
def build_docx(data, path):
    from docx import Document
    from docx.shared import Pt, Inches, RGBColor
    from docx.enum.text import WD_TAB_ALIGNMENT, WD_ALIGN_PARAGRAPH
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement

    ink = RGBColor(*INK); navy = RGBColor(*NAVY); muted = RGBColor(*MUTED)

    def run(p, text, *, bold=False, italic=False, size=None, color=None, caps=False):
        r = p.add_run(text); r.bold = bold; r.italic = italic
        if size: r.font.size = Pt(size)
        r.font.color.rgb = color or ink; r.font.name = "Calibri"
        if caps: r.font.all_caps = True
        return r

    def bottom_border(p):
        pPr = p._p.get_or_add_pPr(); pbdr = OxmlElement("w:pBdr")
        b = OxmlElement("w:bottom")
        b.set(qn("w:val"), "single"); b.set(qn("w:sz"), "6")
        b.set(qn("w:space"), "2"); b.set(qn("w:color"), "163a5f")
        pbdr.append(b); pPr.append(pbdr)

    def section(title):
        p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(7)
        p.paragraph_format.space_after = Pt(3)
        run(p, title.upper(), bold=True, size=10.5, color=navy, caps=True)
        bottom_border(p)

    doc = Document()
    st = doc.styles["Normal"]; st.font.name = "Calibri"; st.font.size = Pt(BODY_PT)
    st.font.color.rgb = ink
    rpr = st.element.get_or_add_rPr(); rf = rpr.get_or_add_rFonts()
    for a in ("w:ascii", "w:hAnsi", "w:cs"): rf.set(qn(a), "Calibri")
    st.paragraph_format.line_spacing = 1.04
    st.paragraph_format.space_after = Pt(0)
    sec = doc.sections[0]
    sec.top_margin = sec.bottom_margin = Inches(MARGIN_TB_IN)
    sec.left_margin = sec.right_margin = Inches(MARGIN_LR_IN)
    usable = (sec.page_width - sec.left_margin - sec.right_margin) / 914400.0

    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(1)
    run(p, data["name"], bold=True, size=21, color=navy)
    if data.get("headline"):
        h = doc.add_paragraph(); h.alignment = WD_ALIGN_PARAGRAPH.CENTER
        h.paragraph_format.space_after = Pt(2); run(h, data["headline"], size=11.5, color=muted)
    c = data.get("contact", {})
    bits = [c.get("location"), c.get("phone"), c.get("email"), c.get("linkedin")]
    cp = doc.add_paragraph(); cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cp.paragraph_format.space_after = Pt(4)
    run(cp, "  •  ".join(b for b in bits if b), size=9, color=muted)

    if data.get("summary"):
        section("Summary"); p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(2)
        run(p, data["summary"])

    if data.get("experience"):
        section("Professional Experience")
        for job in data["experience"]:
            p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(4)
            p.paragraph_format.space_after = Pt(1)
            p.paragraph_format.tab_stops.add_tab_stop(Inches(usable), WD_TAB_ALIGNMENT.RIGHT)
            run(p, job["title"], bold=True, size=10.5, color=ink)
            if job.get("company"): run(p, "  |  " + job["company"], size=10.5, color=navy)
            run(p, "\t" + job.get("dates", ""), size=9, color=muted)
            if job.get("location"):
                sp = doc.add_paragraph(); sp.paragraph_format.space_after = Pt(1)
                run(sp, job["location"], italic=True, size=9, color=muted)
            for b in job.get("bullets", []):
                bp = doc.add_paragraph(); pf = bp.paragraph_format
                pf.left_indent = Inches(0.18); pf.first_line_indent = Inches(-0.18)
                pf.space_after = Pt(1.5)
                run(bp, "•  ", color=navy); run(bp, b)

    if data.get("competencies"):
        section("Core Competencies")
        for g in data["competencies"]:
            p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(1.5)
            run(p, g["category"] + ":  ", bold=True); run(p, ", ".join(g["items"]))

    for title, key in (("Education", "education"), ("Certifications", "certifications")):
        if data.get(key):
            section(title)
            for ln in data[key]:
                p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(1.5); run(p, ln)

    doc.save(path)


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: render_resume.py <resume.json>")
    spec = sys.argv[1]; data = json.load(open(spec))
    base = os.path.splitext(os.path.abspath(spec))[0]
    pdf_path, docx_path = base + ".pdf", base + ".docx"

    build_docx(data, docx_path)
    print("DOCX: %s" % docx_path)
    try:
        pages, fill = build_pdf(data, pdf_path)
        print("PDF:  %s" % pdf_path)
        if pages == 2 and fill >= 0.6:
            verdict = "OK — balanced 2 pages"
        elif pages < 2:
            verdict = "ONLY %d PAGE — add depth/bullets to reach a full, balanced 2 pages" % pages
        elif pages == 2:
            verdict = "PAGE 2 SPARSE (fill %.2f) — add depth, or trim to a tight 1 page" % fill
        else:
            verdict = "TOO LONG (%d pages) — trim least-relevant bullets to 2 pages" % pages
        print("PAGES=%d  LAST_PAGE_FILL=%.2f  -> %s" % (pages, fill, verdict))
    except Exception as e:
        print("PDF build failed: %s" % e)
        print("PAGES=?  (open the .docx to verify pagination)")


if __name__ == "__main__":
    main()
