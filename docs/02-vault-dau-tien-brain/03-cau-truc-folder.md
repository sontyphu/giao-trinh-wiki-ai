---
title: Cấu trúc folder
type: huong-dan
created: 2026-05-29
updated: 2026-05-29
phan: 02
---

# Cấu trúc folder raw/ + wiki/

## Trước đó

[02-claude-md-template](02-claude-md-template.md) — CLAUDE.md đã setup.

---

## Cấu trúc đầy đủ

```
My Brain/
├── CLAUDE.md
├── README.md
├── index.md
├── log.md
│
├── raw/
│   ├── assets/                # ảnh, PDF đính kèm
│   ├── articles/              # Web Clipper output
│   ├── transcripts/           # SRT, TXT từ video
│   ├── notes/                 # ghi chú thủ công
│   ├── photos/                # ảnh chụp iPhone
│   └── exports/               # CSV/XLSX export
│
├── wiki/
│   ├── sources/               # tóm tắt mỗi source
│   ├── concepts/              # framework / phương pháp / triết lý
│   ├── entities/              # người, tổ chức, brand
│   ├── courses/               # bản đồ nội dung mỗi chương trình
│   ├── stories/               # metaphor, ngụ ngôn, nhân vật ẩn dụ
│   ├── topics/                # tổng hợp xuyên source
│   ├── students/              # case học viên (nếu coach/trainer)
│   ├── analyses/              # query lưu lại
│   └── books/                 # tóm tắt sách (tuỳ chọn)
│
└── .obsidian/                 # ẩn — settings Obsidian
```

---

## raw/ — chi tiết

### `raw/assets/`

Ảnh và file binary đính kèm. Obsidian Web Clipper auto download vào đây.

Ví dụ:
```
raw/assets/article-hubspot-marketing.png
raw/assets/diagram-funnel.svg
raw/assets/founder-photo.jpg
```

### `raw/articles/`

Bài web clipped:

```
raw/articles/2026-05-29-paul-graham-product-engineer.md
raw/articles/2026-05-28-sam-altman-startup-playbook.md
```

Format: ngày + slug + `.md`.

Web Clipper config: Settings → Vault `My Brain` → Folder `raw/articles/`.

### `raw/transcripts/`

SRT, TXT từ video (YouTube transcript, Whisper output):

```
raw/transcripts/youtube-paul-graham-startup.txt
raw/transcripts/keynote-jobs-2007-stanford.srt
```

Nếu là khoá đào tạo nhiều buổi:

```
raw/khoa-ban-hang-b/20251128-D1-chunks/
├── chunk-001.txt
├── chunk-002.txt
└── ...
```

Mỗi day 1 subfolder để tránh cross-day leak. Schema folder: `YYYYMMDD-TenKhoa-Version-Diadiem`.

### `raw/notes/`

Ghi chú thủ công bạn viết tay (vd: meeting note):

```
raw/notes/2026-05-29-call-mentor.md
raw/notes/2026-05-28-brainstorm-launch.md
```

### `raw/photos/`

Ảnh iPhone:

```
raw/photos/2026-05-29/
├── IMG_1234.HEIC
├── IMG_1235.HEIC
└── IMG_1236.HEIC
```

Mỗi ngày 1 subfolder.

### `raw/exports/`

CSV/XLSX từ dashboard:

```
raw/exports/2026-W22-google-analytics.csv
raw/exports/2026-05-shopify-orders.xlsx
```

---

## wiki/ — chi tiết

### `wiki/sources/` — Source summary

1 file mỗi source đã ingest. Tóm tắt nguồn 3-5 đoạn + frontmatter + link concept đã touch.

Format file:
```
wiki/sources/Paul Graham — Product Engineer.md
wiki/sources/Khoá Bán Hàng B - Đợt 21 - Ngày 1 (28-11-2025).md
```

Template ở [source-page-template](../99-templates/source-page-template.md).

### `wiki/concepts/` — Concept page

1 file mỗi khái niệm độc lập. Đây là **đơn vị lưu trữ chính**.

Format file:
```
wiki/concepts/Product Engineer.md
wiki/concepts/Hệ thống bán hàng 8+2.md
wiki/concepts/Bộ não thứ 2.md
```

Template ở [concept-page-template](../99-templates/concept-page-template.md).

### `wiki/entities/` — Entity page

1 file mỗi entity có danh tính (người, tổ chức, brand, công cụ).

Format file:
```
wiki/entities/Paul Graham.md
wiki/entities/Y Combinator.md
wiki/entities/Câu lạc bộ kinh doanh.md
```

Section tiêu chuẩn:
- Background
- Vai trò trong vault
- Quote signature
- Source nhắc đến

### `wiki/courses/` — Course bản đồ nội dung (bản đồ nội dung khoá học)

bản đồ nội dung cho mỗi chương trình đào tạo / khoá học.

Format file:
```
wiki/courses/Khoá Bán Hàng B.md
wiki/courses/Khoá Marketing Online.md
```

Template ở [course-moc-template](../99-templates/course-moc-template.md).

### `wiki/stories/` — Story page

Metaphor, ngụ ngôn, nhân vật ẩn dụ signature của chuyên gia.

Ví dụ:
```
wiki/stories/Gã ăn mày giàu có.md
wiki/stories/Cô gái tóc dài.md
wiki/stories/Bút chì cùn.md
```

