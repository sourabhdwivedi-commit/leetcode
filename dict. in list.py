aliens=[]

for i in range(30):
    new_alien={'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

for i in aliens[:5]:
    print(i)

print('...')
print('total number of aliens = '+str(len(aliens)))    

for i in range(3):
    if aliens[i]['color']=='green':
        aliens[i]['color']='yellow'  
        aliens[i]['points']=10
        aliens[i]['speed']='medium' 
    elif aliens[i]['color']=='yellow':
        aliens[i]['color']='red'
        aliens[i]['points']=15
        aliens[i]['speed']='fast'

for i in aliens[:5]:
    print(i)

