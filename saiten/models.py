from django.db import models

# Create your models here.

class Winning_senryu(models.Model):

    """入賞作品モデル"""

    winning_senryu = models.TextField(verbose_name='入賞作品', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Winning_senryu'

    def __str__(self):
        return self.winning_senryu