if __name__ == '__main__':

    n = int(input())
    arr = list(map(int, input().split()))

    print(max([ii for ii in arr if ii != max(arr)]))
