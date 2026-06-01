---
title: Ingest source đầu tiên
type: huong-dan
created: 2026-05-29
updated: 2026-05-29
phan: 02
---

# Ingest source đầu tiên

## Trước đó

[06-course-moc-template](06-course-moc-template.md) — bạn đã có 3 template (concept, source, course).

---

## Mục tiêu

Trong file này bạn sẽ:
1. Chọn 1 source thật để test
2. Thả vào `raw/`
3. Cùng Claude ingest theo workflow
4. Có source page + concept page + entity page đầu tiên
5. Update index.md + log.md

---

## Bước 1 — Chọn source thử nghiệm

Chọn source ngắn dễ ingest. Đề xuất:

- **Article web ngắn** (~2000 chữ) — vd: bài Paul Graham, Naval Ravikant
- **YouTube video ngắn** (~10-15 phút) — lấy transcript qua skill
- **PDF tóm tắt sách 1 chương**
- **Meeting note tự viết**

KHÔNG chọn:
- Sách 500 trang (overwhelm cho lần đầu)
- Transcript 8h khoá học (cần chia chunk trước)
- Source nhiều ngôn ngữ mix

→ Khuyên: dùng 1 article web ngắn.

---

## Bước 2 — Thả source vào raw/

### Cách A — Obsidian Web Clipper (article web)

