# Generated by Django 3.1.3 on 2020-12-07 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('answer', '0004_remove_answer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='date',
        ),
    ]
