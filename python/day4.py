# Day 4: im gonna learn some typical algorithm design paradigms: Backtracking, Greedy, Dynamic Programming, Divide and Conquer, Brute Force

'''
Backtracking: an algorithm technique for solving problems recursively, by trying to build s solution piece-to-piece incremetally
== Quay lui: là kỹ thuật thuật toán giải quyết bài toán bằng cách chia nhỏ các bước giải và đệ quy từng phần một cách tuần tự

If a partially built solution fails to satisfy the constraints, the algorithm "backtrack" that part of solution and try next path
== Nếu phần giải pháp vừa xây không thỏa mãn điều kiện, thuật toán sẽ quay lui phần giải pháp đó và thử hướng tiếp theo

In ML, backtracking and other similar concepts are used in hyperparameter tuning, where we explore a vast space of configurations.
== Trong ML, quay lui và các cấu trúc tương tự được dùng để tìm bộ siêu tham số, nơi ta khám khá một không gian cấu hình rộng lớn
'''
# Find all the permutations (hoán vị) of a List
def get_permutations(elements):
    # Base case: if its an empty array, returning the array containing an empty subarray
    if len(elements) == 0:
        return [[]]
    
    permutations = []
    
    for i in range(len(elements)):
        # Choose current element
        current_element = elements[i]
        
        # Take the remainder of array
        remaining_elements = elements[:i] + elements[i+1:]
        
        # Recursive to break down the remaining part of problem
        # Append the current element to the top of permutation list
        for p in get_permutations(remaining_elements):
            permutations.append([current_element] + p)

    return permutations

print("Permutations of [1, 2]:", get_permutations([1, 2]))
# Output: [[1, 2], [2, 1]]

# --------------------------------------------------------------------------------------------------------

'''
Greedy: an algorithm technique builds up solution piece by piece, always choosing the next most immediate benefit piece (locally optimal choice)
== Tham lam: là giải thuật xây dựng giải pháp từng phần, luôn chọn phần giải pháp tiếp theo mang lại lợi ích lớn nhất (lựa chọn tối ưu cục bộ)

Its fast and memory-efficient but doesnt guarantee the globally optimal solution for all the problems, bc its never considers its past choices
== nó nhanh và tiết kiệm bộ nhớ nhưng không đảm bảo là giải pháp tối ưu toàn cục, vì nó không xem xét lại lựa chọn trong quá khứ của nó

In ML, Decision Trees are built using greedy: at each node, choosing the best feature to split the data, without looking ahead to future splits
== trong ML, Cây quyết định được xây theo Greedy, nó chọn đặc trưng tốt nhất để chia data, và không nhìn xa hơn vào các lần chia tiếp theo
'''
# Coin Change problem: find the minimun number of coins
def greedy_coin_change(amount, coins):
    # Sort the coins by value from highest to lowest
    coins.sort(reverse=True)
    coins_used = []
    
    for coin in coins:
        # Collect as many coins of the highest value as possible
        while amount >= coin:
            amount -= coin
            coins_used.append(coin)
            
    # If cannot return the exact money, Greedy may fail in some currency systems
    if amount != 0:
        return "Cannot make exact change"
        
    return coins_used

money_to_change = 68
available_coins = [20, 10, 5, 1]
print(f"Greedy change for {money_to_change}:", greedy_coin_change(money_to_change, available_coins))
# Output: [20, 20, 20, 5, 1, 1, 1]

#---------------------------------------------------------------------------------------------------------

'''
Dynamic Programming: is an optimization technique that break a complex problem down into the simplers, overlapping subproblems
== Quy hoạch động: một kỹ thuật tối ưu hóa, chia một bài toán phức tạp thành nhiều bài toán con đơn giản hơn, chồng chéo lên nhau

Unlike simple recursion, DP stores the results of these subproblems (called "memoization") so that each subproblem can be solve only once
== Không giống như đệ quy thông thường, DP lưu kết quả của những bài toán con lại, nhằm mục đích chỉ giải bài toán con đó 1 lần

DP is the foundational math behind Reinforcement Learning algorithms, where an AI agent learns the optimal policy by storing expected future rewards
== DP là nền tảng toán học đứng sau các thuật toán Học tăng cường, nơi mà AI học cách tối ưu hóa hành động bằng cách lưu các phần thưởng dự kiến trong tương lai
'''
# Fibonacci
memo = {}   # Declare a dictionary to store the subproblems' results (Memorization Dictionary)

