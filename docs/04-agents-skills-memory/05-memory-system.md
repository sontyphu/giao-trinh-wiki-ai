---
title: Hệ thống bộ nhớ AI
type: huong-dan
created: 2026-06-01
updated: 2026-06-01
phan: 04
---

# Hệ thống bộ nhớ AI

## Trước đó

[04-tao-skill-dau-tien](04-tao-skill-dau-tien.md) — Skill đã tạo xong.

---

## Lớp 1: Hiểu nhanh

Mỗi khi đóng terminal và mở lại, AI quên hết cuộc chat trước. **Memory** giải quyết điều này bằng cách lưu thông tin quan trọng vào file — AI đọc file đó mỗi lần mở session mới, và biết ngay bạn là ai, muốn gì, kho hoạt động theo quy tắc nào.

---

## Lớp 2: Memory hoạt động thế nào

### Không có memory

```
Phiên 1:  Bạn: "Tôi tên Sơn, làm marketing, kho lưu kiến thức kinh doanh"
Phiên 2:  AI không nhớ gì → Bạn phải nói lại từ đầu
(Lặp lại mỗi ngày trong 6 tháng → tốn thời gian, mất tập trung)
```

### Có memory

```
Phiên 1:  AI ghi: "User tên Sơn, marketing, kho = kiến thức kinh doanh"
          → Lưu vào memory/user-identity.md
Phiên 2:  AI đọc file → Biết ngay → Vào việc luôn, không cần giới thiệu lại
```

### Memory lưu ở đâu?

```
~/.claude/projects/<tên-kho>/memory/
├── MEMORY.md                  ← mục lục ngắn, AI đọc mỗi session
├── user-identity.md           ← bạn là ai
├── feedback-khong-dung-emoji.md ← quy tắc AI phải nhớ
├── project-ra-mat-san-pham.md ← dự án đang chạy
└── reference-dashboard.md     ← link/tài nguyên quan trọng
```

---

## Lớp 3: Hiểu sâu

### 4 loại memory

**1. User — Bạn là ai**

Thông tin về bạn giúp AI trả lời phù hợp hơn với bối cảnh cụ thể của bạn.

```markdown
---
name: user-identity
description: Thông tin chủ kho — Sơn, marketing, doanh nhân
metadata:
  type: user
---

Tên: Sơn. Lĩnh vực: marketing và đào tạo doanh nghiệp.
Kho Brain lưu kiến thức về sales, marketing, quản lý.
Ngôn ngữ: Tiếng Việt 100%.
Phong cách muốn AI dùng: ngắn gọn, thẳng vào vấn đề, đưa ví dụ cụ thể.
```

**2. Feedback — Quy tắc AI phải nhớ**

Khi bạn sửa lỗi AI (hoặc xác nhận AI làm đúng một cách không hiển nhiên), AI ghi lại để không sai lần sau.

```markdown
---
name: feedback-khong-bullet-ngan
description: Không dùng bullet point dưới 2 câu
metadata:
  type: feedback
---

Không tạo bullet point ngắn dưới 2 câu.
**Lý do**: user thấy bullet ngắn gây cảm giác sơ sài, thiếu giải thích.
**Áp dụng**: mọi nội dung trong kho — viết câu đủ ý, không viết kiểu liệt kê cụt.
```

**3. Project — Dự án đang chạy**

Context về công việc hiện tại giúp AI ưu tiên đúng khi trả lời.

```markdown
---
name: project-ra-mat-khoa-hoc-thang-7
description: Đang chuẩn bị ra mắt khoá học tháng 7/2026
metadata:
  type: project
---

Đang chuẩn bị ra mắt khoá "Marketing Thực Chiến" vào 15/07/2026.
**Lý do**: mục tiêu doanh thu Q3, cam kết với 50 học viên đăng ký sớm.
**Áp dụng**: ưu tiên ingest tài liệu về marketing; gắn hành động với deadline 15/07.
```

**4. Reference — Đường dẫn quan trọng**

Link, URL, tài nguyên AI cần nhớ để không phải hỏi lại mỗi lần.

```markdown
---
name: reference-dashboard-ads
description: Dashboard theo dõi quảng cáo Facebook
metadata:
  type: reference
---

Dashboard Facebook Ads: https://business.facebook.com/adsmanager
Dùng khi cần tra số liệu chiến dịch quảng cáo đang chạy.
```

### Khi nào AI tự lưu memory (không cần bạn yêu cầu)

