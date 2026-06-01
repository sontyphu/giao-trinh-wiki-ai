---
title: Course bản đồ nội dung template
type: huong-dan
created: 2026-05-29
updated: 2026-05-29
phan: 02
---

# Course bản đồ nội dung template

## Trước đó

[05-source-page-template](05-source-page-template.md) — source page schema OK.

---

## bản đồ nội dung là gì

**bản đồ nội dung** = **bản đồ nội dung** (bản đồ nội dung) — page tổng quan 1 chủ đề lớn (1 chương trình đào tạo, 1 dự án), liệt mọi page con liên quan.

Course bản đồ nội dung = bản đồ nội dung cho 1 chương trình đào tạo:
- Định vị khoá học
- Cấu trúc khoá (modules / story / topic)
- Phiên bản đã ingest
- Cases học viên signature
- Tài sản đã sản xuất

Course bản đồ nội dung là **hub** trong graph view — concept page liên kết quanh nó.

Không phải mọi vault cần Course bản đồ nội dung. Vault knowledge cá nhân không có khoá đào tạo → skip section này.

---

## Khi nào tạo Course bản đồ nội dung

- Bạn là coach/trainer có chương trình đào tạo cụ thể
- Bạn dạy 1 khoá nhiều phiên bản qua thời gian
- Bạn muốn track concept nào dùng ở khoá nào

Vd:
- Chuyên gia có 34 khoá → 34 Course bản đồ nội dung
- Bạn dạy 1 khoá "Email Marketing Basics" → 1 Course bản đồ nội dung

---

## Template đầy đủ

```
---
type: concept
tags: [chuong-trinh, course/<code>, <theme-tags>]
program_code: <CODE>
parent: "[[Hệ sinh thái đào tạo của bạn]]"
sources: [...]
created: 2026-05-29
updated: 2026-05-29
---

# <CODE> — <Tên đầy đủ>

[1-2 đoạn — định vị khoá: ai cho ai, dạy gì, format]

## Định vị

[3-5 bullet — USP khoá học]

## Vai trò trong hệ sinh thái

[Link upstream/downstream/song-song courses]

- **Upstream** (học trước khoá này): [[Course A]]
- **Downstream** (học sau khoá này): [[Course B]]
- **Song song** (cùng level, đi cặp): [[Course C]]

## Cấu trúc khoá

[3-5 ngày / 12 buổi / 6 module — tuỳ format]

- Ngày 1: ...
- Ngày 2: ...
- Ngày 3: ...

## Modules / Khái niệm cốt lõi

[Wikilink mỗi module/concept dạy trong khoá]

- [[Concept 1]] — vai trò trong khoá
- [[Concept 2]] — ...

## Stories / Ngụ ngôn dùng

- [[Story 1]] — dùng để illustrate concept X
- [[Story 2]] — ...

## Topics liên quan

- [[Topic 1]]
- [[Topic 2]]

## Cases học viên signature

- [[Học viên A]] — case nổi bật
- [[Học viên B]]

## Tài sản đã sản xuất

- Sale page: <URL>
- Lead page: <URL>
- Video promo: <URL>
- Email sequence: ... emails

## Phiên bản đã ingest

| # | Phiên bản | Date | Source page | Signature |
|---|---|---|---|---|
| 21 | Đợt 21 | 2025-11-28 | [[Khoá Bán Hàng B - Đợt 21 - Ngày 1 (28-11-2025)]] + D2/D3 | Mới nhất |

## Khoá học liên quan

- [[Course X]] — concept overlap
- [[Course Y]]

## Câu hỏi mở

- ?
```

---

## Giải thích từng section

### Frontmatter

```
---
type: concept                                    # bản đồ nội dung type concept (graph view nhìn như hub concept)
tags: [chuong-trinh, course/khoa-ban-hang-b, ban-hang]  # bắt buộc chuong-trinh + course/<code>
program_code: KHOA-BAN-HANG-B                    # code duy nhất
parent: "[[Hệ sinh thái đào tạo của bạn]]"       # link lên root
sources: ["[[Khoá Bán Hàng B - Đợt 21 - Ngày 1 (28-11-2025)]]", ...]
---
```

#### `program_code`

Mã code duy nhất, chữ thường + gạch nối:
- `khoa-ban-hang-b` — Khoá Bán Hàng B
- `khoa-marketing-online` — Khoá Marketing Online
- `emm` — Email Marketing Mastery

Code dùng để:
- Tag `course/<code>` trên concept đa khoá
- Filter graph view
- Filename không gian cho source page

#### Tag `chuong-trinh`

Tag chính của course page. Graph view color group dùng tag này render hub đỏ/cam.

### Định vị

USP của khoá:
- Cho ai (target persona)
- Dạy gì (modules chính)
- Format (online / offline / hybrid, mấy ngày)
- Giá (tuỳ chọn)

Vd:
```
- **Target**: Doanh chủ vừa và nhỏ, đội sales 5-20 người
- **Dạy**: Hệ thống bán hàng 8+2 + 14 chiến lược lead gen + 7 kỹ thuật xử lý từ chối
- **Format**: 3 ngày offline (T2-T4) hội trường Hà Nội/HCM, ~700 attendees
- **Phiên bản hiện tại**: Đợt 23 (2026-Q3)
```

### Vai trò trong hệ sinh thái

Quan trọng nhất. Map khoá vào graph lớn:
- **Upstream**: học trước khoá này (vd: Khoá Tư Duy trước Khoá Bán Hàng)
- **Downstream**: học sau (vd: Khoá Bán Hàng xong → Khoá Marketing Online)
- **Song song**: cùng level (vd: Khoá Bán Hàng song song Khoá Camp)

