from django.contrib import admin

# Register your models here.
from .models import Question, PersonalModel, IncomeModel

admin.site.register(Question)
admin.site.register(PersonalModel)
admin.site.register(IncomeModel)