# Generated by Django 3.1.6 on 2021-02-07 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sessionapp', '0003_signupdata_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signupdata',
            name='Gender',
        ),
    ]