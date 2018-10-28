#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/29 0:34
# @Author  : caijiangchun
# @Site    : 
# @File    : sys1.py
# @Software: PyCharm
import sys
if __name__ == '__main__':

    print("命令行参数个数： %d" % len(sys.argv))
    print("命令行参数列表： %s" % str(sys.argv))
