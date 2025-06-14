# Must do Pattern Problems before starting DSA.

def pattern1():
    """
    * * * * * 
    * * * * * 
    * * * * * 
    * * * * * 
    * * * * *
    """
    for _ in range(5):
        for _ in range(5):
            print("*", end=" ")
        print("")

def pattern2():
    """
    * 
    * * 
    * * * 
    * * * * 
    * * * * * 
    """
    for i in range(6):
        for _ in range(i):
            print("*", end=" ")
        print("")

def pattern3():
    """
    1 
    1 2 
    1 2 3 
    1 2 3 4 
    1 2 3 4 5 
    """
    for i in range(1,6):
        for j in range(1,i+1):
            print(j, end=" ")
        print("")

def pattern4():
    """
    1 
    2 2 
    3 3 3 
    4 4 4 4 
    5 5 5 5 5 
    """
    for i in range(1,6):
        for _ in range(1,i+1):
            print(i, end=" ")
        print("")

def pattern5():
    """
    * * * * * 
    * * * * 
    * * * 
    * * 
    * 
    """
    for i in range(1,6):
        for _ in range(5,i-1,-1):
            print("*", end=" ")
        print("")
        
def pattern6():
    """
    1 2 3 4 5 
    1 2 3 4 
    1 2 3 
    1 2 
    1 
    """
    for i in range(6):
        for j in range(1,6-i):
            print(j, end=" ")
        print("")

def pattern7():
    """
            * 
          * * * 
        * * * * * 
      * * * * * * * 
    * * * * * * * * * 
    """
    for i in range(1,6):
        for _ in range(5-i):
            print(" ", end=" ")
        for _ in range((i*2)-1):
            print("*", end=" ")
        print("")

def pattern8():
    """
    * * * * * * * * * 
      * * * * * * * 
        * * * * * 
          * * * 
            * 
    """
    for i in range(5,0,-1):
        for _ in range(5-i):
            print(" ", end=" ")
        for _ in range((i*2)-1):
            print("*", end=" ")
        print("")

def pattern9():
    """
    1 
    0 1 
    1 0 1 
    0 1 0 1 
    1 0 1 0 1 
    """
    for i in range(1,6):
        digit = 1 if i%2 else 0
        for j in range(i):
            print(digit, end=" ")
            digit = 1-digit
        print("")

def pattern13():
    """
    1 
    2 3 
    4 5 6 
    7 8 9 10 
    11 12 13 14 15
    """
    num = 1
    for i in range(5):
        for j in range(i+1):
            print(num, end=" ")
            num = num+1
        print("")

def pattern14():
    """
    A 
    A B 
    A B C 
    A B C D 
    A B C D E
    """
    for i in range(5):
        ascii_start = 65
        for j in range(i+1):
            print(chr(ascii_start), end=" ")
            ascii_start = ascii_start+1
        print("")

def pattern15():
    """
    A B C D E 
    A B C D 
    A B C 
    A B 
    A
    """
    for i in range(5):
        ascii_start = 65
        for j in range(5,i,-1):
            print(chr(ascii_start), end=" ")
            ascii_start = ascii_start+1
        print("")

def pattern16():
    """
    A 
    B B 
    C C C 
    D D D D 
    E E E E E
    """
    ascii_start = 65
    for i in range(5):
        for j in range(i+1):
            print(chr(ascii_start), end=" ")
        ascii_start = ascii_start+1
        print("")


pattern1()
pattern2()
pattern3()
pattern4()
pattern5()
pattern6()
pattern7()
pattern8()
pattern9()
pattern13()
pattern14()
pattern15()
pattern16()
