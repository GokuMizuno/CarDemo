from .car.py import car
#Main and dashboard

def main(*args, **kargs):
    #if testing, pull test files from /test
    #otherwise, init car, and dashboard, then pass control to user

    print("init phase 0")
    TestCar = car(electric)
    #dashboard dw = dashboard()

    TestCar.Power(On)
    print("Car powered on successfully")

main()
