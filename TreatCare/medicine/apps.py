from django.apps import AppConfig
from TreatCare.utils.medicine_service import load_medicines

class MedicineConfig(AppConfig):
    name = 'medicine'
    verbose_name = 'Medicine'

    def ready(self):
        Medicine = self.get_model('Medicine')
        load_medicines(Medicine)