AI tự nhận diện và lưu khi:
- Bạn **giới thiệu bản thân** ("Tôi tên X, làm Y")
- Bạn **sửa lỗi AI** ("Đừng làm thế, làm thế này")
- Bạn **xác nhận cách làm đúng** ("Đúng rồi, lần sau cũng làm vậy")
- Bạn **nhắc đến link/tài nguyên** quan trọng

### Khi nào BẠN chủ động lưu memory

```
Lưu vào memory: tôi không dùng emoji trong bất kỳ nội dung nào trong kho
```

```
Lưu vào memory: khoá học tháng 7 deadline ngày 15/07/2026, ưu tiên cao nhất
```

### Khi nào KHÔNG lưu memory

Không lưu những thứ có thể tìm thấy từ file trong kho:
- Cấu trúc thư mục, tên file → đọc được từ kho
- Lịch sử thay đổi → đọc từ log.md
- Nội dung đã ingest → đọc từ wiki/

Memory dành cho thông tin về **bạn và bối cảnh của bạn** — không phải nội dung kho.

### Xem và quản lý memory

**Xem memory hiện tại**:
```
/memory
```

**Thêm memory mới**:
```
Lưu vào memory: tôi prefer markdown plain text, không dùng HTML
```

**Cập nhật memory**:
```
Cập nhật memory về ngôn ngữ: giờ tôi muốn một số trang bằng tiếng Anh cho phần kỹ thuật
```

**Xoá memory**:
```
Xoá memory về dự án ra mắt tháng 7 — đã xong rồi
```

### Memory cho agent riêng

Agent cũng có thể có memory riêng ở `.claude/agent-memory/<tên-agent>/`:

```
.claude/agent-memory/ingest-pipeline/
├── MEMORY.md
├── feedback-cach-viet-source-page.md
└── project-uu-tien-khoa-nao.md
```

Agent học từ feedback bạn đưa cho agent đó — không lẫn lộn với memory chung của bạn.

### 4 lỗi phổ biến với memory

**Lỗi 1 — Memory quá nhiều, quá lộn xộn**: 200+ file memory → AI đọc chậm, dễ miss. Giữ dưới 50 file. Dọn định kỳ mỗi 3 tháng.

**Lỗi 2 — Memory trùng lặp**: 3 file cùng nói "user thích tiếng Việt" → gộp lại 1 file. Hỏi AI: *"Tìm các memory có nội dung trùng nhau"*.

**Lỗi 3 — Memory cũ, không còn đúng**: Memory ghi "đang chuẩn bị khoá tháng 7" nhưng giờ đã tháng 9. Xoá hoặc cập nhật.

**Lỗi 4 — Lưu thông tin nhạy cảm**: Mật khẩu, số tài khoản ngân hàng, thông tin riêng tư → KHÔNG lưu vào memory AI. Dùng phần mềm quản lý mật khẩu (1Password, Bitwarden).

### Memory vs CLAUDE.md — Khác nhau thế nào?

| CLAUDE.md | Memory |
|---|---|
| Quy tắc của kho | Thông tin về bạn |
| Mọi người dùng kho đều theo | Chỉ áp dụng cho bạn |
| Nên commit Git (chia sẻ được) | Không commit (riêng tư) |
| Đặt trong kho | Đặt ngoài kho (~/.claude/) |

Hình dung: CLAUDE.md = "nội quy công ty", Memory = "hồ sơ nhân viên".

---

## Điều quan trọng nhất cần nhớ

> **Memory = dạy AI nhớ về bạn. CLAUDE.md = dạy AI nhớ về kho.**

Hai thứ này bổ sung cho nhau, không thay thế nhau.

---

## 📖 Chú thích

- **ingest** = đưa tài liệu thô vào kho để AI đọc và xử lý thành trang wiki — gồm: đọc nội dung, rút ý chính, tạo trang tóm tắt và cập nhật trang khái niệm liên quan.
- **memory** = file lưu thông tin AI cần nhớ qua các phiên làm việc khác nhau (ai là bạn, quy tắc nào phải theo, dự án nào đang chạy). Không có memory → mỗi lần mở mới AI quên hết.
- **commit** (Git) = hành động lưu lại một điểm phiên bản — như "chụp ảnh" trạng thái toàn bộ kho tại một thời điểm. Có thể khôi phục kho về bất kỳ commit nào trước đó.
- **terminal** (còn gọi là cửa sổ dòng lệnh) = nơi bạn gõ lệnh văn bản thay vì click chuột. Trên Mac: tìm "Terminal" trong Spotlight. Trên Windows: tìm "PowerShell" hoặc "Command Prompt".

## Tiếp theo

[01-lint-wiki-dinh-ky](../05-bao-tri-lint/01-lint-wiki-dinh-ky.md) — Rà soát kho định kỳ để giữ sạch
