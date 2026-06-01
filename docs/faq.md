---
type: note
tags: [faq, giao-trinh, troubleshoot]
created: 2026-06-01
updated: 2026-06-01
---

# FAQ — Câu hỏi thường gặp về toàn hệ thống

Bộ câu hỏi tổng quan cho cả hệ thống ghi chú AI — từ khái niệm, cài đặt, sử dụng đến chiến lược và chi phí. Các câu được **đánh số liên tục (Q1 → Q33)** và chia 6 nhóm. Bị kẹt ở đâu, tra số ở đó.

| Nhóm | Chủ đề | Câu |
|---|---|---|
| A | Tổng quan hệ thống | Q1 – Q6 |
| B | Khái niệm cốt lõi | Q7 – Q14 |
| C | Cài đặt & công cụ | Q15 – Q20 |
| D | Sử dụng hằng ngày | Q21 – Q27 |
| E | Chiến lược & mở rộng | Q28 – Q31 |
| F | Chi phí · Bảo mật · Team | Q32 – Q33 |

---

## Nhóm A — Tổng quan hệ thống

### Q1. Hệ thống này thực chất là gì?

Một **hệ thống ghi chú cá nhân do AI quản lý**. Bạn thả tài liệu thô vào, AI đọc, viết thành trang wiki có cấu trúc và tự liên kết. Nguyên tắc cốt lõi: **AI viết, bạn duyệt**.

### Q2. Nó khác gì Notion, Evernote, Google Docs?

Các app kia bắt **bạn** tự tổ chức, tự liên kết, tự dọn dẹp — nên 80% người bỏ cuộc sau vài tháng. Ở đây **AI** làm phần vận hành đó. Bạn chỉ ra quyết định và duyệt kết quả.

### Q3. Tôi sẽ có được gì sau khi học xong?

Một hệ thống nhiều kho (vault) đồng bộ, được AI quản lý: 1 kho kiến thức "Brain", các kho mở rộng (Life / 4DX / Marketing), cùng agent + skill + memory để tự động hoá việc lặp lại. Xem [README](muc-luc.md) để biết chi tiết.

### Q4. Cần biết lập trình không?

Không. Bạn chỉ cần gõ vài lệnh cơ bản (sẽ được hướng dẫn từng bước) và biết copy-paste. Không cần kiến thức lập trình.

### Q5. Mất bao lâu để chạy được?

Sau **Phần 02** (khoảng 6-10 giờ đầu) là kho Brain đã dùng được. Toàn bộ 7 phần khoảng **15-20 giờ**, trải dài 1-2 tuần. Phần 03-05 là mở rộng theo nhu cầu.

### Q6. Máy Windows / Linux có làm được không?

Được. Giáo trình ưu tiên ví dụ trên Mac nhưng có hướng dẫn cho Windows và Linux. Mọi công cụ (Obsidian, Claude Code) đều chạy đa nền tảng.

---

## Nhóm B — Khái niệm cốt lõi

### Q7. Vault là gì? Khác gì folder thường?

**Vault** là một folder bình thường nhưng được Obsidian nhận diện và xử lý đặc biệt — tạo liên kết giữa file, hiển thị sơ đồ mạng, tìm kiếm toàn văn. Hình dung: "thư mục thông minh".

### Q8. CLAUDE.md là gì? Tại sao cần?

Là file "nội quy" bạn đặt trong vault để **dạy AI hiểu kho của bạn** — dùng làm gì, theo quy tắc nào, lưu theo cấu trúc gì. Không có nó → AI mỗi lần làm mỗi kiểu → kho lộn xộn dần.

### Q9. Folder `raw/` dùng làm gì?

Chứa **tài liệu gốc** (bài viết, transcript, PDF, ghi chú thô) — đặt nguyên xi, không chỉnh sửa. AI đọc `raw/` rồi viết kết quả vào `wiki/`.

### Q10. Folder `wiki/` dùng làm gì?

Chứa **nội dung AI đã xử lý** — trang tóm tắt, khái niệm, phân tích. Bạn đọc `wiki/` để tra cứu, không cần đọc lại `raw/`.

### Q11. Mô hình 3 lớp Raw / Wiki / Schema nghĩa là gì?

- **Raw** = nguyên liệu thô · **Wiki** = trang đã viết lại, liên kết · **Schema** = quy ước đặt tên/cấu trúc (mô tả trong CLAUDE.md).

