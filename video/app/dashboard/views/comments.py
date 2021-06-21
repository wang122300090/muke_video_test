# coding: utf-8

from django.views import View
from django.shortcuts import reverse, redirect
from app.models import Comment

class Comments(View):

    def get(self, request, comment_id, video_id):
        comment = Comment.objects.get(pk=comment_id)
        comment.status = not comment.status
        comment.save()
        return redirect(reverse('video_sub', kwargs={'video_id': video_id}))