# Generated by Django 3.1.3 on 2020-12-07 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('required', models.BooleanField(default=True)),
                ('question_type', models.CharField(default='intro', max_length=200)),
            ],
        ),
    ]
