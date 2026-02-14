# binary search practice with different target

arr = [5, 10, 15, 20, 25, 30]
target = 25

start = 0
end = len(arr) - 1

while start <= end:
    mid = (start + end) // 2

    if arr[mid] == target:
        print("Found at index", mid)
        break
    elif arr[mid] < target:
        start = mid + 1
    else:
        end = mid - 1
else:
    print("Not found")
