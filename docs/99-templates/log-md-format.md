---
title: log.md format
type: template
created: 2026-05-29
updated: 2026-05-29
phan: 99
---

# log.md format (copy-paste)

Template + quy ước cho `log.md` ở root vault. File append-only chronological.

---

## Format chuẩn

```
# Log — <Vault Name>

Nhật ký append-only. Mới nhất ở dưới.

## [YYYY-MM-DD] <action> | <subject>

- <Detail 1>
- <Detail 2>
- Notes: <ghi chú>
```

Mỗi entry mở đầu bằng `## [YYYY-MM-DD] <action> | <subject>` để dễ tìm kiếm bằng lệnh grep.

---

## 5 action chính

| Action | Khi nào |
|---|---|
| `ingest` | Ingest source mới vào vault |
| `query` | User hỏi câu phức tạp, lưu lại |
| `rà soát` | Rà soát pass định kỳ |
| `setup` | Setup vault, plugin, agent, skill |
| `refactor` | Đổi schema, rename, migrate |
| `manual` | User tự sửa, không qua AI |

---

## Ví dụ thực tế

```
# Log — My Brain

Nhật ký append-only.

## [2026-04-26] setup | Tạo vault
- Created: CLAUDE.md, index.md, log.md, README.md
- Created: folder raw/ + wiki/{sources,concepts,entities,courses}/

## [2026-04-27] ingest | Paul Graham — Product Market Fit (2024)
- Created: Paul Graham — Product Market Fit (2024)
- Created: Product Market Fit (concept mới)
- Created: Paul Graham, Y Combinator (entity mới)
- Updated: [index](../muc-luc.md)
- Notes: PMF khái niệm mới, chưa có concept page → tạo mới. Concept "Founder Mode" nhắc cuối bài → chưa tạo, đợi 2 source nữa.

## [2026-04-28] ingest | Sam Altman — Startup Playbook
- Created: Sam Altman — Startup Playbook
- Updated: Product Market Fit (append insight retention curve)
- Created: Sam Altman (entity mới)
- Notes: Sam khác Paul Graham về PMF — Sam nhấn retention curve flatten. Ghi vào section "Mâu thuẫn" của Product Market Fit.

## [2026-04-29] query | "PMF cho B2B SaaS 10 customer nên làm gì?"
- Read: Product Market Fit, Sam Altman — Startup Playbook, Paul Graham — Product Market Fit (2024)
- Output: 5 action recommend, save thành Validate-PMF-cho-B2B-SaaS

## [2026-05-01] rà soát | weekly
- Issues: 3 broken wikilink, 2 page thiếu frontmatter
- Fixed: 3 broken wikilink (rename target)
- Deferred: 2 page frontmatter (đợi user duyệt)

## [2026-05-03] refactor | Tách wiki/courses/ subfolder
- Old: wiki/courses/<file>.md
- New: wiki/courses/<format>/<file>.md (format: offline-camp / online-self-study / coaching-weekly)
- Affected: 15 course page move
- Updated: CLAUDE.md schema, 23 wikilink
- Backup: Git commit "Before courses subfolder refactor"
```

---

## Quy tắc viết log

### Rule 1 — Mới nhất ở dưới

Append vào cuối file, không insert đầu.

### Rule 2 — Format date ISO

`2026-04-26` (YYYY-MM-DD). Không `26/4/2026` hay `Apr 26, 2026`.

→ Sort theo date tự nhiên + greppable.

### Rule 3 — Action lowercase

`ingest`, không `INGEST` hoặc `Ingest`.

### Rule 4 — Subject ngắn

≤ 60 chars. Long → cắt + chi tiết ở bullet.

### Rule 5 — Cite wikilink (liên kết nội bộ)

Mọi page touch → wikilink. Vd:

```
- Created: Page A
- Updated: Page B
```

→ Graph view track inbound link từ log → page.

### Rule 6 — Notes có "Why"

Quan trọng nhất. Notes không phải "what" (wikilink đã cover) mà là "why" + insight:

```
- Notes: Sam khác Paul Graham về PMF — Sam nhấn retention curve flatten. Ghi vào section "Mâu thuẫn".
```

→ 6 tháng sau đọc log biết why quyết định.

---

## Greppable patterns

### Tìm ingest tuần này

```bash
grep "^## \[2026-04-2.\] ingest" log.md
```

### Tìm 10 entry gần nhất

```bash
grep "^## \[" log.md | tail -10
```

### Tìm refactor lịch sử

```bash
grep "^## \[.*\] refactor" log.md
```

