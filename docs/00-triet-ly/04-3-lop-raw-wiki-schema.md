---
title: 3 lớp bên trong mỗi kho
type: triet-ly
created: 2026-06-01
updated: 2026-06-01
phan: 00
---

# 3 lớp bên trong mỗi kho

## Trước đó

[03-tai-sao-multi-vault](03-tai-sao-multi-vault.md) — Bạn đã hiểu khi nào cần tách nhiều kho.

---

## Lớp 1: Hiểu nhanh

Mỗi kho có **3 lớp rõ ràng**:
1. **Raw** — kho nguyên liệu thô. Bạn thả vào, AI đọc.
2. **Wiki** — kho AI đã xử lý. AI viết ra đây.
3. **CLAUDE.md** — bản nội quy. Bạn viết để dạy AI cách làm việc.

Ba lớp này không bao giờ trộn lẫn.

---

## Lớp 2: Hiểu rõ

### Lớp 1 — Thư mục `raw/` (bạn sở hữu, AI chỉ đọc)

**Chứa gì**: Tài liệu gốc chưa qua xử lý:
- Bài viết bạn lưu từ web
- File PDF sách/báo cáo
- Transcript (chép lại) từ video, podcast
- File ghi chú thô
- Ảnh chụp màn hình, ảnh từ điện thoại

**Quy tắc cứng**:
- Chỉ đọc, **không bao giờ sửa** nội dung file trong raw
- Không xoá (trừ khi trùng y chang)
- Tổ chức theo nguồn hoặc ngày: `raw/sach-abc/`, `raw/2026-06/`

**Tại sao không sửa?** Vì AI đã đọc và xử lý raw trước đó. Nếu bạn sửa raw sau, AI sẽ bị lẫn lộn giữa nội dung cũ và mới → wiki có thể sai.

Nếu cần chỉnh sửa → tạo file mới với hậu tố `-v2`, giữ bản gốc.

### Lớp 2 — Thư mục `wiki/` (AI sở hữu, bạn duyệt)

**Chứa gì**: Các trang đã qua AI xử lý:
- Trang khái niệm (mỗi khái niệm 1 trang)
- Trang tóm tắt tài liệu (tóm tắt mỗi file raw)
- Trang bản đồ khoá học (tổng hợp 1 khoá học)
- Trang phân tích (kết quả khi AI tổng hợp nhiều nguồn)
- Trang thực thể (người, tổ chức, dự án)

**Quy tắc cứng**:
- AI viết, AI liên kết, AI rà soát
- Bạn đọc, duyệt, sửa khi AI sai
- Mọi trang đều có phần thông tin đầu (frontmatter)
- Mọi trích dẫn đều link về nguồn gốc

**Cấu trúc gợi ý**:
```
wiki/
├── sources/          # tóm tắt tài liệu đã đọc
├── concepts/         # khái niệm, phương pháp
├── entities/         # người, tổ chức, sản phẩm
├── courses/          # bản đồ khoá học
├── analyses/         # kết quả phân tích, tổng hợp
└── index.md          # mục lục
```

### Lớp 3 — File `CLAUDE.md` (bạn + AI cùng phát triển)

**Chứa gì**: Bản nội quy của kho — dạy AI biết:
- Kho này dùng để làm gì
- Cấu trúc thư mục ra sao
- Quy tắc viết trang như thế nào
- Khi gặp tình huống X thì làm Y
- Không được làm gì

**Tại sao CLAUDE.md quan trọng?** Không có nó, AI làm mỗi phiên mỗi kiểu — kho sẽ lộn xộn dần. CLAUDE.md là **hợp đồng** giữa bạn và AI: bạn cam kết cung cấp nguyên liệu, AI cam kết xử lý theo đúng quy tắc.

**Quy tắc**:
- AI đọc CLAUDE.md **đầu mỗi phiên làm việc**
- AI không tự sửa CLAUDE.md mà không hỏi bạn
- Khi AI làm sai nhiều lần → cập nhật CLAUDE.md để rõ hơn

---

