def Work(n, k):
    for v in range(n):
        p = 0
        numcodes=0
        total = 0
        while total < n:
            numcodes = v // (k ** p)
            p += 1
            if numcodes == 0:
                break
            else:
                total += numcodes
        if total >= n:
            print(v)
            break


def main():
    file = open('work.txt', 'r')
    lines = file.readline()
    lines = lines.strip()
    lines = int(lines)
    for i in range(lines):
        line = list(file.readline())
        mid = line.index(' ')
        if '\n' in line:
            line.remove('\n')
        nline = line[:mid]
        kline = line[mid:]
        n = ''
        k = ''
        for x in nline:
            n += x
        n = int(n)
        for x in kline:
            k += x
        k = int(k)
        Work(n, k)
    file.close()


main()

