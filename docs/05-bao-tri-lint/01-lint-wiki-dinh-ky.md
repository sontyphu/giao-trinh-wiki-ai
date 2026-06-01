---
title: Rà soát wiki định kỳ
type: huong-dan
created: 2026-05-29
updated: 2026-05-29
phan: 05
---

# Rà soát wiki định kỳ

## Trước đó

[04-tao-skill-dau-tien](../04-agents-skills-memory/04-tao-skill-dau-tien.md) — bạn đã hiểu agents + skills.

---

## Vì sao rà soát

Sau 6-12 tháng vault grow, không rà soát định kỳ → vault mục:

- Link broken (file đã rename / delete)
- Page mồ côi (no inbound link)
- Mâu thuẫn (2 source nói khác nhau, chưa hoà giải)
- Tag không nhất quán (`course/khoa-ban-hang-b` vs `course/Khoa-Ban-Hang-B`)
- Frontmatter thiếu (page không có `type:`, `tags:`)
- Concept page nhắc trong 3+ source nhưng chưa có page

→ Rà soát = health check định kỳ. Như developer rà soát code.

---

## Tần suất rà soát

- **Weekly** (chủ nhật): rà soát nhanh — broken link, page mới mồ côi
- **Monthly**: rà soát sâu — consistency, tính độc lập, schema drift
- **Quarterly**: rà soát architecture — vault có nên tách / merge

---

## Bước 1 — Rà soát weekly

Trong Claude Code, root vault Brain:

```
> Lint wiki weekly. Check:
> 1. Broken wikilink (point tới page không tồn tại)
> 2. Page mới tuần này có frontmatter đầy đủ không
> 3. Source page mới đã update concept page liên quan chưa
> 4. log.md có entry weekly chưa
```

Claude:
- Glob `wiki/**/*.md`
- Grep wikilink `\[\[.*?\]\]`
- Check target tồn tại
- Report:

```
Rà soát report 2026-W22

## Broken wikilink (3)
- wiki/concepts/X.md → Concept Y không tồn tại
- wiki/sources/Z.md → Old Source đã rename
- ...

## Frontmatter thiếu (1)
- wiki/concepts/New-Concept.md thiếu `type:`, `tags:`

## Concept page chưa update (2)
- Source mới ingest hôm qua nhắc Concept A nhưng A.md chưa update

## Log entry
- W22 đã có 8 entry — OK
```

Bạn duyệt từng issue, fix hoặc skip.

---

## Bước 2 — Rà soát monthly

Sâu hơn weekly:

```
> Lint wiki monthly. Check:
> 1. Mâu thuẫn giữa concept page và source page
> 2. Concept page tính độc lập — có concept nào gộp 2 idea không?
> 3. Course bản đồ nội dung 2-chiều — concept page nói "Khoá học sử dụng X" thì X.md có link ngược không?
> 4. Tag consistency — có tag duplicate khác case?
> 5. Stale page — page nào > 3 tháng không update?
> 6. Concept page nhắc trong 3+ source nhưng chưa có page riêng → đề xuất tạo
```

Claude:
- Đọc tất cả concept page + source page
- Cross-check
- Report comprehensive

Output dạng:

```
Rà soát monthly 2026-05

## Mâu thuẫn (2)
- Concept Y nói "PMF = 40% user buồn nếu mất". 
  Source Z nói "PMF = retention 90%". 
  → Cần ghi mâu thuẫn / merge / clarify

## Atomicity vi phạm (1)
- Concept HD-NT gộp 2 khái niệm "Hướng đến" + "Né tránh" — cấu trúc khác nhau
  → Tách thành Hướng đến + Né tránh

## Nhất quán 2 chiều (5)
- Concept A nói "Khoá học sử dụng Khoá Bán Hàng B" nhưng bản đồ nội dung không link A
- ...

## Tag inconsistent (2)
- `course/KHOA-BAN-HANG-B` (uppercase) trong 3 page vs `course/khoa-ban-hang-b` (lowercase) trong 47 page
  → Migrate uppercase → lowercase

## Stale (8)
- 8 page không update > 3 tháng — review hoặc archive

## Concept candidate (4)
- "Founder Mode" nhắc 5 source nhưng chưa có page → tạo
- "Burn Rate" nhắc 3 source → tạo
```

