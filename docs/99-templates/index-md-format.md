---
title: index.md format
type: template
created: 2026-05-29
updated: 2026-05-29
phan: 99
---

# index.md format (copy-paste)

Template + quy ước cho `index.md` ở root vault. File mục lục.

---

## Format chuẩn

```
# Index — <Vault Name>

Mục lục đầy đủ. Gom theo nhóm. Mỗi entry 1 dòng.

## <Group 1>

- [[Page A]] — mô tả 1 dòng (date, author nếu source)
- [[Page B]] — ...

## <Group 2>

- [[Page C]] — ...
```

---

## Group cơ bản

Vault knowledge:

```
## Sources
## Concepts
## Entities
## Courses
## Stories
## Topics
## Analyses
## Reference
```

Vault lifestyle:

```
## Domains
## Entities
## Events
## Concepts
## Analyses
## Journal
```

Vault production:

```
## Sources
## Assets
  - Lead pages
  - Sale pages
  - Contents
  - Ads
  - Events
## Reports
## Concepts
## Entities
```

Vault execution (4DX):

```
## mục tiêu tối quan trọng
## Reviews weekly
## Scoreboard
## Cadence
```

---

## Format mỗi entry

```
- [[Page Name]] — <mô tả 1 dòng>
```

Mô tả nên include:
- **Source**: tác giả + date — vd `[[Paul Graham — PMF (2024)]] — bài về PMF process (PG, 09/2024)`
- **Concept**: domain + rating — vd `[[Bộ não thứ 2]] — knowledge management 5/5`
- **Course**: program code + version — vd `[[Khoá Bán Hàng B]] — Sales B2C, đợt 23 (2026-Q3)`
- **Entity**: vai trò trong vault — vd `[[Paul Graham]] — founder Y Combinator, viết essay`

---

## Ví dụ vault knowledge

```
# Index — My Brain

Mục lục.

## Sources

### Articles
- [[Paul Graham — Product Market Fit (2024)]] — bài về PMF process (PG, 09/2024)
- [[Sam Altman — Startup Playbook]] — playbook Y Combinator alumni (Sam, 2022)
- [[Naval Ravikant — Specific Knowledge]] — concept "specific knowledge" (Naval, 2018)

### Sách
- [[Atomic Habits — James Clear (2018)]] — 4 law of behavior change
- [[Lean Startup — Eric Ries (2011)]] — build-measure-learn loop

### Transcripts
- [[Khoá Bán Hàng B - Đợt 21 - Ngày 1 (28-11-2025)]] — khoá bán hàng đợt 21, ngày 1
- [[Khoá Bán Hàng B - Đợt 21 - Ngày 2 (29-11-2025)]] — khoá bán hàng đợt 21, ngày 2
- [[Khoá Bán Hàng B - Đợt 21 - Ngày 3 (30-11-2025)]] — khoá bán hàng đợt 21, ngày 3

## Concepts (đa khoá — top 20)

- [[Hệ thống bán hàng 8+2]] — Sales 5/5, dùng Khoá Bán Hàng A + B + Nâng Cao C
- [[14 chiến lược lead generation]] — Sales 4/5, dùng Khoá Bán Hàng B (mới đợt 21)
- [[Bộ não thứ 2]] — Knowledge 5/5, dùng xuyên nhiều khoá
- [[Customer Value Canvas]] — Persona 4/5, dùng nhiều khoá
- [[6 Nhu cầu con người]] — Psychology 4/5, dùng nhiều khoá
- [[Sự gán nghĩa]] — Psychology 4/5
- [[Hệ thống niềm tin]] — Psychology 4/5
- [[Cài đặt tư duy 5 bước]] — Coaching 5/5, signature chuyên gia
- [[Hot Seat]] — Coaching format 4/5
- [[REM-30s]] — Networking 4/5

## Concepts (single-course)

- [[Founder Mode]] — Startup 3/5, single source Paul Graham (2024-09)
- [[Email DNS setup]] — Email 3/5, single course EMM

## Entities

### Người
- [[Paul Graham]] — founder Y Combinator, essayist
- [[Sam Altman]] — CEO OpenAI, ex-Y Combinator
- [[Naval Ravikant]] — angel investor, author

### Tổ chức
- [[Y Combinator]] — accelerator
- [[Câu lạc bộ kinh doanh]] — community networking

## Courses

### Offline lớn
- [[Khoá Bán Hàng B]] — Sales B2C, 3 ngày, đợt 23 (2026-Q3)
- [[Khoá Marketing Online]] — Marketing online, 3 ngày
- [[Khoá Tư Duy Doanh Chủ]] — Tư duy doanh chủ

### Khoá intensive + summit
- [[Khoá Intensive Camp]] — offline event 3-5 ngày
- [[Khoá Summit Hàng Năm]] — annual event

### Online tự học
- [[EMM — Email Marketing Mastery]] — Email mkt, 6 module

### Coaching weekly
- [[Coaching Weekly]] — 1 năm, tier cao nhất

## Stories / Ngụ ngôn

- [[Gã ăn mày giàu có]] — illustrate "đầu tư vào bản thân"
- [[Cô gái tóc dài]] — illustrate "thay đổi mindset"
- [[Bút chì cùn]] — illustrate "kỹ năng cần mài giũa"

## Topics

- [[Tâm lý khách hàng B2C]]
- [[Persona doanh chủ Việt Nam]]
- [[Building Second Brain]]

## Analyses

- [[Validate PMF cho B2B SaaS]] — 5 action recommend (2026-04-29)
- [[Concept đa khoá xuyên 5 chương trình]] — map concept (2026-02)

## Reference

- [[Schema vault]] — link CLAUDE.md
- [[Workflow ingest]] — link 02-vault-dau-tien-brain/07-ingest-source-dau-tien
```

