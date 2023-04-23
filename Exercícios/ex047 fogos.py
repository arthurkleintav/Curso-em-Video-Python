from time import sleep
for c in range(10, 0, -1):
    sleep(1)
    print(c)
sleep(1)
print('\033[33mFOGOS!\033[m')