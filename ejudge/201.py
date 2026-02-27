numbers = list(map(int, input().split()))

avg = sum(numbers) / len(numbers)

count = 0
for x in numbers:
    if x > avg:
        count += 1

print(count)
