# alien_0 = {'color':'green','points':5}
# print(alien_0['color'])
# print(alien_0['points'])
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)
# alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
# print("Original x-position: "+ str(alien_0['x_position']))
# if alien_0['speed']=='slow':
#     x_increment = 1
# elif alien_0['speed']=='medium':
#     x_increment = 2
# else:
#     x_increment = 3
# alien_0['x_position'] = alien_0['x_position']+x_increment
# print("New x-position: "+ str(alien_0['x_position']))
alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}
alens = [alien_0,alien_1,alien_2]
for alien in alens:
    print(alien['color'])




