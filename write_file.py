with open('guest.txt','a') as guest_list:
    b=False
    while b==False:
        a=input('your name: ')
        guest_list.write(a+"\n")
        print('your response have been submitted '+ a)
        b=True
   