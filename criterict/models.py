from django.db import models


class Experience(models.Model):
    TYPE = (
        ('ruim', 'Ruim'),
        ('bom', 'Bom'),
        ('muito_bom', 'Muito Bom'),
        ('excelente', 'Excelente'),
    )

    experience = models.CharField(max_length=20, choices=TYPE)


class Criterict(models.Model):
    criterict = models.CharField('Criterio', max_length=100, blank=True)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)