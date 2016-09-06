def db_table_exists(table, cursor=None):
    """ Checks if exist a table with the given name
        on database
        Args:
            table: name of table
            cursor: connection cursor (not required)
    """
    try:
        if not cursor:
            from django.db import connection
            cursor = connection.cursor()
        if not cursor:
            raise Exception
        table_names = [table.name for table in connection.introspection.get_table_list(cursor)]
    except:
        raise Exception("unable to determine if the table '%s' exists" % table)
    else:
        return table in table_names
