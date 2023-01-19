"""
simple 2048 games
"""
import random as r
import time


def game_interface(a1, a2, a3, a4, b1, b2, b3, b4, c1, c2, c3, c4, d1, d2, d3, d4):  # Print the game GUI

    arr_list = list((a1, a2, a3, a4, b1, b2, b3, b4, c1, c2, c3, c4, d1, d2, d3, d4))

    a1 = " " if not a1 else a1
    a2 = " " if not a2 else a2
    a3 = " " if not a3 else a3
    a4 = " " if not a4 else a4
    b1 = " " if not b1 else b1
    b2 = " " if not b2 else b2
    b3 = " " if not b3 else b3
    b4 = " " if not b4 else b4
    c1 = " " if not c1 else c1
    c2 = " " if not c2 else c2
    c3 = " " if not c3 else c3
    c4 = " " if not c4 else c4
    d1 = " " if not d1 else d1
    d2 = " " if not d2 else d2
    d3 = " " if not d3 else d3
    d4 = " " if not d4 else d4

    print("\r+-------+-------+-------+-------+\n",
          "\r|       |       |       |       |\n",
          "\r|%s|%s|%s|%s|\n" % (str(a1).center(7), str(a2).center(7), str(a3).center(7), str(a4).center(7)),
          "\r|       |       |       |       |\n",
          "\r+-------+-------+-------+-------+\n",
          "\r|       |       |       |       |\n",
          "\r|%s|%s|%s|%s|\n" % (str(b1).center(7), str(b2).center(7), str(b3).center(7), str(b4).center(7)),
          "\r|       |       |       |       |\n",
          "\r+-------+-------+-------+-------+\n",
          "\r|       |       |       |       |\n",
          "\r|%s|%s|%s|%s|\n" % (str(c1).center(7), str(c2).center(7), str(c3).center(7), str(c4).center(7)),
          "\r|       |       |       |       |\n",
          "\r+-------+-------+-------+-------+\n",
          "\r|       |       |       |       |\n",
          "\r|%s|%s|%s|%s|\n" % (str(d1).center(7), str(d2).center(7), str(d3).center(7), str(d4).center(7)),
          "\r|       |       |       |       |\n",
          "\r+-------+-------+-------+-------+\n", end="")

    for i in arr_list:
        s = int(i)
        if s > 2000:
            raise ImportError("congratulations！！！")


square = (2, 2, 8, 4)


def prime_data():
    # Initiative layout
    data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    pp = r.choice(square)
    pp1 = r.choice(square)
    location = r.sample([i for i in range(16)], 2)
    data[location[0]] = pp
    data[location[1]] = pp1
    return data


def tran_data(data, n):
    small_list = []

    if n == 0:  # up command
        for i in range(4):
            zero = [data[i], data[i + 4], data[i + 8], data[i + 12]]
            small_list.append(zero)
    elif n == 1:  # right command
        zero = data[0:4][::-1]
        one = data[4:8][::-1]
        two = data[8:12][::-1]
        three = data[12:16][::-1]
        small_list = [three, two, one, zero]
    elif n == 2:  # down command
        for i in range(12, 16):
            zero = [data[i], data[i - 4], data[i - 8], data[i - 12]]
            small_list.append(zero)
    elif n == 3:  # left command
        zero = data[:4]
        one = data[4:8]
        two = data[8:12]
        three = data[12:]
        small_list = [three, two, one, zero]
    return small_list


def add_number(data, n):
    # Process the data
    lis = []
    small_list = tran_data(data, n)
    for p in small_list:
        try:
            for x in range(4):
                p.remove(0)
        except ValueError:
            pass
        while True:
            s = len(p)
            if s < 4:
                p.append(0)
            else:
                break
        if p[0] == p[1]:
            if p[2] == p[3]:
                p[0] += p[1]
                p[1] = p[2] + p[3]
                p[2], p[3] = 0, 0
            else:
                p[0] += p[1]
                p[1], p[2], p[3] = p[2], p[3], 0
        elif p[2] == p[1]:
            p[1] += p[2]
            p[2], p[3] = p[3], 0
        elif p[2] == p[3]:
            p[2] += p[3]
            p[3] = 0
        lis.append(p)
    data = tran_list(lis, n)
    return data


def tran_list(small_list, n):
    big_list = []
    if n == 0:
        for x in range(4):
            for i in range(4):
                big_list.append(small_list[i][x])
    elif n == 1:
        for i in [3, 2, 1, 0]:
            s = small_list[i][::-1]
            for x in s:
                big_list.append(x)

    elif n == 2:
        for x in range(4):
            for i in [3, 2, 1, 0]:
                big_list.append(small_list[i][x])
        big_list = big_list[::-1]
    elif n == 3:
        for i in [3, 2, 1, 0]:
            for x in small_list[i]:
                big_list.append(x)

    return big_list


def judgement(big_list):
    # The referee system
    s = []
    for i in range(16):
        if not big_list[i]:
            p = i
            s.append(p)
    try:
        l = r.choice(square)
        z = r.choice(s)
    except (ValueError, IndexError):
        s = input("Game over, press any key to quit!")
        raise NameError("　Game Over！")
    big_list[z] = l
    return big_list


def data_handle(data):
    n = input("W A S D Q(up, down, left, right, return to the upper menu)－－－＞")
    if len(n) > 1:
        n = n[-1]
    if n in ["w", "W"]:
        # Up command
        data = add_number(data, 0)
    elif n in ["d", "D"]:
        # right command
        data = add_number(data, 1)
    elif n in ["s", "S"]:
        # down command
        data = add_number(data, 2)
    elif n in ["a", "A"]:
        # left command
        data = add_number(data, 3)
    elif n in ["q", "Q"]:
        raise OSError
    else:
        raise StopIteration("Please Enter the Correct Key!")
    data = judgement(data)
    return data  # Return to the game GUI


def menu():
    print("+{}+".format("-" * 30))
    print("|%s|" % "\t1．Start\t")
    print("|%s|" % "\t2．Quit\t\t")
    print("+{}+".format("-" * 30))


def showtime():
    # Main Function
    data = prime_data()  # Initiative data
    while True:
        menu()
        option = int(input("Please Enter Your Command："))
        if option == 1:
            game_interface(*data)
            while True:
                try:
                    data = data_handle(data)
                    game_interface(*data)
                except NameError as e:
                    print(e)
                    break
                except ImportError as e:
                    print(e)
                    time.sleep(10)
                    break
                except OSError:
                    break
                except StopIteration as e:
                    print(e)
                    continue

        elif option == 2:
            exit()


if __name__ == "__main__":
    showtime()
