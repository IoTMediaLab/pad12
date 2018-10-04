#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
   １２キーPadをスキャンしてキーONをチェック
   https://www.jw-shop.com/P-keyboard-hmodule10/page119/detail.htm
   ↑対象はこれ。（のコピー品と思われる http://www.aitendo.com/product/17251 これ）
'''

import RPi.GPIO as GPIO  #GPIOにアクセスするライブラリをimportします。
import time

#GPIO Define : PIN-NO
C1 = OUT1 = GPIO4  = 7
C2 = OUT2 = GPIO14 = 8
C3 = OUT3 = GPIO15 = 10

R1 = IN1 = GPIO17 = 11
R2 = IN2 = GPIO18 = 12
R3 = IN3 = GPIO27 = 13
R4 = IN4 = GPIO22 = 15


def GPIO_INIT():
    ''' GPIO INIT '''
    GPIO.setmode(GPIO.BOARD) #GPIOへアクセスする番号を ボードのPIN番号とする

    chan_list = [C1,C2,C3]
    GPIO.setup(chan_list,GPIO.OUT)

    chan_list = [R1,R2,R3,R4]
    GPIO.setup(chan_list,GPIO.IN)



def get():

    c_list = [C1,C2,C3]
    r_list = [R1,R2,R3,R4]
    #GPIO.output(chan_list,GPIO.HIGH)

    for i,c in enumerate(c_list):
        GPIO.output(c,GPIO.HIGH)
        for j,r in enumerate(r_list):
            print('C'+str(j+1),GPIO.input(r),'  ',end='')
        GPIO.output(c,GPIO.LOW)
        print(' ')


if __name__ == '__main__':
    ''' テスト用メイン関数 '''
    GPIO_INIT()

    while(1):
        get()

    GPIO.cleanup()
