# two pointer example: find if two numbers add up to target

arr = [1, 2, 3, 4, 6]
target = 6

left = 0
right = len(arr) - 1

while left < right:
    current_sum = arr[left] + arr[right]

    if current_sum == target:
        print("Pair found:", arr[left], arr[right])
        break
    elif current_sum < target:
        left += 1
    else:
        right -= 1
else:
    print("No pair found")
