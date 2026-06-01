---
title: CLAUDE.md master template
type: template
created: 2026-05-29
updated: 2026-05-29
phan: 99
---

# CLAUDE.md master template (tổng quát)

Template CLAUDE.md tổng quát — không specific cho 1 thương hiệu hay cá nhân nào. Copy thẳng vào vault mới, customize 3-5 chỗ marked `<...>`.

---

## Khi nào dùng

Vault mới bất kỳ kiểu (knowledge / lifestyle / production / execution). Customize tuỳ kiểu vault.

---

## Template

Copy đoạn dưới vào `CLAUDE.md` ở root vault:

```
# CLAUDE.md — Schema Wiki "<Vault Name>"

Vault này là wiki LLM tự duy trì. Kiến thức được biên tập 1 lần khi source vào và giữ cho cập nhật — không tái dựng lại mỗi lần truy vấn.

**Đọc file này đầu mỗi session, trước khi đọc/ghi bất cứ file nào khác.**

## 1. Mục đích vault

<1-2 đoạn — vault này phục vụ mục đích gì, ai dùng, scope thế nào>

Ví dụ:
- Knowledge: "Vault lưu kiến thức cá nhân về <domain>. Source là article web, sách, video. Output là concept page độc lập + cross-link."
- Lifestyle: "Vault lưu đời sống cá nhân — sở thích, hobby, gia đình. Photo + event timeline + entity tracking."
- Production: "Vault lưu trữ + đo lường marketing — content, lead/sale page, ad creative, biến thể A/B."

## 2. Chủ vault

<Tên bạn> — <năm sinh / role / context>.

### Cách xưng hô

- Tự xưng "<bạn>" / "<tôi>" trong wiki content
- Tiếng Việt 100% nội dung (hoặc ngôn ngữ bạn chọn)
- Tên file: kebab-case không dấu (hoặc kebab-case có dấu, tuỳ Obsidian config)

## 3. Vault song song (nếu multi-vault)

- `../<Sibling Vault A>/` — vai trò 1 dòng
- `../<Sibling Vault B>/` — vai trò 1 dòng

Ranh giới giữa vault này và sibling: <ngắn gọn>.

Nếu chỉ 1 vault → bỏ section này.

## 4. Ba lớp

1. **Raw sources** (`raw/`) — tài liệu input bất biến. Chỉ đọc, không sửa.
2. **Wiki** (`wiki/`) — page markdown do AI viết. AI sở hữu lớp này.
3. **Schema** (file này) — quy ước và quy trình. Tiến hoá theo thời gian.

Cộng thêm 2 file root:
- `index.md` — danh mục
- `log.md` — chronological log

## 5. Cấu trúc thư mục

```
/
├── CLAUDE.md
├── README.md
├── index.md
├── log.md
├── raw/
│   ├── assets/
│   └── <subfolder theo nguồn>
└── wiki/
    ├── sources/
    ├── concepts/
    ├── entities/
    └── <subfolder theo archetype>
```

Subfolder trong `wiki/` là gợi ý. Thêm khi domain đòi hỏi.

## 6. Quy ước file

- **Tên file**: <kebab-case không dấu | tên có dấu cách OK>
- **Wikilink (liên kết nội bộ)**: `Page Name` mỗi khi nhắc entity/concept/source
- **Frontmatter (phần thông tin đầu file)**: mọi page mở đầu bằng YAML:

```
---
type: source | entity | concept | topic | analysis
tags: [tag1, tag2]
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: ["Source A"]
---
```

## 7. Workflow chính

### A. INGEST — khi user thả source mới

1. Đọc source đầy đủ
2. Bàn key takeaway với user (3-5 bullet) — hỏi muốn nhấn gì
3. Viết source page `wiki/sources/<Title>.md`
4. Tạo/update concept page `wiki/concepts/`
5. Tạo/update entity page `wiki/entities/`
6. Update `index.md`
7. Append `log.md`
8. Báo cáo tóm tắt cho user

### B. QUERY — khi user hỏi

1. Đọc `index.md` tìm page candidate
2. Drill vào page liên quan, theo wikilink
3. Tổng hợp câu trả lời CITE source
4. Đề xuất lưu thành `wiki/analyses/` nếu giá trị

### C. RÀ SOÁT — khi user nói "rà soát kho"

Check:
- Wikilink broken (liên kết hỏng)
- Page mồ côi
- Frontmatter thiếu
- Concept duplicate
- Mâu thuẫn chưa giải quyết
- Cross-link 2-chiều (nếu có course bản đồ nội dung)

Report dạng checklist. Không tự fix.

## 8. Quy ước log

`## [YYYY-MM-DD] <action> | <subject>`

Action: `ingest` | `query` | `rà soát` | `setup` | `refactor`.

Greppable: `grep "^## \[" log.md | tail -10`.

## 9. Khi không chắc

- Tên entity/concept chưa rõ → placeholder slug `entity-x`
- Số liệu mâu thuẫn → ghi cả 2 với section "Mâu thuẫn" + flag `needs-review`
- Source quá dài (>10k dòng) → chia chunk trước (skill `text-cat-chunk`)
- AI không đủ context → hỏi user 1 câu ngắn rồi tiếp tục

## 10. Tự tiến hoá

Khi AI phát hiện cải tiến workflow, sở thích lặp lại của user — đề xuất sửa file này và xin xác nhận. Schema drift theo feedback.
```

---

## Customize cho kiểu vault cụ thể

### Knowledge vault (vault kiến thức chuyên sâu)

Thêm sau mục 5:

```
## 5b. Nguyên tắc concept-first

