import json
import time


def login_sys():

    
    print('''    \t Simple Python Login System
    \t Welcome to Our Login Portal''')
    try:
        choice =int(input('\n Enter 1 to Login and Enter any key to Create an New Account:'))
        
    except ValueError:
        print('\n Oops .. read the above line correctly!!')
         
          
    if choice == 1 and is_first()== True:
        while True:
            print('\n database is empty! create a new account\n')
            print('\n create an account is first!!!!')
            break
    elif choice == 1 and is_first() == False:
        login()
    else:
        new_account()


    
    

    

   
    
   
    

#profile = {name : [name,passwd]}
def new_account():
    name = input(('\n Enter ur Name :'))
    passwd = input(('Enter ur Passsword:'))
    profile = {name : [name,passwd]}
    if is_first() == False:
        with open('ds.json','r') as file:
            previous_data= json.load(file)
            with open('ds.json','w') as file:
                new_data = { **previous_data,**profile}
                json.dump(new_data,file)
                print('your account is successfully created!!')
                print('lets login')
                

    else:
        with open('ds.json','w') as file:
            json.dump(profile,file)
            print('your account is successfully created!!')
            print('lets login')
            
           
def is_first():
    is_first = True
    with open('ds.json','r') as file:
        data = file.read()
        if len(data) > 0:
            return False
        else:
            return True


def login():
    
    while True:
        name = input(('\n Enter ur Name :'))
        if check_name(name) == True:
            passwd = input(' enter ur password:')
            if check_passwd(name ,passwd) == True:
                print('you are logged in successfully')
                logout()
                break
            else:
                print('enter the correct password!!')
                continue
        else:
            print('enter vaild username')
            continue


def check_name(name):
    with open('ds.json','r') as file:
        data = json.load(file)
        if name in data:
            return True
        else:
            return False

def check_passwd(name,passwd):
    with open('ds.json','r') as file:
        data = json.load(file)
        if name in data:
            if data[name][1] == passwd:
                return True
            else:
                return False

    

def logout():
    print('wait 3 sec')
    time.sleep(3)
    d = input('do you want logout? y/n:\t')
    if d == 'y':
        print('you are logged out successfully!!')
    else:
        print('inga onnum illa!!')


  

 
    

  
    
    



    

if __name__ == "__main__":
    login_sys()
   


    
        
   


    

    
