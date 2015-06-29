from django.contrib import admin
from actions import export_as_excel
from .models  import Track
#Atributos agregados al adminisrador de django en track
class TrackAdmin(admin.ModelAdmin):
    list_display = ('title','artist','order','album','player','es_farrel')
    list_filter = ('artist','album','title')
    search_fields = ('title','artist__first_name')
    list_editable = ('artist','album')
    actions = (export_as_excel, )
    raw_id_fields = ('artist', )

    def es_farrel(self, obj):
        return obj.id == 1;

    es_farrel.boolean = True

admin.site.register(Track,TrackAdmin)