1. Mở article trên Chrome (vd: https://paulgraham.com/pmf.html)
2. Click icon Web Clipper trên toolbar
3. Settings (lần đầu):
   - Vault: `My Brain`
   - Folder: `raw/articles/`
4. Click **Clip**

Sau vài giây, file `.md` xuất hiện trong `raw/articles/`:

```
raw/articles/2026-05-29-pmf-paul-graham.md
```

### Cách B — Copy paste thủ công

1. Mở terminal, vào folder vault
2. Tạo file:

```bash
cd "/Users/$USER/Library/Mobile Documents/iCloud~md~obsidian/Documents/My Brain/raw/articles"
touch "2026-05-29-my-first-source.md"
```

3. Mở file trong Obsidian, paste nội dung article + thêm metadata cơ bản ở đầu:

```
---
url: https://example.com/article
author: Author Name
date: 2024-10
language: en
---

# Title

Content here...
```

### Cách C — PDF tải về

1. Tải PDF vào `raw/assets/`:

```bash
cp ~/Downloads/article.pdf "raw/assets/2026-05-29-article.pdf"
```

2. PDF binary OK — Claude đọc trực tiếp.

---

## Bước 3 — Mở Claude Code

```bash
cd "/Users/$USER/Library/Mobile Documents/iCloud~md~obsidian/Documents/My Brain"
claude
```

Claude tự đọc CLAUDE.md đầu session.

---

## Bước 4 — Nói Claude ingest

Trong prompt:

```
> Ingest file raw/articles/2026-05-29-pmf-paul-graham.md
```

Claude sẽ:

### 4a — Đọc source

Claude dùng tool `Read` đọc file raw. Nếu PDF — dùng skill `pdf`.

### 4b — Hỏi clarify (key takeaway)

Claude phản hồi:

```
Source này về "Product Market Fit" của Paul Graham. 5 ý chính:
1. PMF không phải state, là process
2. ...

Anh muốn em nhấn cái gì trước khi viết? Hay viết hết?
```

Bạn trả lời. Vd:
```
> Viết hết. Tập trung phần PMF không phải state.
```

### 4c — Viết source page

Claude tạo file:

```
wiki/sources/Paul Graham — Product Market Fit (2024).md
```

Nội dung theo template ở [05-source-page-template](05-source-page-template.md):
- Frontmatter đầy đủ
- TL;DR 5 bullet
- Nội dung chính 3-5 đoạn
- Concept đã touch (link wikilink)
- Entity nhắc đến
- Quote signature
- Câu chốt rút ra

### 4d — Tạo concept page

Concept mới phát sinh: `Product Market Fit`.

Claude tạo:

```
wiki/concepts/Product Market Fit.md
```

Theo template ở [04-concept-page-template](04-concept-page-template.md). Stub những phần chưa có data.

Concept khác nhắc trong source nhưng chưa đủ data → Claude **không tạo page**, chỉ note trong source page câu hỏi mở.

### 4e — Tạo entity page

Entity mới: `Paul Graham`, `Y Combinator`.

Claude tạo:
```
wiki/entities/Paul Graham.md
wiki/entities/Y Combinator.md
```

Section: background, vai trò trong vault, quote signature, source nhắc.

### 4f — Update `index.md`

Claude append vào `index.md`:

```
## Sources
- [[Paul Graham — Product Market Fit (2024)]] — bài về PMF process

## Concepts
- [[Product Market Fit]] — PMF không phải state

## Entities
- [[Paul Graham]] — founder Y Combinator, viết essay
- [[Y Combinator]] — accelerator
```

### 4g — Append `log.md`

```
## [2026-05-29] ingest | Paul Graham — Product Market Fit
- Created: [[Paul Graham — Product Market Fit (2024)]], [[Product Market Fit]], [[Paul Graham]], [[Y Combinator]]
- Notes: PMF khái niệm mới chưa có concept page → tạo mới
```

### 4h — Báo cáo bạn

Claude tổng kết:

```
Ingest xong [[Paul Graham — Product Market Fit (2024)]]
- 1 source page mới
- 1 concept page mới: [[Product Market Fit]]
- 2 entity page mới: [[Paul Graham]], [[Y Combinator]]
- Index + log updated

3 quan sát đáng chú ý:
1. PMF là process — gợi mở concept "build-measure-learn" (Lean Startup chưa ingest)
2. Paul Graham nhắc "founder mode" cuối bài — cần ingest source riêng
3. Concept "Y Combinator playbook" có thể tách thành topic page riêng nếu thêm 2-3 source nữa

Có muốn ingest tiếp gì không?
```

---

## Bước 5 — Duyệt output

Mở Obsidian → mở 4 file Claude vừa tạo:

### Source page

- [ ] Frontmatter đầy đủ (`type`, `tags`, `created`, `raw_path`, `author`, `url`)
- [ ] TL;DR rõ
- [ ] Wikilink concept đúng
- [ ] Quote nguyên văn (check vs raw)

### Concept page

- [ ] Định nghĩa rõ
- [ ] Cấu trúc lõi
- [ ] Khoá học sử dụng (stub nếu chưa có khoá)
- [ ] Khái niệm liên quan có nhãn

### Entity page

- [ ] Background đầy đủ
- [ ] Vai trò trong vault

### Index + log

- [ ] Index có entry mới
- [ ] Log có timestamp + action

---

## Bước 6 — Nếu sai → chỉ chỗ

Vd Claude viết sai:

```
> Concept page "Product Market Fit" thiếu section "Ẩn dụ dễ nhớ". 
> Thêm vào, kèm metaphor "PMF như đập nước vỡ — khi nó vỡ, không gì ngăn được" (Paul Graham dùng trong bài này).
```

Claude edit file → check lại.

Sai nhiều lần cùng pattern → update CLAUDE.md để rule mới apply:

```
> Update CLAUDE.md: mọi concept page bắt buộc có section "Ẩn dụ dễ nhớ" — không stub mà phải tìm metaphor trong source nếu có.
```

---

## Bước 7 — Ingest thêm 2-3 source nữa

Để vault có data ban đầu, ingest thêm 2-3 source về cùng chủ đề:

```
> Ingest tiếp raw/articles/<source2>.md
> Ingest tiếp raw/articles/<source3>.md
```

Claude sẽ:
- Tạo source page mới
- **Update** concept page cũ (vd: PMF) nếu source mới mở rộng định nghĩa
- Tạo concept page mới nếu phát sinh
- Update index + log

---

## Bước 8 — Verify với Graph view

Mở Obsidian → Cmd+G mở Graph view.

Bạn sẽ thấy:
- 1 source page (giữa)
- Liên kết tới 1 concept page + 2 entity page
- Sau khi ingest 3 source → 3 source page, vài concept page tụm xung quanh

Nếu graph thưa thớt → wiki còn nhỏ. OK.

Nếu graph có node mồ côi (không link) → đó là vấn đề. Run lần rà soát.

---

## Bước 9 — Khi nào không ingest

Đừng ingest:

- **Source bạn không định dùng** (clipped vì hứng chí — sẽ thành rác wiki)
- **Source trùng nội dung source đã ingest** (vd: 2 article cùng tóm tắt 1 sách)
- **Source low quality** (clickbait, blog spam)

Quy tắc: ingest có chọn lọc. **5 source quality > 50 source rác.**

---

## Bước 10 — Verify Phần 02

Sau khi xong file này, vault Brain có:

- [x] CLAUDE.md ở root
- [x] README, index, log
- [x] Folder raw/articles/ với 3-4 source
- [x] Folder wiki/sources/ với 3-4 source page
- [x] Folder wiki/concepts/ với 2-3 concept page
- [x] Folder wiki/entities/ với 3-5 entity page

→ Vault Brain chạy được. Sang file cuối Phần 02.

---

## 📖 Chú thích

- **vault** = kho ghi chú — một folder thông thường trên máy tính được Obsidian nhận diện và quản lý đặc biệt (tạo liên kết giữa file, tìm kiếm toàn văn, hiển thị sơ đồ mạng lưới).
- **ingest** = đưa tài liệu thô vào kho để AI đọc và xử lý thành trang wiki — gồm: đọc nội dung, rút ý chính, tạo trang tóm tắt và cập nhật trang khái niệm liên quan.
- **wikilink** = cách tạo liên kết nội bộ trong Obsidian bằng cú pháp `[[Tên trang]]`. Click vào liên kết → mở trang đó ngay. AI tự tạo các wikilink này khi viết wiki.
- **frontmatter** = phần thông tin khai báo ở đầu mỗi file, nằm giữa hai dòng `---`. Ví dụ: loại trang (type), từ khoá (tags), ngày tạo. AI dùng phần này để phân loại và tìm kiếm trang.
- **Graph view** = chế độ hiển thị của Obsidian dạng mạng lưới, cho thấy tất cả trang và liên kết giữa chúng. Dùng để phát hiện trang mồ côi (không ai liên kết tới) hoặc cluster kiến thức.
- **terminal** (còn gọi là cửa sổ dòng lệnh) = nơi bạn gõ lệnh văn bản thay vì click chuột. Trên Mac: tìm "Terminal" trong Spotlight. Trên Windows: tìm "PowerShell" hoặc "Command Prompt".

## Tiếp theo

Đọc tiếp: [08-query-wiki-dau-tien](08-query-wiki-dau-tien.md) — Query wiki đầu tiên.
