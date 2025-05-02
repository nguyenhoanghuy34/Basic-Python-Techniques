
from plyer import notification
from plyer import battery

if __name__ == "__main__":
    status = battery.status  # Lấy thông tin pin hiện tại

    if status:  # Kiểm tra nếu có thông tin pin
        percent = status.get('percentage', 'Không rõ')
        is_charging = status.get('isCharging', False)

        notification.notify(
            title="ALERT!!!",
            message=f"Phần trăm pin còn lại là: {percent}%. Đang sạc: {'Có' if is_charging else 'Không'}",
            timeout=5  # hiển thị thông báo trong 5 giây
        )

        print(f"Phần trăm pin: {percent}%")
        print(f"Đang sạc: {'Có' if is_charging else 'Không'}")
    else:
        print("Không thể lấy thông tin pin.")