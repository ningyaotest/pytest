#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@File  : signkey_dispose.py
@Author: 姚宁
@Date  : 2021/5/27 16:33
@Desc  :
'''
import json
import jpype
from jpype import *
from common.configDB import *


def signkey_info(mch_id):
    # 使用jpype 三方库调用java的jar解密商户signkey
    siginfo = db_connect(mch_id=mch_id)
    jvmPath = jpype.getDefaultJVMPath()
    # java扩展包路径
    ext_classpath = r'D:\paytest\jar\merchantdecrypt.jar'
    jvmArg = '-Djava.class.path=%s' % ext_classpath
    if not jpype.isJVMStarted():
        # 启动Java虚拟机
        jpype.startJVM(jvmPath, "-ea", jvmArg)
    JDClass = JClass("com.example.merchantdecrypt.utils.AesUtils")
    jd = JDClass()
    # jprint = java.lang.System.out.println
    signKey = jd.decrypt(siginfo, 'b0ab929094524f53')  # 调用decrypt方法解密
    MyLog.info('调用解密接口解密商户signkey，解密结果为 :{}'.format(signKey))
    return signKey
    shutdownJVM()
