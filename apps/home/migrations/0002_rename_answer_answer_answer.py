# Generated by Django 4.2.4 on 2023-09-20 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='Answer',
            new_name='answer',
        ),
    ]