products = []#大清單
while True:
    name = input('請輸入商品名稱：')
    if name == 'q':
        break
    price = input('請輸入商品價價格：')
    #第一種寫法
    #p = []#小清單
    #p.append(name)#新增商品名稱至小清單
    #p.append(price)#新增價格至小清單
    #第二種寫法
    #p = [name,price]
    #products.append(p)
    #最精簡的寫法
    products.append([name,price])

print(products)