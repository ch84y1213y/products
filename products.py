products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q': #quit離開
	    break
	price = input('請輸入商品價格: ')   
	p = [] #建立小清單 
	p.append(name) #將資料加進小清單中
	p.append(price)
	products.append(p) #將小清單加入大清單中
print(products)	
#7~9行可以簡略成 p = [name, price]，或第10行直接簡略成products.append([name, price])

with open('products.csv', 'w', encoding='utf-8') as f: #w為寫入模式，本行僅為打開檔案
	#encoding為編碼，為解決亂碼問題，utf-8最廣泛使用之編碼
	f.write('商品, 價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n') #本行才是做真正寫入

#存取二維清單
products[0][0] #將第0個商品的name拿出來
products[1][1] #將第1個商品的price拿出來

