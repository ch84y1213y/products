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

#存取二維清單
products[0][0] #將第0個商品的name拿出來
products[1][1] #將第1個商品的price拿出來