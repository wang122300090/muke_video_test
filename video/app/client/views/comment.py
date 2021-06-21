# coding: utf-8

from django.views.generic import View
from django.shortcuts import reverse
from django.http import JsonResponse
from app.models import Comment, ClientUser, Video


class CommentView(View):

    def post(self, request):

        content = request.POST.get('content', '')
        user_id = request.POST.get('userId', '')
        video_id = request.POST.get('videoId', '')

        if not all([content, user_id, video_id]):
            return JsonResponse({'code': -1, 'msg': '缺少必要字段'})

        video = Video.objects.get(pk=video_id)
        user = ClientUser.objects.get(pk=user_id)

        #---------------------------------------------------------------------------
        # _comment = Comment.objects.create(content=content, video=video, user=user)
        # comment = vars(_comment)  # 将其转成json对象
        # comment.pop('_state')
        # data = {'comment': comment}
        #---------------------------------------------------------------------------
        # 将其转换成一个函数操作

        comment = Comment.objects.create(content=content, video=video, user=user)
        data = {'comment': comment.data()}
        return JsonResponse({'code': 0, 'msg': 'success', 'data': data})