# coding: utf-8
import multiprocessing

bind = "127.0.0.1:8003"
workers = multiprocessing.cpu_count() - 1
worker_class = 'gevent' # 有多种方式,这里是协程的方式