class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.bigs = big
        self.meds = medium
        self.smalls = small

    def addCar(self, carType: int) -> bool:
        if carType==1 and self.bigs>0:
            self.bigs-=1
            return True
        elif carType==2 and self.meds>0:
            self.meds-=1
            return True
        elif carType==3 and self.smalls>0:
            self.smalls-=1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)