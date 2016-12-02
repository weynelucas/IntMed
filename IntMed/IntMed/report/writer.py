from reportlab.platypus  import Table, Spacer, Paragraph
from reportlab.lib.units import mm
from .styles             import tableStyles, stylesheet


def add_paragraph(doc_data, text, style='Normal'):
    """ Add paragraph to document
        Args:
            doc_data : Document data to append paragraph
            title    : Text to display on paragraph
    """
    doc_data.append(Paragraph(text, stylesheet[style]))
    add_space(doc_data, height=25)


def wrap_word_cell(text):
    """ Convert a long text string to a Paragraph to wrap on
        a table cell and not escape it and prevents layout breaks
        Args:
            text     : Text to convert in a wrap word cell
        Returns:
            A Paragraph with WrapWord (BodyText child) style
    """
    return Paragraph(text, stylesheet['WrapWord'])

def add_title(doc_data, title):
    """ Add title to document
        Args:
            doc_data : Document data to append title
            title    : Text to display on title
    """
    doc_data.append(Paragraph(title, stylesheet['ReportTitle']))
    add_space(doc_data, height=50)


def add_space(doc_data, width=1, height=25):
    """ Add white space to document
        Args:
            doc_data : Document data to append spacer
            width    : Horizontal space value
            height   : Vertical space value
    """
    doc_data.append(Spacer(width, height))

def add_table(doc_data, table_data, table_style, **kwargs):
    """ Add table to document data
        Args:
            doc_data   : Document data to append table
            table_data : Tuple of tuples with table data
            table_style: Table style object
            **kwargs   : Table settings arguments (hAlign, colWidths)
    """
    table = Table(
        table_data,
        colWidths = kwargs.get('colWidths', [None]*len(table_data[0])),
        hAlign    = kwargs.get('hAlign', 'CENTER')
    )
    table.setStyle(table_style)
    doc_data.append(table)
    add_space(doc_data)

def add_info_table(doc_data, title, labels, table_data, colWidths=None):
    """ Add an info table, a table with two columns, one of labels,
        and other of values

        Args:
            doc_data   : Document data to append table
            title      : Title of info table
            labels     : Array with labels (strings)
            table_data : Array of values
    """
    titlePair = ((title, ''),)
    labelsValuesPair = tuple(zip(labels, table_data))

    table_data = titlePair + labelsValuesPair

    if colWidths:
        add_table(doc_data, table_data, tableStyles['info'], colWidths=colWidths)
    else:
        add_table(doc_data, table_data, tableStyles['info'])

def add_history_table(doc_data, title, labels, table_data, colWidths=None):
    """ Add an history table, a table to display distribution of
        data

        Args:
            doc_data   : Document data to append table
            labels     : Array with labels (strings)
            table_data : Array of arrays with values (each array is a arrange of object properties - values)
    """

    table_data = [labels] + table_data

    if not colWidths:
        colWidths = tuple([None]*(len(labels)))

    add_table(doc_data, table_data, tableStyles['history'], colWidths=colWidths)

def get_tables():
    """ Get the available tables

        Returns:
            A dict with tables and your related writers
    """
    return {
        'info': add_info_table,
        'history': add_history_table,
    }

def get_table_writer(table_style):
    """ Get the table writer given your style

        Args:
            table_style: Table style string

        Returns:
            The related writer method
    """
    tables = get_tables()

    return tables[table_style]
