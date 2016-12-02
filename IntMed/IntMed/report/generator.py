from io import BytesIO
from django.utils import timezone
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from .writer import add_info_table, add_history_table, wrap_word_cell, add_title, get_table_writer, add_paragraph
import ast
from django.utils.translation import ugettext as _

class ReportGenerator:
    report_title = 'Relatório'

    def __init__(self, **kwargs):
        self.buffer   = kwargs.get('buffer', BytesIO())
        self.pageSize = kwargs.get('pageSize', A4)

        if self.pageSize == 'Letter':
            self.pageSize = letter

        self.width, self.height = self.pageSize
        self.doc    = self.loadDocumentTemplate()

    def loadDocumentTemplate(self):
        doc_template =  SimpleDocTemplate(
            self.buffer,
            rightMargin  = 72,
            leftMargin   = 72,
            bottomMargin = 72,
            topMargin    = 30,
            pagesize     = self.pageSize
        )
        return doc_template

    def generatePdfReport(self, *args):
        doc_data = []
        add_title(doc_data, self.report_title)

        for arg in args:
            objects = arg['objects']
            objects_data = []
            table_per_object = arg.get('table_per_object', False)
            writer = get_table_writer(arg['table'])

            if len(objects):
                for obj in objects:
                    if table_per_object:
                        objects_data = arg['formatter'](obj)
                        writer(doc_data=doc_data, labels=arg['labels'], table_data=objects_data, colWidths=arg.get('colWidths'), title=arg.get('title'))
                    else:
                        objects_data.append(arg['formatter'](obj))

                if not table_per_object:
                    writer(doc_data=doc_data, labels=arg['labels'], table_data=objects_data, colWidths=arg.get('colWidths'), title=arg.get('title'))


        self.doc.build(doc_data)
        pdf = self.buffer.getvalue()
        self.buffer.close()

        return pdf
