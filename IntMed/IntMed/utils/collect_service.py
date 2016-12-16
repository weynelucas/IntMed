import http.client as http
import requests
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from .database_service import db_table_exists


def load_drugs(DrugClass=None):
    """ Load drugs from Neo4j drugs interactions graph
        database and save into database if is not empty
        Args:
            DrugClass: Drug class (required if app has not been loaded yet)
    """
    url = "http://api.sim.intmed.com.br/api/drugs"
    token = "8507910ddca9965f915f26c1b71da93b58cd28cd"

    if not DrugClass:
        from drug.models import Drug
        DrugClass = Drug

    if db_table_exists(DrugClass._meta.db_table) and settings.UPDATE_DRUGS_ON_DEPLOY:
        result = requests.get(url, headers={"Authorization": "Token " + token}).json()

        for record in result:
            try:
                drug = DrugClass.objects.get(pk = record['id'])
                drug.name = record['name']
                drug.action = record['action']
            except ObjectDoesNotExist:
                drug = DrugClass(id = record['id'], name=record['name'], action=record['action'])
            finally:
                drug.save()
