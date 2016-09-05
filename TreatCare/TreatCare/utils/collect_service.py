import csv
import http.client as http
from bs4 import BeautifulSoup
from string import ascii_lowercase
from TreatCare.utils.database_service import db_table_exists
from neo4j.v1 import GraphDatabase, basic_auth


def load_drugs(DrugClass=None):
    """ Load medicines from Neo4j drugs interactions graph
        database and save into database if is not empty
        Args:
            DrugClass: Drug class (required if app has not been loaded yet)
    """
    if not DrugClass:
        from drug.models import Drug
        DrugClass = Drug

    if db_table_exists(DrugClass._meta.db_table) and not DrugClass.objects.count():
         driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "password"))
         session = driver.session()

         result = session.run("MATCH (d:DRUG) RETURN d.name AS name")

         for record in result:
             drug = DrugClass(name=record['name'])
             drug.save()

def load_medicines(MedicineClass=None):
    """ Load medicines from http://www.consultamedicamentos.com.br
        and save into database if is not empty
        Args:
            MedicineClass: Medicine class (required if app has not been loaded yet)
    """

    if not MedicineClass:
        from medicine.models import Medicine
        MedicineClass = Medicine

    if db_table_exists(MedicineClass._meta.db_table) and not MedicineClass.objects.count():
        url = "www.consultamedicamentos.com.br"
        uri = "/sp/referencia/"
        conn = http.HTTPConnection(url, 80)

        for letter in ascii_lowercase:
            conn.request("GET", uri+letter)

            resp = conn.getresponse()
            html_doc = resp.read()

            soup = BeautifulSoup(html_doc, 'html.parser')

            table = soup.find("table", class_="TabelaCM")
            if table is not None:
                rows = table.find('tbody').find_all("tr")

                for row in rows:
                    data = row.find_all("td")
                    name = data[1].get_text()
                    presentation = data[2].get_text()
                    laboratory = data[3].get_text()
                    active_principle = data[4].get_text()
                    try:
                        pmc = float(data[5].get_text())
                    except ValueError:
                        pmc = None


                    medicine = MedicineClass(
                        name = name,
                        presentation = presentation,
                        laboratory = laboratory,
                        active_principle = active_principle,
                        pmc = pmc
                    )
                    medicine.save()


def load_diseases(DiseaseClass=None):
    """ Load diseases from International Classification of
        Deseases (ICD-10) from datasus CSV files (http://www.datasus.gov.br/cid10/V2008/cid10.htm)
        and save into database if is not empty
        Args:
            DiseaseClass: Disease class (required if app has not been loaded yet)
    """

    if not DiseaseClass:
        from disease.models import Disease
        DiseaseClass = Disease

    if db_table_exists(DiseaseClass._meta.db_table) and not DiseaseClass.objects.count():
        with open("CID10CSV/CID-10-SUBCATEGORIAS.CSV") as csv_file:
            reader = csv.DictReader(csv_file, delimiter=';')
            for row in reader:
                code = row['SUBCAT']
                description = row['DESCRICAO']
                if len(code) == 4:
                    code = code[:-1] + '.' + code[-1]

                disease = DiseaseClass(
                    code = code,
                    description = description,
                )
                disease.save()


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
