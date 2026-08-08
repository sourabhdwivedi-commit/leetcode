pokemons={
    'charizard':{
        'fact':'gen 1 pokemon',
        'type':'fire',
        'rarity':'mythic'
    },
    'mew two': {
        'fact':'man made pokemon',
        'type':'psychic',
        'rarity':'supreme'
    },
    'lucario':{
        'fact':'ancient pokemon',
        'type':'fighting-steel',
        'rarity':'mythic'
    }
}

for k,v in pokemons.items():
    print('\n')
    print('Pokemon : '+k.title())
    for x in v:
        print(x+' : '+v.get(x,'error'))