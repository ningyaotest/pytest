#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : configXML.py
@Author: 姚宁
@Date  : 2021/5/23 1:25
@Desc  :
'''
import xmltodict

import collections
import datetime
import time
import random
import json
import requests
from common.confFile import *
from common.config_redis import redis_cli
from common.configDB import db_connect
from common.signkey_dispose import signkey_info
from common.configXML import *
from common.Loggin import MyLog


def ailjs(merchant_id, total_fee, refund_fee, service):
    '''
    接收测试用例中的测试数据做处理
    '''
    MyLog.info('******交易信息：商户号为：{}，支付类型为：{}，交易金额为{}'.format(merchant_id, service, total_fee))
    res_mchinfo = redis_cli.get('pay.gateway.merchant_' + merchant_id)  # 查询redis缓存信息
    if res_mchinfo:  # 判断缓存是否不为空则执行
        res_json = json.loads(res_mchinfo)
        signKey = res_json['signKey']
        MyLog.info('缓存中获取商户signkey :{}'.format(signKey))
    else:  # db获取signkey
        signKeys_cipher = db_connect(merchant_id)
        MyLog.info('DB中获取商户signkey加密串 :{}'.format(signKeys_cipher))
        signKey = signkey_info(merchant_id)
        signKey = str(signKey)
        MyLog.info('DB中获取商户signkey :{}'.format(signKey))

    if service == 'unified.trade.micropay':
        template_data = Pay_Template_data(mch_id=merchant_id, service=service, total_fee=total_fee,
                                          refund_fee=refund_fee, signKey=signKey)
        jstrade_data = template_data.alipaymicropay_trade()
        trade_body = jstrade_data[0]
        out_trade_no = jstrade_data[1]
        MyLog.debug('**********交易请求报文：{}'.format(trade_body))
        url = value_date
        trade_requests = requests.post(url, data=trade_body.encode('utf-8'))
        MyLog.debug('*******交易响应报文{}'.format(trade_requests.text))
        query_data = template_data.unify_query()
        MyLog.debug('*******请求查询接口报文信息{}'.format(query_data))
        query_requests = requests.post(url, data=query_data.encode('utf-8'))
        MyLog.debug('*******查询接口返回报文信息：{}'.format(query_requests.text))
        xml_parse = json.dumps(xmltodict.parse(query_requests.text), indent=1)
        xml_dict = json.loads(xml_parse)
        select_dict = xml_dict.get('xml')
        if 'trade_state' in select_dict.keys():
            if select_dict.get('trade_state') == "SUCCESS":
                MyLog.debug('订单“{}交易状态为：{}'.format(out_trade_no, select_dict.get('trade_state')))
                if refund_fee == '':
                    return '{"code": 1, "msg": "支付成功"}'
                else:

                    jsrefund_data = template_data.unify_refund()
                    refund_body = jsrefund_data[0]
                    MyLog.debug('**********退款请求报文：{}'.format(refund_body))
                    out_refund_no = jsrefund_data[1]
                    MyLog.debug('**********退款原支付订单号:{},退款订单号:{}'.format(out_trade_no, out_refund_no))
                    refund_requests = requests.post(url, data=refund_body.encode('utf-8'))
                    MyLog.debug('**********退款响应报文:{}'.format(refund_requests.text))
                    return '{"code": 1, "msg": "退款成功"}'
            else:
                MyLog.debug('订单“{}交易状态为：{}'.format(out_trade_no, select_dict.get('trade_state')))
                return '{"code": 0, "msg": "支付失败"}'
        else:
            return '{"code": 0, "msg": "支付失败"}'
    else:
        template_data = Pay_Template_data(mch_id=merchant_id, service=service, total_fee=total_fee,
                                          refund_fee=refund_fee, signKey=signKey)
        jstrade_data = template_data.alipay_trade()
        trade_body = jstrade_data[0]
        out_trade_no = jstrade_data[1]
        MyLog.debug('**********交易请求报文：{}'.format(trade_body))
        url = value_date
        trade_requests = requests.post(url, data=trade_body.encode('utf-8'))
        MyLog.debug('*******交易响应报文{}'.format(trade_requests.text))
        query_data = template_data.unify_query()
        MyLog.debug('*******请求查询接口报文信息{}'.format(query_data))
        query_requests = requests.post(url, data=query_data.encode('utf-8'))
        MyLog.debug('*******查询接口返回报文信息：{}'.format(query_requests.text))
        xml_parse = json.dumps(xmltodict.parse(query_requests.text), indent=1)
        xml_dict = json.loads(xml_parse)
        select_dict = xml_dict.get('xml')
        if 'trade_state' in select_dict.keys():
            if select_dict.get('trade_state') == "SUCCESS":
                MyLog.debug('订单“{}交易状态为：{}'.format(out_trade_no, select_dict.get('trade_state')))
                if refund_fee == '':
                    return '{"code": 1, "msg": "支付成功"}'
                else:
                    jsrefund_data = template_data.unify_refund()
                    refund_body = jsrefund_data[0]
                    MyLog.debug('**********退款请求报文：{}'.format(refund_body))
                    out_refund_no = jsrefund_data[1]
                    MyLog.debug('**********退款原支付订单号:{},退款订单号:{}'.format(out_trade_no, out_refund_no))
                    refund_requests = requests.post(url, data=refund_body.encode('utf-8'))
                    MyLog.debug('**********退款响应报文:{}'.format(refund_requests.text))
                    return '{"code": 1, "msg": "退款成功"}'

            else:
                MyLog.debug('订单“{}交易状态为：{}'.format(out_trade_no, select_dict.get('trade_state')))
                return '{"code": 0, "msg": "支付失败"}'
        else:
            return '{"code": 0, "msg": "支付失败"}'