Chi tiết: [04-3-lop-raw-wiki-schema](00-triet-ly/04-3-lop-raw-wiki-schema.md).

### Q12. Wikilink là gì?

Cách liên kết giữa file bằng cú pháp `[[Tên trang]]`. Click vào là mở trang đó ngay. AI tự tạo các liên kết này khi viết wiki — bạn không làm thủ công.

### Q13. Concept-first là gì, khác gì lưu theo tài liệu?

Thay vì lưu theo nguồn (mỗi sách 1 file), ta lưu theo **khái niệm** — mỗi concept 1 trang, nhiều nguồn cùng trỏ tới. Nhờ vậy kiến thức được tổng hợp chéo. Xem [02-tai-sao-concept-first](00-triet-ly/02-tai-sao-concept-first.md).

### Q14. Markdown là gì? Cần học không?

Cách định dạng văn bản đơn giản: `#` tiêu đề, `**đậm**`, `-` danh sách. Bạn không cần học sâu — phần còn lại AI làm.

---

## Nhóm C — Cài đặt & công cụ

### Q15. Cần cài những gì tối thiểu?

Obsidian (đọc/ghi wiki) + Claude Code (AI làm việc với file). Tuỳ chọn: iCloud (đồng bộ), MCP servers, plugins. Xem Phần [01-cai-obsidian](01-cai-dat/01-cai-obsidian.md).

### Q16. Lỗi: Obsidian mở vault nhưng không thấy file?

Thường do mở nhầm folder con. Vào `File > Open vault` → chọn đúng folder gốc (chứa CLAUDE.md và các folder 00-, 01-...).

### Q17. Lỗi: gõ `claude` báo "command not found"?

Claude Code chưa cài hoặc chưa vào PATH. Kiểm tra lại [03-cai-claude-code](01-cai-dat/03-cai-claude-code.md), sau khi cài thì **đóng terminal mở lại** rồi thử.

### Q18. Lỗi: Claude báo "Not authenticated"?

Chưa đăng nhập hoặc hết phiên. Gõ `claude auth login` và làm theo hướng dẫn.

### Q19. Lỗi: vault không đồng bộ qua iCloud?

Vault chưa nằm đúng chỗ. Đường dẫn đúng trên Mac: `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/`. Di chuyển vault vào đó rồi mở lại.

### Q20. Lỗi: plugin (Dataview) không chạy sau khi cài?

Vào `Settings > Community plugins` → bật "Enable" cạnh plugin → restart Obsidian.

---

## Nhóm D — Sử dụng hằng ngày

### Q21. Tôi bảo AI "ingest file này" nhưng AI không làm gì?

(1) AI chưa đọc CLAUDE.md — nói rõ *"Đọc CLAUDE.md trước, rồi ingest raw/tên-file.md"*. (2) File không tồn tại ở đường dẫn đó — kiểm tra lại tên & thư mục.

### Q22. AI viết wiki nhưng nội dung sai so với gốc?

File raw quá dài, AI chỉ đọc được một phần. Chia nhỏ raw (~5.000-10.000 chữ/phần) và ingest từng phần.

### Q23. AI tạo nhiều file cho cùng một khái niệm?

Nói: *"Tìm tất cả file nói về X, gộp thành 1, xoá phần còn lại"*. Phòng ngừa: trước khi ingest, nhắc AI *"Kiểm tra khái niệm đã có trong wiki/ trước khi tạo file mới"*.

### Q24. Wikilink bị gãy, click không mở được?

Tên trong wikilink không khớp tên file thật (sai dấu/chính tả/hoa-thường). Trong Obsidian link gãy hiện màu khác — sửa tên file hoặc sửa wikilink.

### Q25. AI làm việc không nhất quán, mỗi lần mỗi kiểu?

Mở đầu mỗi phiên: *"Đọc CLAUDE.md của vault này trước"*. Sai chỗ nào chỉ chỗ đó và nói *"Ghi nhớ: lần sau làm kiểu X"*. Lỗi lặp nhiều → thêm rule vào CLAUDE.md.

### Q26. Làm sao hỏi AI để lấy thông tin từ kho?

