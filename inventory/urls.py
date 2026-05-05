from django.urls import path

from .views import (
    EquipamentoCreateView,
    EquipamentoDeleteView,
    EquipamentoListView,
    EquipamentoUpdateView,
    SalaCreateView,
    SalaDetailView,
    SalaListView,
    SalaUpdateView,
    SalaDeleteView,
    StatusCreateView,
    StatusListView,
    StatusUpdateView,
    StatusDeleteView,
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
    path("salas/<int:pk>/editar/", SalaUpdateView.as_view(), name="sala_update"),
    path("salas/<int:pk>/excluir/", SalaDeleteView.as_view(), name="sala_delete"),
    path("statuses/<int:pk>/editar/", StatusUpdateView.as_view(), name="status_update"),
    path("statuses/<int:pk>/excluir/", StatusDeleteView.as_view(), name="status_delete"),
]
