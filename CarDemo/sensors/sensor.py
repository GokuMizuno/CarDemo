class Sensor:
    '''
    At the most basic level, a sensor takes input, and returns output
    The output is either suppressed, normal, or abnormal.
    EX:  Tire pressure sensor.
    Input (1) is tire pressure.
    Output (1) is supressed if pressure is normal, alerting if abnormal.
    '''

    def __init__(self, name):
        '''Sensor init.  All instance variables go here'''
        self.name = name
        self.logData = []
        self.data = []  #placeholder variable

    def input(*args):
        '''Input takes a variable number of inputs'''
        pass

    def output(*args):
        '''Output returns a variable number of outputs'''
        pass

    def update(self, iterable):
        '''update overwrites the old state of the sensor with a new state'''
        self.data = ""  #Clear old state.  This will change as the class evolves
        #Right now, for rapid prototyping, I am using a string to hold data.
        #This is a problem, as strings will eat lots of memory, quickly.
        #data, and logData will be replaced by another type of object, later.
        for i in iterable:
            self.data.append(i)
#Needs to overwrite, not append.

    def alarm():
        '''alarm is thrown when something goes out of whack.  Alarm is defined in derived classes'''
        pass
    
    def logging(self, iterable):
        '''logging appends new state to old'''
        for i in iterable:
            self.logData.append(i)
