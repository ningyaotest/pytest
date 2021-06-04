#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : sst_cs.py
@Author: 姚宁
@Date  : 2021/5/25 23:45
@Desc  : 
'''
import unittest
import json
from ddt import ddt,data
from testdata.test_data_handler import get_data_from_excel
from Pay_request.haa import minzi
cases = get_data_from_excel('../testdata/testcase_data.xlsx', sheet_name='Alipay')

@ddt
class Testcst():
    @data(*cases)
    def test(self,case):
        res_service=json.loads(case['service'])
        request_data = json.loads(case['requrs_data'])
        res_type=minzi(**res_service,**request_data)
        print(res_type)
    def testyl(self,case):
        res_service=json.loads(case['service'])
        request_data = json.loads(case['requrs_data'])
        res_type=minzi(**res_service,**request_data)
        print(res_type)
if __name__ == '__main__':
    unittest.main()

