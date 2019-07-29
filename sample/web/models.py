from django.db import models


# Create your models here.
class Board(models.Model):
    # def __init__(self):
    user = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name='boards')
    id = models.AutoField(primary_key=True, verbose_name='아이디')
    title = models.CharField(max_length=100, verbose_name='제목')
    content = models.TextField(null=True, verbose_name='본문')

    # def __str__(self):
    #     return self.id

class Comment(models.Model):
    board = models.ForeignKey('web.Board', on_delete=models.CASCADE, related_name='comments')
    id = models.AutoField(primary_key=True)
    content = models.TextField(verbose_name='내용')