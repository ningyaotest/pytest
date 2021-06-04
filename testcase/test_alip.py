#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : test_alip.py
@Author: 姚宁
@Date  : 2021/5/23 22:38
@Desc  : 
'''
import unittest
import json
from os import path
from ddt import ddt, data
from testdata.test_data_handler import get_data_from_excel
from Pay_request.ailpayv4 import ailjs
from common.Loggin import MyLog

path = path.join(path.dirname(path.abspath(__file__)), '../testdata/testcase_data.xlsx')
cases = get_data_from_excel(path, sheet_name='Alipay')


@ddt
class AlipayTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        MyLog.info('==============网关交易接口测试开始=================')

    def setUp(self) -> None:
        MyLog.info('==============开始执行【银联支付宝】接口测试用例=================')

    def tearDown(self) -> None:
        MyLog.info('==============执行【银联支付宝】接口测试用例结束=================')

    @classmethod
    def tearDownClass(cls):
        MyLog.info('==============网关交易接口测试结束=================')

    @data(*cases)
    def testalipay(self, case):
        request_data = json.loads(case['requrs_data'])
        request_service = json.loads(case['service'])
        request_title = (case['title'])
        excepted_data = (case['excepted_data'])
        res = ailjs(**request_data, **request_service)
        try:
            self.assertEqual(excepted_data, res)
            MyLog.info('{}：测试结果：成功'.format(request_title))
            MyLog.info('用例执行成功：预期结果为：{}实际结果与预期结果匹配'.format(str(excepted_data)))

        except Exception as e:
            MyLog.error('{}：测试结果：失败'.format(request_title))
            MyLog.error('用例执行失败：预期结果为：{}实际结果为：{}'.format(str(excepted_data),str(request_data)))

            raise e


if __name__ == '__main__':
    unittest.main()