Wiki này concept-centric. Concept là đơn vị lưu trữ; source/course/entity là context.

### Atomicity (tính nguyên tử — mỗi concept 1 page độc lập)

Mỗi concept độc lập = 1 page. KHÔNG gộp 2 concept dù dạy cặp đôi.

Heuristic:
1. Có cấu trúc riêng → tách
2. Có line ref riêng → tách
3. Link độc lập từ concept khác → tách
4. Enumeration của 1 framework → gộp
```

### Lifestyle vault (vault đời sống cá nhân)

Thay mục 5 với:

```
## 5. <N> mảng đời sống

| Slug | Mảng |
|---|---|
| `<slug-1>` | <Mảng 1> |
| `<slug-2>` | <Mảng 2> |

Quy tắc cứng: mọi entity/event/concept phải neo về ít nhất 1 domain. Domain ghi `domain: [<slug>]` trong frontmatter.

## 5b. Năm loại trang

```
wiki/
├── domains/        # N trang tổng quan
├── entities/       # Thực thể danh tính
├── events/         # Sự kiện theo timeline
├── concepts/       # Khái niệm cần nắm
├── analysis/       # Phân tích / báo cáo
```

## 5c. Xử lý ảnh từ iPhone

Khi thả ảnh vào `raw/photos/YYYY-MM-DD/`:

1. Mở từng ảnh, mô tả nội dung
2. Suy ra event tương ứng
3. Tạo `wiki/events/YYYY-MM-DD-<slug>.md`
4. Update entity liên quan
5. Link ảnh gốc trong frontmatter `source:`
```

### Production vault (vault marketing / sản xuất)

Thêm sau mục 3:

```
## 3b. Cross-vault kiến thức

- `../<Knowledge Vault>/` — đọc concept/course từ vault kiến thức
- Production chỉ đọc, không ghi ngược
- Reference: frontmatter `brain_ref` hoặc wikilink absolute

## 5b. Asset tracking (theo dõi tài sản)

Mỗi asset (lead-page, sale-page, content, ad) là 1 page riêng với:

```
---
type: asset
asset_kind: lead-page | sale-page | content | ad
brand: <brand>
brain_ref:
  program_code: <code>
  course_page: "..."
status: stable | draft | needs-review | archived
variants:
  - id: v1
    label: ...
    metrics: { traffic, opt_in, cvr, ... }
quality_score: 1-5
---
```
```

### Execution vault (vault thực thi — 4DX)

Thay mục 7 với:

```
## 7. Workflow execution

### Daily — user nhập action

Mỗi tối 21:00, nhập action vào `actions/2026-Wxx-actions.md` format:

```
- [x] HH:MM-HH:MM | wig=N | metric=<name> | val=<number> | activity="..."
```

### Weekly — tác vụ tự động theo lịch (lệnh tự động theo lịch) generate review

CN 23:30 tác vụ lệnh tự động theo lịch scan actions/ → traffic light per mục tiêu tối quan trọng → generate `reviews/weekly/Wxx.md`.

### Monthly — review mục tiêu tối quan trọng

User review mục tiêu tối quan trọng hit ratio quarter. Adjust target nếu cần.
```

---

## Khi nào extend template

Add section khi:
- Có workflow đặc thù (lệnh tự động theo lịch, photo pipeline, ingest CSV)
- Có schema đặc thù (asset variant, koi entity, event timeline)
- Có cross-vault relationship rõ rệt

Giữ CLAUDE.md ngắn:
- Vault nhỏ (< 100 page): CLAUDE.md ≤ 100 dòng
- Vault vừa (< 500 page): CLAUDE.md ≤ 200 dòng
- Vault to (> 500 page): CLAUDE.md ≤ 300 dòng

---

## Test template

Sau khi paste CLAUDE.md vào vault mới:

```
> Đọc CLAUDE.md và tóm tắt schema vault trong 3 dòng
```

Claude trả lời đúng schema → template hợp lệ.

---

## 📖 Chú thích

- **vault** = kho ghi chú — một folder thông thường trên máy tính được Obsidian nhận diện và quản lý đặc biệt (tạo liên kết giữa file, tìm kiếm toàn văn, hiển thị sơ đồ mạng lưới).
- **ingest** = đưa tài liệu thô vào kho để AI đọc và xử lý thành trang wiki — gồm: đọc nội dung, rút ý chính, tạo trang tóm tắt và cập nhật trang khái niệm liên quan.
- **wikilink** = cách tạo liên kết nội bộ trong Obsidian bằng cú pháp `Tên trang`. Click vào liên kết → mở trang đó ngay. AI tự tạo các wikilink này khi viết wiki.
- **frontmatter** = phần thông tin khai báo ở đầu mỗi file, nằm giữa hai dòng `---`. Ví dụ: loại trang (type), từ khoá (tags), ngày tạo. AI dùng phần này để phân loại và tìm kiếm trang.
- **schema** = cấu trúc và quy tắc tổ chức kho: mỗi loại trang có những phần nào, thông tin nào bắt buộc, đặt tên file theo kiểu gì. Schema được mô tả trong CLAUDE.md.
- **slug** = cách đặt tên file chuẩn: viết thường không dấu, các từ nối bằng dấu gạch ngang. Ví dụ: `phuong-phap-ban-hang.md`, `tu-khoa-da-xac-minh.md`. Đảm bảo tên file hoạt động trên mọi hệ điều hành.

## Tiếp theo

Đọc tiếp: [concept-page-template](concept-page-template.md) — Concept page template.
