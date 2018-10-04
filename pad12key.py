#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
   １２キーPadをスキャンしてキーONをチェック
   https://www.jw-shop.com/P-keyboard-hmodule10/page119/detail.htm
   ↑対象はこれ。（のコピー品と思われる http://www.aitendo.com/product/17251 これ）

   他のプログラムから呼び出すときは、

    #初期設定
    import pad12key
    pad12key.GPIO_INIT()
    #↑これは最初に一度だけ実行

    #その後、
    keyNo = pad12key.get()
    #↑これでkeyNoに1～12までが入ります。
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
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD) #GPIOへアクセスする番号を ボードのPIN番号とする

    chan_list = [R1,R2,R3,R4]
    GPIO.setup(chan_list,GPIO.OUT)

    chan_list = [C1,C2,C3]
    GPIO.setup(chan_list,GPIO.IN)

def get():
    ''' キーをスキャンしてキー番号 1～12をint値で返す '''
    c_list = [C1,C2,C3]
    r_list = [R1,R2,R3,R4]

    ret = 0

    for i,r in enumerate(r_list):
        GPIO.output(r,GPIO.HIGH)
        for j,c in enumerate(c_list):
            #print('R'+str(j+1),GPIO.input(c),'  ',end='')
            if(GPIO.input(c)):
               ret = j + i*3 +1
        GPIO.output(r,GPIO.LOW)
    #print(':',ret)
    return ret


if __name__ == '__main__':
    ''' テスト用メイン関数 '''
    GPIO_INIT()

    while(1):
      print(get())

    GPIO.cleanup()
