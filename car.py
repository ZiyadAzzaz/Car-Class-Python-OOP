
class car :
    def __init__(self, brand, model, year):
        self.brand = brand 
        self.model = model
        self.year = year
        
    def start_engine(self):
        print(f"The Engine of {self.brand} {self.model} Has Started")
        
    def drive(self):
        print(f"{self.brand} {self.model} is Now Driving")
        
    def details(self):
        print(f"Car Details: {self.brand} {self.model} {self.year}")
        

print("\n")
car1 = car('Mercedes', 'S-Class', 2024)
car2 = car('BMW', '7 Series', 2024)
car3 = car('Audi', 'A8', 2024)

car1.start_engine()
car1.drive()
car1.details()
print('\n')
car2.start_engine()
car2.drive()
car2.details()
print('\n')
car3.start_engine()
car3.drive()
car3.details()

#              ===============================================================  :)  ================================================================
        