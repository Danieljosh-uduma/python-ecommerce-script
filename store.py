import random

class Store:
    def __init__(self):
        self.store = []
        self.amount = []
        self.qty = []
        self.stores = {
            1:'food stuff store',
            2:'beverages store',
        }
    
    def display(self):
        print('This is the stores we have ')
        print(self.stores[1].title())
        print(self.stores[2].title())
        

class Food_stuff(Store):
    def __init__(self):
        super().__init__()
        self.__store = {
            'rice':{'price':15000,'qty':10},
            'garri':{'price':2500,'qty':43},
            'semo':{'price': 1500,'qty': 13},
            'yam':{'price':3700,'qty': 50},
            'wheat':{'price':3000,'qty':10},
            'corn':{'price':350,'qty':90},
            'flour':{'price':7000,'qty':50},
            'spaghetti':{'price':950,'qty':25},
            'noodle':{'price':500,'qty':1000},
            'paste':{'price':200,'qty':500},
            'seasonings':{'price':450,'qty':50},
            'bread':{'price':1300,'qty':1000},
            'groundnut oil':{'price':1800,'qty':150},
            'soya oil':{'price':5000,'qty':30},
            'butter':{'price':680,'qty':430},
            'magarine':{'price':1000,'qty':350},
            'olive oil':{'price':7000,'qty':46},
            'beans':{'price':1300,'qty':70},
            'biscuit':{'price':1200,'qty':670},
            'cupcake':{'price':2300,'qty':25},
            'french fries':{'price':1000,'qty':50}
        }
        
    def display(self):
        x = random.randint(0,20)
        print('Some Items in foodstuff store....')
        item_list = list(self.__store.keys())
        print(item_list[x])
        print(item_list[x-1])
        print(item_list[x-2])
        print(item_list[x-3])
        print('....')
        
    
    def search(self):
        search = input('search for an item here:  ')
        for x,obj in self.__store.items():
            if search == x:
                print(x.title())
                for i in obj:
                    print(f'{i}: {obj[i]}')
                    print(f'you can add {search} to cart')
                break
        else:
            print(f'{search} not available, we are sorry about that')
            self.search()   
    
    def add_cart(self):
        item = input('Enter item you want to buy: ')
        try:
            x = list(self.__store[item].keys())
            y = self.__store[item][x[0]]
            z = self.__store[item][x[1]]
            if item in self.__store:
                if z <= 0:
                    print('unavaialable')
                else:
                    print(f'Price: N{y}')
                    qty = int(input('enter the quantity you want... '))
                    if (z-qty)<0:
                        print(f'we have {z} quantity available')
                    else:
                        print(item.title())
                        print(f'Quantity: {qty}')
                        self.__store[item][x[1]]= z-qty
                        total = y*qty
                        print(f'Total price: N{total}')
                        self.store.append(item)
                        self.amount.append(total)
                        self.qty.append(qty)
        except:
            print(f'{item} unavailable or an error occurred') 
            self.search()

    def delete_item(self):
        item = input('Enter item name: ')
        if item in self.store:
            x = self.store.index(item)
            qty = int(input('enter the qty you want to remove: '))
            if qty < self.qty[x]:
                self.qty[x] = self.qty[x] - qty
                y = list(self.__store[item].keys())
                total_price = (qty)*(self.__store[item][y[0]])
                self.amount[x] -= total_price
            elif qty > self.qty[x]:
                print(f'you have {self.qty[x]} in your cart')
            elif int(qty) == self.qty[x] or qty == 'all':
                del self.store[x], self.amount[x], self.qty[x]
            else: 
                print('wrong value or syntax')
        else:
            print(f'{item} not available')

    def empty_cart(self):
        self.store.clear()
        self.amount.clear()     
        self.qty.clear()

    def restock_store(self):
        r_item = input('enter name of item you')
        if r_item in self.__store: 
            x = self.__store[r_item]
            n_qty = int(input('enter the qty: '))
            n_price = int(input('enter price of unit: '))
            x['price'] = n_price
            x['qty'] = n_qty
            print(x)
        else:
            print('do you want to enter a new product?')
            ans = input('enyer yes/no: ')
            if ans == 'yes':
                name = input('comfirm product name: ')
                if name==r_item:
                    price = int(input('enter price of goods: '))
                    qty = int(input('enter quantity:'))
                    value = {
                        'price': price,
                        'qty': qty
                    }
                    item = {name: value}
                    self.__store.update(item)
                else:
                    print('try inputing the correct value...')
                    self.restock_store()
            else:
                print('item unavailable')
                self.restock_store()


