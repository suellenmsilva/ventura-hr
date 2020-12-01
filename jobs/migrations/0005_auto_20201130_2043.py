# Generated by Django 3.1.3 on 2020-11-30 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20201130_2013'),
    ]

    operations = [
        migrations.CreateModel(
            name='Criterio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criterict', models.CharField(blank=True, max_length=100, verbose_name='Criterio')),
                ('experience', models.CharField(choices=[('ruim', 'Ruim'), ('bom', 'Bom'), ('muito_bom', 'Muito Bom'), ('excelente', 'Excelente')], max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='jobs',
            name='experience',
        ),
        migrations.RemoveField(
            model_name='jobs',
            name='criterict',
        ),
        migrations.AddField(
            model_name='jobs',
            name='criterict',
            field=models.ManyToManyField(blank=True, max_length=100, to='jobs.Criterio'),
        ),
    ]