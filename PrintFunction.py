if __name__ == '__main__':
    n = int(input())

    if n < 1 or n > 150:

        print("Out Of Bounds!")
    
    string = ""

    for ii in range(1, n + 1):

        string += str(ii)

        
    print(string)