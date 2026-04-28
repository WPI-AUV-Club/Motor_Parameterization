Code from https://www.geeksforgeeks.org/python/3d-curve-fitting-with-python/

Yoinked the motor performance data for the T200 thruster, then mapped it in 3 dimensions, where:
x = thrust (kg)
y = voltage
z = motor throttle (-1 to 1)

Then mapped a polynomial surface of best fit to the data to allow us to determine the nessecary motor throttle for a desired thrust (accounting for voltage drop over time)

a = 	0.00891753782
b = 	0.542521431
c =	-0.00877194667
d =	-0.00695148647
e =	0.000439710158
f =	-0.017756417
throttle = a + b*thrust_kg + c*batt_v + d*thrust_kg^2 + e*batt_v^2 + f*thrust_kg*batt_v

https://docs.google.com/spreadsheets/d/1rI6A6pfYlhxgBcik8Z6lXceg4hGCgs8VEYoh9mVdXdM/edit?usp=sharing