Hỏi tự nhiên: *"Tổng hợp giúp tôi mọi điều đã ghi về X"*. AI đọc wiki và trả lời kèm link nguồn. Xem [08-query-wiki-dau-tien](02-vault-dau-tien-brain/08-query-wiki-dau-tien.md).

### Q27. Memory là gì, dùng khi nào?

File lưu thông tin AI cần nhớ qua các phiên (bạn là ai, quy tắc nào, dự án nào). Không có memory → mỗi lần mở mới AI quên hết. Xem [05-memory-system](04-agents-skills-memory/05-memory-system.md).

---

## Nhóm E — Chiến lược & mở rộng

### Q28. Nên ingest tài liệu gì đầu tiên?

Tài liệu **ngắn và quen thuộc** (1 bài bạn đã đọc). Tránh PDF 300 trang. Mục tiêu lần đầu: thấy quy trình chạy, chưa cần hoàn hảo.

### Q29. Kho nên lưu bao nhiêu tài liệu?

Không giới hạn kỹ thuật, nhưng **chất lượng hơn số lượng**. 50 tài liệu tóm tắt tốt > 500 tài liệu lộn xộn. Chỉ ingest thứ bạn sẽ tra cứu lại.

### Q30. Khi nào cần tách thêm vault mới?

Khi vault vượt ~**500 file** VÀ thấy khó tìm. Đừng tách sớm. Chi tiết: [01-khi-nao-tach-vault](03-mo-rong-multi-vault/01-khi-nao-tach-vault.md).

### Q31. Khi nào cần cải tổ (pivot) toàn bộ hệ thống?

Khi schema cũ liên tục cản trở (query khó, nhiều ngoại lệ). Pivot có chủ đích, đừng vá chắp vá. Xem [04-khi-nao-pivot-architecture](05-bao-tri-lint/04-khi-nao-pivot-architecture.md).

---

## Nhóm F — Chi phí · Bảo mật · Team

### Q32. Tại sao phải trả tiền Claude? Bản miễn phí được không?

Bản miễn phí giới hạn lượt hỏi và không đủ sức đọc file lớn. Để dùng Claude Code (đọc/ghi file trực tiếp) cần Pro (~$20/tháng). Hình dung: bạn đang thuê "nhân viên AI" toàn thời gian.

### Q33. Dữ liệu của tôi nằm ở đâu? Dùng cho team được không?

Vault nằm **cục bộ trên máy bạn** (folder thường), đồng bộ qua iCloud/Git tuỳ chọn — không khoá vào nền tảng nào. Hệ thống thiết kế cho **cá nhân**; cần chia sẻ thì xuất ra Google Docs/Notion hoặc dùng Git (xem [02-backup-icloud-git](05-bao-tri-lint/02-backup-icloud-git.md)).

---

## Không thấy câu trả lời ở đây?

Hỏi thẳng Claude: mô tả vấn đề + tên file đang lỗi + hành động bạn vừa làm.

Ví dụ: *"Tôi vừa gõ 'claude' trong terminal nhưng báo 'command not found'. Tôi dùng Mac, đã cài theo bước 3 nhưng vẫn lỗi. Sửa thế nào?"*

---

## 📖 Chú thích

- **vault** = kho ghi chú — một folder thông thường trên máy tính được Obsidian nhận diện và quản lý đặc biệt (tạo liên kết giữa file, tìm kiếm toàn văn, hiển thị sơ đồ mạng lưới).
- **ingest** = đưa tài liệu thô vào kho để AI đọc và xử lý thành trang wiki — gồm: đọc nội dung, rút ý chính, tạo trang tóm tắt và cập nhật trang khái niệm liên quan.
- **wikilink** = cách tạo liên kết nội bộ trong Obsidian bằng cú pháp `[[Tên trang]]`. Click vào liên kết → mở trang đó ngay. AI tự tạo các wikilink này khi viết wiki.
- **Dataview** = tiện ích mở rộng của Obsidian cho phép tạo danh sách và bảng tự động bằng cách truy vấn thông tin từ frontmatter của các file.
- **terminal** (cửa sổ dòng lệnh) = nơi bạn gõ lệnh văn bản thay vì click chuột. Trên Mac: tìm "Terminal" trong Spotlight. Trên Windows: tìm "PowerShell".

## Trước đó

[README](muc-luc.md) — Tổng quan giáo trình

## Tiếp theo

[QUICK-START](quick-start.md) — Chọn lộ trình học phù hợp
