import json
def get_fav_num():
    with open('numbers.json') as f:
     n=json.load(f)
     print('your fav number is: '+str(n))



get_fav_num()    
    