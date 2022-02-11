from django.db import models

# Create your models here.

class Kobo_info(models.Model):

    """公募情報モデル"""

    title = models.CharField(verbose_name='タイトル', max_length=40)
    deadline = models.DateField(verbose_name='締切日', blank=True, null=True)
    prize = models.TextField(verbose_name='賞金', blank=True, null=True)
    contents = models.TextField(verbose_name='募集内容', blank=True, null=True)
    requirements = models.TextField(verbose_name='応募資格', blank=True, null=True)
    sponsor = models.TextField(verbose_name='主催', blank=True, null=True)
    link = models.TextField(verbose_name='応募リンク', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Kobo_info'

    def __str__(self):
        return self.title