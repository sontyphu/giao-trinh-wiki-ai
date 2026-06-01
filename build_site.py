# -*- coding: utf-8 -*-
"""Generator: tạo cấu trúc MkDocs cho Giáo trình Wiki AI (tông xanh)."""
import os, textwrap

ROOT = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(ROOT, "docs")

def w(relpath, content):
    path = os.path.join(DOCS, relpath)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(textwrap.dedent(content).lstrip("\n"))
    print("  +", relpath)

def nxt(label, link):
    return f"\n\n---\n\n[Tiếp theo: {label} →]({link})\n"

# ----------------------------------------------------------------------------
# HOME
# ----------------------------------------------------------------------------
w("index.md", """
    # 📚 Giáo trình Wiki AI

    > Xây hệ thống wiki cá nhân **AI-first** với Obsidian + Claude — từ triết lý nền tảng
    > đến vault chạy thật và đa vault.

    Biến mớ ghi chú rời rạc thành một **"bộ não thứ hai"** có AI đọc, viết và kết nối tri thức
    tự động. Bạn đổ nguyên liệu thô vào, AI viết bản nháp có cấu trúc, bạn duyệt.

    ## Bắt đầu nhanh

    [🚀 Quick Start — chạy trong 15 phút](quick-start.md){ .md-button .md-button--primary }
    [📖 Đọc từ triết lý](00-triet-ly/01-tai-sao-ai-first.md){ .md-button }

    ## Lộ trình 7 phần

    | Phần | Nội dung |
    |------|----------|
    | **00 · Triết lý** | Vì sao AI-first, concept-first, multi-vault, 3 lớp Raw/Wiki/Schema |
    | **01 · Cài đặt** | Obsidian, iCloud sync, Claude Code, MCP servers, plugins |
    | **02 · Vault Brain** | Tạo bộ não đầu tiên — template, ingest, query |
    | **03 · Multi-vault** | Tách vault Life / 4DX / Marketing, cross-vault query |
    | **04 · Agents-Skills** | Tự động hoá: agent, skill, memory |
    | **05 · Bảo trì** | Lint, backup, migrate, pivot architecture |
    | **99 · Templates** | Bộ mẫu copy-paste dùng ngay |

    !!! tip "Cốt lõi"
        Bạn không "chép" kiến thức nữa. Bạn *nuôi* một bộ não số: đổ Raw vào → AI tiêu hoá
        thành Wiki theo Schema → bạn duyệt & dùng.
""")

# ----------------------------------------------------------------------------
# QUICK START
# ----------------------------------------------------------------------------
w("quick-start.md", """
    # 🚀 Quick Start — chạy trong 15 phút

    Ba bước tối thiểu để có một vault Wiki AI hoạt động ngay.

    1. Cài **Obsidian** (miễn phí) — nơi chứa & đọc wiki, có graph view và `[[wikilink]]`.
    2. Cài **Claude Code CLI** (cần tài khoản Anthropic Pro ~$20/tháng) — AI đọc nguyên liệu, viết wiki.
    3. Copy `CLAUDE.md` template vào vault — đặt "luật chơi" để AI biết cách viết.

    !!! warning "Vault giáo trình ≠ vault của bạn"
        Folder giáo trình này chỉ để **tham khảo**. Học xong, bạn tạo vault MỚI cho riêng mình.
""" + nxt("Tại sao AI-first wiki", "00-triet-ly/01-tai-sao-ai-first.md"))

# ----------------------------------------------------------------------------
# 00 — TRIẾT LÝ
# ----------------------------------------------------------------------------
w("00-triet-ly/01-tai-sao-ai-first.md", """
    # 1. Tại sao AI-first wiki

    Wiki truyền thống bắt *con người* vừa thu thập vừa viết — tốn sức nên bỏ dở.
    Wiki AI-first đảo vai: **bạn đổ nguyên liệu thô, AI viết bản nháp có cấu trúc, bạn duyệt**.

    Chi phí duy trì giảm mạnh, kho tri thức mới sống được lâu dài.

    ## Vòng lặp cốt lõi

    1. **Đổ** nguyên liệu (bài web, transcript, ghi chú) vào `raw/`.
    2. **AI viết** lại thành trang wiki có cấu trúc, liên kết.
    3. **Bạn duyệt** — sửa, xác nhận, dùng.
""" + nxt("Tại sao concept-first", "02-tai-sao-concept-first.md"))

