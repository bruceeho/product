import os
#讀取檔案
def read_file(filename):
    products = []#大清單
    with open(filename,'r',encoding = 'UTF-8') as f:
        for line in f:
            if '商品,價格,數量,總金額' in line:
                continue
            name,price,quantity,total = line.strip().split(',')
            products.append([name,price,quantity,total])
    return products
#讓使用者輸入
def user_input(products):
    while True:
        name = input('請輸入商品名稱：')
        if name == 'q':
            break
        price = int(input('請輸入商品價價格：'))
        quantity = int(input('請輸入數量：'))
        total = price*quantity
        #第一種寫法
        #p = []#小清單
        #p.append(name)#新增商品名稱至小清單
        #p.append(price)#新增價格至小清單
        #第二種寫法
        #p = [name,price]
        #products.append(p)
        #最精簡的寫法
        products.append([name,price,quantity,total])
    print(products)
    return products
#印出所有購買紀錄
def print_products(products):
    for p in products:
        print('商品：',p[0],'價格：',p[1],'數量：',p[2],'總金額',p[3])
#寫入檔案
def write_file(filename, products):
    with open(filename,'w', encoding = 'UTF-8') as f:
        f.write('商品,價格,數量,總金額\n')
        for p in products:
           f.write(p[0] + ',' + str(p[1]) + ',' + str(p[2]) + ',' + str(p[2]) + '\n')

def main():
    filename = 'products.csv'
    if os.path.isfile(filename):#檢查檔案是否存在
        print('已找到檔案')
        products = read_file(filename)
    else:
        print('找不到檔案')
    products = user_input(products)
    print_products(products)
    write_file('produsts.csv', products)

main()