def main():
    n = int(input())
    arr = list(map(int, input().split()))
    
        
    arr.sort(reverse=True)

    max = arr[0]
    result = 0

    for i in arr:
        if i < max:
            result = i
            break

    print(result)

if __name__ == '__main__':
   main()