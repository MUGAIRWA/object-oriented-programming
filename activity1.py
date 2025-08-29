# Parent class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"Device: {self.brand} {self.model}"

# Child class (inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, camera):
        super().__init__(brand, model)   # Call parent constructor
        self.storage = storage
        self.camera = camera
    
    def take_photo(self):
        return f"{self.brand} {self.model} takes a photo with {self.camera} camera 📸"
    
    def device_info(self):   #polymorphism (method overriding)
        return f"Smartphone: {self.brand} {self.model}, {self.storage}GB storage, {self.camera}MP camera"

# Creating objects
phone1 = Smartphone("Samsung", "Galaxy S24", 256, 108)
phone2 = Smartphone("Apple", "iPhone 15", 512, 48)

print(phone1.device_info())
print(phone1.take_photo())
print(phone2.device_info())
