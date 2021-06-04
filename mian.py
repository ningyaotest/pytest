#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : mian.py
@Author: 姚宁
@Date  : 2021/5/23 22:24
@Desc  : 
'''
import unittest
from BeautifulReport import BeautifulReport
if __name__ == '__main__':
    #收集测试用例
    ts = unittest.TestLoader().discover('testcase/.')
    print(ts)
    #运行测试用例输出测试报告
    runner = BeautifulReport(ts)
    runner.report(description='自动化测试报告', filename='test_report', report_dir='reports')
