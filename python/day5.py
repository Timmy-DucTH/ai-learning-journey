# Day 5: i gonna learn ab Time and Space Complexity

'''
Time Complexity: measures how the number of operations grows as the input size (N) increases
== Độ phức tạp Thời gian đo lường số lượng phép tính tăng lên khi tăng kích thước đầu vào

We often use "Big O Notation" (kí hiệu Big O) to describe this growth. Here are the 3 common ones in ML:
- O(1): Constant Time: the execution time remains the same regardless of the input size
== Thời gian hằng số: thời gian thực thi sẽ không đổi bất kể thay đổi kích thước đầu vào thế nào

- O(N): Linear Time: the execution time grows directly in proportion to the input size
== Thời gian tuyến tính: thời gian thực thi tăng tỷ lệ thuận với kích thước đầu vào

- O(N^2): Quadratic Time: the time grows exponentially. This usually happens with nested loops
== Thời gian bậc 2: thời gian tăng theo cấp số nhân. Thường xảy ra với các vòng lặp lồng nhau
'''
# O(1)
arr = [1, 2, 3]
print(arr[0])

# O(N)
for i in range(3):
    print(arr[i])

# O(N^2)
arr2 = [[1, 2, 3], [4, 5, 6]]
for i in range(2):
    for j in range(3):
        print(arr2[i][j])

#-------------------------------------------------------------------------------------------------------

'''
Space Complexity: measures how much extra memory (RAM) an algorithm needs to run as the input size increases
== Độ phức tạp Không gian: đo lường lượng bộ nhớ phụ thêm khi kích thước đầu vào tăng thêm

In ML, there is often a "Time-Space Trade off"
== Trong ML, thường có sự đánh đổi giữa Không gian và Thời gian

Sometimes, to make an algorithms run faster, we have to use more memory to store temporary results. E.g. Dynamic Programing technique
== Đôi khi, để thuật toán chạy nhanh hơn, chúng ta phải sử dụng nhiều bộ nhớ để lưu các kqua tạm thời. Vd: kỹ thuật Quy hoạch động
'''