num = int(input())

step = 1
while num > step:
    num -= step
    step += 1

if step % 2 == 0:
    top = num
    bottom = step - num + 1
else:
    top = step - num + 1
    bottom = num

print(f"{top}/{bottom}")