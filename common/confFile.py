#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : confFile.py
@Author: 姚宁
@Date  : 2021/5/23 21:07
@Desc  : 
'''
import configparser
from os import path

config = configparser.ConfigParser()
path = path.join(path.dirname(path.abspath(__file__)), '../settings/config.ini')
# path = r'../settings/config.ini'
config.read(path)
# 网关请求地址信息
value_date = config['select']['gateway_url']

# redis配置信息
redis_host = config['redis_service']['host']
redis_port = config['redis_service']['port']
redis_auth = config['redis_service']['auth']

# oracle连接信息
oracle_listener = config['oracle_db']['listener']
oracle_use = config['oracle_db']['user']
oracle_pwd = config['oracle_db']['password']






