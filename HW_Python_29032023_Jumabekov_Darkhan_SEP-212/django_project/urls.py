"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from app.views import AuthorsCreateView, BooksCreateView, PublishersCreateView, PublicationsCreateView, SalesCreateView

"""
Definition of urls for Policklinika.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),

    path('authors/', AuthorsCreateView.as_view(), name='authors'),
    path('delete_author/<int:author_id>', views.delete_author, name='delete_author'),

    path('books/', BooksCreateView.as_view(), name='books'),
    path('delete_book/<int:book_id>', views.delete_book, name='delete_book'),

    path('publishers/', PublishersCreateView.as_view(), name='publishers'),
    path('delete_publisher/<int:publisher_id>', views.delete_publisher, name='delete_publisher'),

    path('publications/', PublicationsCreateView.as_view(), name='publications'),
    path('delete_publication/<int:publication_id>', views.delete_publication, name='delete_publication'),

    path('sales/', SalesCreateView.as_view(), name='sales'),
    path('delete_sale/<int:sale_id>', views.delete_sale, name='delete_sale'),

    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),

    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]

