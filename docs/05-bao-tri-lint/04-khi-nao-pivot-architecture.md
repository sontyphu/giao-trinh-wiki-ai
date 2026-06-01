---
title: Khi nào cải tổ hệ thống
type: huong-dan
created: 2026-06-01
updated: 2026-06-01
phan: 05
---

# Khi nào cải tổ hệ thống

## Trước đó

[03-migrate-rename-vault](03-migrate-rename-vault.md) — Biết cách đổi tên và di chuyển kho.

---

## Lớp 1: Hiểu nhanh

Có 4 mức can thiệp từ nhỏ đến lớn. Luôn thử mức nhỏ trước. Đừng "đập đi xây lại" khi "cập nhật quy tắc" là đủ.

---

## Lớp 2: 4 mức can thiệp

| Mức | Phạm vi | Thời gian | Khi nào dùng |
|---|---|---|---|
| **1. Sửa nhỏ** | 1-5 file | Vài phút | Link gãy, lỗi cụ thể |
| **2. Cập nhật cấu trúc** | Sửa CLAUDE.md + áp dụng toàn kho | Vài giờ | Thêm quy tắc mới, thêm loại trang |
| **3. Tách / gộp kho** | Tạo hoặc gộp vault | 1-2 ngày | Domain tách rõ, kho quá lớn |
| **4. Làm lại từ đầu** | Xây kho mới từ raw | 1-2 tuần | Cấu trúc hỏng nặng không sửa được |

**Quy tắc vàng**: leo thang từ mức thấp. Không nhảy thẳng lên mức 4 khi mức 2 chưa thử.

---

## Lớp 3: Hiểu sâu

### Mức 1 — Sửa nhỏ

Dùng khi: dưới 10 file có vấn đề, lỗi cô lập.

Ví dụ: 3 wikilink gãy sau khi đổi tên file → sửa thủ công trong Obsidian (Cmd+P → Rename file → Obsidian tự update link).

### Mức 2 — Cập nhật cấu trúc

Dùng khi: bạn muốn thêm quy tắc mới hoặc thay đổi mẫu trang, áp dụng cho toàn bộ kho.

**Quy trình**:

1. Cập nhật CLAUDE.md — thêm quy tắc mới
2. Cập nhật file mẫu trong 99-templates — thêm section mới
3. Yêu cầu AI áp dụng đại trà:

```
Cập nhật tất cả trang concept trong wiki/concepts/ để có thêm section
"## Ghi chú áp dụng" ngay trước section "## Khái niệm liên quan".
Điền nội dung stub nếu chưa có dữ liệu. Báo cáo số trang đã cập nhật.
```

AI cập nhật 100+ trang theo batch — bạn không cần làm thủ công từng trang.

### Mức 3 — Tách / gộp kho

Xem [01-khi-nao-tach-vault](../03-mo-rong-multi-vault/01-khi-nao-tach-vault.md) — quy trình đầy đủ 4 bước.

### Mức 4 — Làm lại từ đầu

Chỉ làm khi **tất cả** điều sau đều đúng:

- [ ] Đã thử cập nhật CLAUDE.md (mức 2) — vẫn không sửa được
- [ ] Hơn 50% trang trong kho có sai cấu trúc
- [ ] AI không thể làm việc đúng dù đã hướng dẫn rõ
- [ ] Bạn sẵn sàng dành 1-2 tuần làm lại

**Quy trình làm lại**:

