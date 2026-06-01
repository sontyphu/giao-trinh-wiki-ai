---
title: Skill là gì
type: huong-dan
created: 2026-05-29
updated: 2026-05-29
phan: 04
---

# Skill là gì

## Trước đó

[02-tao-agent-dau-tien](02-tao-agent-dau-tien.md) — bạn đã build agent đầu tiên.

---

## Skill vs Agent

| Skill | Agent |
|---|---|
| Workflow markdown user-defined | Sub-Claude system prompt riêng |
| Gọi qua `/skill-name` | Gọi qua Agent tool |
| Context chung main loop | Context isolation (cô lập ngữ cảnh) |
| Lightweight (file < 200 dòng) | Heavyweight (system prompt 500+ dòng) |
| Best cho workflow đơn giản, đặc thù | Best cho domain expertise sâu |

→ Đơn giản nhất: **skill** cho thao tác nhanh, **agent** cho job phức tạp.

---

## Skill là gì cụ thể

Skill = file markdown ở `.claude/skills/<skill-name>/SKILL.md` (hoặc `~/.claude/skills/`) định nghĩa:

1. **Trigger keyword** — khi user nói "X" thì invoke skill
2. **Workflow** — step-by-step làm gì
3. **Output format** — kết quả trả về thế nào

Khi bạn type `/skill-name` (hoặc keyword khớp), Claude:
1. Đọc SKILL.md
2. Follow workflow
3. Return output

---

## Ví dụ skill phổ biến cho vault AI

Các chuyên gia thường build skill như:

| Skill | Use case |
|---|---|
| `text-cat-chunk` | Cắt file dài thành chunk + metadata |
| `srt-cat-chunk` | Cắt SRT (transcript subtitle) thành chunk |
| `blog-nau-an` | Viết blog nấu ăn SEO |
| `ho-so-khach-hang` | Build customer profile |
| `giao-an-module` | Viết module giáo án |
| `tu-van-phuong-phap` | Tư vấn theo phương pháp đặc thù |
| `csv-to-md` | Convert CSV sang markdown table |
| `heic-to-jpg` | Convert ảnh HEIC sang JPG |

Built-in Anthropic skills:
- `pdf` — work với PDF
- `xlsx` — work với spreadsheet
- `docx` — work với Word doc
- `pptx` — work với PowerPoint
- `find-skills` — tìm skill có sẵn

---

## Khi nào tạo skill mới

Skill phù hợp cho:

### A. Workflow simple lặp lại

Vd: convert HEIC ảnh sang JPG → tạo skill `heic-to-jpg`.

```
---
description: Convert HEIC images to JPG using sips
---

Khi user nói "convert HEIC tới JPG":
1. Đọc folder path từ user
2. Chạy: sips -s format jpeg <path>/*.HEIC --out <path>/jpg/
3. Báo done
```

### B. Style guide writing

Vd: viết blog theo style cụ thể → skill `blog-tone-style`.

### C. Data transformation đơn giản

Vd: parse CSV → markdown table → skill `csv-to-md`.

### D. Domain prompt expertise (chuyên môn domain)

Vd: tư vấn theo phương pháp Y → skill `tu-van-phuong-phap-Y` (chứa rule guideline).

---

## Khi nào tạo agent thay vì skill

- Workflow phức tạp > 200 dòng → agent
- Cần tool subset isolation → agent
- Cần context window riêng → agent
- Cần memory persist → agent

---

## Skill file structure

```
.claude/skills/<skill-name>/
├── SKILL.md          # luật chơi
├── examples/         # tuỳ chọn — example output
├── templates/        # tuỳ chọn — template input
└── scripts/          # tuỳ chọn — script Python/Bash
```

Hoặc gọn hơn: chỉ file `.claude/skills/<skill-name>.md` (không folder).

---

## SKILL.md format

