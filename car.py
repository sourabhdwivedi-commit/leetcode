class car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer=0

    def get_descriptive_name(self):
        name= str(self.year)+" "+self.model+' '+self.make     
        return name

    def odometer(self):
        print('this car has '+self.odometer+' on it')  

    def update_odometer(self,mileage):
        if mileage>=self.odometer:
            self.odometer=mileage
        else:
            print('you cant roll back odometer')

    def increment_odometer(self,miles):
        self.odometer+=miles
         
class Battery:
    def __init__(self,batterysize=75):
        self.batterysize=batterysize
        
    def describe_battery(self):
         print('this car has a battery size of '+str(self.batterysize)) 

    def get_range(self):
        if self.batterysize==75:
            range=260
        elif self.batterysize==100:
           renge=315   

        print(f"this car can go about {range} miles on a full charge")
    def upgrade_battery(self):
        if self.batterysize!=100:
            self.batterysize=100

class  electriccar(car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery=Battery()

      
        

mytesla=electriccar('tesla','model s',2019)
print(mytesla.get_descriptive_name())  

mytesla.battery.describe_battery()
mytesla.battery.get_range()


