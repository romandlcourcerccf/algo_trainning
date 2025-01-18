def main():
    a = [1,2,3,4]
    b = [0]* (len(a)+1)

    for i in range(1, len(b)):
        b[i] = b[i-1] + a[i-1]
    
    print(a)
    print(*b[1:])

if __name__ == '__main__':
    main()