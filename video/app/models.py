# coding:utf-8
# 在做makemigrations时,一般是读这个models.py文件,因此要引入

from .model.auth import ClientUser
from .model.video import Video, VideoSub, VideoStar, IdentityType, NationalityType, VideoType
from .model.comment import Comment

