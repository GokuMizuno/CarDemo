#from ./sensor/sensor.py import *
from state import State

class PoweredOff(object):
    '''
    The state is that the car is powered off, and nothing else can work
    '''
    def onEvent(self, event):
        if event == 'powerOn':
            return PoweredOn()
        return self

class PoweredOn(object):
    '''
    The state is that the car is powered on, and everything works
    '''
    def onEvent(self, event):
        if event == 'powerOff':
            return PoweredOff()
        return self
    
class Car(object):

    #velocity is a global var atm, but it will be moved into the velocity method once it is fully fleshed out.
    speed = 0
    direction = ['left', 'forward', 'right']
    
    def __init__(self, carType):
        if(carType == 'electric'):
            self.state = PoweredOff()
        elif(carType == "gas"):
            self.state = PoweredOff()
        else:
            print("Something went wrong, carType cannot be " + carType)
            #Throw error

    def Power(self, event):
        '''Two args can be passed, on, and off.
        On inits all other parts of the car, whilst off releases them, and frees the memory
        '''
        self.state = self.state.onEvent(event)
        if (event == 'On'):
            self.state.PoweredOff('powerOn')
        else: #(event == 'Off'):
            self.state.PoweredOn('powerOff')

    def Velocity(event):
        if(event == 'up'):
            speed = speed + 1
#            if(speed == SPEED_MAX):
#                print("You are at your max speed!  Slow down.")
#                speed--
            #check tires, and subtract energy
            self.Battery.Drain()
            self.AlarmCheck()
        if(event == 'down'):
            speed = speed - 1
#            if(speed == SPEED_MIN):
#                speed = 0
            #subtract energy
