from django.contrib import admin
from myproject.zoo.models import *
from myproject.zoo.forms import *


class EventoZoonosisAdmin(admin.ModelAdmin):
    pass

class MascotaZoonosisAdmin(admin.ModelAdmin):
    exclude = ('adoptado',)
	
class AdoptanteZoonosisAdmin(admin.ModelAdmin):
    form = AdoptanteForm

    def save_model(self, request, obj, form, change):
        obj.save()
        mascotas = obj.mascota.all()

        if isinstance(mascotas, MascotaZoonosis):
            mascota.adoptado = True
            mascota.save()
        else:
            for mascota in mascotas:
                mascota.adoptado = True
                mascota.save()

admin.site.register(EventoZoonosis, EventoZoonosisAdmin)
admin.site.register(MascotaZoonosis, MascotaZoonosisAdmin)
admin.site.register(AdoptanteZoonosis, AdoptanteZoonosisAdmin)
