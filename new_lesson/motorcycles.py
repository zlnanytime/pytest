motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
motorcycles.insert(0,'ducati')
print(motorcycles)
del motorcycles[0]
print(motorcycles)
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
poped_motorcycles = motorcycles.pop()
print(motorcycles)
print(poped_motorcycles)
motorcycles.append(poped_motorcycles)
print(motorcycles)
