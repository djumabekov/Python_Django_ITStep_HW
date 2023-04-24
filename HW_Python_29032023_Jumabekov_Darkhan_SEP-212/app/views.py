import time
from decimal import Decimal
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from app.models import Authors, Books, Publishers, Publications, Sales
from .forms import AuthorsForm, BooksForm, PublishersForm, PublicationsForm, SalesForm


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

class AuthorsCreateView(CreateView):
    template_name = 'app/authors.html'
    form_class = AuthorsForm
    success_url = reverse_lazy('authors')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = Authors.objects.all()
        return context


def delete_author(request, author_id: int):
    assert isinstance(request, HttpRequest)
    Authors.objects.filter(id=author_id).delete()
    return redirect("/authors")


class BooksCreateView(CreateView):
    template_name = 'app/books.html'
    form_class = BooksForm
    success_url = reverse_lazy('books')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Books.objects.all()
        return context


def delete_book(request, book_id: int):
    assert isinstance(request, HttpRequest)
    Books.objects.filter(id=book_id).delete()
    return redirect("/books")


class PublishersCreateView(CreateView):
    template_name = 'app/publishers.html'
    form_class = PublishersForm
    success_url = reverse_lazy('publishers')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['publishers'] = Publishers.objects.all()
        return context


def delete_publisher(request, publisher_id: int):
    assert isinstance(request, HttpRequest)
    Publishers.objects.filter(id=publisher_id).delete()
    return redirect("/publishers")


class PublicationsCreateView(CreateView):
    template_name = 'app/publications.html'
    form_class = PublicationsForm
    success_url = reverse_lazy('publications')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['publications'] = Publications.objects.all()
        return context


def delete_publication(request, publication_id: int):
    assert isinstance(request, HttpRequest)
    Publications.objects.filter(id=publication_id).delete()
    return redirect("/publications")


class SalesCreateView(CreateView):
    template_name = 'app/sales.html'
    form_class = SalesForm
    success_url = reverse_lazy('sales')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sales'] = Sales.objects.all()
        return context


def delete_sale(request, sale_id: int):
    assert isinstance(request, HttpRequest)
    Sales.objects.filter(id=sale_id).delete()
    return redirect("/sales")
