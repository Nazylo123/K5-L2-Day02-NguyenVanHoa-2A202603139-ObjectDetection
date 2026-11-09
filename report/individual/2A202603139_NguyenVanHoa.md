# Báo cáo cá nhân — Ngày 2 Object Detection

Xem [quy định nộp](../../SUBMISSION.md). Mục 5 còn trống số model vì notebook Colab chưa chạy xong.

## 1. Thông tin học viên

- Họ tên: Nguyễn Văn Hòa
- MSSV: 2A202603139
- Email: hoanv0300@gmail.com
- Lớp: K5-L2
- Link repo bài làm: https://github.com/Nazylo123/K5-L2-Day02-NguyenVanHoa-2A202603139-ObjectDetection
- Link Colab đã chạy: đang chạy, chưa có link bản đã share

## 2. Schema và mini guideline

Định nghĩa lớp, quy tắc box và ba ca mơ hồ nằm ở [GUIDELINE_MINI.md](../../GUIDELINE_MINI.md).

Ba ca đã chốt:

- `drive_002`: xe khách trắng giữa ngã tư là `bus`; xe bạc bị cắt mép phải là `van`; taxi/sedan là `car`; người đi bộ không gán.
- `drive_018`: taxi vẫn là `car` dù bị cảnh che và đang ở lề; xe tối cuối đường còn nhận ra thân thì là `truck`; xe máy và người không gán.
- `drive_042`: phần xe cắt mép dưới là `van` và box chạm biên; xe hai tầng là `bus`; xe thùng nhỏ chất bao tải là `van`, không nâng thành `truck`.

Cần giảng viên làm rõ hai chỗ schema không có tên riêng:

- `drive_034`: xe cứu hộ/cẩu ở giữa ảnh đang mang class `bus` (một box class 2, không có box `truck` trong file). Hình gần xe chuyên dụng hơn là xe buýt chở khách.
- `drive_015`: xe buýt dài bên trái đang là một box `van` rất rộng, trong khi một xe nhỏ hơn bên phải là `bus`.

Hai chỗ này giữ nguyên vì bản chấm gold đã khớp box và đã qua cổng. Không tự đổi schema sau khi khóa.

## 3. Annotation và self-QC

- Số file nhãn train: 50 file `drive_001.txt`–`drive_050.txt`, 653 box (car 533, truck 45, bus 21, van 54).
- Kết quả checker: `python tools/check_yolo_labels.py` in `ĐẠT cấu trúc: 50/50 file nhãn hợp lệ`. Không còn lỗi basename, số cột, class ID hay box vượt biên.
- Danh sách 10 ảnh đã rà bằng mắt: `drive_002`, `drive_008`, `drive_009`, `drive_015`, `drive_018`, `drive_026`, `drive_034`, `drive_036`, `drive_041`, `drive_042`.
- Lỗi bỏ sót/box/class phát hiện khi rà và cách sửa: người đi bộ, xe máy và xe đạp không có box. Xe bị che (`drive_018`, `drive_041`) và xe cắt khung (`drive_002`, `drive_042`) vẫn có box riêng trên phần nhìn thấy. `drive_036` có xe trắng bị nhòe gần camera, vẫn giữ một box `truck` vì còn thấy thân xe. Lệch lớn lúc chấm lần đầu là gán `bus` cho nhiều van/minivan; đã chỉnh lại phân lớp trước lần chấm đạt.
- Commit nhãn trên GitHub: `fd66780` (`fd66780ccea15e5bbc3a8f2370155ebeaf6f5ff3`, message `push`).

## 4. Gold QC và rework

| Chỉ số | Trước sửa | Sau sửa |
|---|---:|---:|
| TP | 422 | 651 |
| FP | 373 | 2 |
| FN | 231 | 2 |
| Precision | 0.5308 | 0.9969 |
| Recall | 0.6462 | 0.9969 |
| F1 | 0.5829 | 0.9969 |
| mean_iou_of_matches | 0.8464 | 1.0 |
| passed | false | true |

File kết quả lần sau: [outputs/annotation_evaluation.json](../../outputs/annotation_evaluation.json). Ngưỡng bài là F1 ≥ 0.80 và mean IoU ≥ 0.70.

Lần đầu chưa đạt. Box khớp thì khá sát (mean IoU 0.8464) nhưng F1 thấp vì thừa box và lệch lớp: bản đó có car 678, truck 23, bus 79, van 15 so với gold car 533, truck 46, bus 20, van 54. Hướng sửa là giảm `bus` gán nhầm cho van/minivan, tăng `van` và `truck`, bỏ box thừa ngoài xe thuộc schema.

Sau sửa, 49/50 ảnh khớp hết số box. Chỉ `drive_002` còn 11/13 box ghép được (mỗi bên 13 box, 2 box không ghép cùng lớp). `passed` đã là true nên không rework thêm và không sửa file gold. FP/FN còn lại chưa đủ để kết luận nguyên nhân từng xe nếu không mở lại ảnh cùng hai file nhãn.

## 5. Kết quả YOLO

Colab đang chạy. Chưa điền precision, recall, mAP và chưa gắn ảnh prediction.

- Runtime, GPU/CPU, phiên bản Ultralytics và Torch: python 3. T4 GPU
- Các tham số thay đổi so với notebook nếu có và lý do: chưa đổi tham số; chạy đúng notebook với nhãn đã qua cổng gold
- Đường dẫn best checkpoint trong phiên chạy: "/content/Day2-Lab/outputs/yolo26_runs/vehicle_annotation/weights/best.pt"

| Chỉ số trên 10 ảnh eval | Giá trị |
|---|---:|
| Precision | 0.7411127065121624 |
| Recall | 0.6103333433246294 |
| mAP50 | 0.6467943014906667 |
| mAP50–95 | 0.4390906118545412 |

