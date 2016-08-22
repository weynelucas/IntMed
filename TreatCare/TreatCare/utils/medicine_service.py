from bs4 import BeautifulSoup
import http.client as http
from string import ascii_lowercase
from TreatCare.utils.database_service import db_table_exists

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
