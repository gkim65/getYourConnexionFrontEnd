from django.urls import path

from application.forms import PersonalForm, IncomeForm
from application.views import ContactWizard
from . import views

# Need to specify my urls to be used within this project
urlpatterns = [
    path('', views.index, name='index'),
    path('Questions/', ContactWizard.as_view([PersonalForm, IncomeForm]), name="intros"),
    path('submit/', views.submitPage, name='submitPage'),
]