```
---
name: skill-name
description: "When user says X, invoke this skill. Use this skill BẤT CỨ KHI NÀO ..."
trigger_keywords: [keyword1, keyword2, ...]
---

# Skill Name

## Mục tiêu

[1-2 đoạn — skill này làm gì]

## Trigger

User nói:
- "Phrase 1"
- "Phrase 2"
- "Câu trigger khác"

→ Invoke skill.

## Workflow

### Bước 1 — ...

[Mô tả step 1]

### Bước 2 — ...

### Bước 3 — ...

## Output format

[Format kết quả]

## Constraint

[Rule cứng skill phải tuân]

## Edge case

[Tình huống đặc biệt]
```

---

## Bước 1 — Tạo skill mẫu

Vd: skill `summarize-source-vault-style` — tóm tắt source theo style vault Brain.

```bash
mkdir -p .claude/skills/summarize-source-vault-style
```

`.claude/skills/summarize-source-vault-style/SKILL.md`:

```
---
name: summarize-source-vault-style
description: "Tóm tắt source raw theo style vault Brain. Use BẤT CỨ KHI NÀO user nói 'tóm tắt source X', 'summarize raw/X', 'làm TL;DR cho file Y'."
---

# Summarize Source — Vault Style

## Mục tiêu

Tóm tắt 1 source raw thành format wiki-ready cho vault Brain.

## Trigger

User nói:
- "Tóm tắt raw/articles/X.md"
- "Summarize file Y"
- "TL;DR cho article Z"

## Workflow

### 1. Đọc source

Đọc full file user chỉ. Nếu PDF — dùng skill pdf.

### 2. Identify

- Author
- Date
- URL (nếu có)
- Language
- Domain (business / tech / lifestyle...)

### 3. Tóm tắt

Format output:

**Title**: <Title source>

**TL;DR** (3-5 bullet):
- Ý chính 1
- ...

**Nội dung chính** (3 đoạn):

[Đoạn 1]

[Đoạn 2]

[Đoạn 3]

**Concept đã touch**:
- Concept A

**Entity nhắc đến**:
- Entity X

**Quote signature**:

> "Quote nguyên văn"
> — Author, line/page

**Câu chốt rút ra**:

[1-2 takeaway]

**Câu hỏi mở**:

- ?

### 4. Đề xuất

Hỏi user:
- Có muốn save thành source page chính thức vào `wiki/sources/`?
- Có concept page nào nên tạo?

## Constraint

- KHÔNG bịa quote (phải nguyên văn từ source)
- KHÔNG cite concept page chưa tồn tại
- Output format đúng template

## Edge case

- Source quá dài (>10k dòng) → tóm tắt theo chunk, output split file
- Source không có author → ghi "Author: unknown"
- Source nhiều ngôn ngữ → tóm tắt theo ngôn ngữ chính
```

---

## Bước 2 — Test skill

Trong Claude Code:

```
> /summarize-source-vault-style raw/articles/2026-05-29-pmf.md
```

Hoặc keyword match:

```
> Tóm tắt source raw/articles/2026-05-29-pmf.md
```

Claude:
- Match keyword "Tóm tắt source" với skill description
- Invoke skill
- Follow workflow
- Return output theo format

---

## Bước 3 — Skill với script

Skill có thể chạy script Python/Bash:

```
.claude/skills/heic-to-jpg/
├── SKILL.md
└── scripts/
    └── convert.sh
```

`scripts/convert.sh`:

```bash
#!/bin/bash
INPUT_DIR="$1"
OUTPUT_DIR="$INPUT_DIR/jpg"
mkdir -p "$OUTPUT_DIR"
sips -s format jpeg "$INPUT_DIR"/*.HEIC --out "$OUTPUT_DIR"
```

`SKILL.md`:

```
---
name: heic-to-jpg
description: Convert HEIC images to JPG
---

# Convert HEIC → JPG

Khi user nói "convert HEIC <folder>":

1. Get folder path từ user
2. Run script:

bash .claude/skills/heic-to-jpg/scripts/convert.sh "<folder>"

3. Báo: "Converted N HEIC → JPG, output: <folder>/jpg/"
```

---

## Bước 4 — Skill đặc thù domain

Skill cũng có thể đóng gói **phương pháp coaching / tư vấn signature** của bạn — biến quy trình 5-7 bước thường dùng thành 1 slash command.

