num = []

for i in range(1, int(input())+1):
    if i % 2 == 0:
        num.append(i)
print(sum(num))