if __name__ == '__main__':
    arr = [2, 3, 1, 0, 2, 5, 3]
    for i in range(len(arr) - 1):
        element = arr[i]
        if i + 1 == len(arr):
            break
        for j in range(i + 1, len(arr)):
            if element == arr[j]:
                print(element)

