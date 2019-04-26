with open("font.hex") as f:
    num=0
    for line in f:
        if num >= 32:
            print("-- ", num, '\'' + chr(num) + '\'')
        else:
            print("-- ", num)
        chr = [int(x, 16) for x in line.split(' ')]
        if True:
            for v in chr:
                print('2#{0:08b}#,'.format(v))
        else:
            # Rotate
            for i in range(7):
                v = 0
                for j in range(7):
                    v = v | ((chr[j] >> (7 - i) & 1) << j)
                print('2#{0:08b}#,'.format(v))
        num = num + 1
        print()
