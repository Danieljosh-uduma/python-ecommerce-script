import store


class Profile:
    def __init__(self):
        self.user_name = ['josh']
        self.password = ['pass']

                
    def sign_in(self):
        self.name = input('create user name: ')
        if self.name in self.user_name:
            print('user name exist, try a unique name')
            self.sign_in()
        else:
            password = input('create password: ')
            trial = 3
            while trial > 0:
                if len(password)<= 5:
                    print('password must not be less than 5 letters')
                    password = input('create password: ')
                    trial -= 1
                else: 
                    break
            else:
                print('something went wrong')
                self.sign_in()
                
            self.comfirm_password = input('comfirm your password: ')
            if password == self.comfirm_password:
                print('password saved')
                self.user_name.append(self.name)
                self.password.append(self.comfirm_password)
                print(f'{self.name} you can now login')
            else:
                print('incorrect password')
                print('try again')
                self.sign_in()
    
    def log_in(self):
            self.name = input('enter user name: ')
            password = input('enter password: ')
            for x,y in zip(self.user_name, self.password):
                if self.name == x and password == y:
                    print(f'Welcome {self.name} to Josh Super Store')
                    break
            else:
                print('incorrect password or user name')
                print('try again')
                self.log_in()
            
            
    def log_out(self):
        print('do you want to log out?\nenter yes or no')
        ans = input()
        if ans == 'yes':
            print(f'{self.name.capitalize()} you have successfully logged out')
            print('\nDo you an account?')
            ans1 = input('enter yes/no: ')
            if ans1=='yes':
                self.log_in()
            elif ans1=='no':
                self.sign_in()
                self.log_in()
            else:
                self.log_out()
        else:
            print('we have more for you to try\ncheck out our stores')
            

                

        
            
    
                
                
        