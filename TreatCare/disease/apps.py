from django.apps import AppConfig
from TreatCare.utils.collect_service import load_medicines, load_diseases

class DiseaseConfig(AppConfig):
    name = 'disease'
    verbose_name = 'Disease'

    def ready(self):
        Disease = self.get_model('Disease')
        load_diseases(Disease)