---

## Bước 3 — Rà soát quarterly architecture (kiến trúc)

Mỗi 3 tháng, rà soát sâu hơn:

```
> Lint architecture. Trả lời:
> 1. Vault hiện tại có schema drift không?
> 2. Có subfolder nào > 200 file → nên split?
> 3. Có archetype nào emerge → nên tách vault?
> 4. CLAUDE.md có rule outdated không?
> 5. Memory có entry stale không?
```

Claude:
- Đánh giá size vault
- Check distribution subfolder
- Suggest restructuring nếu cần

Output:

```
Architecture review 2026-Q2

## Vault size
- 1245 page (raw: 580, wiki: 665)
- Tăng 220 page từ Q1

## Subfolder distribution
- wiki/concepts/ — 312 (vẫn OK)
- wiki/sources/ — 234 (OK)
- wiki/students/ — 158 (BIG — cân nhắc tách)
  → Đề xuất: tách wiki/students/ thành vault riêng nếu sẽ vượt 300

## Archetype emerge
- 50 page về personal hobby lẫn trong wiki/concepts/
  → Đề xuất: tách vault Life

## CLAUDE.md outdated
- Rule "Frontmatter type chỉ có 5 loại" nhưng đã thấy `type: story`, `type: student` không trong list
  → Update CLAUDE.md add 2 type này

## Memory stale
- 3 memory về preference cũ (đã đổi)
- 1 memory về tool deprecated
  → Cleanup
```

---

## Bước 4 — Tạo skill rà soát

Để chạy rà soát nhanh, tạo skill `/lint-wiki`:

```bash
mkdir -p .claude/skills/lint-wiki
```

`.claude/skills/lint-wiki/SKILL.md`:

```
---
name: lint-wiki
description: "Rà soát wiki vault. Use khi user nói 'rà soát kho', 'health check', 'audit wiki'. Mode: weekly | monthly | quarterly."
---

# Rà soát Wiki Skill

## Trigger

User nói:
- `/lint-wiki weekly`
- `/lint-wiki monthly`  
- `/lint-wiki quarterly`
- "Rà soát wiki tuần này"
- "Health check vault"

Mode mặc định: weekly.

## Workflow weekly

[Như bước 1 ở trên]

## Workflow monthly

[Như bước 2 ở trên]

## Workflow quarterly

[Như bước 3 ở trên]

## Output

Report markdown lưu vào `wiki/rà soát-reports/YYYY-MM-DD-<mode>.md`.

## Constraint

- KHÔNG tự fix issue — chỉ report
- User quyết thứ tự fix
- Report ngắn gọn (5-15 bullet, không > 1 page)
```

Gọi:

```
> /lint-wiki monthly
```

Skill tự chạy + tạo report.

---

## Bước 5 — Fix issue từ rà soát

Sau khi có rà soát report, fix dần:

### Fix broken link (liên kết hỏng)

```
> Fix broken wikilink trong wiki/concepts/X.md — link Concept Y không tồn tại. 
> Tạo concept page Y dạng stub hoặc rename link.
```

Claude:
- Hỏi: tạo Y hay rename link?
- Apply quyết định

### Fix mâu thuẫn

```
> Concept Y và Source Z mâu thuẫn về PMF. Ghi section "Mâu thuẫn" trong cả 2 page.
```

### Fix tính độc lập (tính nguyên tử)

```
> Tách concept page "HD-NT" thành 2 page "Hướng đến" + "Né tránh".
> Update tất cả wikilink ref.
```

Claude:
- Tạo 2 page mới
- Move nội dung phù hợp
- Update wikilink trong page khác

---

## Bước 6 — Audit log

Sau khi rà soát xong, log:

```
## [2026-05-29] rà soát | monthly
- Issues found: 18
- Fixed: 12
- Deferred: 4 (chờ user quyết)
- Skipped: 2 (false positive)
- Report: 2026-05-29-monthly
```

