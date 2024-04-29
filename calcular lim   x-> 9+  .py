import math
def lim_calc_dir(x):
    if x != 9 and x > 9 :
        y=7
        while y > 6.00000000000001:
            if x <= 10.0 and x > 9.0 :
                x -= (x-9)/2               
            else:
                x -= 1 
            y = ((x-9)/(math.sqrt(x)-3))
        print(y)    

x= float(input("Diga o x:"))
lim_calc_dir(x) 