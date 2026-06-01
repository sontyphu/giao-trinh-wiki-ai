---
type: note
tags: [giao-trinh, wiki-ai, dao-tao]
created: 2026-06-01
updated: 2026-06-01
---

# Giáo trình: Xây hệ thống ghi chú AI tự quản lý

Chào mừng bạn đến với giáo trình dạy bạn xây **hệ thống wiki cá nhân** kiểu AI-first, concept-first, multi-vault — AI quản lý tự động, bạn chỉ thả tài liệu vào và duyệt kết quả.

> Đây là 1 vault Obsidian. Có 3 cách đọc:
>
> 1. 📦 **Mở bằng Obsidian** — có graph view, wikilink click được, tìm kiếm toàn văn
> 2. 📄 **Đọc plain text** — mở từng file `.md` bằng bất kỳ text editor nào
> 3. 🚀 **Đi thẳng vào** — xem [QUICK-START](quick-start.md) để chọn lộ trình phù hợp

---

## Bắt đầu nhanh

**Người mới hoàn toàn**: đọc [QUICK-START](quick-start.md) trước — checklist 30 phút đầu + 3 lộ trình.

**Sẵn sàng đi luôn**: vào [01-tai-sao-ai-first-wiki](00-triet-ly/01-tai-sao-ai-first-wiki.md) — file đầu tiên.

**Lấy mẫu trước, đọc sau**: vào [claude-md-master-template](99-templates/claude-md-master-template.md) — mẫu CLAUDE.md copy-paste được ngay.

---

## Bạn sẽ học được gì

Giáo trình gồm **37 file nội dung** + 4 file root, chia 7 phần. Sau khi hoàn thành, bạn sẽ có:

- **1 hệ thống nhiều kho Obsidian** đồng bộ qua iCloud, được AI Claude quản lý tự động
- **1 kho kiến thức "Brain"** kiểu concept-first — AI đọc tài liệu 1 lần, viết wiki, không cần scan lại mỗi khi tra cứu
- **3 kho sibling** (Life theo dõi cá nhân / 4DX thực thi / Marketing vận hành) tách bạch rõ ràng
- **Agent + skill + memory** — AI tự xử lý workflow lặp đi lặp lại
- **Quy trình rà soát + sao lưu + di chuyển** để hệ thống sống lâu dài

Tổng thời gian học: **15-20 giờ** trải dài 1-2 tuần.

---

## Đối tượng

Giáo trình này viết cho:

- Người **chưa biết Obsidian** — sẽ dạy từ bước cài đặt
- Người **chưa dùng Claude Code** — sẽ dạy từ đầu
- Doanh nhân, chuyên gia, trainer, coach muốn xây kho tri thức cá nhân có hệ thống
- Người muốn dùng AI làm "trợ lý quản lý kiến thức" thay vì chỉ chat

Không cần biết lập trình. Không cần biết dòng lệnh nâng cao (sẽ dạy lệnh cơ bản từng bước). Máy Mac ưu tiên nhưng Windows + Linux cũng có hướng dẫn riêng.

---

## Yêu cầu trước khi bắt đầu

- **Máy tính** (macOS / Windows / Linux đều được)
- **iCloud Drive** hoặc dịch vụ đồng bộ tương đương (Dropbox / Google Drive / OneDrive)
- **Tài khoản Claude Pro** (~$20/tháng) — phiên bản miễn phí không đủ để dùng Claude Code lâu dài
- **Tài khoản GitHub** (tuỳ chọn — để sao lưu kho)
- **2-3 giờ tuần đầu** để cài đặt và xây kho Brain đầu tiên

---

## Lộ trình học — 7 phần

Đi tuần tự từ đầu đến cuối:

| Phần | Nội dung | Thời gian |
|---|---|---|
| [00-triet-ly](00-triet-ly/01-tai-sao-ai-first-wiki.md) | 4 file — Tại sao thiết kế thế này | 1-2h |
| [01-cai-dat](01-cai-dat/01-cai-obsidian.md) | 5 file — Cài Obsidian + Claude + tiện ích | 2-3h |
| [02-vault-dau-tien-brain](02-vault-dau-tien-brain/01-tao-vault-brain.md) | 8 file — Xây kho Brain đầu tiên | 4-6h |
| [03-mo-rong-multi-vault](03-mo-rong-multi-vault/01-khi-nao-tach-vault.md) | 5 file — Tách thêm kho khi cần | 3-4h |
| [04-agents-skills-memory](04-agents-skills-memory/01-agent-la-gi.md) | 5 file — Tự động hoá với agent + skill + memory | 3-4h |
| [05-bao-tri-lint](05-bao-tri-lint/01-lint-wiki-dinh-ky.md) | 4 file — Bảo trì hệ thống dài hạn | 1-2h |
| [99-templates](99-templates/claude-md-master-template.md) | 6 file — Mẫu copy-paste sẵn | — |

