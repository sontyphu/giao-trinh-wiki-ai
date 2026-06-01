---
type: note
tags: [faq, giao-trinh, troubleshoot]
created: 2026-06-01
updated: 2026-06-01
---

# FAQ — Câu hỏi thường gặp & Lỗi phổ biến

Đọc file này khi bị kẹt. Phần lớn vấn đề đã có câu trả lời ở đây.

---

## Nhóm 1 — Câu hỏi về khái niệm

### "Vault là gì? Khác gì với folder thông thường?"

**Vault** chỉ là một folder (thư mục) bình thường trên máy tính, nhưng được **Obsidian nhận ra** và xử lý đặc biệt — tạo liên kết giữa các file, hiển thị sơ đồ mạng, hỗ trợ tìm kiếm nhanh.

Hình dung đơn giản: vault = "thư mục thông minh" mà Obsidian biết cách đọc.

### "CLAUDE.md là gì? Tại sao cần nó?"

CLAUDE.md là file văn bản bạn đặt trong vault, dùng để **dạy AI hiểu kho của bạn** — kho này dùng để làm gì, theo quy tắc nào, lưu thông tin theo cấu trúc gì.

Hình dung đơn giản: CLAUDE.md = "bản nội quy" mà bạn viết ra để AI làm việc đúng ý bạn, không phải làm theo kiểu mặc định của nó.

Không có CLAUDE.md → AI mỗi lần làm mỗi kiểu → kho lộn xộn dần.

### "Raw folder là gì? Tôi có phải đặt mọi thứ vào đó không?"

`raw/` là thư mục chứa **tài liệu gốc** — bài viết bạn lưu về, transcript video, PDF sách, ghi chú thô. Đặt nguyên xi vào, không chỉnh sửa.

AI sẽ đọc raw → viết tóm tắt → lưu vào `wiki/`. Bạn không cần làm thêm bước nào.

Không cần đặt mọi thứ vào raw. Chỉ những tài liệu bạn muốn AI xử lý.

### "Wiki folder dùng để làm gì?"

`wiki/` là nơi chứa **nội dung AI đã xử lý** — các trang tóm tắt, khái niệm, phân tích. AI viết ra đây sau khi đọc raw.

Bạn đọc wiki để tra cứu, không cần đọc lại raw gốc.

### "Wikilink là gì?"

Wikilink là cách liên kết giữa các file: `Tên file`. Khi bạn click vào `Khái niệm A` trong Obsidian, nó sẽ mở file "Khái niệm A" ngay lập tức.

AI tự tạo các liên kết này khi viết wiki — bạn không cần làm thủ công.

### "Markdown là gì? Tôi cần học không?"

Markdown là cách định dạng văn bản đơn giản bằng ký tự đặc biệt:
- `# Tiêu đề lớn`
- `## Tiêu đề nhỏ hơn`
- `**chữ đậm**`
- `- dấu gạch đầu dòng`

Obsidian dùng markdown. Bạn không cần học sâu — chỉ cần biết `#` là tiêu đề, `-` là danh sách. Phần còn lại AI làm cho bạn.

### "Tại sao cần trả tiền Claude? Miễn phí không được sao?"

Phiên bản miễn phí của Claude có giới hạn số lần hỏi mỗi ngày và không có đủ khả năng đọc file lớn. Để dùng Claude Code (công cụ AI đọc/ghi file trực tiếp), bạn cần tài khoản Pro (~$20/tháng).

Nghĩ đơn giản: bạn đang thuê "nhân viên AI" — phiên bản Pro là nhân viên toàn thời gian, miễn phí là thực tập sinh chỉ làm một lúc rồi nghỉ.

---

## Nhóm 2 — Lỗi khi cài đặt

### Lỗi: Obsidian mở vault nhưng file không hiện lên

**Nguyên nhân phổ biến**: Bạn mở *folder con* thay vì folder vault chính.

**Cách fix**: Trong Obsidian, vào `File > Open vault` → chọn đúng folder gốc (folder chứa CLAUDE.md và các folder con 00-triet-ly, 01-cai-dat...).

### Lỗi: Claude Code báo "command not found" khi gõ `claude`

**Nguyên nhân**: Claude Code chưa được cài hoặc chưa thêm vào PATH (đường dẫn hệ thống).

**Cách fix**:
1. Kiểm tra đã cài chưa: [03-cai-claude-code](01-cai-dat/03-cai-claude-code.md)
2. Sau khi cài, đóng terminal → mở lại → thử lại

### Lỗi: Claude Code báo "Not authenticated"

**Nguyên nhân**: Chưa đăng nhập hoặc phiên đăng nhập hết hạn.

**Cách fix**: Gõ `claude auth login` → làm theo hướng dẫn trên màn hình.

### Lỗi: Vault không đồng bộ qua iCloud

**Nguyên nhân phổ biến**: Vault không nằm trong thư mục iCloud Drive đúng chỗ.

**Đường dẫn đúng trên Mac**: `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/`

**Cách fix**: Di chuyển folder vault vào đúng đường dẫn trên, rồi mở lại trong Obsidian.

### Lỗi: Plugin Dataview không hoạt động sau khi cài

**Cách fix**: Vào `Settings > Community plugins` → bật nút "Enable" cạnh Dataview → restart Obsidian.

---

## Nhóm 3 — Lỗi khi dùng

### "Tôi nói với AI 'ingest file này' nhưng AI không làm gì"

**Nguyên nhân phổ biến 1**: AI chưa đọc CLAUDE.md của vault. Hãy nói rõ: *"Đọc CLAUDE.md trước, rồi ingest file raw/tên-file.md"*.

