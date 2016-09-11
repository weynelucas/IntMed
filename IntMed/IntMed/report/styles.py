from reportlab.pdfbase         import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums       import TA_CENTER, TA_JUSTIFY
from reportlab.lib.units       import mm
from reportlab.lib             import colors
from reportlab.platypus        import TableStyle
from reportlab.lib.styles      import getSampleStyleSheet, ParagraphStyle
from IntMed.settings   import STATIC_ROOT

# Load fonts
pdfmetrics.registerFont(TTFont('Type Writer',             STATIC_ROOT + '/fonts/cmuntt.ttf'))
pdfmetrics.registerFont(TTFont('Type Writer Bold',        STATIC_ROOT + '/fonts/cmuntb.ttf'))

# Table styles
tableStyles = {
    'info': TableStyle([
        ('FONT', (0,0), (0,-1),  'Type Writer Bold'),
        ('FONT', (1,0), (1,-1),  'Type Writer Bold'),
        ('FONT', (1,1), (-1,-1), 'Type Writer'),
        ('ALIGN', (0,0), (-1,0), 'CENTER'),
        ('VALIGN', (0,0), (-1, -1), 'MIDDLE'),
        ('BACKGROUND', (0,0), (-1,0), colors.gray),
        ('BACKGROUND', (0,0), (0,-1), colors.gray),
        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
        ('SPAN', (0,0), (1,0)),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.black),
    ]),
    'history': TableStyle([
        ('FONT', (0,0), (-1,0),  'Type Writer Bold'),
        ('FONT', (0,1), (-1,-1), 'Type Writer'),
        ('ALIGN', (0,0), (-1,0), 'CENTER'),
        ('VALIGN', (0,0), (-1, -1), 'MIDDLE'),
        ('BACKGROUND', (0,0), (-1,0), colors.gray),
        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.black),
    ]),
}


def loadStyles():
    """ Function to load report stylesheet """
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="ReportTitle",     alignment=TA_CENTER,  fontName="Type Writer Bold", fontSize=25))
    styles.add(ParagraphStyle(name="SectionTitle",    alignment=TA_JUSTIFY, fontName="Type Writer Bold", fontSize=16))
    styles.add(ParagraphStyle(name="ParagraphCenter", alignment=TA_CENTER,  fontName="Type Writer", parent=styles['Normal']))
    styles.add(ParagraphStyle(name="WrapWord",        alignment=TA_JUSTIFY, fontName="Type Writer", parent=styles['BodyText']))

    return styles


# Load stylesheet
stylesheet = loadStyles()
