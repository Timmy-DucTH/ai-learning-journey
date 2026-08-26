Day 1 of learning foundational math for ML/AI  
Today i gonna learn about Derivatives and Loss Function

### Loss Function: Hàm mất mát  
**In ML, a model learns by making mistakes. The "Loss Function" is a mathematical formula that calculates exactly how wrong those predictions are.**

**Our ultimate goal is to adjust the model's parameters to minimize this Loss value.**  
Mục tiêu tối thượng của chúng ta là điều chỉnh các tham số của model để giảm thiểu giá trị Loss này.

**A classic example is Mean Squared Error (MSE), heavily used in regression tasks:**
$$MSE = \frac{1}{N} \sum_{i=1}^{N} (y_i - \hat{y}_i)^2$$
**Where $y_i$ is the actual truth, and the $\hat{y}_i$ is what your model predicted**  
Trong đó $y_i$ là kết quả thật, còn $\hat{y}_i$ là kết quả mô hình dự đoán

---

### Derivatives: Đạo hàm
**Once we know how wrong the model is, how do we know which way to adjust the weights to fix it? That is where Derivatives come in.**
Khi ta đã biết model sai như thế nào, làm sao chúng ta biết được nên điều chỉnh trọng số theo hướng nào để sửa nó? Đây là lúc Đạo hàm xuất hiện

**A Derivative measures the rate of change, or the "slope" of the Loss Function curve at a specific point**
Đạo hàm đo lường mức độ thay đổi, hoặc độ dốc đường cong của Loss Function ở một điểm cụ thể

**By calculating the derivative, the model knows whether to increase or decrease its weights to reach the minimum error (the bottom of the curve)**
Bằng cách tính đạo hàm, model sẽ biết nên tăng hay giảm trọng số để đạt đến mức sai số tối thiểu (đáy của đường cong)

**For example, if our simplified loss function is $f(x) = x^2$, the basic derivative is $f'(x) = 2x$**