w("00-triet-ly/02-tai-sao-concept-first.md", """
    # 2. Tại sao concept-first

    Thay vì lưu theo "nguồn" (mỗi cuốn sách một file), ta lưu theo **khái niệm**:
    mỗi concept một trang, được nhiều nguồn cùng trỏ tới.

    Kết quả là kiến thức *tổng hợp chéo* — một concept gom hiểu biết từ 10 nguồn khác nhau,
    liên kết bằng `[[wikilink]]`.
""" + nxt("Tại sao multi-vault", "03-tai-sao-multi-vault.md"))

w("00-triet-ly/03-tai-sao-multi-vault.md", """
    # 3. Tại sao multi-vault

    Một vault khổng lồ trộn lẫn công việc, đời sống, marketing sẽ rối và chậm.

    Tách thành nhiều vault theo **ngữ cảnh** (Brain, Life, Work...) giúp AI tập trung
    đúng phạm vi, schema gọn, query nhanh.
""" + nxt("3 lớp Raw / Wiki / Schema", "04-ba-lop-raw-wiki-schema.md"))

w("00-triet-ly/04-ba-lop-raw-wiki-schema.md", """
    # 4. Ba lớp Raw / Wiki / Schema

    - **Raw** — nguyên liệu thô chưa xử lý (bài web, transcript, ghi chú nhanh).
    - **Wiki** — trang đã được AI viết lại có cấu trúc, liên kết (concepts, sources).
    - **Schema** — quy ước về cách đặt tên, frontmatter, folder — "khung xương" giữ vault nhất quán.

    !!! tip "Cốt lõi"
        Đổ Raw vào → AI tiêu hoá thành Wiki theo Schema → bạn duyệt & dùng.
""" + nxt("Cài Obsidian", "../01-cai-dat/01-cai-obsidian.md"))

# ----------------------------------------------------------------------------
# 01 — CÀI ĐẶT
# ----------------------------------------------------------------------------
w("01-cai-dat/01-cai-obsidian.md", """
    # 1. Cài Obsidian

    Tải tại [obsidian.md](https://obsidian.md), cài như app thường.

    Obsidian đọc thẳng các file `.md` trong một folder (gọi là "vault") — dữ liệu của bạn
    nằm cục bộ, không khoá vào nền tảng nào.
""" + nxt("Cài iCloud sync", "02-cai-icloud-sync.md"))

w("01-cai-dat/02-cai-icloud-sync.md", """
    # 2. Cài iCloud sync

    Đặt vault trong iCloud Drive để đồng bộ giữa máy tính và iPhone/iPad — đọc & ghi mọi nơi.

    > Windows có thể thay bằng OneDrive hoặc Git.
""" + nxt("Cài Claude Code", "03-cai-claude-code.md"))

w("01-cai-dat/03-cai-claude-code.md", """
    # 3. Cài Claude Code

    Cài Claude Code CLI và đăng nhập tài khoản Anthropic Pro.

    Đây là "người viết wiki": nó đọc file trong vault, hiểu schema từ `CLAUDE.md`,
    rồi viết/sửa trang theo yêu cầu.
""" + nxt("Cài MCP servers", "04-cai-mcp-servers.md"))

w("01-cai-dat/04-cai-mcp-servers.md", """
    # 4. Cài MCP servers

    MCP (Model Context Protocol) cho AI kết nối công cụ ngoài: đọc web, truy cập Google Drive,
    lấy transcript YouTube...

    Mỗi server mở thêm một "giác quan" cho AI khi xây vault.
""" + nxt("Cài plugins Obsidian", "05-cai-plugins-obsidian.md"))

w("01-cai-dat/05-cai-plugins-obsidian.md", """
    # 5. Cài plugins Obsidian

    - **Dataview** — truy vấn và liệt kê trang theo metadata (như "SQL cho vault").
    - **Web Clipper** — lưu nhanh bài web vào folder `raw/`.
""" + nxt("Tạo vault Brain", "../02-vault-brain/01-tao-vault-brain.md"))

