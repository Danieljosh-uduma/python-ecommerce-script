import _info
import datetime

class Pay:
    def __init__(self, amount, items):
        self.amount = amount
        self.items = items
        self.__info = _info.Profile()
        self.user_name = input('Enter user name: ')
        self.password = self.__info.password
        self.file = self.user_name+'.txt'
        self.user_file = 'general_user.txt'
        self.time = datetime.datetime.now()
        self.date = self.time.strftime('%D')+self.time.strftime('%M')+self.time.strftime('%Y')
        
    def pay_bank(self):
        bank = input('Enter bank name: ')
        acct_number = input('Enter account number: ')
        if len(acct_number)==10:
            pin = input('Enter pin: ')
            if len(pin)==4 and type(int(pin)) is int:
                password = input('Enter password: ')
                if password in self.password:
                        print('payment successful')
                        print(f'paid N{self.amount}')
                        with open(self.file, 'a') as file:
                            file.write(f'***{self.time}')
                            file.write(f'\nyou bought {str(self.items)}\nand total money paid is N{self.amount}')
                            file.write('\npayment successful\npaid N{self.amount}')
                            file.write('\nPaid with bank account\n\n')
                else:
                    print('wrong password')
                    self.pay_bank()
            #elif not type(int(pin)) is int:
             #   print('enter four digit pin')
              #  self.pay_bank()
            else:
                print('enter four digit pin')
                self.pay_bank()
        else:
            print('Enter account number.')
            self.pay_bank()
            
    def pay_card(self):
        bank = input('Enter bank name: ')
        card_number = input('Enter card number: ')
        if len(card_number)==15:
            pin = input('Enter pin: ')
            if len(pin)==4 and type(int(pin)) is int:
                password = input('Enter password: ')
                if password in self.password:
                        print('payment successful')
                        print(f'paid N{self.amount}')
                        with open(self.file, 'a') as file:
                            file.write(f'***{self.time}')
                            file.write(f'\nyou bought {self.items}\nand total money paid is N{self.amount}')
                            file.write(f'\npayment successful\npaid N{self.amount}')
                            file.write('\nPaid with bank card\n\n')
                else:
                    print('wrong password')
                    self.pay_card()
            #elif not type(int(pin)) is int:
             #   print('enter four digit pin')
              #  self.pay_card()
            else:
                print('enter four digit pin')
                self.pay_card()
        else:
            print('Enter account number.')
            self.pay_card()
        
        
    def gen_file(self):
        print('Do you want to pay with bank card or account?')
        ans = input('Enter Card or account Number: ')
        if ans == 'card':
            self.pay_card()
            with open(self.user_file, 'a') as file:
                file.write(f'***{self.time}')
                file.write(f'\n{self.user_name} bought {str(self.items)}\nand total money paid is N{self.amount}')
                file.write(f'\npayment successful\npaid N{self.amount}')
                file.write('\nPaid with bank card\n\n')
        elif ans =='account number':
            self.pay_bank()
            with open(self.user_file, 'a') as file:
                file.write(f'***{self.time}')
                file.write(f'\n{self.user_name} bought {str(self.items)}\nand total money paid is N{self.amount}')
                file.write(f'\npayment successful\npaid N{self.amount}')
                file.write('\nPaid with bank account\n\n')
        else:
            print('enter either "card" or "bank account"')
            self.gen_file()
            
        