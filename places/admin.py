from django.contrib import admin
from django.db.models import fields
from .models import Place, Feedback


admin.site.register(Place)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['text', 'place', 'user']  # 'checked'
    list_editable = ['user']   #  'checked'
    list_filter = ['place'] # 'checked'
    search_fields = ['text', 'place__name', 'place__location', 'place__description']

    fields = ['user', 'place', 'text']
    readonly_fields = ['place', 'text']

admin.site.register(Feedback, FeedbackAdmin)