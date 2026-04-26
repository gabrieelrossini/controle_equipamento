from django.urls import path

from .views import (
    EquipamentoCreateView,
    EquipamentoDeleteView,
    EquipamentoListView,
    EquipamentoUpdateView,
    SalaCreateView,
    SalaDetailView,
    SalaListView,
    StatusCreateView,
    StatusListView,
)

urlpatterns = [
    path("", SalaListView.as_view(), name="sala_list"),
    path("salas/<int:pk>/", SalaDetailView.as_view(), name="sala_detail"),
    path("equipamentos/", EquipamentoListView.as_view(), name="equipamento_list"),
    path("equipamentos/novo/", EquipamentoCreateView.as_view(), name="equipamento_create"),
    path("equipamentos/<int:pk>/editar/", EquipamentoUpdateView.as_view(), name="equipamento_update"),
    path("equipamentos/<int:pk>/excluir/", EquipamentoDeleteView.as_view(), name="equipamento_delete"),
    path("salas/novo/", SalaCreateView.as_view(), name="sala_create"),
    path("statuses/", StatusListView.as_view(), name="status_list"),
    path("statuses/novo/", StatusCreateView.as_view(), name="status_create"),
]
