from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Page

# Create your views here.

def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')  # Agrega este bloque para evitar el error

def pages_list(request):
    pages = Page.objects.all()  # Asegúrate de que esta consulta sea correcta
    return render(request, 'blog/pages_list.html', {'pages': pages})

def page_detail(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    return render(request, 'blog/page_detail.html', {'page': page})

def inicio(request):
    return render(request, 'blog/inicio.html')

class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    fields = ['title', 'subtitle', 'content', 'image', 'genre', 'rating']
    template_name = 'blog/page_form.html'
    success_url = reverse_lazy('pages_list')

class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    fields = ['title', 'subtitle', 'content', 'image', 'genre', 'rating']
    template_name = 'blog/page_form.html'
    success_url = reverse_lazy('pages_list')

class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = 'blog/page_confirm_delete.html'
    success_url = reverse_lazy('pages_list')
