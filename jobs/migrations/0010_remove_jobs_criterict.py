# Generated by Django 3.1.3 on 2020-12-02 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_remove_criterio_experience'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobs',
            name='criterict',
        ),
    ]