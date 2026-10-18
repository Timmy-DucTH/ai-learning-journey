# Day 6: Today im gonna learn about Numpy

'''
NumPy (Numerical Python): is a foundational library for scientific computing and Machine Learning in Python.

Almost every modern ML/DL framework (PyTorch, Tensor Flow, Pandas, Scikit-Learn) is built on top of or designed to work seamlessly with NumPy arrays
== Hầu như mọi framework ML/DL hiện đại đều được xây dựng trên hoặc thiết kế để hoạt động một cách liền mạch với mảng NumPy
'''


'''
1. Why Numpy over Python Lists?
- Speed and C Backend: NumPy arrays are store in contiguous memory blocks and implemented in C, making operations up to 50x-100x faster than standard Python loops.
== Tốc độ vượt trội: Mảng NumPy được lưu trong những khối bộ nhớ liền kề và được chạy bằng C, khiến tốc độ nhanh gấp 50-100 lần so với vòng lặp Python tiêu chuẩn.

- Vectorization: We can perform element-wise mathematical operations on entire datasets without writing slow for loops.
== Vector hóa: Ta có thể thực hiện các phép toán theo phần tử mà không cần viết các vòng for chậm chạp để duyệt.

- Data Consistency: All elements is a NumPy array must share the same data type (dtype), optimizing memory allocation.
== Tính nhất quán dữ liệu: Mọi phần tử trong mảng NumPy phải có cùng dạng dữ liệu, tối ưu hóa phân bổ bộ nhớ.
'''
import numpy as np

# 1D Array (Vector):
vector = np.array([1, 2, 3, 4])

# 2D Array (Matrix - 2 rows, 3 columns):
list_matrix = [[1, 2, 3],
               [4, 5, 6]]
np_matrix = np.array(list_matrix, dtype=np.float32)

# Common utility initializers
zeros_arr = np.zeros((2, 3))        # Matrix fill with zeros
ones_arr = np.ones((2, 3))          # Matrix fill with ones
range_arr = np.arange(0, 10, 2)     # Make a NumPy array: [0, 2, 4, 6, 8] (similar to range)
linear_arr = np.linspace(0, 5, 3)   # 3 evenly spaced values from 0 to 5: [0.0, 2.5, 5.0]


'''
2. Array Attributes & Indexing: Thuộc tính và Truy xuất Mảng
Understanding array shape is the #1 debugging skill in Machine Learning

Key Attributes / Thuộc tính chính:
    .shape: Return a tuple showing dimensions (e.g. (rows, columns))
    .ndim: Return a number of dimensions/axes
    .dtype: data type of elements
'''
# Slicing and Boolean Masking / Cắt lát và Lọc điều kiện:
data = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Slicing [row, column]:
print(data[0, 1])       # Element at row 0, col 1 -> return 2
print(data[:, 2])       # Element at all row, col 2 -> return [3, 6, 9]
print(data[0:2, 1:3])   # Sub-matrix: rows 0-1, col 1-2

# Boolean Masking (Filtering):
mask = data > 4         # Create a True-False mask
print(data[mask])       # Apply that mask to filter out the element <= 4


'''
3. Reshaping & Matrix Operations: Tái định hình & Toán tử ma trận
In ML pipelines, features and neural network inputs frequently need dimesion adjustments
== Trong ML pipelines, đặc trưng và đầu vào mạng nơ ron thường xuyên cần chỉnh sửa chiều

Reshaping: arr.reshape(rows, cols) - changes dimensions without altering the underlying data. Use -1 to let NumPy automatically calculate a dimension
== Tái định hình: hàm .reshape(rows, cols) - thay đổi chiều mà không ảnh hưởng đến dữ liệu nền tảng. Dùng -1 để NumPy tự tính số chiều

Transpose: arr.T - swaps rows and columns (matrix transposition)
== Chuyển vị: hàm .T - đổi hàng và cột với nhau (chuyển vị ma trận)

Matrix Multiplication: Use the @ operator or np.dot()
== Nhân ma trận: dùng toán tử @ hoặc hàm np.dot()
'''
# Reshaping an array:
x = np.array([1, 2, 3, 4, 5,  6])
x_reshaped = x.reshape(2, 3) # return a 2 rows, 3 cols matrix
print("Reshaped:\n", x_reshaped)

# Transposing a matrix
x_transposed = x_reshaped.T
print("Transposed:\n", x_transposed)

# Matrix Multiplication
weights = np.array([[1, 2], [3, 4], [5, 6]])
output = x_reshaped @ weights
print("Result after multiply:\n", output)


'''
4. Broadcasting & Reductions: Cơ chế Broadcasting và Thống kê
- Broadcasting: NumPy automatically expands smaller arrays across larger arrays during arithmetic operations without copying data in memory
== Bắt sóng: NumPy tự động 
'''