def dp_fibonacci(n):
    # Base case
    if n == 0: return 0
    if n == 1: return 1

    # If the result is stored, use that result instead of caculating again. Time compleity: O(1)
    if n in memo:
        return memo[n]

    # Caculate and add the result to memo
    memo[n] = dp_fibonacci(n-1) + dp_fibonacci(n-2)

    return memo[n]

print("Fibonacci of 10 is:", dp_fibonacci(10))
# Output: 55

#---------------------------------------------------------------------------------------------------------

'''
Divide and Conquer: is an algorithm design paradigm that recursively breaks down a problem into 2 or more subproblems, untill these become simple enough to be solve directly.
== Chia để trị: là mô hình thiết kế ttoan, bằng cách phân chia đệ quy bài toán thành 2 hay nhiều bài toán con, cho đến khi những bài toán con này đủ đơn giản để có thể giải trực tiếp

The solutions to the subproblems are then combined to give a solution to the original problem. This approach drastically reduces time complexity, often down to O(logN) or O(NlogN)
== Giải pháp của các bài toán con sẽ được ghép lại để trở thành giải pháp cho bài toán gốc. Cách tiếp cận này làm giảm đáng kể độ phức tạp thời gian, thường xuống O(logN) hoặc O(NlogN)

In ML, DnC is the core idea behind ensemble methods like Random Forests, where the large dataset is divided into small subsets to train multiple decision trees. Its also the basis for data sorting or searching algorithms.
'''
# Binary search
def bin_search(arr, target):
    # initialize left, right pointer
    left, right = 0, len(arr) - 1

    while(left <= right):
        mid = (left + right) // 2
        if arr[mid] == target: return mid
        elif arr[mid] > target: right = mid - 1
        else: left = mid + 1

    return -1

sorted_data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target_value = 23
print(f"Index of {target_value}:", bin_search(sorted_data, target_value))
# Output: Index of 23: 5

#---------------------------------------------------------------------------------------------------------

'''
Brute Force: is a straightfoward approach to problem-solving that relies on sheer computing power and tries every possible combination rather than using advanced techniques to improve the efficiency
== Vét cạn: là phương pháp tiếp cận giải quyết vấn đề đơn giản, dựa vào khả năng tính toán thuần túy để thử tất cả mọi tổ hợp thay vì dùng những kĩ thuật nâng cao nhằm cải thiện hiệu suất

While often mathematically slow, its extremely reliable and guarantees finding the correct solution if one exists
== Mặc dù về mặt toán học nó rất chậm, nhưng lại rất đáng tin cậy và đảm bảo tìm ra giải pháp nếu nó tồn tại

In ML, BF is often used as a baseline to evaluate more complex models. E.g. The standard KNN algorithm uses a BF approach to calculate the Euclidean distance
'''
# Simulating how KNN scans the entire dataset to find the nearest point
import math

def bf_nearest_neighbour(target_point, dataset):
    # Initialize min distance is infinity
    min_distance = float('inf')
    nearest_point = None

    # Scanning all possible points in the dataset
    for point in dataset:
        # Calculating Euclidean distance
        distance = math.sqrt((target_point[0] - point[0])**2 + (target_point[1] - point[1])**2)

        # If the distance is lower than min_distance, update the min_distance and nearest_point
        if min_distance > distance:
            min_distance = distance
            nearest_point = point

    return nearest_point, min_distance

# Dataset (x, y coordinates)
training_data = [(1, 2), (5, 5), (8, 3), (2, 9)]
new_input = (4, 4)
closest, dist = bf_nearest_neighbour(new_input, training_data)
print(f"Nearest neighbor to {new_input} is {closest} with distance {dist:.2f}")
# Output: Nearest neighbour to (4, 4) is (5, 5) with distance 1.41


