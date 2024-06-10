def is_number(n):
    try:
        float(n)  # Chuyển đổi n thành số float
        return 1.0  # Nếu không có lỗi, n là một số hợp lệ
    except ValueError:
        return 0.0  # Nếu có lỗi, n không phải là một số hợp lệ

# Kiểm tra đầu ra
print(is_number(1))  # Kết quả: 1.0
print(is_number('n'))  # Kết quả: 0.0
