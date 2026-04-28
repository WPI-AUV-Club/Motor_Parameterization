Code from https://www.geeksforgeeks.org/python/3d-curve-fitting-with-python/  

Yoinked the motor performance data for the T200 thruster, then mapped it in 3 dimensions, where:  
x = thrust (kg)  
y = voltage  
z = motor throttle (-1 to 1)  

Then mapped a polynomial surface of best fit to the data to allow us to determine the nessecary motor throttle for a desired thrust (accounting for voltage drop over time)  
throttle = a + b x thrust_kg + c x batt_v + d x thrust_kg^2 + e x batt_v^2 + f x thrust_kg x batt_v  

Actually got much better results splitting the data in half along forward vs reverse thrust, so two seperate curves of best fit. (Shown in best_fit_test.py)  

https://docs.google.com/spreadsheets/d/1rI6A6pfYlhxgBcik8Z6lXceg4hGCgs8VEYoh9mVdXdM/edit?usp=sharing
