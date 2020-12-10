from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .forms import PersonalForm, IncomeForm
from formtools.wizard.views import SessionWizardView
from .models import PersonalModel, IncomeModel

# Use Django Wizard in order to spread Form across several pages
class ContactWizard(SessionWizardView):
    template_name = "application/intros.html"

    # Only save into database if user completes both pages of the form
    def done(self, form_list, **kwargs):
        process_form_data(form_list,self)
        return HttpResponseRedirect(reverse("application:submitPage"))

# Save information from form after user completes it
def process_form_data(form_list,self):
    form_data = [form.cleaned_data for form in form_list]
    # save form data into sql here
    p = PersonalModel(
    username = self.request.user,
    first_Name = form_data[0]['first_Name'],
    last_Name = form_data[0]['last_Name'],
    email = form_data[0]['email'],
    phone_Number = form_data[0]['phone_Number'],
    street_Address = form_data[0]['street_Address'],
    address_2 = form_data[0]['address_2'],
    city = form_data[0]['city'],
    state_Abb = form_data[0]['state_Abb'],
    zipCode = form_data[0]['zipCode'])
    p.save()

    i = IncomeModel(
    username = self.request.user,
    Have_a_W2 = form_data[1]['Have_a_W2'],
    annual_Income = form_data[1]['annual_Income'],
    family =  form_data[1]['family'])
    i.save()
    return form_data

# Will be handling requests/response cycles of our web application
def index(request):
     return render(request, 'application/index.html',)

def submitPage(request):
    return render(request, 'application/submitPage.html',)