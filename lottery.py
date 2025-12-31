from random import choice
a=[40,0,58,23,12,5,6,7,2,89,'v','a','w','u','n']

print('tickets matching these four letters or numbers' \
'wins a prze :')

my_ticket='40 89 v n' 

flag=False
p=0

while flag==False:
    p+=1
    b=''
    
    for i in range(4):
        b=b+str(choice(a))+' '
        
    print(str(p)+ "  " +b)

    if b.strip()==my_ticket:
      print('your ticket '+my_ticket+' won ')
      flag=True
            
         


