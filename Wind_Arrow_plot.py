import numpy as np
import matplotlib.pyplot as plt

# Tạo lưới tọa độ (khu vực 10x10)
x, y = np.meshgrid(np.linspace(-5, 5, 20), np.linspace(-5, 5, 20))

distance = np.sqrt(x**2 + y**2)

# Tạo tốc độ gió giảm dần theo khoảng cách từ tâm (gió mạnh ở giữa)
speed = 5 * np.exp(-distance / 3)

# Gió thổi hướng vào tâm: hướng vector ngược với (x, y)
u = -x / (distance + 1e-3) * speed
v = -y / (distance + 1e-3) * speed

# Vẽ biểu đồ
plt.figure(figsize=(8, 8))
plt.quiver(x, y, u, v, speed, cmap='cool', scale=40)
plt.colorbar(label='Tốc độ gió (m/s)')
plt.title("Mô phỏng trường gió thổi vào tâm (áp thấp)")
plt.xlabel("Kinh độ (°)")
plt.ylabel("Vĩ độ (°)")
plt.grid(True)
plt.axis('equal')
plt.show()