Tag: `storytelling`, `nhan-vat-an-du`.

### `wiki/topics/` — Topic synthesis

Tổng hợp xuyên source về 1 chủ đề rộng.

Format file:
```
wiki/topics/Tâm lý khách hàng B2B.md
wiki/topics/Founder journey.md
```

### `wiki/students/` — Case học viên

(Nếu vault dành cho coach/trainer)

```
wiki/students/Học viên A.md
wiki/students/Học viên B.md
```

Section: background, lý do tham gia khoá, mục tiêu, kết quả.

### `wiki/analyses/` — Query lưu lại

Tổng hợp query đáng giữ:

```
wiki/analyses/So sánh Khoá Marketing vs Khoá Bán Hàng.md
wiki/analyses/Concept đa khoá xuyên 5 chương trình.md
```

### `wiki/books/` — Tóm tắt sách (tuỳ chọn)

Nếu vault tách Books riêng → skip. Nếu gộp:

```
wiki/books/Atomic Habits.md
wiki/books/Influence.md
```

---

## Khi nào thêm subfolder mới

3 tín hiệu:

### Tín hiệu 1 — 1 loại page xuất hiện 10+ lần

Vault có 10 source weekly coaching → tạo `wiki/sources/coaching-weekly/`.

### Tín hiệu 2 — Loại page có schema riêng

Page sản phẩm có frontmatter riêng (`price`, `category`, `sku`) khác entity thường → tách `wiki/products/`.

### Tín hiệu 3 — Group nhằm graph view dễ đọc

Settings → Graph view → Color groups: tag `path:wiki/courses/` → đỏ → tạo cluster course dễ nhìn.

---

## Quy ước tên subfolder

- Tiếng Anh số ít hoặc số nhiều OK (chọn nhất quán)
- Số nhiều: `wiki/sources/`, `wiki/concepts/` — phổ thông hơn
- Tránh viết hoa folder (`Wiki/Sources` khó type)

---

## Quy ước tên file

Mỗi loại page có pattern riêng:

| Loại | Pattern | Ví dụ |
|---|---|---|
| Source | Tiêu đề gốc | `Paul Graham — Product Engineer.md` |
| Concept | Tên concept | `Hệ thống bán hàng 8+2.md` |
| Entity | Tên đầy đủ | `Câu lạc bộ kinh doanh.md` |
| Course | `<CODE> - <Tên đầy đủ>.md` | `Khoá Bán Hàng B.md` |
| Story | Tên ngụ ngôn | `Gã ăn mày giàu có.md` |
| Analysis | Chủ đề + so sánh | `So sánh hai khoá bán hàng.md` |

Wikilink luôn dùng tên file: `Hệ thống bán hàng 8+2`.

---

## Cleanup khi subfolder bừa

Sau 6 tháng, có thể subfolder mất tổ chức:
- `wiki/concepts/` có 50+ concept, không phân loại
- `wiki/entities/` lẫn người + tổ chức + công cụ

Lúc đó:
- **Không refactor sớm**. Chờ pattern rõ ràng (vd: thấy rõ 20 entity là "mentor", 30 là "đối tác") rồi tách
- Tách subfolder mới: `wiki/entities/mentors/`, `wiki/entities/partners/`
- Cập nhật CLAUDE.md schema
- Rà soát pass để check link không vỡ

Chi tiết refactor ở [03-migrate-rename-vault](../05-bao-tri-lint/03-migrate-rename-vault.md).

---

## 📖 Chú thích

- **vault** = kho ghi chú — một folder thông thường trên máy tính được Obsidian nhận diện và quản lý đặc biệt (tạo liên kết giữa file, tìm kiếm toàn văn, hiển thị sơ đồ mạng lưới).
- **ingest** = đưa tài liệu thô vào kho để AI đọc và xử lý thành trang wiki — gồm: đọc nội dung, rút ý chính, tạo trang tóm tắt và cập nhật trang khái niệm liên quan.
- **wikilink** = cách tạo liên kết nội bộ trong Obsidian bằng cú pháp `Tên trang`. Click vào liên kết → mở trang đó ngay. AI tự tạo các wikilink này khi viết wiki.
- **frontmatter** = phần thông tin khai báo ở đầu mỗi file, nằm giữa hai dòng `---`. Ví dụ: loại trang (type), từ khoá (tags), ngày tạo. AI dùng phần này để phân loại và tìm kiếm trang.
- **schema** = cấu trúc và quy tắc tổ chức kho: mỗi loại trang có những phần nào, thông tin nào bắt buộc, đặt tên file theo kiểu gì. Schema được mô tả trong CLAUDE.md.
- **Graph view** = chế độ hiển thị của Obsidian dạng mạng lưới, cho thấy tất cả trang và liên kết giữa chúng. Dùng để phát hiện trang mồ côi (không ai liên kết tới) hoặc cluster kiến thức.
- **slug** = cách đặt tên file chuẩn: viết thường không dấu, các từ nối bằng dấu gạch ngang. Ví dụ: `phuong-phap-ban-hang.md`, `tu-khoa-da-xac-minh.md`. Đảm bảo tên file hoạt động trên mọi hệ điều hành.

## Tiếp theo

Đọc tiếp: [04-concept-page-template](04-concept-page-template.md) — Concept page template chi tiết.
