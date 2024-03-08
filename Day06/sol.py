size = 14
buf = []
with open("AoC2022/Day06/input02.txt") as infile:
    for _ in range(size):
        buf.append(infile.read(1))
    for i in range(size-1):
        if buf[i] == buf[i+1]:
            break
        if i == size-1:
            print(size)
            exit
    while True:
        c = infile.read(1) #read one byte at time
        if not c:
            print("End of file.")
            break
        buf.append(c)
        buf.pop(0)
        for element in buf:
            if buf.count(element) != 1:
                break
        else:
            print(infile.tell())
            break