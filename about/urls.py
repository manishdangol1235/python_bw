from django.urls import path
from about import views

urlpatterns = [
    # http://127.0.0.1:8000/about/
    path('', views.show_about),

    # http://127.0.0.1:8000/about/contacts
    path('contacts', views.show_contacts)
]
