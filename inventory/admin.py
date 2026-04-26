from django.contrib import admin
from .models import Equipamento, Sala, Status


@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ("nome", "descricao")
    search_fields = ("nome",)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ("nome", "descricao")
    search_fields = ("nome",)


@admin.register(Equipamento)
class EquipamentoAdmin(admin.ModelAdmin):
    list_display = ("nome", "sala", "status", "data_atualizacao")
    list_filter = ("sala", "status")
    search_fields = ("nome",)
