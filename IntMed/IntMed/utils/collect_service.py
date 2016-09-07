import http.client as http
from bs4 import BeautifulSoup
from .database_service import db_table_exists
from neo4j.v1 import GraphDatabase, basic_auth


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
         driver = GraphDatabase.driver("bolt://54.152.213.214/browser/", auth=basic_auth("neo4j", "ufc=1890"))
         session = driver.session()

         result = session.run("MATCH (d:DRUG) RETURN d.name AS name, d.drugAction AS action")

         for record in result:
             drug = DrugClass(name=record['name'], action=record['action'])
             drug.save()


def get_html_soup_response(url, uri, port=80):
    """ Get the html of a HTTP response parsed by
        BeautifulSoup
        Args:
            url: URL of HTTP connection
            uri: URI of HTTP connection
            port: port number of HTPP connection
    """
    conn = http.HTTPConnection(url, 80)
    conn.request("GET", uri)
    resp = conn.getresponse()

    return BeautifulSoup(resp.read(), 'html.parser')