### Tìm mọi entry liên quan PMF

```bash
grep -B0 -A5 "PMF" log.md
```

---

## Đếm số entry mỗi action

```bash
awk -F'|' '/^## \[/{print $1}' log.md | grep -oE 'ingest|query|rà soát|refactor|setup|manual' | sort | uniq -c
```

Ví dụ output:

```
  47 ingest
  12 rà soát
   5 query
   3 refactor
   1 setup
```

→ Track tỷ lệ ingest vs query — ingest nhiều mà query ít → đang accumulate without using (tích lũy mà không dùng).

---

## Khi log quá dài

Sau 1-2 năm, log.md có thể > 10000 dòng → load chậm.

### Option A — Archive theo năm

```bash
# Cuối năm
mv log.md log-2025.md
echo "# Log — 2026" > log.md
```

Index trong `index.md`:

```
## Logs

- log — 2026 (current)
- log-2025
- log-2024
```

### Option B — Archive theo quý

Cho vault rất active.

### Option C — Không archive, dùng tail

`log.md` giữ nguyên, dùng tail/grep để check recent. Obsidian search vẫn fast nếu file < 50000 dòng.

→ Khuyên Option A. Archive cuối năm. Đủ đơn giản.

---

## Log entry cho 4 workflow chính

### Ingest

```
## [YYYY-MM-DD] ingest | <Source Title>
- Created: Source, Concept mới (nếu mới)
- Updated: Concept cũ (nếu append)
- Notes: <insight đáng nhớ>
```

### Query

```
## [YYYY-MM-DD] query | "<câu hỏi>"
- Read: Page 1, Page 2, Page 3
- Output: <format>, save thành <file> (nếu lưu)
```

### Rà soát

```
## [YYYY-MM-DD] rà soát | <mode>
- Issues: <số issue>
- Fixed: <số fix>
- Deferred: <số deferred>
- Report: <file>
```

### Refactor

```
## [YYYY-MM-DD] refactor | <subject>
- Old: <state cũ>
- New: <state mới>
- Affected: <số file>
- Updated: <thứ gì update>
- Backup: <commit hash>
```

---

## Log format cho agent

Agent (vd `article-ingest`) tự động append log khi run. Format:

```
## [YYYY-MM-DD] ingest | <Title> [agent: article-ingest]
- Created: ...
- Updated: ...
- Notes: ...
```

Suffix `[agent: <name>]` để track entry nào AI làm, entry nào user làm thủ công.

---

## Khi log entry không cần

KHÔNG log:

- Edit nhỏ (typo fix) — trivial, không cần track
- Action repeat (vd: mỗi 5 phút run `rà soát quick` → đừng log mỗi lần, gộp daily)
- Action không thay đổi vault (vd: query không lưu output)

Log entry là quyền lợi, không phải obligation. Quá nhiều log → noise.

---

## 📖 Chú thích

- **vault** = kho ghi chú — một folder thông thường trên máy tính được Obsidian nhận diện và quản lý đặc biệt (tạo liên kết giữa file, tìm kiếm toàn văn, hiển thị sơ đồ mạng lưới).
- **ingest** = đưa tài liệu thô vào kho để AI đọc và xử lý thành trang wiki — gồm: đọc nội dung, rút ý chính, tạo trang tóm tắt và cập nhật trang khái niệm liên quan.
- **wikilink** = cách tạo liên kết nội bộ trong Obsidian bằng cú pháp `Tên trang`. Click vào liên kết → mở trang đó ngay. AI tự tạo các wikilink này khi viết wiki.
- **frontmatter** = phần thông tin khai báo ở đầu mỗi file, nằm giữa hai dòng `---`. Ví dụ: loại trang (type), từ khoá (tags), ngày tạo. AI dùng phần này để phân loại và tìm kiếm trang.
- **schema** = cấu trúc và quy tắc tổ chức kho: mỗi loại trang có những phần nào, thông tin nào bắt buộc, đặt tên file theo kiểu gì. Schema được mô tả trong CLAUDE.md.
- **commit** (Git) = hành động lưu lại một điểm phiên bản — như "chụp ảnh" trạng thái toàn bộ kho tại một thời điểm. Có thể khôi phục kho về bất kỳ commit nào trước đó.
- **Graph view** = chế độ hiển thị của Obsidian dạng mạng lưới, cho thấy tất cả trang và liên kết giữa chúng. Dùng để phát hiện trang mồ côi (không ai liên kết tới) hoặc cluster kiến thức.

## Tiếp theo

[index-md-format](index-md-format.md) — index.md format.
