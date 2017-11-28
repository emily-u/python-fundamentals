# Multiples Part I
for count in range(1, 1001, 2):
    print count

# Multiples Part I
for count in range(0, 1001):
    if count % 2 != 0:
        print count
        count +=1

# Multiples Part I
count = 1
while count<1001:
    print count
    count +=2

# Multiples Part II
for count in range(5, 1000001, 5):
    print count

# Multiples Part II
count = 5
while count<1000001:
    print count
    count +=5

# Multiples Part II
for count in range(5, 1000001):
    if count % 5 ==0:
        print count
        count +=1

#sum list
a = [1, 2, 5, 10, 255, 3]
sum = 0
for i in a:
    sum += i
print sum
        
#sum list
a = [1, 2, 5, 10, 255, 3]
sum = 0
for i in range(0, len(a)):
    sum += a[i]
print sum

#avg list
print sum / len(a)

#avg list
a = [1, 2, 5, 10, 255, 3]
sum = 0
for i in range(0, len(a)):
    sum += a[i]
avg = sum / len(a)
print avg