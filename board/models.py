from django.db import models

# Create your models here.
from user.models import User #user를 임포트


class Board(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=2000)
    hit = models.IntegerField(default=0) # 기본값으로 0이 들어가도록 설정 조회수
    regdate = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE) # 주키삭제되면 전부삭제됨
    name = models.CharField(max_length=30)

    def __str__(self):
        return "Board( %s, %s, %d, %s, %d, %s)" % (self.title, self.content, self.hit, str(self.regdate), self.user.id, self.name)