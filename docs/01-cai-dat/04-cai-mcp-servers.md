---
title: Cài MCP servers
type: cai-dat
created: 2026-05-29
updated: 2026-05-29
phan: 01
---

# Cài MCP servers

## Trước đó

[03-cai-claude-code](03-cai-claude-code.md) — Claude Code chạy được.

---

## MCP là gì

**MCP** = **Model Context Protocol** — chuẩn mở do Anthropic phát hành để LLM (Claude) kết nối với app khác qua server trung gian.

Pattern:
```
Claude ←→ MCP server ←→ External app (Gmail, Calendar, GitHub...)
```

Mỗi MCP server expose 1 set tool. Claude dùng tool đó như tool built-in.

---

## MCP cho người mới

Bạn không cần MCP để bắt đầu. Phần này là **tuỳ chọn** — bạn có thể skip và quay lại sau.

Khi nào dùng MCP:
- Cần Claude đọc/ghi Gmail
- Cần Claude xem Calendar
- Cần Claude query database (PostgreSQL, BigQuery)
- Cần Claude điều khiển browser
- Cần Claude integrate với app custom

Skip MCP nếu:
- Bạn chỉ làm Brain (knowledge wiki) — tools built-in đủ
- Bạn không có app cần kết nối ngoài

→ Khuyên: **skip section này** lần đầu đọc. Quay lại sau khi vault Brain chạy ổn.

---

## Ví dụ MCP servers phổ biến

Tham khảo các MCP server chuyên gia thường dùng cho hệ thống wiki AI đa vault:

| Server | Tác dụng |
|---|---|
| **Gmail** | Tự động đọc/gửi email |
| **Google Calendar** | Lịch họp, event |
| **Google Drive** | File sharing |
| **GitHub** | Version control, code review |
| **Zoom** | Recording, transcript meeting |
| **Meta Ads** | Performance ads |
| **Claude in Chrome** | Browser automation |
| **Slack** | Messaging tổ chức |

Mỗi server tự config riêng. Không phải tất cả đều free.

---

## Bước 1 — Xem MCP servers có sẵn

Trong Claude Code:

```
/mcp
```

Hiển thị danh sách MCP đã connect.

Mặc định Claude Code có một số MCP built-in:
- File system (đọc/ghi local)
- Bash (chạy command)
- Web fetch / web search

---

## Bước 2 — Thêm MCP server qua marketplace

Một số MCP có sẵn trong **Claude marketplace**:

1. Mở https://claude.ai/settings/connectors
2. Chọn MCP muốn cài (vd: Google Calendar)
3. Click **Connect**
4. Authorize quyền truy cập

Sau khi authorize, MCP server xuất hiện trong list `/mcp` của Claude Code.

---

## Bước 3 — Thêm MCP server qua config file

MCP custom cài qua file:

```
~/.claude/mcp.json
```

Format:

```json
{
  "mcpServers": {
    "my-custom-app": {
      "command": "npx",
      "args": ["-y", "@myorg/mcp-server"],
      "env": {
        "API_KEY": "your-key-here"
      }
    }
  }
}
```

Sau khi save, restart Claude Code → MCP server load.

---

## Bước 4 — Verify MCP

Trong Claude Code:

```
> Có MCP nào kết nối?
```

Claude liệt kê. Hoặc:

```
/mcp
```

Test 1 tool:

```
> Đọc email mới nhất của tôi
```

Claude dùng MCP Gmail (nếu đã connect) trả về.

---

## Bước 5 — Tránh quá nhiều MCP

Mỗi MCP cộng thêm context. Nhiều MCP = Claude chậm + token đắt.

Khuyên:
- Bắt đầu: 0 MCP. Dùng tools built-in.
- Khi cần app cụ thể → add 1 MCP đó.
- Đừng cài cho có.

---

## Bước 6 — Disable MCP tạm thời

Nếu MCP gây lỗi, disable qua config:

```json
{
  "mcpServers": {
    "my-custom-app": {
      "disabled": true
    }
  }
}
```

Restart Claude Code.

---

## Khi nào dùng MCP marketplace vs config

| Trường hợp | Cách cài |
|---|---|
| MCP phổ thông (Google, GitHub, Slack) | Marketplace (1 click) |
| MCP custom của bạn (app nội bộ) | Config file |
| MCP đang dev (chưa publish) | Config file |
| Chỉ muốn cho 1 vault | `.claude/mcp.json` trong vault |

---

## Ví dụ MCP custom — app CRM nội bộ

Nếu bạn có CRM hay hệ thống quản lý đơn hàng riêng, có thể viết MCP server kết nối API:

Config trong `~/.claude/mcp.json`:

```json
{
  "mcpServers": {
    "my-crm": {
      "command": "node",
      "args": ["/path/to/my-crm-mcp/dist/index.js"],
      "env": {
        "CRM_API_TOKEN": "...",
        "CRM_SHOP_ID": "..."
      }
    }
  }
}
```

Khi vault Marketing query "đơn nào chốt tuần này?", Claude dùng MCP CRM auto pull data.

---

## 📖 Chú thích

- **vault** = kho ghi chú — một folder thông thường trên máy tính được Obsidian nhận diện và quản lý đặc biệt (tạo liên kết giữa file, tìm kiếm toàn văn, hiển thị sơ đồ mạng lưới).
- **MCP Server** (Model Context Protocol) = phần mềm cầu nối giúp AI Claude kết nối và làm việc trực tiếp với ứng dụng khác (Gmail, Google Drive, Slack, lịch...) mà không cần copy-paste thủ công.
- **Dataview** = tiện ích mở rộng của Obsidian cho phép tạo danh sách và bảng tự động bằng cách truy vấn thông tin từ frontmatter của các file. Ví dụ: "liệt kê tất cả trang có type = concept theo thứ tự ngày tạo".

## Tiếp theo

Đọc tiếp: [05-cai-plugins-obsidian](05-cai-plugins-obsidian.md) — Cài plugin Obsidian (Web Clipper, Dataview, Excalidraw).
