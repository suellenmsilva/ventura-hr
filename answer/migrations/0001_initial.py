# Generated by Django 3.1.3 on 2020-12-02 02:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0009_remove_criterio_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerCriterict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.CharField(choices=[('ruim', 'Ruim'), ('bom', 'Bom'), ('muito_bom', 'Muito Bom'), ('excelente', 'Excelente')], max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('criterict', models.ManyToManyField(to='jobs.Criterio')),
            ],
            options={
                'verbose_name': 'AnswerCriterict',
                'verbose_name_plural': 'AnswerCritericts',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('answercriterict', models.ManyToManyField(to='answer.AnswerCriterict')),
                ('jobs', models.ManyToManyField(to='jobs.Jobs')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Answer',
                'verbose_name_plural': 'Answers',
            },
        ),
    ]