class Beverage(Food_stuff):
    def __init__(self):
        super().__init__()
        self.__store = {
            'chocolate':{'price':500,'qty':100},
            'milk':{'price':550,'qty':50},
            'butter':{'price':670,'qty':98},
            'wine':{'price':7500,'qty':70},
            'biscuit':{'price':350,'qty':1000},
            'juice':{'price':2300,'qty':28},
            'smoothy':{'price':10000,'qty':30},
            'coke':{'price':350,'qty':500},
            'fanta':{'price':350,'qty':500},
            'pepsi':{'price':350,'qty':500},
            'coffee':{'price':400,'qty':59},
            'water':{'price':200,'qty':1200},
            'beer':{'price':650,'qty':70},
        }
    def display(self):
        x = random.randint(0,12)
        print('Some Items in foodstuff store....')
        item_list = list(self.__store.keys())
        print(item_list[x])
        print(item_list[x-1])
        print(item_list[x-2])
        print(item_list[x-3])
        print('....')

    def search(self):
        search = input('search for an item here:  ')
        for x,obj in self.__store.items():
            if search == x:
                print(x.title())
                for i in obj:
                    print(f'{i}: {obj[i]}')
                    print('you can add item to your cart')
                    print(f'you can add {search} to cart')
                break
        else:
            print(f'{search} not available, we are sorry about that')
            self.search()

    def add_cart(self):
        item = input('Enter item you want to buy: ')
        try:
            x = list(self.__store[item].keys())
            y = self.__store[item][x[0]]
            z = self.__store[item][x[1]]
            if item in self.__store:
                if z <= 0:
                    print('unavaialable')
                else:
                    print(f'Price: N{y}')
                    qty = int(input('enter the quantity you want... '))
                    if (z-qty)<0:
                        print(f'we have {z} quantity available')
                    else:
                        print(item.title())
                        print(f'Quantity: {qty}')
                        self.__store[item][x[1]]= z-qty
                        total = y*qty
                        print(f'Total price: N{total}')
                        self.store.append(item)
                        self.amount.append(total)
                        self.qty.append(qty)
        except:
            print(f'{item} unavailable or an error occurred')
            self.search()
     
    def delete_item(self):
        item = input('Enter item name: ')
        if item in self.store:
            x = self.store.index(item)
            qty = int(input('enter the qty you want to remove: '))
            if qty < self.qty[x]:
                self.qty[x] = self.qty[x] - qty
                y = list(self.__store[item].keys())
                total_price = (qty)*(self.__store[item][y[0]])
                self.amount[x] -= total_price
            elif qty > self.qty[x]:
                print(f'you have {self.qty[x]} in your cart')
            elif int(qty) == self.qty[x] or qty == 'all':
                del self.store[x], self.amount[x], self.qty[x]
            else: 
                print('wrong value or syntax')
        else:
            print(f'{item} not available')

    def empty_cart(self):
        self.store.clear()
        self.amount.clear()     
        self.qty.clear()
    
    def restock_store(self):
        r_item = input('enter name of item you')
        if r_item in self.__store: 
            x = self.__store[r_item]
            n_qty = int(input('enter the qty: '))
            n_price = int(input('enter price of unit: '))
            x['price'] = n_price
            x['qty'] = n_qty
            print(x)
        else:
            print('do you want to enter a new product?')
            ans = input('enyer yes/no: ')
            if ans == 'yes':
                name = input('comfirm product name: ')
                if name==r_item:
                    price = int(input('enter price of goods: '))
                    qty = int(input('enter quantity:'))
                    value = {
                        'price': price,
                        'qty': qty
                    }
                    item = {name: value}
                    self.__store.update(item)
                else:
                    print('try inputing the correct value...')
                    self.restock_store()
            else:
                print('item unavailable')
                self.restock_store()