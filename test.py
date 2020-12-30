# coding:utf-8

import os

# class 이해하기

class classA():
    def __init__(self):
        print 'start class'

    def push_command(self, ver):
        print 'push %s' %ver

    def run_command(self):
        print 'run'


classA().push_command('button')