### Cấu trúc khoá

Chia theo format:
- 3 ngày → 3 mục Ngày 1/2/3
- 6 module → 6 mục Module 1-6
- 12 buổi → 12 mục

Mỗi mục liệt main concept dạy.

### Modules / Khái niệm cốt lõi

**Bắt buộc** — link mọi concept dạy trong khoá:

```
- [[Hệ thống bán hàng 8+2]] — module chính, 12 giờ
- [[14 chiến lược lead generation]] — bổ trợ, 4 giờ
- [[7 kỹ thuật xử lý từ chối]] — practice live, 3 giờ
```

Mỗi link concept → course → bắt buộc link ngược concept → course ở concept page section "Khoá học sử dụng".

### Phiên bản đã ingest

Bảng timeline:

```
| # | Phiên bản | Date | Source page | Signature |
|---|---|---|---|---|
| 21 | Đợt 21 | 2025-11-28 | [[Khoá Bán Hàng B - Đợt 21 - Ngày 1]] | Mới nhất, thêm 14 lead gen |
```

Khi ingest source mới → add row mới.

### Tài sản đã sản xuất

Link ra sale page, lead page, video promo, email sequence:

```
- Sale page: https://example.com/khoa-ban-hang-b (current)
- Lead page: https://example.com/lp/checklist-30s
- Video promo: https://youtu.be/abc123
- Email sequence: 12 emails
```

---

## Quy tắc 2 chiều (nhất quán)

Mỗi link course → concept (trong "Modules") **phải có** link ngược concept → course (trong "Khoá học sử dụng" của concept page).

Vd:
- `Khoá Bán Hàng B.md` có `## Modules — [[Hệ thống bán hàng 8+2]]`
- → `Hệ thống bán hàng 8+2.md` phải có `## Khoá học sử dụng — [[Khoá Bán Hàng B]]`

Rà soát pass sẽ check và flag bất nhất.

---

## Concept đa khoá

Concept dùng ở **nhiều khoá** → tag `course/<code>` đa khoá:

```
tags: [framework, course/khoa-ban-hang-a, course/khoa-ban-hang-b, course/khoa-nang-cao-c, signature]
```

Và section "Khoá học sử dụng" liệt cả 3:

```
## Khoá học sử dụng
- [[Khoá Bán Hàng B]] — module chính (12h)
- [[Khoá Bán Hàng A]] — tiền thân, dạy lần đầu
- [[Khoá Nâng Cao C]] — mở rộng sang giai đoạn after-sales
```

Graph view: concept ngồi giữa 3 course hub → render đẹp.

---

## Course bản đồ nội dung cha — Hệ sinh thái

Nếu bạn có 5+ khoá → tạo bản đồ nội dung cha "Hệ sinh thái đào tạo":

```
# Hệ sinh thái đào tạo

## Nhóm khoá cốt lõi
- [[Khoá Bán Hàng B]] — bán hàng
- [[Khoá Marketing Online]] — marketing online

## Nhóm khoá bổ trợ
- [[Khoá Bán Hàng A]] — bán hàng nền tảng
- [[Khoá Email Marketing]] — email marketing

## Coaching weekly
- [[Coaching Weekly]] — 1 năm, tier cao nhất
```

Mỗi course bản đồ nội dung có frontmatter `parent: "[[Hệ sinh thái đào tạo]]"` → graph render hierarchy.

---

## Test với Claude

```
> Tạo course bản đồ nội dung giả cho khoá "Email Marketing Mastery" (code: emm) theo template.
> Định vị: dạy email marketing cho freelancer + agency.
> Format: 4 module online, mỗi module 2h.
> Stub những phần chưa có data.
> Lưu vào wiki/courses/EMM - Email Marketing Mastery.md
```

Claude tạo file → mở Obsidian xem template đúng chưa.

---

## 📖 Chú thích

- **vault** = kho ghi chú — một folder thông thường trên máy tính được Obsidian nhận diện và quản lý đặc biệt (tạo liên kết giữa file, tìm kiếm toàn văn, hiển thị sơ đồ mạng lưới).
- **ingest** = đưa tài liệu thô vào kho để AI đọc và xử lý thành trang wiki — gồm: đọc nội dung, rút ý chính, tạo trang tóm tắt và cập nhật trang khái niệm liên quan.
- **wikilink** = cách tạo liên kết nội bộ trong Obsidian bằng cú pháp `[[Tên trang]]`. Click vào liên kết → mở trang đó ngay. AI tự tạo các wikilink này khi viết wiki.
- **frontmatter** = phần thông tin khai báo ở đầu mỗi file, nằm giữa hai dòng `---`. Ví dụ: loại trang (type), từ khoá (tags), ngày tạo. AI dùng phần này để phân loại và tìm kiếm trang.
- **schema** = cấu trúc và quy tắc tổ chức kho: mỗi loại trang có những phần nào, thông tin nào bắt buộc, đặt tên file theo kiểu gì. Schema được mô tả trong CLAUDE.md.
- **Graph view** = chế độ hiển thị của Obsidian dạng mạng lưới, cho thấy tất cả trang và liên kết giữa chúng. Dùng để phát hiện trang mồ côi (không ai liên kết tới) hoặc cluster kiến thức.

## Tiếp theo

Đọc tiếp: [07-ingest-source-dau-tien](07-ingest-source-dau-tien.md) — Ingest source đầu tiên cùng Claude.
