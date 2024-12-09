def sorter(a):
    if a % 2 == 0 :
        print(f'число {a} четное')
    else:
        print(f"число {a} нечетное")

while True:
    b = int(input("введи число: "))
    sorter(b)

