def get_speed(thrust_kg, batt_v):
    x = thrust_kg
    y = batt_v
    if (thrust_kg == 0):
        return 0
    elif (thrust_kg > 0):
        a,b,c,d,e,f = 0.80159994,0.4042657,-0.09132469,-0.01855475,0.00281378,-0.00812859
    else:
        a,b,c,d,e,f = -0.78689061,0.51407952,0.08920133,0.02886842,-0.00272574,-0.01048958
    return a + b*x + c*y + d*x**2 + e*y**2 + f*x*y
    
def calc_pwm_us(speed):
    return 1500+400*speed
    
print(get_speed(-2.5, 12))    
