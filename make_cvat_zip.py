import os
import zipfile

# Thư mục nhãn và ảnh hiện tại
labels_dir = os.path.join("dataset", "labels", "train")
images_dir = os.path.join("dataset", "images", "train")
zip_name = "cvat_upload_ready.zip"

# Danh sách lớp chuẩn của bài lab
classes = ["car", "truck", "bus", "van"]

# Lấy danh sách ảnh đã sắp xếp
images = sorted([f for f in os.listdir(images_dir) if f.endswith((".jpg", ".png"))])

# 1. Nội dung file obj.data
obj_data_content = f"""classes = {len(classes)}
train = data/train.txt
names = data/obj.names
backup = backup/
"""

# 2. Nội dung file obj.names
obj_names_content = "\n".join(classes) + "\n"

# 3. Nội dung file train.txt
train_txt_content = "\n".join([f"data/obj_train_data/{img}" for img in images]) + "\n"

# Đóng gói vào zip đúng cấu trúc CVAT YOLO 1.1
with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as z:
    # Ghi các file cấu hình vào root của zip
    z.writestr("obj.data", obj_data_content)
    z.writestr("obj.names", obj_names_content)
    z.writestr("train.txt", train_txt_content)
    
    # Ghi các file nhãn vào obj_train_data/
    for img in images:
        base_name = os.path.splitext(img)[0]
        txt_name = f"{base_name}.txt"
        lbl_path = os.path.join(labels_dir, txt_name)
        
        if os.path.exists(lbl_path):
            with open(lbl_path, "r", encoding="utf-8") as f:
                content = f.read()
        else:
            content = ""  # File rỗng nếu không có xe
            
        z.writestr(f"obj_train_data/{txt_name}", content)

print(f"-> Đã tạo thành công file: {zip_name}")