# ----------------------------------------------------------------------------
# 02 — VAULT BRAIN
# ----------------------------------------------------------------------------
brain = [
 ("01-tao-vault-brain", "1. Tạo vault Brain",
  "Tạo một folder MỚI (vd `My Brain`), mở bằng Obsidian. Đây là vault tri thức của bạn — "
  "**khác** với vault giáo trình (chỉ để tham khảo).", "02-claude-md-template", "CLAUDE.md template"),
 ("02-claude-md-template", "2. CLAUDE.md template",
  "File `CLAUDE.md` ở gốc vault là \"hiến pháp\": mô tả mục đích vault, schema, quy ước đặt tên, "
  "cách AI ingest và viết. Copy từ template rồi chỉnh theo phong cách bạn.", "03-cau-truc-folder", "Cấu trúc folder"),
 ("03-cau-truc-folder", "3. Cấu trúc folder",
  "Tối thiểu: `raw/` (nguyên liệu), `wiki/sources/` (trang nguồn), `wiki/concepts/` (trang khái niệm). "
  "Có thể thêm `moc/` (bản đồ nội dung) và `templates/`.", "04-concept-page-template", "Concept page template"),
 ("04-concept-page-template", "4. Concept page template",
  "Mỗi khái niệm một trang: định nghĩa ngắn → giải thích → ví dụ → liên kết tới concept liên quan "
  "và nguồn đã trích. Đây là đơn vị tri thức tái dùng được.", "05-source-page-template", "Source page template"),
 ("05-source-page-template", "5. Source page template",
  "Mỗi nguồn (sách, video, bài) một trang: metadata (tác giả, link, ngày) + tóm tắt + các điểm chính, "
  "mỗi điểm trỏ tới concept tương ứng.", "06-course-moc-template", "Course MOC template"),
 ("06-course-moc-template", "6. Course MOC template",
  "MOC (Map of Content) cho một khoá học/chủ đề: trang mục lục gom các concept và source liên quan "
  "thành một lộ trình đọc mạch lạc.", "07-ingest-source-dau-tien", "Ingest source đầu tiên"),
 ("07-ingest-source-dau-tien", "7. Ingest source đầu tiên",
  "Bỏ 3–5 nguyên liệu vào `raw/`, bảo Claude \"ingest\" → AI đọc, tạo source page, rút concept, "
  "viết concept page và nối `[[wikilink]]` tự động.", "08-query-wiki-dau-tien", "Query wiki đầu tiên"),
 ("08-query-wiki-dau-tien", "8. Query wiki đầu tiên",
  "Hỏi Claude một câu dựa trên vault (\"tổng hợp giúp tôi mọi điều đã ghi về X\"). "
  "Trải nghiệm vòng lặp **\"AI viết — bạn duyệt\"**: đây là khoảnh khắc vault bắt đầu trả lãi.",
  "../03-multi-vault/01-khi-nao-tach-vault", "Khi nào tách vault"),
]
for slug, title, body, nslug, nlabel in brain:
    w(f"02-vault-brain/{slug}.md", f"# {title}\n\n{body}" + nxt(nlabel, f"{nslug}.md"))

# ----------------------------------------------------------------------------
# 03 — MULTI-VAULT
# ----------------------------------------------------------------------------
multi = [
 ("01-khi-nao-tach-vault", "1. Khi nào tách vault",
  "Tách khi nội dung khác *mục đích* và khác *schema* (vd kiến thức học thuật vs theo dõi đời sống). "
  "Đừng tách quá sớm — bắt đầu một vault, tách khi thấy rõ ranh giới.", "02-vault-life", "Vault Life"),
 ("02-vault-life", "2. Vault Life (lifestyle)",
  "Theo dõi đời sống: sức khoẻ, tài sản (xe, thú cưng...), thói quen. "
  "Schema thiên về dữ liệu lặp và timeline thay vì khái niệm.", "03-vault-4dx", "Vault 4DX"),
 ("03-vault-4dx", "3. Vault 4DX (execution)",
  "Quản trị mục tiêu theo 4 Disciplines of Execution: WIG (mục tiêu tối quan trọng), lead measures, "
  "scoreboard, nhịp cam kết. Vault này lo OKR và thực thi.", "04-vault-marketing", "Vault Marketing"),
 ("04-vault-marketing", "4. Vault Marketing",
  "Quản lý tài sản marketing: campaign, content, swipe file, theo dõi hiệu suất. "
  "Tách riêng để AI tập trung đúng ngữ cảnh kinh doanh.", "05-cross-vault-query", "Cross-vault query"),
 ("05-cross-vault-query", "5. Cross-vault query",
  "Cho AI truy vấn xuyên nhiều vault để tổng hợp góc nhìn (vd nối kiến thức ở Brain với mục tiêu ở 4DX) "
  "mà vẫn giữ mỗi vault gọn gàng.", "../04-agents-skills/01-agent-la-gi", "Agent là gì"),
]
for slug, title, body, nslug, nlabel in multi:
    w(f"03-multi-vault/{slug}.md", f"# {title}\n\n{body}" + nxt(nlabel, f"{nslug}.md"))

