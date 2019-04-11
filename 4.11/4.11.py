# def my_abs(x):
#     if x >= 0:
#         return x
#     else:
#         return -x
# print(my_abs(-99))

# def my_abs(x):
#     if not isinstance(x,(int,float)):
#         raise TypeError('bad operand type')
#     if x >= 0:
#         return x
#     else:
#         return -x
# print(my_abs('A'))


import math

# def move(x,y,step,angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx,ny;
# x,y = move(100,100,60,math.pi / 6)
# # print(x,y)
# r = move(100,100,60,math.pi / 6)
# print(r)
def quadrati(a,b,c):
    if math.pow(b,2) - 4*a*c < 0:
        print('无解')
    elif math.pow(b,2) - 4*a*c == 0:
        print('只有一根')
        x = (-b)/2*a
        print(x)
    else:
        x1 = ((-b)+math.sqrt(math.pow(b,2)-4*a*c))/2*a
        x2 = ((-b)-math.sqrt(math.pow(b,2)-4*a*c))/2*a
        print('第一个根为：',x1)
        print('第二个根为：',x2)
quadrati(4,2,-2)