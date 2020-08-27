#from django.db import models
#from django.utils import timezone

from __future__ import unicode_literals
from django.db import models

class DjangoBoard(models.Model):#게시판 디비
    title = models.CharField(max_length=50, blank = True)#제목
    contents = models.CharField(max_length=200, blank = True)#내용
    kindOfStudy = models.CharField(max_length=200, blank = True)#웹/안드로이드 이런거
    state = models.CharField(max_length=200, blank = True) #모집중/모집종료
    location = models.CharField(max_length=200, blank = True)#스터디 지역
    nickName = models.CharField(max_length=50, blank = True)#닉네임
    date = models.DateField(null=True, blank=True) #글을 쓴 날짜
    hits = models.IntegerField(null=True, blank = True)#조회수
    