# Parent Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"{self.brand} {self.model}"

# Child Class (Inheritance from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)  # call parent constructor
        self.storage = storage
        self.battery = battery
    
    # Method to display info
    def phone_info(self):
        return f"{self.device_info()} | Storage: {self.storage}GB | Battery: {self.battery}mAh"
    
    # Method to simulate calling
    def make_call(self, number):
        return f"Calling {number} from {self.device_info()}..."
    
    # Method to simulate charging
    def charge(self):
        return f"{self.device_info()} is charging 🔋"

# Create Objects
phone1 = Smartphone("Samsung", "Galaxy S23", 256, 5000)
phone2 = Smartphone("Apple", "iPhone 14", 128, 3200)

# Test Methods
print(phone1.phone_info())
print(phone1.make_call("0723456789"))
print(phone2.charge())
