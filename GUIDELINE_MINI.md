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
| `drive_002` | Giữa ngã tư có xe khách trắng thân dài, dễ lẫn `bus` với `van`. Mép phải có xe bạc bị cắt khung. Cùng ảnh có taxi, sedan và người đi bộ. | Xe khách trắng = `bus`. Xe bạc mép phải = `van`, box chạm đúng biên ảnh. Taxi và sedan = `car`. Không gán người đi bộ. | `bus` là xe chở khách thân dài; `van` là van/minivan. Vật bị cắt khung chỉ bao phần nằm trong ảnh. Người đi bộ ngoài bốn lớp. |
| `drive_018` | Cột đèn che dọc khung. Bên trái có xe máy và người. Taxi vàng nằm sát lề. Cuối đường có một xe tối, nhỏ nhưng còn thấy thân. | Taxi = `car`. Xe tối cuối đường = `truck`. Không gán xe máy và người. Box không lấy cột đèn hay nền đường. | Lớp theo loại xe, kể cả xe đang đỗ hoặc bị che một phần. Xe máy và người không thuộc schema. Xe nhỏ chỉ gán khi còn nhận ra lớp. |
| `drive_042` | Mái một xe bị cắt mép dưới. Bên phải có xe khách hai tầng và một xe thùng nhỏ chất bao tải, dễ gọi nhầm thành `truck`. Có taxi đỏ. | Mái xe cắt khung = `van`, box chạm mép dưới. Xe hai tầng = `bus`. Xe thùng nhỏ chất đồ = `van`. Taxi đỏ = `car`. | Không suy phần xe nằm ngoài ảnh. `truck` dành cho xe tải thùng lớn, xe ben hoặc đầu kéo. Xe thùng nhỏ chở hàng thuộc `van`. |
