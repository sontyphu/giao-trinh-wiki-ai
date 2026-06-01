---
title: Khi nào tách kho mới
type: huong-dan
created: 2026-06-01
updated: 2026-06-01
phan: 03
---

# Khi nào tách kho mới

## Trước đó

[08-query-wiki-dau-tien](../02-vault-dau-tien-brain/08-query-wiki-dau-tien.md) — Kho Brain đang chạy được.

---

## Lớp 1: Hiểu nhanh

Tách kho khi: kho Brain vượt **500 file** VÀ bạn thấy khó tìm kiếm. Không tách vì thích, chỉ tách khi cần.

---

## Lớp 2: 4 dấu hiệu cần tách

**Dấu hiệu 1 — Nội dung không liên quan nhau**

Kho Brain chứa cả kiến thức kinh doanh lẫn ghi chú sức khoẻ cá nhân lẫn hồ sơ học viên. Ba mảng này không liên quan logic → khó tìm, AI dễ lẫn lộn khi trả lời.

Thường tách kho **Life** (cuộc sống cá nhân) ra khỏi Brain đầu tiên. Đây là tách phổ biến nhất.

**Dấu hiệu 2 — Cần bảo mật khác nhau**

Hồ sơ khách hàng VIP, thông tin hợp đồng, dữ liệu nội bộ — không nên để chung với kiến thức công khai. Lỡ chia sẻ kho kiến thức ra ngoài = lộ hết thông tin nhạy cảm.

→ Tách thư mục riêng isolate trong Brain, hoặc tách hẳn kho riêng nếu đủ lớn.

**Dấu hiệu 3 — Cách làm việc khác nhau**

Kho theo dõi mục tiêu (4DX) cần tự động chạy báo cáo mỗi tuần. Kho kiến thức thì không. Workflow khác nhau → nên tách để CLAUDE.md không phải mô tả quá nhiều thứ cùng lúc.

**Dấu hiệu 4 — Cùng loại nội dung lặp lại theo chu kỳ**

Bạn dạy khoá học, mỗi khoá có 50 học viên với hàng trăm trang hồ sơ và bài tập. 3 khoá x 50 học viên = 150 trang chỉ riêng hồ sơ học viên → làm chậm và lộn kho chính.

→ Mỗi khoá một kho riêng.

---

## Lớp 3: Hiểu sâu

### 3 câu hỏi trước khi tách

**1. Kho đã vượt 500 file chưa?**

- Dưới 200 file: tổ chức bằng thư mục con là đủ, chưa cần tách
- 200–500 file: có thể tách nếu archetype rõ ràng
- Trên 500 file: nên tách 1-2 kho chính

**2. 2 mảng định tách có liên kết nhau nhiều không?**

Nếu kho Marketing tham chiếu Brain ở hơn 30% trang → không tách, để chung tiện liên kết. Nếu dưới 10% → tách OK, liên kết chéo là ngoại lệ không phải thường xuyên.

**3. Đã hình dung ra cấu trúc kho mới chưa?**

Chưa rõ kho mới sẽ có cấu trúc thế nào → đợi thêm. Tách sớm = phải làm lại khi cấu trúc rõ. Quy tắc an toàn: tách khi bạn có thể viết được CLAUDE.md cho kho mới mà không cần đoán.

### Quy trình tách an toàn (4 bước)

**Bước 1 — Xác định file sẽ chuyển**

Liệt kê cụ thể file nào chuyển từ Brain sang kho mới. Ví dụ tách kho Life:

```
wiki/concepts/quan-ly-suc-khoe.md      → Life/wiki/concepts/
wiki/entities/bac-si-nguyen-van-a.md   → Life/wiki/entities/
wiki/sources/sach-dinh-duong-abc.md    → Life/wiki/sources/
```

Hỏi AI để tìm file theo nhóm:
```
Liệt kê tất cả file trong wiki/ có liên quan đến chủ đề sức khoẻ và cuộc sống cá nhân.
```

**Bước 2 — Tạo kho mới**

```bash
cd "$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents"
mkdir "My Life"
cd "My Life"
mkdir -p raw/assets wiki/concepts wiki/entities wiki/sources
touch CLAUDE.md index.md log.md
```

