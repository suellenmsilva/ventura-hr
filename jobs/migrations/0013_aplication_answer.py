# Generated by Django 3.1.3 on 2020-12-07 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('answer', '0003_auto_20201206_2159'),
        ('jobs', '0012_remove_criterio_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='aplication',
            name='Answer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='answer.answer'),
            preserve_default=False,
        ),
    ]
