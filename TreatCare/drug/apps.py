from django.apps import AppConfig
from TreatCare.utils.collect_service import load_drugs

class DrugConfig(AppConfig):
    name = 'drug'

    def ready(self):
        Drug = self.get_model('Drug')
        load_drugs(Drug)
