# Register your models here.
from django.contrib import admin
from .models import Partner, Menu


@admin.register(Partner, Menu)
class PartnerAdmin(admin.ModelAdmin):
    pass