# ----------------------------------------------------------------------------
# 04 — AGENTS-SKILLS
# ----------------------------------------------------------------------------
agents = [
 ("01-agent-la-gi", "1. Agent là gì",
  "Agent là một \"nhân vật AI\" có vai trò và phạm vi riêng (vd Agent biên tập, Agent nghiên cứu). "
  "Giao việc cho đúng agent giúp kết quả nhất quán hơn là một prompt chung chung.", "02-tao-agent-dau-tien", "Tạo agent đầu tiên"),
 ("02-tao-agent-dau-tien", "2. Tạo agent đầu tiên",
  "Định nghĩa agent bằng một file system prompt: vai trò, nguyên tắc, định dạng output. "
  "Sau đó gọi agent này mỗi khi cần đúng loại việc đó.", "03-skill-la-gi", "Skill là gì"),
 ("03-skill-la-gi", "3. Skill là gì",
  "Skill là một quy trình đóng gói (hướng dẫn + template + tham chiếu) cho một tác vụ cụ thể — "
  "ví dụ \"ingest source\" hay \"lint vault\" — để AI làm theo chuẩn mỗi lần.", "04-tao-skill-dau-tien", "Tạo skill đầu tiên"),
 ("04-tao-skill-dau-tien", "4. Tạo skill đầu tiên",
  "Viết một `SKILL.md`: mô tả khi nào dùng, các bước thực hiện, mẫu output. "
  "Skill tốt = mô tả kích hoạt rõ + các bước lặp lại được.", "05-memory-system", "Memory system"),
 ("05-memory-system", "5. Memory system",
  "Lưu các sự thật bền vững (sở thích, quy ước, bối cảnh dự án) để AI nhớ qua nhiều phiên — "
  "tránh phải lặp lại bối cảnh mỗi lần.", "../05-bao-tri/01-lint-dinh-ky", "Lint wiki định kỳ"),
]
for slug, title, body, nslug, nlabel in agents:
    w(f"04-agents-skills/{slug}.md", f"# {title}\n\n{body}" + nxt(nlabel, f"{nslug}.md"))

# ----------------------------------------------------------------------------
# 05 — BẢO TRÌ
# ----------------------------------------------------------------------------
baotri = [
 ("01-lint-dinh-ky", "1. Lint wiki định kỳ",
  "Định kỳ cho AI rà: link gãy, trang mồ côi, frontmatter thiếu, concept trùng. "
  "Lint giữ vault khỏi \"mục\" theo thời gian.", "02-backup-icloud-git", "Backup iCloud + Git"),
 ("02-backup-icloud-git", "2. Backup iCloud + Git",
  "Hai lớp an toàn: iCloud cho sync tức thời, Git cho lịch sử phiên bản (rollback khi lỡ tay). "
  "Vault là tài sản — sao lưu nghiêm túc.", "03-migrate-rename-vault", "Migrate / rename vault"),
 ("03-migrate-rename-vault", "3. Migrate / rename vault",
  "Khi đổi tên hoặc di chuyển vault, cập nhật đường dẫn và wikilink một cách có kiểm soát "
  "để không vỡ liên kết.", "04-khi-nao-pivot", "Khi nào pivot architecture"),
 ("04-khi-nao-pivot", "4. Khi nào pivot architecture",
  "Khi schema cũ liên tục cản trở (query khó, nhiều ngoại lệ), đó là tín hiệu nên tái cấu trúc. "
  "Pivot có chủ đích, đừng vá chắp vá.", "../99-templates/index", "Templates copy-paste"),
]
for slug, title, body, nslug, nlabel in baotri:
    w(f"05-bao-tri/{slug}.md", f"# {title}\n\n{body}" + nxt(nlabel, f"{nslug}.md"))

# ----------------------------------------------------------------------------
# 99 — TEMPLATES
# ----------------------------------------------------------------------------
w("99-templates/index.md", """
    # 📋 Templates copy-paste

    Bộ mẫu dùng ngay — không phải viết lại từ đầu.

    | Template | Dùng cho |
    |----------|----------|
    | **CLAUDE.md master** | Hiến pháp cho vault |
    | **Concept page** | Khung trang khái niệm |
    | **Source page** | Khung trang nguồn |
    | **Course MOC** | Bản đồ nội dung khoá học |
    | **log.md** | Nhật ký thay đổi vault |
    | **index.md** | Mục lục vault |

    !!! warning "Lưu ý quan trọng"
        Vault "giáo trình" ≠ vault tri thức của bạn. Học xong, tạo vault MỚI cho riêng mình;
        vault giáo trình chỉ để tra cứu khi gặp vướng.
""")

print("\nDONE — docs/ generated.")
