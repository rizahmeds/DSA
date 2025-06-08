# Must do Pattern Problems before starting DSA

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
        
    
pattern1()
pattern2()
pattern3()
pattern4()
pattern5()
pattern6()
pattern7()
pattern8()