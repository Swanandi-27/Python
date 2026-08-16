from vehicle import  vehicle
class Bike(vehicle):
    def start(self):
        print("Bike started")

    def stop(self):
        print("Bike stop!!")

obj=Bike()
obj.start()
obj.stop()
