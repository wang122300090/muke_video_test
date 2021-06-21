# coding: utf-8

from celery import task
import os
from app.libs.base_qiniu import video_qiniu
from app.models import Video, VideoSub
import time

# 先启动celery:python manage.py celery worker -c 4 --loglevel=info

@task
def video_task(command, out_path, path_name, video_file_name, video_sub_id):
    # celery队列中,不能加上对象的
    from app.utils.common import remove_path
    os.system(command)

    out_name = '.'.join([out_path, 'mp4'])
    if not os.path.exists(out_name):
        remove_path([out_name, path_name])  # 上传失败,删掉本地的中转视频
        return False
    final_name = '{}_{}'.format(int(time.time()), video_file_name)
    url = video_qiniu.put(final_name, out_name)
    # print(url)
    if url:
        try:
            video_sub = VideoSub.objects.get(pk=video_sub_id)
            video_sub.url = url
            video_sub.save()
            return True
        except:
            remove_path([out_name, path_name])
            return False
    remove_path([out_name, path_name])