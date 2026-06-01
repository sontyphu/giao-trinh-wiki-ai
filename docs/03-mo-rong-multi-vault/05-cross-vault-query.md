---
title: Cross-vault query
type: huong-dan
created: 2026-05-29
updated: 2026-05-29
phan: 03
---

# Cross-vault query

## Trước đó

[04-vault-marketing](04-vault-marketing.md) — bạn có 3-4 vault sibling.

---

## Vấn đề

Bạn có 4 vault: Brain, Life, 4DX, Marketing. Hỏi 1 câu, câu trả lời nằm xuyên 2-3 vault. Vd:

- *"Sale page khoá Marketing Online Q2 thu được bao nhiêu, dùng concept gì từ khoá đó, ROI so với mục tiêu mục tiêu tối quan trọng 2026?"*

Câu này cần:
- Marketing/wiki/reports/2026-Q2-khoa-marketing-funnel.md (số doanh thu)
- Brain/wiki/courses/Khoá Marketing Online.md (concept)
- 4DX/wig/2026-mục tiêu tối quan trọng-4-revenue.md (mục tiêu)

Claude phải đọc 3 vault đồng thời, tổng hợp.

---

## Setup cross-vault — 2 cách

### Cách 1 — Mở Claude ở vault parent

```bash
cd "/Users/$USER/Library/Mobile Documents/iCloud~md~obsidian/Documents"
claude
```

Claude scope ở folder Documents/ → đọc được mọi vault sibling.

CLAUDE.md vault này (nếu có) sẽ là parent — không có cũng được, Claude vẫn đọc cả 4 vault.

**Khuyên**: tạo `Documents/CLAUDE.md` đơn giản:

```
# CLAUDE.md — Parent of all sibling vaults

Vault list:
- [[My Brain/]] — knowledge
- [[My Life/]] — lifestyle
- [[My 4DX/]] — execution
- [[My Marketing/]] — production

Mỗi vault có CLAUDE.md riêng. Đọc theo schema vault tương ứng khi work.

Cross-vault wikilink: `[[<vault>/<path>/<page>]]`.
```

### Cách 2 — Mở Claude ở vault cụ thể, dùng absolute path

```bash
cd "/Users/$USER/Library/Mobile Documents/iCloud~md~obsidian/Documents/My Brain"
claude
```

Claude scope ở Brain. Khi cần đọc vault khác:

```
> Đọc file ../My Marketing/wiki/assets/sale-pages/sp-khoa-marketing-2026.md
```

Cumbersome hơn, nhưng vẫn work.

---

## Cross-vault wikilink (liên kết nội bộ xuyên vault)

### Trong file của vault A, link tới vault B

```
Concept này dùng trong [[../My Marketing/wiki/assets/sale-pages/sp-khoa-marketing-2026]]
```

### Quy tắc absolute path

- Path bắt đầu từ folder cha 2 vault (`Documents/`)
- Format `../<Vault Name>/<path>/<file>`
- Obsidian render link OK nếu mở vault parent
- Obsidian KHÔNG render link nếu mở vault con (chỉ thấy plain text)

### Workaround: frontmatter `brain_ref`

Thay vì wikilink absolute (dễ vỡ khi rename vault), dùng frontmatter reference:

```
---
brain_ref:
  program_code: khoa-marketing-online
  course_page: "[[Khoá Marketing Online]]"
  vault: "My Brain"
---
```

Claude đọc frontmatter biết:
- Vault: `My Brain`
- File: `wiki/courses/Khoá Marketing Online.md`

Khi rename vault → chỉ sửa frontmatter `vault:`, không phải rewrite mọi wikilink.

---

## Pattern query phổ biến

### Query 1 — Cross 2 vault (Brain + Marketing)

```
> Sale page nào cho khoá Marketing Online đang chạy? Concept nào khoá dạy chưa được apply vào sale page?
```

Claude:
1. Đọc `Marketing/wiki/assets/sale-pages/` filter brain_ref khoa-marketing-online
2. Đọc `Brain/wiki/courses/Khoá Marketing Online.md` lấy danh sách concept
3. Cross-ref: concept nào có wikilink trong sale page, concept nào không
4. Trả lời + đề xuất

### Query 2 — Cross 3 vault (Brain + Marketing + 4DX)

```
> Doanh thu Q2 từ khoá Marketing Online, so với mục tiêu tối quan trọng 4 target, dùng concept gì, sale page nào?
```

Claude:
1. 4DX/wig/2026-mục tiêu tối quan trọng-4-revenue.md → target Q2
2. Marketing/wiki/reports/2026-Q2-revenue.md → actual
3. Marketing/wiki/assets/sale-pages/ → sale page khoá Marketing Online
4. Brain/wiki/courses/Khoá Marketing Online... → concept dạy
5. Tổng hợp

### Query 3 — Brain + Life

```
> Concept "Atomic Habits" từ Brain có ứng dụng nào vào lịch tập Ironman trong Life chưa?
```

Claude:
1. Brain/wiki/concepts/Atomic Habits.md → đọc rule chính
2. Life/wiki/domains/the-thao-triathlon.md → đọc lịch tập
3. So sánh: rule nào đã apply, rule nào chưa
4. Suggest action

### Query 4 — Life + 4DX

```
> Tuần W22 hit bao nhiêu giờ training, có đủ target mục tiêu tối quan trọng 2 không?
```

