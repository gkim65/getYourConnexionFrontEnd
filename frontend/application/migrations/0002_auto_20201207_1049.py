# Generated by Django 3.1.3 on 2020-12-07 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(default='intros', max_length=200),
        ),
    ]
