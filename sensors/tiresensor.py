class TireSensor(Sensor):
    '''TireSensor has the following scope
    TireSensor has the following variables:
        rpm = 0
        tirePressure = 0
        Variables will be overwritten, but are init to zero, to prevent garbage data
    '''

    def __init__(self, name, rpm, tirePressure):
        self.name = name
        int rpm = 0
        int tirePressure = 0

    #On each tick, TireSensor.update() will run, alarm will be checked, and thrown
        #if there is a problem, otherwise, continue
    def alarm():
        if(tirePressure > TIREPRESSURE_MAX) or (tirePressure < TIREPRESSURE_MIN):
            #throw alarm
            print("Tire pressure in tire " + self.name + "is abnormal")
    
