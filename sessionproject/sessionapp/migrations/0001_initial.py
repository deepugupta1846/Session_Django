# Generated by Django 3.1.6 on 2021-02-04 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignupData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
                ('Mob_No', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=50)),
                ('Password', models.CharField(max_length=20)),
            ],
        ),
    ]