## Lớp 3: Hiểu sâu

### Quy trình hoạt động từ đầu đến cuối

```
Bước 1: Bạn thả tài liệu vào raw/
        (PDF, bài web, transcript, ảnh)
              ↓
Bước 2: Bạn nói với AI "xử lý file X"
              ↓
Bước 3: AI đọc CLAUDE.md → biết quy tắc của kho
        AI đọc index.md → biết những trang nào đã có
        AI đọc file raw → hiểu nội dung
        AI thảo luận 3-5 ý chính với bạn
              ↓
Bước 4: AI tạo/cập nhật:
        - wiki/sources/Tên-tài-liệu.md
        - wiki/concepts/Khái-niệm-X.md (nếu có khái niệm mới)
        - wiki/entities/Tên-người.md (nếu nhắc đến ai đó)
        - Cập nhật index.md
        - Thêm vào log.md
              ↓
Bước 5: Bạn duyệt kết quả
        Đúng → OK
        Sai → Chỉ chỗ sai, AI sửa
```

Sau bước này, mọi lần bạn hỏi về tài liệu đó → AI đọc wiki, không cần đọc lại raw.

### 2 file hệ thống quan trọng

**`index.md` — Mục lục**

Liệt kê mọi trang trong kho theo nhóm. AI cập nhật tự động sau mỗi lần ingest.

```markdown
## Khái niệm
- [[Phễu bán hàng]] — 5 bước từ khách lạ đến khách trung thành
- [[Chốt sale]] — 6 kỹ thuật phổ biến

## Tài liệu đã đọc
- [[Sách Marketing 4.0]] — Philip Kotler
- [[Khoá Sales Mastery]] — ghi chú buổi 1-5
```

**`log.md` — Nhật ký**

Ghi lại mọi việc AI đã làm, theo thứ tự thời gian. Dùng để review lại, debug khi có vấn đề.

```markdown
## [2026-06-01] ingest | Sách Marketing 4.0
- Tạo: [[Sách Marketing 4.0]]
- Cập nhật: [[Phễu bán hàng]], [[Hành trình khách hàng]]
- Ghi chú: file PDF 300 trang, chia 3 phần để ingest

## [2026-06-02] query | "Phễu bán hàng online khác offline thế nào?"
- Đọc: [[Phễu bán hàng]], [[Marketing số]]
- Kết quả: bảng so sánh 6 điểm khác biệt
```

### Khi nào cần cập nhật CLAUDE.md

3 tình huống:
1. **AI lặp lại sai lần 3**: Thêm rule rõ ràng vào CLAUDE.md
2. **Có loại nội dung mới**: Vd bạn bắt đầu ingest video → thêm quy trình xử lý video vào CLAUDE.md
3. **Workflow thay đổi**: Vd thêm bước tự động → mô tả bước mới

---

## Điều quan trọng nhất cần nhớ

> **raw/ = bạn thả vào. wiki/ = AI viết ra. CLAUDE.md = luật chơi.**

Ba lớp này tách bạch rõ ràng → kho không bao giờ lộn xộn dù 3 năm sau vẫn dùng.

---

## 📖 Chú thích

- **vault** = kho ghi chú — một folder thông thường trên máy tính được Obsidian nhận diện và quản lý đặc biệt (tạo liên kết giữa file, tìm kiếm toàn văn, hiển thị sơ đồ mạng lưới).
- **ingest** = đưa tài liệu thô vào kho để AI đọc và xử lý thành trang wiki — gồm: đọc nội dung, rút ý chính, tạo trang tóm tắt và cập nhật trang khái niệm liên quan.
- **frontmatter** = phần thông tin khai báo ở đầu mỗi file, nằm giữa hai dòng `---`. Ví dụ: loại trang (type), từ khoá (tags), ngày tạo. AI dùng phần này để phân loại và tìm kiếm trang.

## Tiếp theo

Bạn đã hiểu đủ triết lý. Sang phần cài đặt công cụ.

[01-cai-obsidian](../01-cai-dat/01-cai-obsidian.md) — Cài Obsidian
