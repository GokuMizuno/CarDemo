from car import Car
import sensors.sensor
#from .car import *
#Main and dashboard

def main(*args, **kargs):
    #if testing, pull test files from /test
    #otherwise, init car, and dashboard, then pass control to user

    print("init phase 0")
    TestCar = Car('electric')
    #dashboard dw = dashboard()

    TestCar.Power('On')
    print("Car powered on successfully")

    #Loop until you shutdown
    #reads keys, displays output
    #output = velocity, fuel left
    print("WASD to speed up, slow down, and turn left and right.  P to power off, and quit.")
    while(1):
        key = input()
        if(key == 'w'):
            #speed up
            print(key)
            TestCar.velocity('up')
        if(key == 's'):
            #slow down
            print(key)
            TestCar.velocity('down')
        if(key == 'a'):
            #turn left
            print(key)
        if(key == 'd'):
            #turn right
            print(key)
        if(key == 'p'):
            print("powering down")
            TestCar.Power('Off')
            break


main()
