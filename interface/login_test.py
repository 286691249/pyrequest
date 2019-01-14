#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
import requests
from db_fixture.mysql_db import MysqldbHelper

class LoginTest(unittest.TestCase):
    '''手机号登录测试'''

    @classmethod
    def setUpClass(self):
        print('----------开始执行用例-----------\n')
        self.base_url = 'https://aq.api.shan666.com/api.php?m=Safe&a=login&sign=340431964b4a3ecbd979ac220661897a'

    @classmethod
    def tearDownClass(self):
        print('----------用例执行结束----------\n')

    def test_login_phone_null(self):
        '''手机号为空'''
        payload={
            'res' :'1080 * 1920',
            'app_type': '4',
            'code': '',
            'os': 'ios',
            'user_name': '',
            'channel':'taojj',
            'scope_code': '1546952978',
            'version': '2.11.1',
            'uuid':'3CB505E9-8254-4D26-8E02-9277CAA9EDAA',
            'system_model': 'iPhone',
            'system_version': '12.1',
            'imei': '8f6861a59b334b8_',
            'timestamp': '1546953028'
        }
        r=requests.post(self.base_url,data=payload,verify=False)
        self.result=r.json()
        self.assertEqual(self.result['result'],-1)
        self.assertEqual(self.result['message'],'请正确传入手机号信息!')

    def test_login_phone_error(self):
        '''手机号格式错误'''
        payload={
            'res' :'1080 * 1920',
            'app_type': '4',
            'code': '1234',
            'os': 'ios',
            'user_name': '113321223',
            'channel':'taojj',
            'scope_code': '1546952978',
            'version': '2.11.1',
            'uuid':'3CB505E9-8254-4D26-8E02-9277CAA9EDAA',
            'system_model': 'iPhone',
            'system_version': '12.1',
            'imei': '8f6861a59b334b8_',
            'timestamp': '1546953028'
        }
        r=requests.post(self.base_url,data=payload,verify=False)
        self.result=r.json()
        self.assertEqual(self.result['result'],-1)
        self.assertEqual(self.result['message'],'手机号码格式不正确!')

    def test_login_wrong_code(self):
        '''验证码错误'''
        payload={
            'res' :'1080 * 1920',
            'app_type': '4',
            'code': '1234',
            'os': 'ios',
            'user_name': '13797802070',
            'channel':'taojj',
            'scope_code': '1546952978',
            'version': '2.11.1',
            'uuid':'3CB505E9-8254-4D26-8E02-9277CAA9EDAA',
            'system_model': 'iPhone',
            'system_version': '12.1',
            'imei': '8f6861a59b334b8_',
            'timestamp': '1546953028'
        }
        r=requests.post(self.base_url,data=payload,verify=False)
        self.result=r.json()
        self.assertEqual(self.result['result'],-1)
        self.assertEqual(self.result['message'],'用户注册失败：您尚未获取验证码或验证码已过期。')

    def test_login_oldUser_success(self):
        '''老用户登录成功'''

        helper = MysqldbHelper()
        selectResult=helper.executeSelect('select user_id from cbd_users where user_name=13797802071')
        if selectResult:
            pass
        else:
            helper.executeInsert('insert into cbd_users values "1379797802071"')
        payload={
            'res' :'1080 * 1920',
            'app_type': '4',
            'code': '1234',
            'os': 'ios',
            'user_name': '13797802071',
            'channel':'taojj',
            'scope_code': '1546952978',
            'version': '2.11.1',
            'uuid':'3CB505E9-8254-4D26-8E02-9277CAA9EDAA',
            'system_model': 'iPhone',
            'system_version': '12.1',
            'imei': '8f6861a59b334b8_',
            'timestamp': '1546953028'
        }
        r = requests.post(self.base_url,data=payload,verify=False)
        result=r.json()

if __name__=='__main__':
    LoginTest.main()