Sau khi có `day2_colab_outputs.zip`, đặt `eval_predictions/` và `yolo26_runs/` vào `report/individual/assets/`, rồi copy 4 số từ `model_eval_metrics.json` vào bảng trên.

Trả lời bốn câu hỏi cuối notebook:

1. Lớp nào recall thấp nhất? Ảnh nào minh họa? Chưa trả lời được. Cần bảng recall theo lớp và một ảnh trong `assets/eval_predictions/visuals/` sau khi Colab xong. Tập train lệch mạnh về `car` (533) so với `truck` 45, `bus` 21, `van` 54, nên lớp ít mẫu là chỗ cần xem trước.
2. Nếu mAP50 cao nhưng mAP50–95 thấp, cần kiểm điều gì trên box? mAP50 chỉ cần IoU ≥ 0.50 nên box lệch cạnh vẫn tính đúng. mAP50–95 lấy trung bình từ IoU 0.50 đến 0.95. Khoảng cách hai số lớn nghĩa là box đúng vùng xe nhưng chưa ôm sát: thừa nền, thiếu đầu/đuôi xe, hoặc gộp hai xe sát nhau. Việc cần kiểm là độ khít của box, không phải chỉ class.
3. Lỗi class nào có thể liên quan guideline? Dữ kiện nào hỗ trợ nhận xét? Chưa có confusion matrix của model. Trên nhãn, chỗ dễ lẫn đã ghi ở guideline là `bus`/`van` (`drive_002`, `drive_015`) và `van`/`truck` (`drive_042`, xe cứu hộ `drive_034`). Khi có `assets/yolo26_runs/vehicle_eval/`, đối chiếu ô nhầm đó với các ảnh eval trước khi kết luận lỗi đến từ guideline.
4. Vì sao không dùng 10 ảnh eval để train? Vai trò validation của chúng trong notebook là gì? `data.yaml` để `val` trỏ vào 10 ảnh eval. Notebook dùng chính tập này để chọn `best.pt` trong lúc train. Đưa eval vào train làm model học luôn ảnh dùng để chấm, mAP không còn đo được ảnh chưa train. Eval ở đây là validation để chọn checkpoint, không phải test set độc lập, và vẫn phải giữ nguyên split.

## 6. Khó khăn và cách xử lý

| Bước/thời điểm | Lỗi quan sát | Cách đã thử | Kết quả/còn thiếu |
|---|---|---|---|
| Xuất nhãn CVAT | File `.txt` nằm trong `dataset/labels/train/dataset/labels/Test/`, kèm `Test.txt` và `data.yaml` của CVAT | Kéo 50 file `drive_*.txt` ra đúng `dataset/labels/train/`, không ghi đè `data.yaml` của bài | Checker đạt 50/50 |
| Đặt gold | Zip gold giải nén thành `gold_train_labels/gold_train_labels/` | Trỏ `--gold-labels` vào tầng chứa file `.txt` | Chấm được, không commit gold |
| Gold QC lần 1 | F1 0.5829, mean IoU 0.8464; `bus` nhiều hơn gold, `van` và `truck` ít hơn | Sửa phân lớp theo schema rồi chạy lại `evaluate_annotations.py` | F1 0.9969, mean IoU 1.0, `passed` true. Còn 2 box lệch ở `drive_002` |
| Train Colab | Notebook chưa chạy xong tại thời điểm viết báo cáo | Giữ `REPO_URL` là repo đã push, không upload gold | Thiếu link Colab, 4 chỉ số model và 2 folder assets |

## 7. Tự đánh giá theo rubric

Đối chiếu [RUBRIC.md](../../RUBRIC.md).

| Tiêu chí | Trạng thái |
|---|---|
| Hoàn thành và định dạng YOLO (10) | Đã có 50/50 file, checker đạt |
| Đầy đủ vật thể (20) | Đã rà 10 ảnh về che khuất, cắt khung và vật ngoài schema. Lần chấm sau có FN = 2, chỉ ở `drive_002` |
| Độ bám sát box (20) | mean IoU lần sau = 1.0 trên các box ghép được |
| Phân lớp nhất quán (15) | Lần đầu lệch `bus`/`van`/`truck`, lần sau đã qua cổng. Còn câu hỏi ở `drive_034` và `drive_015` |
| Mini guideline (10) | Đã điền định nghĩa bốn lớp, quy tắc box và ba ca có ảnh, quyết định, lý do |
| Gold-set QC (15) | Có JSON, F1 0.9969 và mean IoU 1.0, cả hai trên ngưỡng. Có số trước/sau |
| Pipeline YOLO (10) | Chưa có. Colab chưa xong nên chưa có metrics, ảnh eval hay nhận xét lỗi model |

## 8. Công cụ AI và tài liệu tham khảo

Dùng Cursor (Grok) để đọc các file hướng dẫn của bài, chạy `check_yolo_labels.py` và `evaluate_annotations.py`, đối chiếu số box theo lớp, và soạn các mục chữ trong `GUIDELINE_MINI.md` cùng báo cáo này. Số ở mục 3 và 4 lấy từ output checker và `outputs/annotation_evaluation.json`, không phải số minh họa. Ba ca mơ hồ được viết sau khi xem các ảnh train tương ứng. Phần chỉ số model ở mục 5 chưa điền vì chưa có log Colab. Không ghi token, mật khẩu, và không đính kèm gold train.

Nguồn ngoài repo: hướng dẫn trong repo bài (`GUIDE.md`, `RUBRIC.md`, `SUBMISSION.md`) và schema bốn lớp của lab. Ảnh gốc thuộc tập con UA-DETRAC (CC-BY-4.0) đã được biên tập trong đề, không truy vết ID nguồn.
