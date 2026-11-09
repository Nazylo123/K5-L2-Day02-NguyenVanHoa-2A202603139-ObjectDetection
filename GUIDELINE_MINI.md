# Mini guideline — bài làm cá nhân

> Điền nội dung này trước khi bắt đầu gán nhãn. Giữ lại các quyết định sau khi self-QC.

## Định nghĩa lớp

| Lớp | Định nghĩa của bạn | Ví dụ/điểm phân biệt |
| --- | --- | --- |
| `car` | Xe con | Sedan, SUV, taxi, xe bán tải; không gồm xe tải, xe buýt hoặc mô tô. |
| `truck` | Xe tải chở hàng hoặc xe đầu kéo | Phân biệt với xe bán tải/cabin nhỏ, thuộc `car`. |
| `bus` | Xe buýt hoặc minibus chở khách | Không gán van/minivan; phân biệt theo loại xe, không theo việc xe đang đỗ hay di chuyển. |
| `van` | Xe van/minivan chở người hoặc chở hàng | Không gán xe buýt lớn (`bus`) hoặc xe con thông thường (`car`). |

## Quy tắc chung

- Box bám sát vật thể nghĩa là: ôm sát phần thân xe nhìn thấy được, không lấy thêm nền hay xe bên cạnh; mỗi xe có một box riêng.
- Vật thể bị che khuất: vẫn gán box quanh phần nhìn thấy nếu đủ nhận diện lớp; nếu có nhiều xe chồng lấp thì vẽ box riêng cho từng xe.
- Vật thể bị cắt bởi rìa ảnh: box chạm đúng mép ảnh và chỉ bao phần nằm trong ảnh, không đoán phần bị khuất ngoài khung.
- Vật thể rất nhỏ/mơ hồ: không tự đoán lớp nếu không thể nhận diện chắc; ghi lại ảnh và tình huống để hỏi giảng viên.

## Ghi lại quyết định cho ít nhất ba ca mơ hồ

| Ảnh | Tình huống | Quyết định cuối | Lý do theo schema |
| --- | --- | --- | --- |
| `drive_...` | | | |
| `drive_...` | | | |
| `drive_...` | | | |
