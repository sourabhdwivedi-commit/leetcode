class restaurant:
    def __init__(self,name,cuisine_type):
        self.name=name
        self.cuisine_type=cuisine_type
        self.number_served=0

    def describe_restaurant(self):
        print(f'{self.name.title()} is popular for {self.cuisine_type} cuisine')

    def open_restaurant(self):
        print(self.name.title()+' is open')
    
    def check_served(self):
        print('the number of coustomers served: '+str(self.number_served))

    def set_number_served(self,n):
        self.number_served=n

    def increment_number_served(self):
        self.number_served+=1





class IcecreamStand (restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors=['vanilla','chocolate','strawberry']

    def flavor_list(self):
        for i in self.flavors:
            print(i)
