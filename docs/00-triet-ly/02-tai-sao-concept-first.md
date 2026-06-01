---
title: Tại sao lưu theo khái niệm
type: triet-ly
created: 2026-06-01
updated: 2026-06-01
phan: 00
---

# Tại sao lưu theo khái niệm

## Trước đó

[01-tai-sao-ai-first-wiki](01-tai-sao-ai-first-wiki.md) — Bạn đã hiểu AI làm thay bạn việc viết kho.

---

## Lớp 1: Hiểu nhanh

Khi AI đọc 100 tài liệu về cùng một chủ đề, nó nên viết ra **50 trang khái niệm** (mỗi khái niệm một trang) — không phải 100 trang tóm tắt (mỗi tài liệu một trang).

Tại sao? Vì bạn không tra cứu theo tài liệu. Bạn tra cứu theo **ý tưởng, khái niệm, phương pháp**.

---

## Lớp 2: Hiểu rõ

### Hai cách AI tổ chức kho

**Cách 1 — Theo tài liệu (source-first)**:
AI đọc 100 tài liệu về sales → viết 100 trang tóm tắt, mỗi trang = 1 tài liệu. Khi bạn hỏi, AI phải quét lại 100 trang để tìm câu trả lời.

**Cách 2 — Theo khái niệm (concept-first)**:
AI đọc 100 tài liệu → rút ra 40 khái niệm chính (phễu bán hàng, chốt sale, xử lý từ chối...) → viết 40 trang khái niệm. Khi bạn hỏi, AI chỉ cần đọc 1-2 trang liên quan → trả lời ngay.

### Ví dụ cụ thể

Giả sử bạn học về **"phễu bán hàng"** từ 4 nguồn khác nhau:
- Buổi đào tạo tháng 3/2024 (lần đầu nghe)
- Sách marketing (hệ thống hoá 5 bước)
- Video YouTube (thêm bước tái kích hoạt)
- Khoá online (thêm chiến lược online)

**Theo tài liệu**: 4 trang tóm tắt, mỗi trang một phiên bản "phễu bán hàng" khác nhau.

**Theo khái niệm**: **1 trang** "Phễu bán hàng" có:
- Định nghĩa cốt lõi
- Các bước đầy đủ (tổng hợp từ 4 nguồn)
- Phần "Nguồn và phiên bản": danh sách 4 nguồn kèm ghi chú mỗi nguồn thêm gì mới

Khi bạn hỏi *"Phễu bán hàng cập nhật nhất khác gì bản đầu?"* → AI đọc 1 trang, trả lời ngay.

### Vì sao cách 1 thất bại theo thời gian

Theo tài liệu, sau 1 năm bạn có 500 trang tóm tắt. Khi hỏi bất kỳ câu gì, AI phải quét 500 trang → chậm, tốn tiền, dễ sót ý.

Tệ hơn: cùng một khái niệm "phễu bán hàng" nằm rải rác ở 10 trang khác nhau, mỗi trang một phiên bản. AI phải tự tổng hợp mỗi lần bạn hỏi — không đảm bảo nhất quán.

---

## Lớp 3: Hiểu sâu

### Nguyên tắc "mỗi khái niệm một trang"

Mỗi ý tưởng/phương pháp **độc lập** = một trang riêng. Không gộp 2 khái niệm vào 1 trang chỉ vì chúng hay được dạy cùng nhau.

**Ví dụ nên tách ra 2 trang**:
- "Nỗi đau khách hàng" vs "Mong muốn khách hàng" → 2 trang (khác nhau về bản chất)
- "Leads lạnh" vs "Leads nóng" vs "Leads ấm" → 3 trang (3 chiến lược xử lý khác nhau)

**Ví dụ gộp lại được**:
- "6 giai đoạn hành trình khách hàng" → 1 trang (là danh sách của 1 framework duy nhất)
- "Ưu điểm và nhược điểm của landing page" → 1 trang (là 2 mặt của cùng chủ đề)

**Cách quyết định**: Nếu 2 khái niệm có **cách áp dụng khác nhau**, tách ra. Nếu chỉ là 2 góc nhìn của cùng 1 thứ, gộp lại.

### Cấu trúc một trang khái niệm

Mỗi trang khái niệm có các phần bắt buộc:

```markdown
---
type: concept
tags: [sales, marketing]
created: 2026-06-01
updated: 2026-06-01
sources: ["[[Tài liệu A]]", "[[Tài liệu B]]"]
---

# Tên khái niệm

[Giải thích ngắn 2-3 câu]

## Áp dụng vào thực tế
- Tình huống nào dùng khái niệm này
- Bước cụ thể cần làm

## Nguồn học
- [[Tài liệu A]] — học lần đầu từ đây
- [[Tài liệu B]] — bổ sung thêm góc nhìn X

## Khái niệm liên quan
- [[Khái niệm cha]] — rộng hơn, chứa cái này
- [[Khái niệm liền kề]] — thường dùng cặp với cái này
```

Template đầy đủ: [concept-page-template](../99-templates/concept-page-template.md)

### Lợi ích cụ thể

Kho theo khái niệm có 200 trang thay vì 1,000 trang tóm tắt. Khi bạn hỏi:

- **Theo tài liệu**: AI quét 1,000 trang → mất 30 giây, tốn nhiều
- **Theo khái niệm**: AI đọc 1-2 trang liên quan → trả lời trong 5 giây, tốn ít

**Nhanh hơn 6 lần. Rẻ hơn 5 lần.**

---

## Điều quan trọng nhất cần nhớ

> **Khái niệm là đơn vị lưu trữ. Tài liệu chỉ là nguồn gốc.**

Tài liệu gốc vẫn lưu trong `raw/` — nhưng bạn sẽ không bao giờ cần mở lại. Kho `wiki/` với các trang khái niệm là nơi bạn tra cứu thật sự.

---

## 📖 Chú thích

- **vault** = kho ghi chú — một folder thông thường trên máy tính được Obsidian nhận diện và quản lý đặc biệt (tạo liên kết giữa file, tìm kiếm toàn văn, hiển thị sơ đồ mạng lưới).

## Tiếp theo

[03-tai-sao-multi-vault](03-tai-sao-multi-vault.md) — Khi nào 1 kho, khi nào nhiều kho
