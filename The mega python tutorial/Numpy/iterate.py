import numpy
array = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
a = numpy.asarray(array)
ar = a[1:2]
print(ar)
for i in a :
    print(i)
print("\n")

for i in a.T :
    print(i)

for i in a.flat:
    print(i)

print((ar,ar,ar))

print(numpy.vstack((ar,ar,ar))) #concatenate array

print(numpy.hstack((ar,ar,ar))) #concatenate array