Claude:
1. Life/4dx/actions/2026-W22-actions.md → count training_hours
2. 4DX/wig/2026-mục tiêu tối quan trọng-2-ironman.md → target
3. Trả lời + traffic light

---

## Setup ranh giới rõ — quan trọng

Mỗi vault có CLAUDE.md mô tả **vault này** + **mối quan hệ với vault khác**. Vd:

### Brain CLAUDE.md có section

```
## Vault song song

- `../Life/` — vault anh em chứa lifestyle. Brain = kiến thức work; Life = personal hobby.
- `../Marketing/` — vault anh em đọc kiến thức Brain để sản xuất. Marketing chỉ đọc Brain, không ghi ngược.
- `../4DX/` — vault execution. 4DX chỉ đọc Brain + Life + Marketing actions.
```

### Marketing CLAUDE.md có section

```
## Cross-vault Brain

- `../My Brain/` — đọc kiến thức course / concept
- Marketing chỉ đọc Brain, không ghi ngược
- Reference: frontmatter `brain_ref` hoặc wikilink absolute `[[../My Brain/...]]`
- Phát hiện concept mới chưa có Brain → log, để user xử lý bên Brain
```

→ Mỗi vault có rule "ai đọc ai", "ai ghi ai".

---

## Anti-pattern cross-vault

### Sai 1 — Ghi 2 chiều

Marketing chỉ đọc Brain. KHÔNG ghi ngược. Nếu Marketing tự sửa concept page bên Brain → conflict ownership, dễ vỡ.

→ Marketing phát hiện concept mới chưa có → log lại trong `Marketing/log.md`. User vào Brain xử lý.

### Sai 2 — Wikilink absolute lan tràn

Mỗi page Marketing wikilink absolute tới Brain. Sau khi rename Brain → vỡ hết.

→ Dùng frontmatter `brain_ref` (1 chỗ) thay 50 wikilink absolute.

### Sai 3 — Schema duplicate

Concept "Hệ thống bán hàng 8+2" có page ở Brain VÀ Marketing → duplicate.

→ Page ở Brain duy nhất. Marketing chỉ link.

### Sai 4 — Query không clarify vault

```
> Lead page nào CVR cao nhất?
```

(Không nói vault nào)

→ Claude phải hỏi: "Bạn hỏi lead page trong Marketing vault, đúng không?"

Sửa:

```
> Trong Marketing vault, lead page nào CVR cao nhất Q2?
```

---

## bản đồ nội dung cross-vault

Tạo bản đồ nội dung ở Brain `wiki/Hệ sinh thái 4 vault.md`:

```
---
type: meta-moc
tags: [meta, cross-vault]
---

# Hệ sinh thái 4 vault

## Brain (vault hiện tại)

Knowledge concept-first.

## Life

Lifestyle cá nhân. Photo + entity + event.

- Cross-ref: concept "Atomic Habits" từ Brain → apply lịch tập trong Life

## 4DX

Meta execution. Tác vụ lệnh tự động theo lịch đêm CN.

- Pull Life actions → traffic light mục tiêu tối quan trọng 2 (Ironman)
- Pull Marketing actions → traffic light mục tiêu tối quan trọng 4 (revenue)

## Marketing

Production + measurement.

- Reference Brain concept → sale page
- Output asset metric → 4DX lệnh tự động theo lịch pick up
```

---

## Workflow query xuyên vault

```
1. Bạn ask câu hỏi vắt N vault
   ↓
2. Claude đọc CLAUDE.md các vault liên quan
   ↓
3. Claude identify file cần đọc mỗi vault
   ↓
4. Read các file → tổng hợp
   ↓
5. Cite source theo vault: "Theo Brain: ... Theo Marketing: ... Theo 4DX: ..."
   ↓
6. Đề xuất action cross-vault
   ↓
7. Lưu analysis vào vault phù hợp
```

---

## Verify Phần 03 xong

Sau Phần 03:
- [x] Hiểu khi nào tách vault
- [x] Có Life vault (nếu cần)
- [x] Có 4DX vault (nếu cần)
- [x] Có Marketing vault (nếu cần)
- [x] Query xuyên vault OK

→ Sang Phần 04 agents + skills + memory.

---

## 📖 Chú thích

- **vault** = kho ghi chú — một folder thông thường trên máy tính được Obsidian nhận diện và quản lý đặc biệt (tạo liên kết giữa file, tìm kiếm toàn văn, hiển thị sơ đồ mạng lưới).
- **memory** = file lưu thông tin AI cần nhớ qua các phiên làm việc khác nhau (ai là bạn, quy tắc nào phải theo, dự án nào đang chạy). Không có memory → mỗi lần mở mới AI quên hết.
- **wikilink** = cách tạo liên kết nội bộ trong Obsidian bằng cú pháp `[[Tên trang]]`. Click vào liên kết → mở trang đó ngay. AI tự tạo các wikilink này khi viết wiki.
- **frontmatter** = phần thông tin khai báo ở đầu mỗi file, nằm giữa hai dòng `---`. Ví dụ: loại trang (type), từ khoá (tags), ngày tạo. AI dùng phần này để phân loại và tìm kiếm trang.
- **schema** = cấu trúc và quy tắc tổ chức kho: mỗi loại trang có những phần nào, thông tin nào bắt buộc, đặt tên file theo kiểu gì. Schema được mô tả trong CLAUDE.md.

## Tiếp theo

Đọc tiếp: [01-agent-la-gi](../04-agents-skills-memory/01-agent-la-gi.md) — Khái niệm agent.
