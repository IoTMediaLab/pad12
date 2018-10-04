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
