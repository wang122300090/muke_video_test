# coding: utf-8

import os
import time
from django.conf import settings  # 这里是对的
import shutil
from app.libs.base_qiniu import video_qiniu
from app.models import VideoSub, Video


def check_and_get_video_type(type_obj, type_value, message):
    try:
        type_obj(type_value)
    except:
        return {'code': -1, 'msg': message}
    return {'code': 0, 'msg': 'success'}

def remove_path(paths):
    for path in paths:
        if os.path.exists(path):
            os.remove(path)

def handle_video(video_file, video_id, number):
    in_path = os.path.join(settings.BASE_DIR, 'app/dashboard/temp-in')
    out_path = os.path.join(settings.BASE_DIR, 'app/dashboard/temp-out')
    # print(video_file, video_id, number)
    # print(settings.BASE_DIR)  # 这个地址就到video
    #将上传的视频存在这个temp文件夹中
    name = '{}_{}'.format(int(time.time()), video_file.name)
    path_name = '/'.join([in_path, name])

    temp_path = video_file.temporary_file_path()
    shutil.copyfile(temp_path, path_name)  # 复制文件

    out_name = '{}_{}'.format(int(time.time()), video_file.name.split('.')[0])
    out_path = '/'.join([out_path, out_name])
    # print(path_name, out_path)
    # os.system('ls')  #使用os.system来实现是命令行的功能,在video目录下
    command = 'ffmpeg -i {} -vcodec copy -acodec copy {}.mp4'.format(path_name, out_path)
    os.system(command)

    out_name = '.'.join([out_path, 'mp4'])
    if not os.path.exists(out_name):
        remove_path([out_name, path_name])  # 上传失败,删掉本地的中转视频
        return False
    url = video_qiniu.put(video_file.name, out_name)
    # print(url)
    if url:
        video = Video.objects.get(pk=video_id)

        try:
            VideoSub.objects.create(
                video=video,
                url=url,
                number=number
            )
            return True
        except:
            remove_path([out_name, path_name])
            return False
    remove_path([out_name, path_name])
    return False