1. **Backup toàn bộ** kho cũ (Git commit + copy ra ổ cứng ngoài)
2. **Tạo kho mới** với CLAUDE.md sạch
3. **Re-ingest từ raw/**: đưa tài liệu gốc qua kho mới — AI tạo wiki mới từ đầu
4. **Chọn lọc chuyển** một số trang có giá trị từ kho cũ (không chuyển hết)
5. **Kiểm tra** kho mới hoạt động đúng
6. **Lưu kho cũ** vào nơi khác (không xoá ngay) — giữ 6 tháng phòng cần tra cứu lại

### 5 dấu hiệu kho cần cải tổ

**Dấu hiệu 1 — Tìm kiếm trả về kết quả lẫn lộn**

Gõ "marketing" ra cả trang kiến thức lẫn hồ sơ khách hàng lẫn ghi chú cá nhân. Không phân biệt được.

→ Cải tổ: tách domain hoặc thêm tag namespace (vd: `domain: business` vs `domain: personal`).

**Dấu hiệu 2 — Mỗi phiên AI mất nhiều thời gian "khởi động"**

Trước khi làm gì, AI cũng phải đọc 10 file để có context. 40% thời gian mỗi phiên là setup.

→ Cải tổ: thu gọn CLAUDE.md, tạo agent cho các tác vụ lặp — agent mang context sẵn, không cần setup lại.

**Dấu hiệu 3 — Nhiều trang nói về cùng một chủ đề**

Khái niệm "phễu bán hàng" xuất hiện ở 4 trang khác nhau với 4 phiên bản khác nhau. AI không biết dùng cái nào.

→ Cải tổ: gộp lại thành 1 trang chính thức (trang chính thức), 3 trang kia chỉ link về trang chính.

```
Tìm tất cả trang trong wiki/concepts/ nói về chủ đề "phễu bán hàng".
Liệt kê, đánh giá trang nào đầy đủ nhất. Không tự gộp.
```

**Dấu hiệu 4 — Bạn không muốn mở kho**

Kho "nặng nề", cảm giác phiền phức mỗi lần mở. Thường do cấu trúc không còn phù hợp với nhu cầu thật.

→ Trước cải tổ, hỏi AI để chẩn đoán:

```
Nhìn vào cấu trúc kho và log.md 3 tháng gần nhất, bạn thấy điểm nào làm workflow
trở nên phức tạp hơn cần thiết? Đề xuất đơn giản hoá (không tự thay đổi).
```

**Dấu hiệu 5 — AI lặp lại sai dù đã sửa nhiều lần**

CLAUDE.md không đủ rõ ràng. Quy tắc mơ hồ → AI diễn giải khác nhau mỗi phiên.

→ Cập nhật CLAUDE.md: thêm ví dụ cụ thể (SAI: ... / ĐÚNG: ...), thêm quy tắc phủ định ("KHÔNG được làm X").

### Quy tắc khi cải tổ

**Đo trước, sửa sau**: Đếm số trang lỗi, không sửa theo cảm tính.

**Backup trước bất kỳ thay đổi nào** ở mức 2 trở lên.

**Test trên 5 trang trước, rồi áp dụng toàn kho**: Tránh lỗi nhân đôi ra toàn bộ.

**Ghi lại lý do**: Append vào log.md — 6 tháng sau bạn sẽ hiểu tại sao mình làm vậy.

```markdown
## [2026-06-01] update | Cập nhật cấu trúc — thêm section "Ghi chú áp dụng"
- Lý do: 60% trang concept không có hành động cụ thể, AI hay trả lời lý thuyết
- Phạm vi: 45 trang wiki/concepts/
- Kết quả: cập nhật xong, AI bắt đầu gợi ý hành động trong câu trả lời
```

### 5 sai lầm phổ biến khi cải tổ

**Sai 1 — Cải tổ quá thường xuyên**: Thay đổi cấu trúc mỗi tháng → kho không ổn định, AI confuse, bạn confuse. Thay đổi lớn tối đa 1-2 lần/năm.

**Sai 2 — Cải tổ mà không có mục tiêu rõ**: "Cảm giác cần thay đổi" không phải lý do đủ. Phải có vấn đề cụ thể cần giải quyết.

**Sai 3 — Cải tổ cấu trúc khi nội dung là vấn đề**: Kho có 200 trang rác → cải tổ cấu trúc không cứu được. Phải dọn nội dung trước.

**Sai 4 — Không có kế hoạch rollback**: Cải tổ fail → mất dữ liệu. Backup bắt buộc trước mọi thay đổi mức 2+.

**Sai 5 — Tự quyết mà không hỏi AI**: AI đọc được toàn bộ kho → đôi khi nhìn thấy vấn đề bạn bỏ sót. Hỏi AI trước khi cải tổ:

```
Nhìn vào cấu trúc và log của kho, bạn thấy vấn đề gì đáng lo ngại?
Đề xuất mức can thiệp phù hợp nhất. Không tự sửa.
```

---

## ✅ Bạn đã hoàn thành giáo trình!

Sau Phần 05, bạn có đầy đủ:

- Kho Brain chạy được với AI quản lý tự động
- Biết cách mở rộng khi cần
- Có agent và skill tự động hoá tác vụ lặp
- Có quy trình bảo trì dài hạn
- Biết khi nào và cách cải tổ hệ thống

**Bước thực tế tiếp theo**: Mỗi tuần thêm 3-5 tài liệu vào kho. Sau 3 tháng, kho sẽ đủ dày để thật sự thay đổi cách bạn học và làm việc.

---

## 📖 Chú thích

- **vault** = kho ghi chú — một folder thông thường trên máy tính được Obsidian nhận diện và quản lý đặc biệt (tạo liên kết giữa file, tìm kiếm toàn văn, hiển thị sơ đồ mạng lưới).
- **ingest** = đưa tài liệu thô vào kho để AI đọc và xử lý thành trang wiki — gồm: đọc nội dung, rút ý chính, tạo trang tóm tắt và cập nhật trang khái niệm liên quan.
- **wikilink** = cách tạo liên kết nội bộ trong Obsidian bằng cú pháp `Tên trang`. Click vào liên kết → mở trang đó ngay. AI tự tạo các wikilink này khi viết wiki.
- **commit** (Git) = hành động lưu lại một điểm phiên bản — như "chụp ảnh" trạng thái toàn bộ kho tại một thời điểm. Có thể khôi phục kho về bất kỳ commit nào trước đó.

## Tiếp theo

[claude-md-master-template](../99-templates/claude-md-master-template.md) — Mẫu CLAUDE.md để copy-paste
