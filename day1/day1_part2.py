from collections import Counter

with open("input.txt", "r") as file:
    left_list = []
    right_list = []
    for line in file:
        left, right = line.strip().split("   ")
        left_list.append(int(left)), right_list.append(int(right))

    right_counts = Counter(right_list)
    sum = 0
    for left_num in left_list:
        sum += left_num * right_counts[left_num]

    print(sum)
