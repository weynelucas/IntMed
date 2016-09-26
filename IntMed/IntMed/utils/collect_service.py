import http.client as http
import requests
from .database_service import db_table_exists


def load_drugs(DrugClass=None):
    """ Load drugs from Neo4j drugs interactions graph
        database and save into database if is not empty
        Args:
            DrugClass: Drug class (required if app has not been loaded yet)
    """
    url = "http://api.startupfactor.com.br/api/drugs"
    token = "f2360d4b17b259c0b15d0b1f57025a9580feb127"

    if not DrugClass:
        from drug.models import Drug
        DrugClass = Drug

    if db_table_exists(DrugClass._meta.db_table) and not DrugClass.objects.count():
        result = requests.get(url, headers={"Authorization": "Token " + token}).json()

        for record in result:
            drug = DrugClass(id = record['id'], name=record['name'], action=record['action'])
            drug.save()