**Checkpoint quan trọng**: Sau khi xong Phần 02 → kho Brain đã chạy được. Có thể dừng ở đây và dùng ngay. Phần 03-05 là mở rộng theo nhu cầu.

---

## Cách dùng giáo trình

**Cách 1 — Đọc tuần tự**: theo link `## Tiếp theo` ở cuối mỗi file. Không cần nhớ cấu trúc.

**Cách 2 — Tra cứu**: dùng [index](muc-luc.md) để tìm chủ đề cụ thể theo từ khoá.

**Cách 3 — Copy mẫu trước**: vào thẳng [claude-md-master-template](99-templates/claude-md-master-template.md) lấy mẫu, đọc giải thích sau.

---

## Quy ước trong giáo trình

- `bạn` — người đọc (bạn)
- `Claude` hoặc `AI` — phần mềm AI Claude dùng để quản lý kho
- `vault` hoặc `kho` — folder Obsidian chứa toàn bộ nội dung
- Code block `bash` — copy paste vào terminal (cửa sổ dòng lệnh)
- Code block `markdown` — copy paste vào file `.md`
- `[[Tên trang]]` — liên kết nội bộ (wikilink) trong Obsidian

---

## Khi gặp khó khăn

- Bị kẹt ở bước nào → đọc lại `## Trước đó` ở đầu file đang đọc để chắc nền tảng
- Lỗi kỹ thuật → xem [FAQ](faq.md) — hơn 80% vấn đề đã có giải pháp
- Lỗi dòng lệnh → chụp màn hình + hỏi Claude trực tiếp: "Lỗi này nghĩa là gì và sửa thế nào?"
- Lỗi Obsidian → search trong Obsidian Help (Cmd+H trên Mac)

---

## Cấu trúc thư mục

```
giao-trinh-wiki-ai/
├── README.md          ← file này — đọc đầu tiên
├── QUICK-START.md     ← 3 lộ trình + checklist 30 phút đầu
├── FAQ.md             ← câu hỏi thường gặp và lỗi phổ biến
├── index.md           ← mục lục đầy đủ 41 file
│
├── 00-triet-ly/       ← 4 file triết lý
├── 01-cai-dat/        ← 5 file cài đặt
├── 02-vault-dau-tien-brain/  ← 8 file xây kho đầu tiên
├── 03-mo-rong-multi-vault/   ← 5 file mở rộng
├── 04-agents-skills-memory/  ← 5 file tự động hoá
├── 05-bao-tri-lint/          ← 4 file bảo trì
└── 99-templates/             ← 6 file mẫu copy-paste
```

---

## Lưu ý

**Giáo trình này ≠ Kho kiến thức của bạn.** Folder này chỉ chứa bài học. Sau khi học xong, bạn tạo kho riêng ở folder khác. Giữ giáo trình làm tài liệu tham khảo — khi rà soát kho, gặp vấn đề, hay cần nhớ lại quy trình, quay lại đây tra cứu.

---

## 📖 Chú thích

- **vault** = kho ghi chú — một folder thông thường trên máy tính được Obsidian nhận diện và quản lý đặc biệt (tạo liên kết giữa file, tìm kiếm toàn văn, hiển thị sơ đồ mạng lưới).
- **memory** = file lưu thông tin AI cần nhớ qua các phiên làm việc khác nhau (ai là bạn, quy tắc nào phải theo, dự án nào đang chạy). Không có memory → mỗi lần mở mới AI quên hết.
- **wikilink** = cách tạo liên kết nội bộ trong Obsidian bằng cú pháp `[[Tên trang]]`. Click vào liên kết → mở trang đó ngay. AI tự tạo các wikilink này khi viết wiki.
- **Graph view** = chế độ hiển thị của Obsidian dạng mạng lưới, cho thấy tất cả trang và liên kết giữa chúng. Dùng để phát hiện trang mồ côi (không ai liên kết tới) hoặc cluster kiến thức.
- **terminal** (còn gọi là cửa sổ dòng lệnh) = nơi bạn gõ lệnh văn bản thay vì click chuột. Trên Mac: tìm "Terminal" trong Spotlight. Trên Windows: tìm "PowerShell" hoặc "Command Prompt".
