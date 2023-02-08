import math

def kilog_lbs(x):
    lbs = x * 2.2046244202
    print("The amount of kilograms", (x), "in pounds is: ", lbs, "pounds")

def kilom_mile(x):
    miles = 0.6213688756 * x
    print("The amount of kilometers" , (x), "in miles is:" , miles, "miles")

def meter_foot(x):
    foot = x * 3.280839895
    print("The amount of meters" , (x),"in feet is:" , foot, "feet")

kilog_lbs(3)
kilom_mile(3)
meter_foot(3)
