"""Embed real TrueType fonts in rendered PDFs so applicant tracking systems
extract text correctly.

The base-14 PDF fonts (Helvetica, Times) are not embedded and carry no
ToUnicode map, so some ATS parsers mis-decode non-ASCII glyphs: the bullet
"•" came through Workday-style systems as "&#127;" and "(~94%)" as "- 94% ."
Liberation Sans / Liberation Serif are metric-compatible with Helvetica /
Times (same layout, same page breaks) and ReportLab embeds them with a proper
ToUnicode CMap. Font files live in build/fonts (SIL OFL 1.1, see
OFL-LICENSE.txt). If they're missing, fall back to the base-14 names.
"""
import os

_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts")
_FAMILIES = {
    "Helvetica": ("LiberationSans", {"Helvetica": "Regular", "Helvetica-Bold": "Bold",
                                     "Helvetica-Oblique": "Italic"}),
    "Times": ("LiberationSerif", {"Times-Roman": "Regular", "Times-Bold": "Bold",
                                  "Times-Italic": "Italic"}),
}


def embedded(base14_name):
    """Return the name of a registered, embeddable TTF matching a base-14 font
    name, registering it on first use. Unknown names are returned unchanged."""
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    for fam, (ttf_family, styles) in _FAMILIES.items():
        if base14_name in styles:
            reg_name = "%s-%s" % (ttf_family, styles[base14_name])
            if reg_name in pdfmetrics.getRegisteredFontNames():
                return reg_name
            path = os.path.join(_DIR, reg_name + ".ttf")
            if not os.path.exists(path):
                return base14_name
            pdfmetrics.registerFont(TTFont(reg_name, path))
            return reg_name
    return base14_name
