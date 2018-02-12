import math

def move(x,y,step,angle=0):
    nx = x+step*math.cos(angle)
    ny = y+step*math.sin(angle)
    return nx,ny

x,y = move(100,100,60,math.pi/6)
print(x,y)#151.96152422706632 130.0 Python的函数返回多值其实就是返回一个tuple