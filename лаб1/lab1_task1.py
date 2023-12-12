numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

num1 = numbers[:4] + numbers[5:]
res1 = sum(num1)
res2 = len(numbers)
res3 = res1 / res2
numbers[4] = res3
print("Измененный список:", numbers)
