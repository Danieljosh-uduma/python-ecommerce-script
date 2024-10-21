import _info
import store
import payment


#name of company
company_name = 'Josh Super Store'
address = 'ago palace'

#greeting customers
print(f'Hello FRIEND, welcome to {company_name}')
print('This is a place where you can find everything you want, just name it...\n\n')

#customer logging in or signing in
print('You need to sign in or log in before you can use this product')
print('Do you have an account?\nEnter yes or no')
ans = input()
user = _info.Profile()
if ans == 'yes':
    print(f'Welcome to {company_name}')
    print('LOG IN')
    user.log_in()
    
else:
    print(f'Welcome to {company_name}')
    print('SIGN IN')
    user.sign_in()
    user.log_in()
    
myStore = store.Store()

#choosing a store
def Ans_store():
    #customer look for product available
    myStore.display()
    print('\nwhich store will you like....')
    global ans_store
    ans_store = input('enter food stuff or beverages\n')
 
Ans_store()   
if ans_store == 'food stuff':
    myStore = store.Food_stuff()
    myStore.display()
elif ans_store == 'beverages':
    myStore = store.Beverage()
    myStore.display()
else:
    print('enter a correct name')
    Ans_store()
    
#searching and picking items
def work():
    try:
        global time
        time = int(input('how many items will you like to add to your cart: '))
    except:
        print('enter the number of items to add to cart')
        work()
    print('you can add item to you cart by typing the name\nyou can also search for items\n')
    while time > 0:
        myStore.add_cart()
        if time <= 1:
            ans_time = input('are you done adding to cart?\nyes/no: ')
            if ans_time == 'no':
                work()
            else:
                break
        time -= 1
    
work()

#done selecting what they want 
print('yhew finally done')

#print out items in the cart
item_price = []
for x,y in zip(myStore.store,myStore.amount):
    k = x + ': N' + str(y)
    item_price.append(k)

item_qty = []
for x,y in zip(item_price,myStore.qty):
    k = x + ' qty: '+ str(y)
    item_qty.append(k)
    
for x in item_qty:
    print(x)
    
#removing items
def rm_item():
    print('\nWould you like to remove any item from the list')
    global ans_rm
    ans_rm = input('enter yes or no: ')

    global total
    total = 0
    if ans_rm=='yes':
        myStore.delete_item()
        rm_item()
    else:
        for x in myStore.amount:
            total += x
        print(f'total amount: N{total}\n')
    
rm_item()


#paying section
def pay_amt():
    pay = payment.Pay(total,item_qty)
    pay.gen_file()
    
pay_amt()

#loging out
print('\tHow was your experience with us?')
review = input('Enter your review and any problem you\'ll like us to fix\n(if you have no review just enter none)\n')
if review != 'none':
    with open('review.txt', 'a') as file:
        name = input('\nenter user name: ')
        file.write(f'\n***{name}: {review}\n')
        
print('\nDo you want to log out or continue buying items you need?')
ans_log = input('Enter log out/continue: ')
if ans_log=='log out':
    user.log_out()
    Ans_store()
else:
    Ans_store()