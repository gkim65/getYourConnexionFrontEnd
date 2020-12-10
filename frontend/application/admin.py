from django.contrib import admin

# Register your models here.
from .models import Question, PersonalModel, IncomeModel

# Need to put models here so that we can see them in models later for admin settings
admin.site.register(Question)
admin.site.register(PersonalModel)
admin.site.register(IncomeModel)