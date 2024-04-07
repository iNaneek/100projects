import time

triangles = 1000
t1 = time.time()

#print(' /\ '*triangles); print("/__\\"*triangles)

for i in range(triangles): print(' '*(triangles - i) + '/' + ' '*i*2 + '\\')

#strin = ''
#for i in range(triangles): strin += ' '*(triangles - i) + '/' + ' '*i*2 + '\\' + '\n'
#print(strin)


t2 = time.time()
print(str(t2-t1))