---

## Quy tắc viết index

### Rule 1 — Mỗi entry 1 dòng

```
- [[Page]] — short description
```

KHÔNG nhiều dòng cho 1 entry.

### Rule 2 — Wikilink (liên kết nội bộ) bắt buộc

Mọi entry phải có `[[Page Name]]`. Không paste plain text.

### Rule 3 — Group theo loại / domain

Không sort alphabet (đó là filename rồi). Sort theo nhóm logic.

### Rule 4 — Top N quan trọng

Group "Concepts (đa khoá — top 20)" — chỉ liệt 20 quan trọng. Không liệt 600 concept.

Đầy đủ → dùng Dataview query trong Obsidian (xem dưới).

### Rule 5 — Update khi tạo page mới

Mỗi ingest → AI append entry mới vào group đúng. KHÔNG để page tồn tại mà index không có.

Rà soát pass sẽ flag drift.

---

## Sub-index thay vì index khổng lồ

Vault > 500 page → index khổng lồ khó dùng. Tách sub-index:

```
## Concepts

- [[index-concepts]] — 600 concept đầy đủ, link đến đây
- Top 20 concept dưới đây:
  - [[Hệ thống bán hàng 8+2]]
  - ...
```

`wiki/index-concepts.md`:

```
# Index — Concepts

Toàn bộ 600 concept page. Sort theo domain.

## Sales (120)
- [[Hệ thống bán hàng 8+2]]
- ...

## Marketing (95)
- ...

## Psychology (88)
- ...
```

---

## Dataview alternative

Obsidian Dataview plugin cho phép query phần thông tin đầu file (frontmatter) YAML — tự động generate list:

```
## Concepts (Dataview auto-generated)

TABLE 
  tags as "Tags",
  rating as "Rating"
FROM "wiki/concepts"
WHERE type = "concept"
SORT rating DESC
LIMIT 20
```

Khi cài Dataview, switch sang Reading mode → auto render bảng.

Ưu: auto sync, không phải update index khi tạo page mới.
Nhược: chậm khi > 1000 page.

→ Hybrid: index tay cho top 20 + Dataview cho full list.

---

## Khi index có entry stale

Page đã rename / delete nhưng index vẫn còn entry cũ → broken link (liên kết hỏng).

Fix:
- Rà soát pass detect
- AI bulk remove entry stale

```
> Rà soát index.md: tìm entry trỏ page không tồn tại. Remove.
```

---

## Cross-vault index

Nếu multi-vault, có thể tạo `Documents/INDEX.md` ở folder cha:

```
# Index — All Sibling Vaults

## Brain
- 1245 page knowledge — [[My Brain/index]]

## Life
- 320 page lifestyle — [[My Life/index]]

## 4DX
- 45 page execution — [[My 4DX/index]]

## Marketing
- 180 page production — [[My Marketing/index]]
```

Mở Obsidian ở Documents/ → có overview toàn ecosystem.

---

## 📖 Chú thích

- **vault** = kho ghi chú — một folder thông thường trên máy tính được Obsidian nhận diện và quản lý đặc biệt (tạo liên kết giữa file, tìm kiếm toàn văn, hiển thị sơ đồ mạng lưới).
- **ingest** = đưa tài liệu thô vào kho để AI đọc và xử lý thành trang wiki — gồm: đọc nội dung, rút ý chính, tạo trang tóm tắt và cập nhật trang khái niệm liên quan.
- **wikilink** = cách tạo liên kết nội bộ trong Obsidian bằng cú pháp `[[Tên trang]]`. Click vào liên kết → mở trang đó ngay. AI tự tạo các wikilink này khi viết wiki.
- **frontmatter** = phần thông tin khai báo ở đầu mỗi file, nằm giữa hai dòng `---`. Ví dụ: loại trang (type), từ khoá (tags), ngày tạo. AI dùng phần này để phân loại và tìm kiếm trang.
- **schema** = cấu trúc và quy tắc tổ chức kho: mỗi loại trang có những phần nào, thông tin nào bắt buộc, đặt tên file theo kiểu gì. Schema được mô tả trong CLAUDE.md.
- **Dataview** = tiện ích mở rộng của Obsidian cho phép tạo danh sách và bảng tự động bằng cách truy vấn thông tin từ frontmatter của các file. Ví dụ: "liệt kê tất cả trang có type = concept theo thứ tự ngày tạo".

## Tiếp theo

Bạn đã hoàn thành 99-templates. Bạn đã hoàn thành toàn bộ giáo trình.

Quay lại README để review hoặc bắt đầu apply.
