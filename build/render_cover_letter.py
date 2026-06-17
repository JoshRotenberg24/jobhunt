#!/usr/bin/env python3
"""
render_cover_letter.py — build a professional, ATS-safe one-page cover letter.

Outputs <base>.pdf (ReportLab) and <base>.docx (python-docx), matching the resume
letterhead. Warns if it exceeds one page.

JSON schema:
{
  "name": "Joshua Rotenberg",
  "contact": {"location":"","phone":"","email":"","linkedin":""},
  "date": "June 17, 2026",
  "company": "Acme Inc.",
  "role": "Revenue Operations Manager",
  "recipient": "Hiring Team",          # optional
  "salutation": "Dear Hiring Team,",   # optional; derived from recipient if omitted
  "body": ["paragraph one", "paragraph two", "paragraph three"],
  "closing": "Sincerely,"              # optional
}

Usage:  python3 build/render_cover_letter.py <cover-letter.json>
"""
import json, os, sys

NAVY = (0x16, 0x3a, 0x5f); INK = (0x1a, 0x1a, 0x1a); MUTED = (0x55, 0x55, 0x55)
MARGIN_TB_IN = 0.8; MARGIN_LR_IN = 0.9; BODY_PT = 10.8


def build_pdf(data, path):
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.units import inch
    from reportlab.lib.colors import Color
    from reportlab.lib.enums import TA_CENTER, TA_LEFT
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                    Spacer, HRFlowable)
    navy = Color(*[c/255 for c in NAVY]); ink = Color(*[c/255 for c in INK])
    muted = Color(*[c/255 for c in MUTED])
    pw, ph = letter; ml = MARGIN_LR_IN*inch; mt = MARGIN_TB_IN*inch
    usable = pw-2*ml; frameH = ph-2*mt

    name_st = ParagraphStyle("n", fontName="Helvetica-Bold", fontSize=18, textColor=navy,
                             alignment=TA_CENTER, leading=21, spaceAfter=1)
    contact_st = ParagraphStyle("c", fontName="Helvetica", fontSize=9, textColor=muted,
                                alignment=TA_CENTER, leading=12, spaceAfter=2)
    body = ParagraphStyle("b", fontName="Helvetica", fontSize=BODY_PT, textColor=ink,
                          leading=BODY_PT+4, spaceAfter=8, alignment=TA_LEFT)
    tight = ParagraphStyle("t", fontName="Helvetica", fontSize=BODY_PT, textColor=ink,
                           leading=BODY_PT+3, spaceAfter=2)

    c = data.get("contact", {})
    bits = [c.get("location"), c.get("phone"), c.get("email"), c.get("linkedin")]
    sal = data.get("salutation") or ("Dear %s," % data.get("recipient", "Hiring Team"))

    story = [Paragraph(data["name"], name_st),
             Paragraph("&nbsp;&nbsp;&bull;&nbsp;&nbsp;".join(b for b in bits if b), contact_st),
             HRFlowable(width="100%", thickness=0.7, color=navy, spaceBefore=2, spaceAfter=10)]
    if data.get("date"):
        story.append(Paragraph(data["date"], tight)); story.append(Spacer(1, 6))
    if data.get("company"):
        story.append(Paragraph("<b>%s</b>" % data["company"], tight))
    if data.get("role"):
        story.append(Paragraph("Re: %s" % data["role"], tight))
    story.append(Spacer(1, 8))
    story.append(Paragraph(sal, body))
    for para in data.get("body", []):
        story.append(Paragraph(para, body))
    story.append(Spacer(1, 4))
    story.append(Paragraph(data.get("closing", "Sincerely,"), tight))
    story.append(Spacer(1, 14))
    story.append(Paragraph(data["name"], tight))

    class _Doc(BaseDocTemplate):
        _last_page = 1
        def afterFlowable(self, f): self._last_page = self.canv.getPageNumber()
    doc = _Doc(path, pagesize=letter, leftMargin=ml, rightMargin=ml,
               topMargin=mt, bottomMargin=mt)
    doc.addPageTemplates([PageTemplate(id="m", frames=[Frame(ml, mt, usable, frameH,
                          leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)])])
    doc.build(story)
    return doc._last_page


def build_docx(data, path):
    from docx import Document
    from docx.shared import Pt, Inches, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.oxml.ns import qn
    ink = RGBColor(*INK); navy = RGBColor(*NAVY); muted = RGBColor(*MUTED)
    doc = Document()
    st = doc.styles["Normal"]; st.font.name = "Calibri"; st.font.size = Pt(BODY_PT)
    st.font.color.rgb = ink
    rf = st.element.get_or_add_rPr().get_or_add_rFonts()
    for a in ("w:ascii", "w:hAnsi", "w:cs"): rf.set(qn(a), "Calibri")
    st.paragraph_format.line_spacing = 1.08
    s = doc.sections[0]
    s.top_margin = s.bottom_margin = Inches(MARGIN_TB_IN)
    s.left_margin = s.right_margin = Inches(MARGIN_LR_IN)

    def para(text, *, align=None, bold=False, size=None, color=None, after=8):
        p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(after)
        if align is not None: p.alignment = align
        r = p.add_run(text); r.bold = bold; r.font.name = "Calibri"
        if size: r.font.size = Pt(size)
        r.font.color.rgb = color or ink
        return p

    para(data["name"], align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, size=18, color=navy, after=1)
    c = data.get("contact", {})
    bits = [c.get("location"), c.get("phone"), c.get("email"), c.get("linkedin")]
    para("  •  ".join(b for b in bits if b), align=WD_ALIGN_PARAGRAPH.CENTER, size=9,
         color=muted, after=10)
    if data.get("date"): para(data["date"], after=6)
    if data.get("company"): para(data["company"], bold=True, after=1)
    if data.get("role"): para("Re: " + data["role"], after=8)
    para(data.get("salutation") or ("Dear %s," % data.get("recipient", "Hiring Team")), after=8)
    for b in data.get("body", []): para(b, after=8)
    para(data.get("closing", "Sincerely,"), after=14)
    para(data["name"])
    doc.save(path)


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: render_cover_letter.py <cover-letter.json>")
    spec = sys.argv[1]; data = json.load(open(spec))
    base = os.path.splitext(os.path.abspath(spec))[0]
    build_docx(data, base + ".docx"); print("DOCX: %s" % (base + ".docx"))
    try:
        pages = build_pdf(data, base + ".pdf")
        print("PDF:  %s" % (base + ".pdf"))
        print("PAGES=%d  -> %s" % (pages, "OK" if pages == 1 else "TRIM to one page"))
    except Exception as e:
        print("PDF build failed: %s" % e)


if __name__ == "__main__":
    main()
