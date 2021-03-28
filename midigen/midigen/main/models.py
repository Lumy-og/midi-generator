from django.db import models

# Create your models here.
class Midi1(models.Model):
    tempo=models.CharField('Tempo', max_length=50)
    instrument=models.CharField('Instrument', max_length=50)
    repeats=models.CharField('Repeats', max_length=50)
    track=models.CharField('Track', max_length=50)
    mood=models.CharField('Mood', max_length=50)
    melody=models.CharField('Melody', max_length=150)

    class Meta:
        verbose_name= 'Music'
        verbose_name_plural = 'Music'
        # verbose_name_plural= 'Задачи'

    def __str__(self):
        return  self.tempo


