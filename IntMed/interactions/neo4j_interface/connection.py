from . import query
from . db_settings import DB_SETTINGS
from neo4j.v1 import GraphDatabase, basic_auth

def get_driver():
    return GraphDatabase.driver(DB_SETTINGS['HOST'], auth=basic_auth(DB_SETTINGS['USER'], DB_SETTINGS['PASSWORD']))

def get_all_drugs():
    return perform_query(query.ALL_DRUGS)

def get_multiple_drugs_interactions(drugs_ids):
    return perform_query(query.MULTIPLE_DRUGS_INTERACTIONS, {'drugs_ids': [int(drug_id) for drug_id in drugs_ids]})

def get_drug_interactions(drug_id):
    return perform_query(query.INTERACTIONS_PER_DRUG, {'drug_id': int(drug_id)})

def perform_query(query, arg=None):
    driver = get_driver()
    session = driver.session()

    result = session.run(query, arg)
    return result
