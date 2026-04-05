import os
import random
import subprocess
import time

# ---------- Cấu hình ----------
IMAGE_FOLDER = "troll_images"       # Thư mục chứa ảnh bựa
LOOP_COUNT = 3                      # Số lần hiển thị (0 = lặp vô hạn)
VIBRATE_DURATION = 500              # Rung mỗi lần (ms)
SLEEP_BETWEEN = 2                   # Giây nghỉ giữa các lần (chờ người xem ảnh)

# ---------- Tạo thư mục ảnh nếu chưa có ----------
if not os.path.exists(IMAGE_FOLDER):
    os.makedirs(IMAGE_FOLDER)
    print(f"📁 Đã tạo thư mục '{IMAGE_FOLDER}'. Hãy copy ảnh bựa vào đây rồi chạy lại.")
    exit()

# ---------- Lấy danh sách ảnh ----------
extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')
images = [f for f in os.listdir(IMAGE_FOLDER) if f.lower().endswith(extensions)]
if not images:
    print(f"❌ Không tìm thấy ảnh nào trong thư mục '{IMAGE_FOLDER}'. Hãy thêm ảnh vào.")
    exit()

# ---------- Thực hiện troll ----------
count = 0
while LOOP_COUNT == 0 or count < LOOP_COUNT:
    # Chọn ảnh ngẫu nhiên
    img_file = random.choice(images)
    img_path = os.path.join(IMAGE_FOLDER, img_file)
    
    # Mở ảnh bằng app mặc định (thoát khỏi terminal)
    subprocess.run(['termux-open', img_path])
    
    # Rung điện thoại (nếu có termux-api)
    try:
        subprocess.run(['termux-vibrate', '-d', str(VIBRATE_DURATION)], timeout=2)
    except:
        pass  # Bỏ qua nếu không có quyền rung
    
    # Đợi một lát rồi mở ảnh tiếp (người dùng vẫn ở app ảnh)
    time.sleep(SLEEP_BETWEEN)
    count += 1

print("🎉 Hết rồi! Hẹn gặp lại lần sau.")
