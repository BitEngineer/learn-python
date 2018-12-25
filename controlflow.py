# 控制流

# 分支
print('==== 分支 if elif else ====')
a = 20
if a == 10 :
    print(a)
elif a > 10 :
    print('a > 10')
else :
    print('a < 10')


# 循环
print('==== for循环 ====')
for i in range(1,5) :
    print(i)

print('==== for循环，continue ====')
for i in range(1,5) :
    if i > 3 :
        print(i)
    else :
        continue

print('==== while循环 ====')
i = 0
while i < 5 :
    print(i)
    i += 1

print('==== while循环，break ====')
i = 0
while i < 5 :
    print(i)
    i += 1
    if i > 3 :
        break
