from django.db.models import Count
from django import forms
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .models import Equipamento, Sala, Status


class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ["nome", "descricao"]
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }


class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ["nome", "sala", "status"]
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'sala': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }


class EquipamentoListView(ListView):
    model = Equipamento
    template_name = "inventory/equipamento_list.html"
    context_object_name = "equipamentos"

    def get_queryset(self):
        queryset = super().get_queryset()
        self.order = self.request.GET.get('order', 'nome')
        if self.order == 'sala':
            queryset = queryset.order_by('sala__nome')
        elif self.order == '-sala':
            queryset = queryset.order_by('-sala__nome')
        elif self.order == 'status':
            queryset = queryset.order_by('status__nome')
        elif self.order == '-status':
            queryset = queryset.order_by('-status__nome')
        else:
            queryset = queryset.order_by('nome')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_order'] = self.order
        return context


class EquipamentoCreateView(CreateView):
    model = Equipamento
    form_class = EquipamentoForm
    template_name = "inventory/equipamento_form.html"
    success_url = reverse_lazy("sala_list")

    def get_initial(self):
        initial = super().get_initial()
        sala_id = self.request.GET.get('sala')
        if sala_id:
            try:
                initial['sala'] = Sala.objects.get(pk=sala_id)
            except Sala.DoesNotExist:
                pass
        return initial


class EquipamentoUpdateView(UpdateView):
    model = Equipamento
    form_class = EquipamentoForm
    template_name = "inventory/equipamento_form.html"
    success_url = reverse_lazy("sala_list")


class EquipamentoDeleteView(DeleteView):
    model = Equipamento
    template_name = "inventory/equipamento_confirm_delete.html"
    success_url = reverse_lazy("sala_list")


class SalaListView(ListView):
    model = Sala
    template_name = "inventory/sala_list.html"
    context_object_name = "salas"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        salas = context['salas']
        salas_with_counts = []
        for sala in salas:
            counts = Equipamento.objects.filter(sala=sala).values('status__nome').annotate(count=Count('status')).order_by('status__nome')
            count_dict = {}
            for item in counts:
                nome = item['status__nome']
                if 'Operante' in nome:
                    count_dict['operante'] = item['count']
                elif 'Parcialmente' in nome:
                    count_dict['parcial'] = item['count']
                elif 'Inoperante' in nome:
                    count_dict['inoperante'] = item['count']
            salas_with_counts.append({'sala': sala, 'counts': count_dict})
        context['salas_with_counts'] = salas_with_counts
        return context


class SalaDetailView(DetailView):
    model = Sala
    template_name = "inventory/sala_detail.html"
    context_object_name = "sala"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sala = self.object
        equipamentos = Equipamento.objects.filter(sala=sala)
        context['equipamentos'] = equipamentos
        return context


class SalaCreateView(CreateView):
    model = Sala
    form_class = SalaForm
    template_name = "inventory/sala_form.html"
    success_url = reverse_lazy("sala_list")


class StatusListView(ListView):
    model = Status
    template_name = "inventory/status_list.html"
    context_object_name = "statuses"


class StatusCreateView(CreateView):
    model = Status
    fields = ["nome", "descricao"]
    template_name = "inventory/status_form.html"
    success_url = reverse_lazy("status_list")
