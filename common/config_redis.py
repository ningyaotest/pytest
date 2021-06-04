#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@File  : config_redis.py
@Author: 姚宁
@Date  : 2021/5/27 16:41
@Desc  : 
'''
import redis
from common.confFile import *
redis_cli = redis.Redis(host=redis_host, port=redis_port, password=redis_auth, decode_responses=True)