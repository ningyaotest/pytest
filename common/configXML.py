#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : configXML.py
@Author: 姚宁
@Date  : 2021/6/1 22:30
@Desc  : 
'''

import datetime
import json
import random
import xmltodict
import collections
from common.Loggin import MyLog


class Pay_Template_data():

    def __init__(self, mch_id, service, total_fee, refund_fee, signKey):
        self.mch_id = mch_id
        self.service = service
        self.total_fee = total_fee
        self.refund_fee = refund_fee
        self.signKey = signKey
        self.order_info = self.mch_id + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + str(random.randint(0, 9))
        self.out_trade_no = self.order_info
        self.refund_info = self.mch_id + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + str(random.randint(0, 99))
        self.out_refund_no = self.refund_info
        MyLog.info('******交易信息：商户订单号为：{}'.format(self.out_trade_no))

    def alipay_trade(self):
        with open('D:/paytest/templates/Alipayv4_jspay.xml', encoding='utf-8') as fb:
            res_xml = fb.read()

        dic_response = xmltodict.parse(res_xml)  # XML文件内容转化为类字典
        dic_jsorder = dict(dic_response)  # 类字典转化为dict

        for key, value in dic_jsorder.items():  # 遍历dict
            value = dict(value)
            for k, v in value.items():  # 用变量修改对应的值
                value['mch_id'] = f"{self.mch_id}"
                value['total_fee'] = f"{self.total_fee}"
                value['signKey'] = f"{self.signKey}"
                value['out_trade_no'] = f"{self.out_trade_no}"
                value['service'] = f"{self.service}"
            value = collections.OrderedDict(value)
        dict_jsorder = {key: value}
        dict_jsorder = collections.OrderedDict(dict_jsorder)
        dict_jsorder = xmltodict.unparse(dict_jsorder, pretty=True)
        json_jsorder = json.dumps(xmltodict.parse(dict_jsorder), indent=1)
        xml_dict = json.loads(json_jsorder)
        extract_orderinfo = xml_dict.get('xml')
        order = extract_orderinfo.get('out_trade_no')

        return dict_jsorder, order

    def alipaymicropay_trade(self):
        with open('D:/paytest/templates/Alipayv4_micropay.xml', encoding='utf-8') as fb:
            res_xml = fb.read()

        dic_response = xmltodict.parse(res_xml)  # XML文件内容转化为类字典
        dic_jsorder = dict(dic_response)  # 类字典转化为dict

        for key, value in dic_jsorder.items():  # 遍历dict
            value = dict(value)
            for k, v in value.items():  # 用变量修改对应的值
                value['mch_id'] = f"{self.mch_id}"
                value['total_fee'] = f"{self.total_fee}"
                value['signKey'] = f"{self.signKey}"
                value['out_trade_no'] = f"{self.out_trade_no}"
                value['service'] = f"{self.service}"
            value = collections.OrderedDict(value)
        dict_jsorder = {key: value}
        dict_jsorder = collections.OrderedDict(dict_jsorder)
        dict_jsorder = xmltodict.unparse(dict_jsorder, pretty=True)
        json_jsorder = json.dumps(xmltodict.parse(dict_jsorder), indent=1)
        xml_dict = json.loads(json_jsorder)
        extract_orderinfo = xml_dict.get('xml')
        order = extract_orderinfo.get('out_trade_no')

        return dict_jsorder,order

    def unify_query(self):
        with open('D:/paytest/templates/unified.trade.query.xml', encoding='utf-8') as fb:
            res_xml = fb.read()

        dic_response = xmltodict.parse(res_xml)  # XML文件内容转化为类字典
        dic_query = dict(dic_response)  # 类字典转化为dict

        for key, value in dic_query.items():  # 遍历dict
            value = dict(value)
            for k, v in value.items():  # 用变量修改对应的值
                value['mch_id'] = f"{self.mch_id}"
                value['signKey'] = f"{self.signKey}"
                value['out_trade_no'] = f"{self.out_trade_no}"
            value = collections.OrderedDict(value)
        dict_query = {key: value}
        dict_query = collections.OrderedDict(dict_query)
        dict_query = xmltodict.unparse(dict_query, pretty=True)
        return dict_query

    def unify_refund(self):

        with open('D:/paytest/templates/unified.refund.xml', encoding='utf-8') as fb:
            res_xml = fb.read()

        dic_response = xmltodict.parse(res_xml)  # XML文件内容转化为类字典
        dic_query = dict(dic_response)  # 类字典转化为dict

        for key, value in dic_query.items():  # 遍历dict
            value = dict(value)
            for k, v in value.items():  # 用变量修改对应的值
                value['mch_id'] = f"{self.mch_id}"
                value['signKey'] = f"{self.signKey}"
                value['total_fee'] = f"{self.total_fee}"
                value['refund_fee'] = f"{self.refund_fee}"
                value['out_refund_no'] = f"{self.out_refund_no}"
                value['out_trade_no'] = f"{self.out_trade_no}"
            value = collections.OrderedDict(value)
        dict_refund = {key: value}
        dict_refund = collections.OrderedDict(dict_refund)
        dict_refund = xmltodict.unparse(dict_refund, pretty=True)
        json_refund = json.dumps(xmltodict.parse(dict_refund), indent=1)
        xml_dict = json.loads(json_refund)
        extract_refundinfo = xml_dict.get('xml')
        refund = extract_refundinfo.get('out_trade_no')

        return dict_refund,refund