Copy mẫu CLAUDE.md từ [claude-md-master-template](../99-templates/claude-md-master-template.md) → chỉnh sửa cho đúng kho mới.

**Bước 3 — Di chuyển file**

```bash
mv "../My Brain/wiki/concepts/quan-ly-suc-khoe.md" "wiki/concepts/"
mv "../My Brain/wiki/entities/bac-si-nguyen-van-a.md" "wiki/entities/"
```

Sau khi di chuyển, các wikilink trong Brain trỏ vào file đó sẽ bị gãy. Có 3 cách xử lý:

- **Cách A**: Rewrite link thành đường dẫn đầy đủ: `[[../My Life/wiki/concepts/quan-ly-suc-khoe]]`
- **Cách B**: Xoá link (nếu trang đó không cần cross-reference)
- **Cách C**: Tạo trang tóm tắt ngắn trong Brain, link sang Life

**Bước 4 — Rà soát link gãy**

Mở Claude trong Brain:
```
Tìm tất cả wikilink gãy sau khi tôi vừa chuyển một số file sang kho Life. Liệt kê theo file nguồn. Không tự sửa.
```

AI báo cáo → bạn quyết cách xử lý từng link.

### 5 loại kho theo mục đích

| Loại | Mục đích | Ví dụ tên kho |
|---|---|---|
| **Kiến thức** | Lưu những gì bạn học từ sách, khoá, bài viết | Brain, Kiến Thức Kinh Doanh |
| **Cuộc sống** | Theo dõi cá nhân, sự kiện, ảnh | Life, Cuộc Sống |
| **Thực thi** | Mục tiêu, báo cáo tự động, theo dõi KPI | 4DX, Execution |
| **Vận hành** | Tài sản marketing, số liệu, A/B test | Marketing, Social Media |
| **Khoá học** | 1 khoá = 1 kho: học viên, bài tập, tiến độ | Sales Master 01, Claude AI 02 |

Mỗi loại có CLAUDE.md khác nhau → không dùng chung được.

### Đặt tên kho sibling

| Kiểu đặt tên | Ví dụ |
|---|---|
| `[Tên] [Loại]` | `Son Brain`, `Minh Life`, `Huong Knowledge` |
| `[Thương hiệu] [Mảng]` | `Winnet Marketing`, `AcadAI Coaching` |
| `[Khoá] [Đợt]` | `Sales Master 01`, `Claude AI 02` |

Không đặt tên quá dài. Có khoảng trắng không sao.

### Khi KHÔNG nên tách

- Kho chưa đến 200 file — thư mục con là đủ
- 2 mảng còn liên quan nhiều đến nhau
- Bạn chưa hình dung được CLAUDE.md của kho mới
- Đang bận deadline — tách kho tốn thời gian fix link gãy

### Lộ trình đề xuất

- **Tháng 1-3**: 1 kho Brain duy nhất. Xây và ổn định trước.
- **Tháng 4-6**: Tách Life (nếu có nhu cầu theo dõi cá nhân)
- **Tháng 7-9**: Tách Marketing (nếu chạy kinh doanh)
- **Tháng 10-12**: Thêm 4DX nếu cần theo dõi mục tiêu nghiêm túc
- **Năm 2+**: Mỗi khoá học mới → 1 kho riêng → dần đến 6-10 kho

Đừng tách 6 kho ngay từ đầu. Build dần tự nhiên khi nhu cầu thật sự phát sinh.

---

## Điều quan trọng nhất cần nhớ

> **Bắt đầu với 1 kho. Tách khi cần, không tách vì thích.**

Hệ thống nhiều kho là kết quả của sự phát triển tự nhiên — không phải mục tiêu cần đạt từ đầu.

---

## 📖 Chú thích

- **vault** = kho ghi chú — một folder thông thường trên máy tính được Obsidian nhận diện và quản lý đặc biệt (tạo liên kết giữa file, tìm kiếm toàn văn, hiển thị sơ đồ mạng lưới).
- **wikilink** = cách tạo liên kết nội bộ trong Obsidian bằng cú pháp `[[Tên trang]]`. Click vào liên kết → mở trang đó ngay. AI tự tạo các wikilink này khi viết wiki.

## Tiếp theo

[02-vault-life-lifestyle](02-vault-life-lifestyle.md) — Xây kho cuộc sống cá nhân
