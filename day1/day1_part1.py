with open("input.txt", "r") as file:
    left_list = []
    right_list = []
    for line in file:
        left, right = line.strip().split("   ")
        left_list.append(int(left)), right_list.append(int(right))

    left_list.sort(), right_list.sort()
    sum = 0
    for i in range(len(left_list)):
        sum += abs(right_list[i] - left_list[i])
    print(sum)