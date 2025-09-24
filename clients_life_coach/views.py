from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView
from .models import Client
from .forms import ClientForm
class ClientListView(ListView):
    model = Client
    template_name = 'clients/client_list.html'
    context_object_name = 'clients'
    paginate_by = 10

class ClientCreateView(View):
    def get(self, request):
        form = ClientForm()
        return render(request, 'clients/client_form.html', {'form': form, 'title': 'Add Client'})

    def post(self, request):
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
        return render(request, 'clients/client_form.html', {'form': form, 'title': 'Add Client'})

class ClientUpdateView(View):
    def get(self, request, pk):
        client = get_object_or_404(Client, pk=pk)
        form = ClientForm(instance=client)
        return render(request, 'clients/client_form.html', {'form': form, 'title': 'Edit Client'})

    def post(self, request, pk):
        client = get_object_or_404(Client, pk=pk)
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_detail', pk=client.pk)
        return render(request, 'clients/client_form.html', {'form': form, 'title': 'Edit Client'})

class ClientDetailView(View):
    def get(self, request, pk):
        client = get_object_or_404(Client, pk=pk)
        return render(request, 'clients/client_detail.html', {'client': client})

class ClientDeleteView(View):
    def get(self, request, pk):
        client = get_object_or_404(Client, pk=pk)
        return render(request, 'clients/client_confirm_delete.html', {'client': client})

    def post(self, request, pk):
        client = get_object_or_404(Client, pk=pk)
        client.delete()
        return redirect('client_list')
