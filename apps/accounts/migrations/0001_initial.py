# Generated by Django 4.2.4 on 2023-09-25 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricule', models.CharField(max_length=8, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('forename', models.CharField(max_length=100)),
                ('code', models.CharField(default=True, max_length=100)),
                ('date', models.DateField()),
                ('phone_number', models.IntegerField()),
                ('password', models.CharField(max_length=100)),
                ('confirm_password', models.CharField(max_length=100)),
                ('actif', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Candidat',
                'verbose_name_plural': 'Candidats',
            },
        ),
    ]