---

## Bước 7 — Pattern rà soát hay gặp

5 issue thường nhất:

### Issue 1 — Broken wikilink sau rename file

User rename file `Concept-A.md` → `Concept A.md` (thêm space). Mọi `Concept-A` cũ vỡ.

Fix: Obsidian "Refactor file" (Cmd+P → Refactor → rename) → tự update wikilink. Hoặc dùng Claude bulk fix.

### Issue 2 — Concept tạo nhưng chưa link course

Concept page có frontmatter `tags: [course/khoa-ban-hang-b]` nhưng bản đồ nội dung khoá đó không liệt concept.

Fix: update Course bản đồ nội dung, add `## Modules — Concept`.

### Issue 3 — Source page không cite concept

Source page có nội dung touch concept nhưng quên cite `concept`.

Fix: Claude scan source page → đề xuất concept liên quan → cite.

### Issue 4 — Frontmatter inconsistent

Page A có `tags: [framework, course/khoa-ban-hang-b]`. Page B có `tag: framework` (typo `tag` thiếu `s`).

Fix: standard `tags` (plural). Bulk fix.

### Issue 5 — Stale snapshot

Source page snapshot tại 2024-10. Source raw đã update 2025-06 nhưng wiki không update.

Fix: ingest lại source mới với agent → wiki update.

---

## Bước 8 — Tránh over-engineering rà soát

Đừng:

- Rà soát mỗi ngày (overhead, ít issue)
- Auto-fix mọi issue (false positive risk)
- Tạo 100 rà soát rule (complexity)

Giữ:
- Weekly basic (5 rule)
- Monthly comprehensive (10-15 rule)
- Quarterly architectural (5 question)

---

## Bước 9 — Khi rà soát phát hiện vấn đề lớn

Vd rà soát thấy 50% wikilink broken → vault bị corrupt:

- DỪNG ngay
- Kiểm tra Git history (revert nếu cần)
- Restore từ backup gần nhất
- Investigate nguyên nhân (rename script lỗi? Migrate folder sai?)

KHÔNG bulk fix khi có dấu hiệu corruption.

---

## Bước 10 — Rà soát cross-vault

Nếu có multi-vault, rà soát cross-vault:

```
> Lint cross-vault: check brain_ref trong Marketing có trỏ page tồn tại trong Brain không?
```

Claude:
- Đọc Marketing/wiki/assets/ frontmatter
- Check brain_ref → file Brain exist
- Report broken cross-ref

---

## 📖 Chú thích

- **vault** = kho ghi chú — một folder thông thường trên máy tính được Obsidian nhận diện và quản lý đặc biệt (tạo liên kết giữa file, tìm kiếm toàn văn, hiển thị sơ đồ mạng lưới).
- **ingest** = đưa tài liệu thô vào kho để AI đọc và xử lý thành trang wiki — gồm: đọc nội dung, rút ý chính, tạo trang tóm tắt và cập nhật trang khái niệm liên quan.
- **memory** = file lưu thông tin AI cần nhớ qua các phiên làm việc khác nhau (ai là bạn, quy tắc nào phải theo, dự án nào đang chạy). Không có memory → mỗi lần mở mới AI quên hết.
- **wikilink** = cách tạo liên kết nội bộ trong Obsidian bằng cú pháp `Tên trang`. Click vào liên kết → mở trang đó ngay. AI tự tạo các wikilink này khi viết wiki.
- **frontmatter** = phần thông tin khai báo ở đầu mỗi file, nằm giữa hai dòng `---`. Ví dụ: loại trang (type), từ khoá (tags), ngày tạo. AI dùng phần này để phân loại và tìm kiếm trang.
- **schema** = cấu trúc và quy tắc tổ chức kho: mỗi loại trang có những phần nào, thông tin nào bắt buộc, đặt tên file theo kiểu gì. Schema được mô tả trong CLAUDE.md.

## Tiếp theo

Đọc tiếp: [02-backup-icloud-git](02-backup-icloud-git.md) — Backup chiến lược.