Pattern chung:

```
---
name: <ten-phuong-phap>
description: "Dẫn dắt user qua quy trình <X> N bước. Use khi user nói '<trigger 1>', '<trigger 2>'..."
---

# <Tên phương pháp>

## Bước 1 — <Mục đích bước 1>

[Hỏi gì / làm gì]

## Bước 2 — <Mục đích bước 2>

## Bước 3-N — ...
```

User chỉ cần `/<ten-phuong-phap>` → AI dẫn dắt N bước tự động theo đúng pipeline bạn đã chuẩn hoá.

**Khi nào skill domain hữu ích**:
- Bạn là coach / trainer / tư vấn viên có phương pháp riêng
- Quy trình tư vấn lặp đi lặp lại với mỗi khách
- Muốn AI dùng được đúng phương pháp của bạn, không generic

**Lưu ý privacy**: nếu skill chứa **IP/signature method** của bạn → để ở `.claude/skills/` local hoặc agent-memory private, KHÔNG commit vào repo public.

---

## Bước 5 — Skill chain

Skill có thể gọi skill khác. Vd skill `ingest-flow-full`:

```
1. /text-cat-chunk → chia source dài
2. /summarize-source-vault-style → tóm tắt mỗi chunk
3. Tạo source page tổng
4. /update-index → update index.md
```

---

## Bước 6 — Skill user-level vs vault-level

| Path | Scope |
|---|---|
| `.claude/skills/<name>/` | Chỉ vault hiện tại |
| `~/.claude/skills/<name>/` | Mọi vault user |

Skill generic (vd `heic-to-jpg`) → global.
Skill đặc thù vault (vd `summarize-source-vault-style`) → vault-level.

---

## Bước 7 — List skill available

Trong Claude Code:

```
/skills
```

Hoặc xem file:

```bash
ls .claude/skills/
ls ~/.claude/skills/
```

---

## Quy ước đặt tên skill

- kebab-case
- Verb-first nếu skill thực hiện hành động (`convert-X`, `summarize-Y`)
- Noun-first nếu skill là domain (`blog-nau-an`, `tu-van-ban-hang`)
- Không quá dài (≤ 30 char)

---

## Anti-pattern khi tạo skill

### Sai 1 — Skill quá generic

```
name: do-everything
description: Làm mọi thứ user yêu cầu
```

→ Vô dụng. Skill phải single-purpose.

### Sai 2 — Description mơ hồ

```
description: Tool useful
```

→ Claude không biết khi nào invoke. Cụ thể trigger keyword.

### Sai 3 — Skill duplicate Agent

Đã có agent `blog-writer-style` → đừng tạo skill `viet-blog-style` duplicate. Agent có context isolation, skill không.

### Sai 4 — Skill phụ thuộc context bên ngoài

```
1. Đọc câu hỏi user vừa hỏi 5 phút trước
```

→ Skill không có context history. Phải pass đủ trong trigger.

---

## 📖 Chú thích

- **vault** = kho ghi chú — một folder thông thường trên máy tính được Obsidian nhận diện và quản lý đặc biệt (tạo liên kết giữa file, tìm kiếm toàn văn, hiển thị sơ đồ mạng lưới).
- **ingest** = đưa tài liệu thô vào kho để AI đọc và xử lý thành trang wiki — gồm: đọc nội dung, rút ý chính, tạo trang tóm tắt và cập nhật trang khái niệm liên quan.
- **memory** = file lưu thông tin AI cần nhớ qua các phiên làm việc khác nhau (ai là bạn, quy tắc nào phải theo, dự án nào đang chạy). Không có memory → mỗi lần mở mới AI quên hết.
- **commit** (Git) = hành động lưu lại một điểm phiên bản — như "chụp ảnh" trạng thái toàn bộ kho tại một thời điểm. Có thể khôi phục kho về bất kỳ commit nào trước đó.

## Tiếp theo

Đọc tiếp: [04-tao-skill-dau-tien](04-tao-skill-dau-tien.md) — Build skill đầu tiên thực hành.
