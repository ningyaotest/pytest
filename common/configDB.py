#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : configDB.py
@Author: 姚宁
@Date  : 2021/5/23 0:04
@Desc  : 
'''
import cx_Oracle
from common.confFile import *
from common.Loggin import MyLog


def db_connect(mch_id):
    # 传入商户号连接DB查询商户的signkey加密串
    MERCHANT_ID = mch_id
    # 连接数据库，下面括号里内容根据自己实际情况填写

    db_url = oracle_use + '/' + oracle_pwd + '@' + oracle_listener  # 拼接DB连接信息

    conn = cx_Oracle.connect(db_url, encoding="UTF-8")  # 调用cx_oracle连接oracle
    cursor = conn.cursor()
    sql = 'select sign_key from CMS_MERCHANT  where MERCHANT_ID=:MERCHANT_ID'
    sql_id = {'MERCHANT_ID': MERCHANT_ID}
    cursor.execute(sql, sql_id)  # 执行sql语句
    select_result = cursor.fetchall()  # 用变量接收查询到的结果
    select_result = str(select_result)  # 将查询到的结果转化为str
    signKeys_cipher = select_result[3:-4]  # 用字符串切片方式截取调包装的部分
    MyLog.info('=========交易商户signkey加密串信息：{}=========='.format(signKeys_cipher))
    return signKeys_cipher
    cursor.close()
    conn.close()
