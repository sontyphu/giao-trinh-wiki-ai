---
title: Course bản đồ nội dung template
type: template
created: 2026-05-29
updated: 2026-05-29
phan: 99
---

# Course bản đồ nội dung template (copy-paste)

Template Course bản đồ nội dung (bản đồ nội dung — bản đồ nội dung) cho chương trình đào tạo. Copy vào `wiki/courses/<CODE> - <Tên>.md`.

---

## Template đầy đủ

```
---
type: concept
tags: [chuong-trinh, course/<code>, <theme-tags>]
program_code: <CODE>
parent: "Hệ sinh thái đào tạo của bạn"
sources:
  - "<Source signature 1>"
  - "<Source signature 2>"
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# <CODE> — <Tên đầy đủ>

<1-2 đoạn — định vị khoá: ai cho ai, dạy gì, format>

## Định vị

- **Target**: <persona đích>
- **Dạy**: <modules chính>
- **Format**: <online/offline/hybrid, mấy ngày, mấy attendees>
- **Phiên bản hiện tại**: <CODE version> (<date>)

## Vai trò trong hệ sinh thái

- **Upstream** (học trước): <Course A>
- **Downstream** (học sau): <Course B>
- **Song song** (cùng level): <Course C>

## Cấu trúc khoá

- Ngày 1: <main topic>
- Ngày 2: <main topic>
- Ngày 3: <main topic>

(Hoặc theo module nếu format khác)

## Modules / Khái niệm cốt lõi

- <Concept 1> — vai trò trong khoá
- <Concept 2> — ...
- <Concept N>

## Stories / Ngụ ngôn dùng

- <Story 1> — illustrate concept X
- <Story 2>

## Topics liên quan

- <Topic 1>
- <Topic 2>

## Cases học viên signature

- <Học viên A> — case nổi bật
- <Học viên B>

## Tài sản đã sản xuất

- Sale page: <URL>
- Lead page: <URL>
- Video promo: <URL>
- Email sequence: <N> emails

## Phiên bản đã ingest

| # | Phiên bản | Date | Source page | Signature |
|---|---|---|---|---|
| <N> | <CODE N> | YYYY-MM-DD | <Source> | <gì signature> |
| <N-1> | <CODE N-1> | YYYY-MM-DD | <Source> | <gì signature> |

## Khoá học liên quan

- <Course X> — concept overlap
- <Course Y>

## Câu hỏi mở

- ?
```

---

## Variant — Khoá offline 3 ngày

```
---
type: concept
tags: [chuong-trinh, course/khoa-ban-hang-b, ban-hang]
program_code: KHOA-BAN-HANG-B
parent: "Hệ sinh thái đào tạo của bạn"
sources:
  - "Khoá Bán Hàng A - Phần 1 (Livestream)"
  - "Khoá Bán Hàng B - Đợt 10 - Ngày 1 (15-07-2020)"
  - "Khoá Bán Hàng B - Đợt 21 - Ngày 1 (28-11-2025)"
---

# Khoá Bán Hàng B — Hệ thống bán hàng chuyên sâu

Khoá đào tạo bán hàng B2C cá nhân hoá flagship. Dạy hệ thống 8+2 + 14 chiến lược lead gen + 7 kỹ thuật xử lý từ chối.

## Định vị

- **Target**: Doanh chủ vừa và nhỏ, đội sales 5-20 người
- **Dạy**: Hệ thống bán hàng 8+2 + 14 chiến lược lead gen + 7 kỹ thuật xử lý từ chối
- **Format**: 3 ngày offline (T2-T4) hội trường Hà Nội/HCM, ~700-900 attendees
- **Phiên bản hiện tại**: Đợt 23 (2026-Q3)

## Vai trò trong hệ sinh thái

- **Upstream**: Khoá Tư Duy Doanh Chủ — học tư duy trước
- **Downstream**: Khoá Marketing Online — scale online sau khi master bán hàng
- **Song song**: Khoá Intensive Camp — cùng level deep dive

## Cấu trúc khoá

- **Ngày 1**: Hệ thống bán hàng 8+2 (4h) + 14 chiến lược lead gen (3h) + 7 kỹ thuật xử lý từ chối (2h)
- **Ngày 2**: Practice case học viên (hot seat) + REM-30s + REM-60s + Persona Customer Value
- **Ngày 3**: Tích hợp + DMO + commit DMO 90 ngày + bài tập về nhà

## Modules / Khái niệm cốt lõi

- Hệ thống bán hàng 8+2 — module chính (12h)
- 14 chiến lược lead generation — module bổ trợ (3h)
- 7 kỹ thuật xử lý từ chối — practice live (2h)
- REM-30s — bài thuyết trình 30 giây
- Customer Value Canvas — tiền đề persona
- Hot Seat — format coaching ngày 2

## Stories / Ngụ ngôn dùng

- Gã ăn mày giàu có — illustrate "đầu tư vào bản thân"
- Bút chì cùn — illustrate "kỹ năng cần mài giũa"

## Topics liên quan

- Tâm lý khách hàng B2C
- Persona doanh chủ Việt Nam

## Cases học viên signature

- Học viên A — chuyển từ -50% YoY sang +200% sau khoá
- Học viên B — vận hành team 30 sale rep

## Tài sản đã sản xuất

- Sale page: https://example.com/khoa-ban-hang-b (current)
- Lead page: https://example.com/lp/checklist-30s
- Video promo: https://youtu.be/abc123
- Email sequence: 12 emails onboarding

## Phiên bản đã ingest

| # | Phiên bản | Date | Source page | Signature |
|---|---|---|---|---|
| 21 | Đợt 21 | 2025-11-28 | Khoá Bán Hàng B - Đợt 21 - Ngày 1 + D2/D3 | Mới nhất, +14 lead gen, +7 kỹ thuật xử lý từ chối |
| 10 | Đợt 10 | 2020-07-15 | Khoá Bán Hàng B - Đợt 10 - Ngày 1 | Hệ thống hoá đủ 8+2 (foundation) |

## Khoá học liên quan

- Khoá Bán Hàng A — tiền thân lịch sử, nền tảng 8+2
- Khoá Nâng Cao C — mở rộng after-sales

## Câu hỏi mở

- Phiên bản đợt 22 chưa ingest — chờ source
- Có version online ngắn 6h thay vì 3 ngày? Chưa có lịch
```

