from . import query
from . db_settings import DB_SETTINGS
from neo4j.v1 import GraphDatabase, basic_auth

def get_driver():
    return GraphDatabase.driver(DB_SETTINGS['HOST'], auth=basic_auth(DB_SETTINGS['USER'], DB_SETTINGS['PASSWORD']))

def get_all_drugs():
    return perform_query(query.ALL_DRUGS)

def get_multiple_drugs_interactions(drugs_names):
    return perform_query(query.MULTIPLE_DRUGS_INTERACTIONS, {'names': drugs_names})

def get_drug_interactions(drug_name):
    return perform_query(query.INTERACTIONS_PER_DRUG, {'name':drug_name})

def perform_query(query, arg=None):
    driver = get_driver()
    session = driver.session()

    result = session.run(query, arg)
    return result
