# pad12
12key pad with raspberry pi

１２キーPadをスキャンしてキーONをチェック  
https://www.jw-shop.com/P-keyboard-hmodule10/page119/detail.htm  
↑対象はこれ。（のコピー品と思われる http://www.aitendo.com/product/17251 これ）  

他のプログラムから呼び出すときは、  

~~~
 #初期設定  
 import pad12key  
 pad12key.GPIO_INIT()  
 #↑これは最初に一度だけ実行  

 #その後、  
 keyNo = pad12key.get()  
 #↑これでkeyNoに1～12までが入ります。
~~~

----

接続結線  


|KeyPad側→|0|1|2|3|4|5|6|7|  
|--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| |GND|COL2|ROW1|COL1|ROW4|COL3|ROW3|ROW2|  
|RasPi側Pin→|6|8|11|7|15|10|13|12|  

