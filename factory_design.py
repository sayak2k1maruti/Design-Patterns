from abc import ABC, abstractmethod
from enum import Enum

class ThaliType(Enum):
    VEG = 1
    NON_VEG = 2


class Thali(ABC):
    def __init__(self):
        self.name : str = None
        self.items : list = []
        self.drink : str = None
        self.dessert : str = None

    def maincourse(self):
        print(f"Serving {self.name} with items: {', '.join(self.items)}")
    
    def serve_drink(self):
        print(f"Serving drink {self.drink}")
    
    def serve_desserts(self):
        print(f"Serving dessert {self.dessert}")
    

class BengaliVegThali(Thali):
    def __init__(self):
        self.name = "Bengali Veg Thali"
        self.items = ["Rice", "Dal", "Vegetable Curry", "Chutney"]
        self.drink = "Lassi"
        self.dessert = "Rasgulla"

class BengaliNonVegThali(Thali):
    def __init__(self):
        self.name = "Bengali Non-Veg Thali"
        self.items = ["Rice", "Fish Curry", "Mutton Curry", "Chutney"]
        self.drink = "Lassi"
        self.dessert = "Mishti Doi"

class PunjabiVegThali(Thali):
    def __init__(self):
        self.name = "Punjabi Veg Thali"
        self.items = ["Roti", "Paneer Butter Masala", "Dal Makhani", "Rice"]
        self.drink = "Lassi"
        self.dessert = "Gulab Jamun"
    
class PunjabiNonVegThali(Thali):
    def __init__(self):
        self.name = "Punjabi Non-Veg Thali"
        self.items = ["Roti", "Chicken Butter Masala", "Dal Makhani", "Rice"]
        self.drink = "Lassi"
        self.dessert = "Gulab Jamun"
class SouthIndianVegThali(Thali):
    def __init__(self):
        self.name = "South Indian Veg Thali"
        self.items = ["Idli", "Sambar", "Coconut Chutney", "Dosa"]
        self.drink = "Filter Coffee"
        self.dessert = "Payasam"
class SouthIndianNonVegThali(Thali):
    def __init__(self):
        self.name = "South Indian Non-Veg Thali"
        self.items = ["Idli", "Chicken Sambar", "Coconut Chutney", "Dosa"]
        self.drink = "Filter Coffee"
        self.dessert = "Payasam"
class GujaratiVegThali(Thali):
    def __init__(self):
        self.name = "Gujarati Veg Thali"
        self.items = ["Roti", "Dal", "Sabzi", "Rice", "Dhokla"]
        self.drink = "Chaas"
        self.dessert = "Shrikhand"
class GujaratiNonVegThali(Thali):
    def __init__(self):
        self.name = "Gujarati Non-Veg Thali"
        self.items = ["Roti", "Dal", "Sabzi", "Rice", "Dhokla", "Khaman"]
        self.drink = "Chaas"
        self.dessert = "Shrikhand"

######################################

#Abstrct factory class
class ThaliCenter(ABC):
    def serve(self,thali_type:ThaliType):
        thali = self.create_thali(thali_type)
        thali.maincourse()
        thali.serve_drink()
        thali.serve_desserts()
        print("Thali served successfully!\n")
    @abstractmethod
    def create_thali(self, thali_type: ThaliType) -> Thali: pass


##Now we can create concrete factories for each type of Thali
class BengaliThaliCenter(ThaliCenter):
    def create_thali(self,thali_type:ThaliType) -> Thali:
        if thali_type == ThaliType.VEG:
            return BengaliVegThali()
        else:
            return BengaliNonVegThali()

class PunjabiThaliCenter(ThaliCenter):
    def create_thali(self,thali_type:ThaliType) -> Thali:
        if thali_type == ThaliType.VEG:
            return PunjabiVegThali()
        else:
            return PunjabiNonVegThali()
class SouthIndianThaliCenter(ThaliCenter):
    def create_thali(self,thali_type:ThaliType) -> Thali:
        if thali_type == ThaliType.VEG:
            return SouthIndianVegThali()
        else:
            return SouthIndianNonVegThali()
class GujaratiThaliCenter(ThaliCenter):
    def create_thali(self,thali_type:ThaliType) -> Thali:
        if thali_type == ThaliType.VEG:
            return GujaratiVegThali()
        else:
            return GujaratiNonVegThali()
        
if __name__ == "__main__":
    bengali_thali_center = BengaliThaliCenter()
    bengali_thali_center.serve(ThaliType.VEG)
    bengali_thali_center.serve(ThaliType.NON_VEG)
    punjabi_thali_center = PunjabiThaliCenter()
    punjabi_thali_center.serve(ThaliType.VEG)
    punjabi_thali_center.serve(ThaliType.NON_VEG)
    south_indian_thali_center = SouthIndianThaliCenter()
    south_indian_thali_center.serve(ThaliType.VEG)
    south_indian_thali_center.serve(ThaliType.NON_VEG)
    gujarati_thali_center = GujaratiThaliCenter()
    gujarati_thali_center.serve(ThaliType.VEG)
    gujarati_thali_center.serve(ThaliType.NON_VEG)
