#!/usr/bin/python3.6
#_*_coding:utf-8_*_
import time,sys
sys.path.append('./interface')
sys.path.append('./db_fixture')
from HTMLTestRunner import HTMLTestRunner
import unittest
from db_fixture import test_data

#指定测试用例为当前文件夹下的interface目录
test_dir = './interface'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='*_test.py')    #匹配文件名为_test.py结尾的测试文件

if __name__=='__main__':
    test_data.init_data()
    now = time.strftime('%Y-%m-%d %H_%M_%S')    #获取当前时间并转化成 2018-12-11 00:58:00的格式
    filename = './report/' + now + '_result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,title='Guest Manage System Interface Test Report',description='Implementation Example wigh:')
    runner.run(discover)
    fp.close()
