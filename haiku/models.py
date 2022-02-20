from django.db import models
from accounts.models import CustomUser
# Create your models here.

class Kobo_info(models.Model):

    """公募情報モデル"""

    # user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)

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



class Saiten_info(models.Model):

    """採点機能に使う過去の入賞作品の分析結果モデル"""

    pos = models.CharField(verbose_name='品詞文字列', max_length=80)
    winningCount = models.PositiveIntegerField(verbose_name='入賞頻度', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Saiten_info'

    def __str__(self):
        return self.pos

