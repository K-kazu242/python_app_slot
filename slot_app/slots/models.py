from django.db import models
from django.contrib.auth.models import User


class SlotRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='ユーザー')
    date = models.DateField(verbose_name='日付')
    amount = models.IntegerField(verbose_name='収支', default=0)
    memo = models.CharField(verbose_name='メモ', max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date', '-created_at']
        verbose_name = 'スロット記録'
        verbose_name_plural = 'スロット記録'

    def __str__(self):
        sign = '+' if self.amount >= 0 else ''
        return f"{self.user.username} / {self.date} : {sign}{self.amount:,}円"
