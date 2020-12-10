from django.db import models
from .forms import PersonalForm, IncomeForm
from django.conf import settings

# Format of the various application questions
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    required = models.BooleanField(default = True)
    # Lets use question_type to separate questions into separate pages
    question_type = models.CharField(max_length=200, default = "intros")
    
    # This will let me see the question represented in text form rather than other form
    def __str__(self):
        return self.question_text


class PersonalModel(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    first_Name = models.CharField(max_length=100)
    last_Name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_Number = models.DecimalField(max_digits=10, decimal_places=0)
    street_Address = models.CharField(max_length=200)
    address_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state_Abb = models.CharField(max_length=2)
    zipCode = models.DecimalField(max_digits=6, decimal_places=0)

class IncomeModel(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    Have_a_W2 = models.BooleanField()
    annual_Income = models.CharField(max_length=100, default="['0']")
    family = models.DecimalField(max_digits=5,decimal_places=0)
    