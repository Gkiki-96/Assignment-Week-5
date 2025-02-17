# Base class
class Smartphone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.battery = battery  # Battery percentage

    def check_battery(self):
        print(f"{self.brand} {self.model} has {self.battery}% battery left.")

    def charge(self, amount):
        self.battery = min(self.battery + amount, 100)  
        print(f"{self.brand} {self.model} charged to {self.battery}%.")

# Subclass (Inheritance)
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, battery, camera_megapixels):
        super().__init__(brand, model, battery)
        self.camera_megapixels = camera_megapixels  # Additional attribute

    def take_photo(self):
        print(f"📸 Taking a photo with {self.camera_megapixels}MP camera!")

# Example usage
phone1 = Smartphone("Samsung", "Galaxy S23", 50)
phone1.check_battery()
phone1.charge(30)

phone2 = SmartphoneWithCamera("iPhone", "15 Pro", 70, 48)
phone2.check_battery()
phone2.take_photo()
