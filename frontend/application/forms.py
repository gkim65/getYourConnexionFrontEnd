from django import forms

class PersonalForm(forms.Form):
    first_Name = forms.CharField(max_length=100)
    last_Name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    phone_Number = forms.DecimalField(max_digits=10)
    street_Address = forms.CharField(max_length=200)
    address_2 = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    state_Abb = forms.CharField(max_length=2)
    zipCode = forms.DecimalField(max_digits=6)

DEMO_CHOICES =( 
    ("1", "Below $30,000"), 
    ("2", "$30,000 - $60,000"), 
    ("3", "Above $60,000"),
) 
class IncomeForm(forms.Form):
    Have_a_W2 = forms.BooleanField()
    annual_Income = forms.MultipleChoiceField(choices = DEMO_CHOICES)
    family = forms.DecimalField()
    
