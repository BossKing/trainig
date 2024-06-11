def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not the prime number.")



# copilot below code
def is_prime(n):
    if n < 2 or (n != 2 and n % 2 == 0):
        return False
    return all(n % i for i in range(3, int(n**0.5) + 1, 2))

num = int(input("Enter a number: "))
print(f"{num} is {'a prime' if is_prime(num) else 'not a prime'} number.")



a=5
for i in range(1,i+1):
    for j in range(1,i+1):
        print('*'+,end='')
print()

a="mari"
for i in a:
    print(i)


a="mari is good boy"
print("good"in a)
if "good" in a:
    print("good is present")




a="my friend name is mariswami"
print(a[0:6])



a="my friend name is mariswami"
print(a[:6])


a="my friend name is mariswami"
print(a[-6:-1])



a="mariswami"
b="MARISWAMI"
print(a.upper())
print(b.lower())


a="mariswami is a person"
print(a.strip())


a="mariswami is a person"
print((a.replace("iswami","efhfr")))


a="mariswami is, a person"
print(a.split('','',))

txt="my name is \"punith\"gowda"
print(txt)

a=int(input("Enter the number"))
b=int(input("Enter the number"))
if b>a:
    print("b is greater then a")
else:
    print("a is greater then b")
print(bool,"hello")

a=["mys","mand","beng"]
a.insert(1,"mang")
print(a)

a=["dosa","roti"]
b=["tea","cofee"]
a.extend(b)
# print(a)

a=["dosa","roti"]
b=["tea","cofee"]
a.remove("dosa")
b.pop(1)
print(a)
print(b)



a=["orange","mango","apple"]
a.sort()
print(a)
b=[55,100,1,20]
b.sort()
print(b)

a=["orange","mango","apple"]
a.sort()
print(a)
b=[55,100,1,20]
b.sort(reverse=)
print(b)

a=[1,2,3,4]
b=a.copy()
print(b)
a.extend(b)
print(a)









n=5
for x in range(1,n+1):
    for y in range(1,x+1):
        print("*",end='')



































































































































