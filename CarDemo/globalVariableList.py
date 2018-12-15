'''
Here is a list of all the car specific global variables for this simulation.
It contains such gems as: TIREPRESSURE_MAX, VELOCITY_MAX, and more
These variables can change as the car model changes.

These are stored in a file, rather than a database, simply for speed of prototyping
'''

#Tires
#in psi, because yay freedom units
TIREPRESSURE_MAX = 50
TIREPRESSURE_MIN = 0
TIRERPM_MAX = 10000 #velocity = (rpm*tire_radius)/time_elapsed

#Engine
    #min is -1, in case of electric car, no engine, no alarms set
    #this will be changed later, as noted in changelog
ENGINERPM_MAX = 8000
ENGINERPM_MIN = -1
ENGINETEMP_MAX = 400
ENGINETEMP_MIN = -1

#fuel level
FUELLEVEL_MIN = 0
FUELLEVEL_MAX = 15 #gallons.  Everything is done in gpm, to simplify the demo

#battery
STARTERBATVOLT_MAX = 12
STARTERBATVOLT_MIN = 0
STARTERBATAMP_MAX = 750
STARTERBATAMP_MIN = 0

#other batteries (for electric cars)
EBATVOLT_MAX = 48
EBATVOLT_MIN = 0
EBATAMP_MAX = 100
EBATAMP_MIN = 0
NUMEBAT_MAX = int(0xffff)
NUMEBAT_MIN = 0

#Speed
SPEED_MAX = 200
SPEED_MIN = 0
