

answer= 'y'

# random
while answer in ['y', 'Y']:
    import random
    rand = random.randint(1, 99)
    print('Enter coins that add up to', rand, 'cents, one per line.')

# check the first coin    
    coin1 = input('Enter first coin: ')
    while coin1 not in ['1', '5', '10', '25']: 
        if coin1 == '':
            coin1=input('Enter the first coin: ')
        else: 
            print('Invaild entry')
            coin1 = input('Enter first coin: ')
            
            
    if int(coin1) == rand:
        print('Correct!')
        answer= input('Try again (y/n)?: ')
         
                                                       
    elif int(coin1) > rand:
        print('Sorry - total amount exceeds', rand, 'cents')
        answer=input('Try again (y/n)?:  ')     
    
            
# coin1+coin_n    
    sum= int(coin1)   
    while sum < rand:
        coin2=input('Enter next coin: ')
        if coin2 == '':
            print('sorry, you only entered', sum, 'cents')
            answer=('Try again (y/n)?: ')
        elif coin2 not in ['1', '5', '10', '25']:
            print('Invalid entry')
            coin2= input('Enter next coin: ')
                 
        elif coin2 in ['1', '5', '10', '25']:
            coin2=int(coin2)
            sum=sum+coin2
            print(sum)    
   
    if sum == rand:
        print('Correct!')
        answer=input('Try again (y/n)?£º ')
                                               
    elif sum > rand:
        print('Sorry - total amount exceeds', rand, 'cents')
        answer=input('Try again (y/n)?:  ') 


print('Thanks for playing ... goodbye')
        