---

## Variant — Khoá online tự học (module-based)

```
---
type: concept
tags: [chuong-trinh, course/khoa-email-marketing, email-marketing]
program_code: EMM
parent: "Hệ sinh thái đào tạo của bạn"
---

# EMM — Email Marketing Mastery

Khoá online tự học 6 module Email Marketing cho freelancer + agency. Mỗi module 2-3h video.

## Định vị

- **Target**: Freelancer marketer + agency owner
- **Dạy**: 6 module Email Marketing — setup → segmentation → automation → optimization → ROI tracking
- **Format**: Online tự học, 6 module, 15h video + bài tập
- **Giá**: $497 lifetime hoặc $49/tháng

## Vai trò trong hệ sinh thái

- **Upstream**: Khoá Marketing Cơ Bản — cần biết funnel concept cơ bản
- **Downstream**: Khoá Marketing Automation Nâng Cao — cho người đã master EMM
- **Song song**: Khoá Content Marketing — paired hữu ích

## Cấu trúc khoá (6 module)

- **Module 1**: Email infrastructure + DNS setup (3h)
- **Module 2**: List building + lead magnet (2h)
- **Module 3**: Segmentation + tagging strategy (2h)
- **Module 4**: Automation workflows (Welcome, Re-engagement, Cart abandonment) (3h)
- **Module 5**: Copy + design optimization (2h)
- **Module 6**: ROI tracking + A/B test (3h)

## Modules / Khái niệm cốt lõi

- Email DNS setup (SPF, DKIM, DMARC)
- Lead magnet design
- Segmentation strategy
- Email automation workflow
- Email copy patterns
- ROI tracking email

## Tài sản đã sản xuất

- Sale page: https://example.com/emm
- Lead page: https://example.com/lp/emm-checklist
- Video promo: https://youtu.be/xyz789
- Drip sequence sau opt-in: 7 emails

## Phiên bản đã ingest

| # | Phiên bản | Date | Source page | Signature |
|---|---|---|---|---|
| 1 | EMM v1 | 2026-04-15 | EMM Module 1-6 (v1) | Launch baseline |

## Câu hỏi mở

- Cần add module mới về AI-powered email?
- Pricing $49/tháng vs $497 lifetime — ratio nào convert tốt hơn?
```

---

## Variant — Coaching weekly (tier cao nhất)

```
---
type: concept
tags: [chuong-trinh, course/coaching-weekly, coaching-weekly]
program_code: COACHING-WEEKLY
parent: "Hệ sinh thái đào tạo của bạn"
---

# Coaching Weekly — Chương trình 1 năm

Tier cao nhất hệ sinh thái. Coaching weekly 1 năm cho 50-80 thành viên elite. Lifetime relationship.

## Định vị

- **Target**: Doanh chủ đã qua các khoá cốt lõi, sẵn sàng commit 1 năm
- **Format**: 50 buổi weekly (Zoom hoặc offline HN/HCM), 2-3h/buổi
- **Cohort size**: 50-80 thành viên
- **Đầu tư**: Tier cao nhất

## Vai trò trong hệ sinh thái

- **Upstream**: Các khoá cốt lõi — qua hết mới đủ điều kiện
- **Downstream**: Không có — tier cao nhất

## Format buổi

Mỗi buổi:
- 30 phút check-in chia sẻ
- 1h hot seat (1-2 thành viên được coach deep)
- 30 phút Q&A
- 30 phút commitment tuần mới

## Concept thường dùng

- Hot Seat format
- Quarterly Goal Review
- Accountability Partner

## Cohorts đã ingest

| Cohort | Date | Sessions ingested |
|---|---|---|
| 2025 | 2025-01 — 2025-12 | 12 buổi (samples) |
| 2026 | 2026-01 — đang chạy | 22 buổi (partial) |

## Câu hỏi mở

- Có nên migrate Coaching Weekly sang vault sibling riêng nếu info nhạy cảm vượt ngưỡng?
```

---

## Khi nào không tạo Course bản đồ nội dung

- Bạn không có chương trình đào tạo chính thức
- Vault knowledge cá nhân (không dạy ai)
- 1 khoá < 5 source ingest (chưa đủ data)

Trong những trường hợp đó, knowledge vẫn organize được qua concept page + topic page, không cần Course bản đồ nội dung.

---

## 📖 Chú thích

- **vault** = kho ghi chú — một folder thông thường trên máy tính được Obsidian nhận diện và quản lý đặc biệt (tạo liên kết giữa file, tìm kiếm toàn văn, hiển thị sơ đồ mạng lưới).
- **ingest** = đưa tài liệu thô vào kho để AI đọc và xử lý thành trang wiki — gồm: đọc nội dung, rút ý chính, tạo trang tóm tắt và cập nhật trang khái niệm liên quan.
- **commit** (Git) = hành động lưu lại một điểm phiên bản — như "chụp ảnh" trạng thái toàn bộ kho tại một thời điểm. Có thể khôi phục kho về bất kỳ commit nào trước đó.

## Tiếp theo

[log-md-format](log-md-format.md) — log.md format.