**Nguyên nhân phổ biến 2**: File bạn chỉ định không tồn tại ở đường dẫn đó. Kiểm tra lại tên file và thư mục.

### "AI viết wiki nhưng nội dung không đúng với tài liệu gốc"

**Nguyên nhân**: File raw quá dài, AI chỉ đọc được một phần.

**Cách fix**: Chia file raw thành nhiều phần nhỏ hơn (mỗi phần ~5,000-10,000 chữ). Ingest từng phần một.

### "AI tạo nhiều file cho cùng một khái niệm"

**Ví dụ**: Khái niệm "phễu bán hàng" xuất hiện ở 3 file khác nhau.

**Cách fix**: Nói với AI: *"Tìm tất cả file nói về phễu bán hàng, gộp thành 1 file, xoá 2 file còn lại"*.

Để tránh lặp lại: Trước khi ingest source mới, nhắc AI *"Kiểm tra khái niệm nào đã có trong wiki/ trước khi tạo file mới"*.

### "Wikilink bị gãy — click vào không mở được file"

**Nguyên nhân**: Tên file trong wikilink không khớp với tên file thật (sai chính tả, sai dấu, sai viết hoa).

**Cách fix**: Trong Obsidian, file gãy link sẽ hiện màu khác. Click phải → "Rename" để đổi tên đúng, hoặc sửa wikilink trong file nguồn.

### "AI mỗi lần làm mỗi kiểu, không nhất quán"

**Nguyên nhân**: CLAUDE.md chưa đủ rõ ràng, hoặc AI không đọc CLAUDE.md trước.

**Cách fix**:
1. Mở đầu mỗi session: *"Đọc CLAUDE.md của vault này trước"*
2. Nếu AI làm sai → chỉ chỗ sai → nói *"Ghi nhớ: lần sau làm kiểu X, không làm kiểu Y"*
3. Nếu lỗi lặp lại nhiều lần → thêm rule vào CLAUDE.md

---

## Nhóm 4 — Câu hỏi về chiến lược

### "Tôi nên bắt đầu ingest tài liệu gì trước?"

Bắt đầu với tài liệu **ngắn và quen thuộc** nhất — ví dụ 1 bài viết bạn đã đọc và có ý kiến về nó. Tránh bắt đầu với PDF 300 trang.

Mục tiêu lần đầu: thấy quy trình hoạt động, không phải hoàn thiện kho ngay.

### "Kho tôi nên lưu bao nhiêu tài liệu?"

Không có giới hạn kỹ thuật, nhưng chất lượng hơn số lượng. 50 tài liệu được tóm tắt tốt hơn 500 tài liệu lộn xộn.

Ingest có chọn lọc: chỉ những gì bạn thực sự sẽ tra cứu lại.

### "Khi nào thì tôi cần tách thêm vault mới?"

Khi vault vượt **500 file** VÀ bạn thấy khó tìm kiếm — lúc đó mới nên tách. Đừng tách sớm.

Chi tiết: [01-khi-nao-tach-vault](03-mo-rong-multi-vault/01-khi-nao-tach-vault.md)

### "Tôi có thể dùng hệ thống này cho team không?"

Hệ thống này thiết kế cho **cá nhân** — một người quản lý vault trên máy của mình. Obsidian không hỗ trợ nhiều người cùng sửa một vault.

Nếu cần chia sẻ: xuất nội dung ra Google Docs / Notion, hoặc dùng Git để đồng bộ (xem [02-backup-icloud-git](05-bao-tri-lint/02-backup-icloud-git.md)).

---

## Không thấy câu trả lời ở đây?

Hỏi thẳng Claude: mô tả vấn đề + tên file đang gặp lỗi + hành động bạn vừa làm.

Ví dụ: *"Tôi vừa gõ lệnh 'claude' trong terminal nhưng nhận được lỗi 'command not found'. Tôi đang dùng Mac, đã cài Claude Code theo bước 3 nhưng vẫn lỗi. Lỗi này nghĩa là gì và sửa thế nào?"*

---

## Trước đó

[README](muc-luc.md) — Tổng quan giáo trình


---

## 📖 Chú thích

- **vault** = kho ghi chú — một folder thông thường trên máy tính được Obsidian nhận diện và quản lý đặc biệt (tạo liên kết giữa file, tìm kiếm toàn văn, hiển thị sơ đồ mạng lưới).
- **ingest** = đưa tài liệu thô vào kho để AI đọc và xử lý thành trang wiki — gồm: đọc nội dung, rút ý chính, tạo trang tóm tắt và cập nhật trang khái niệm liên quan.
- **wikilink** = cách tạo liên kết nội bộ trong Obsidian bằng cú pháp `Tên trang`. Click vào liên kết → mở trang đó ngay. AI tự tạo các wikilink này khi viết wiki.
- **Dataview** = tiện ích mở rộng của Obsidian cho phép tạo danh sách và bảng tự động bằng cách truy vấn thông tin từ frontmatter của các file. Ví dụ: "liệt kê tất cả trang có type = concept theo thứ tự ngày tạo".
- **terminal** (còn gọi là cửa sổ dòng lệnh) = nơi bạn gõ lệnh văn bản thay vì click chuột. Trên Mac: tìm "Terminal" trong Spotlight. Trên Windows: tìm "PowerShell" hoặc "Command Prompt".

## Tiếp theo

[QUICK-START](quick-start.md) — Chọn lộ trình học phù hợp
