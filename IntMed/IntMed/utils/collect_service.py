import http.client as http
from .database_service import db_table_exists
from interactions.neo4j_interface import connection


def load_drugs(DrugClass=None):
    """ Load drugs from Neo4j drugs interactions graph
        database and save into database if is not empty
        Args:
            DrugClass: Drug class (required if app has not been loaded yet)
    """
    if not DrugClass:
        from drug.models import Drug
        DrugClass = Drug

    if db_table_exists(DrugClass._meta.db_table) and not DrugClass.objects.count():
         result = connection.get_all_drugs()

         for record in result:
             drug = DrugClass(id = record['id'], name=record['name'], action=record['action'])
             drug.save()
