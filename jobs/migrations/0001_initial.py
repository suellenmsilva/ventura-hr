# Generated by Django 3.1.3 on 2020-11-23 21:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(blank=True, max_length=100, verbose_name='Cargo')),
                ('description', models.TextField(max_length=250, verbose_name='Descrição')),
                ('city', models.CharField(max_length=50, verbose_name='Cidade')),
                ('state', models.CharField(max_length=50, verbose_name='Estado')),
                ('contract_type', models.CharField(choices=[('clt', 'CLT'), ('temporario', 'Temporario'), ('freelance', 'Freelance'), ('home_office', 'Home Office')], max_length=20)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('expiration_date', models.DateField(verbose_name='Data de Expiração')),
                ('first_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
