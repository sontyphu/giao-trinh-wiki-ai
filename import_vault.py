# -*- coding: utf-8 -*-
"""Import nội dung CHUẨN từ vault Obsidian -> MkDocs docs/, chuyển [[wikilink]] -> link md,
sinh lại mkdocs.yml với nav 7 phần."""
import os, re, shutil, json

VAULT = r"C:\Users\Thanh Son\Documents\Obsidian Vault\Son's Brain\wiki\work\Đào tạo\giao-trinh-wiki-ai"
ROOT  = os.path.dirname(os.path.abspath(__file__))
DOCS  = os.path.join(ROOT, "docs")

# Root files -> tên file trên web
ROOT_REMAP = {
    "README.md":      "index.md",
    "index.md":       "muc-luc.md",
    "QUICK-START.md": "quick-start.md",
    "FAQ.md":         "faq.md",
}

SECTIONS = [
    ("00-triet-ly",              "📖 00. Triết lý"),
    ("01-cai-dat",               "⚙️ 01. Cài đặt"),
    ("02-vault-dau-tien-brain",  "🧠 02. Kho đầu tiên (Brain)"),
    ("03-mo-rong-multi-vault",   "🌳 03. Mở rộng multi-vault"),
    ("04-agents-skills-memory",  "🤖 04. Agents · Skills · Memory"),
    ("05-bao-tri-lint",          "🛠️ 05. Bảo trì"),
    ("99-templates",             "📋 99. Templates"),
]

# ---- thu thập file ----
def vault_files():
    out = []
    for dp, _, fns in os.walk(VAULT):
        for fn in fns:
            if fn.endswith(".md"):
                rel = os.path.relpath(os.path.join(dp, fn), VAULT).replace("\\", "/")
                out.append(rel)
    return out

files = vault_files()

# docs target cho 1 vault-rel-path
def target_of(rel):
    if "/" not in rel and rel in ROOT_REMAP:
        return ROOT_REMAP[rel]
    return rel

# ---- map phân giải wikilink ----
link_map = {}   # key (không .md) -> docs target path (posix)
for rel in files:
    tgt = target_of(rel)
    no_ext_vault = rel[:-3]                 # 00-triet-ly/01-...
    stem = os.path.basename(no_ext_vault)   # 01-...
    link_map[no_ext_vault] = tgt
    link_map[stem] = tgt
# alias rõ ràng cho file gốc
link_map["README"] = "index.md"
link_map["index"]  = "muc-luc.md"
link_map["QUICK-START"] = "quick-start.md"
link_map["FAQ"] = "faq.md"

# folder -> file đầu tiên (cho link dạng "00-triet-ly/")
folder_first = {}
for folder, _ in SECTIONS:
    fs = sorted([f for f in files if f.startswith(folder + "/")])
    if fs:
        folder_first[folder] = target_of(fs[0])

WIKILINK = re.compile(r"\[\[([^\]]+?)\]\]")
MDLINK   = re.compile(r"\]\(([^)]+)\)")

def relpath_posix(target, from_doc):
    base = os.path.dirname(from_doc)
    rp = os.path.relpath(target, base) if base else target
    return rp.replace("\\", "/")

def convert(content, from_doc):
    # 1) wikilink [[target]] / [[target|alias]] / [[target#heading]]
    def w(m):
        raw = m.group(1)
        alias = None
        if "|" in raw:
            raw, alias = raw.split("|", 1)
        heading = ""
        if "#" in raw:
            raw, heading = raw.split("#", 1)
        key = raw.strip().rstrip("/")
        text = (alias or os.path.basename(key)).strip()
        tgt = link_map.get(key) or link_map.get(os.path.basename(key))
        if tgt:
            href = relpath_posix(tgt, from_doc)
            if heading:
                anchor = re.sub(r"[^a-z0-9\- ]", "", heading.strip().lower()).replace(" ", "-")
                href += "#" + anchor
            return f"[{text}]({href})"
        return text  # link ngoài giáo trình -> để text

    content = WIKILINK.sub(w, content)

    # 2) link md thường: folder "xxx/" -> file đầu tiên; file gốc README/FAQ/... -> tên web
    def md(m):
        href = m.group(1)
        path, frag = (href.split("#", 1) + [""])[:2]
        path = path[2:] if path.startswith("./") else path
        bare = path.rstrip("/")
        new = None
        if path.endswith("/") and bare in folder_first:          # link tới folder
            new = folder_first[bare]
        elif path in ROOT_REMAP:                                  # README.md / FAQ.md / index.md / QUICK-START.md
            new = ROOT_REMAP[path]
        elif path[:-3] in link_map if path.endswith(".md") else False:
            new = link_map[path[:-3]]
        if new:
            rp = relpath_posix(new, from_doc)
            return "](" + rp + ("#" + frag if frag else "") + ")"
        return m.group(0)

    content = MDLINK.sub(md, content)
    return content

def title_of(content, fallback):
    m = re.search(r"^title:\s*(.+)$", content, re.M)
    if m:
        return m.group(1).strip().strip('"')
    m = re.search(r"^#\s+(.+)$", content, re.M)
    return m.group(1).strip() if m else fallback

# ---- ghi docs/ ----
if os.path.isdir(DOCS):
    shutil.rmtree(DOCS)
os.makedirs(DOCS)

titles = {}
for rel in files:
    src = os.path.join(VAULT, rel.replace("/", os.sep))
    with open(src, encoding="utf-8") as f:
        content = f.read()
    tgt = target_of(rel)
    content = convert(content, tgt)
    dst = os.path.join(DOCS, tgt.replace("/", os.sep))
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, "w", encoding="utf-8") as f:
        f.write(content)
    titles[tgt] = title_of(content, os.path.basename(tgt))
    print("  +", tgt)

# ---- assets: theme xanh đậm + menu ngang gom nhóm có dropdown ----
ASSETS = os.path.join(DOCS, "assets")
os.makedirs(ASSETS, exist_ok=True)

EXTRA_CSS = """\
/* ===== THEME XANH ĐẬM (navy) ===== */
[data-md-color-primary="blue"]{
  --md-primary-fg-color:#0d47a1;
  --md-primary-fg-color--light:#5472d3;
  --md-primary-fg-color--dark:#002171;
}
[data-md-color-accent="light blue"]{ --md-accent-fg-color:#2962ff; }
[data-md-color-scheme="slate"]{
  --md-primary-fg-color:#0d47a1;
  --md-primary-fg-color--dark:#001a5c;
}

/* ===== MENU NGANG GOM NHÓM (hover dropdown) ===== */
.tm-bar{position:sticky;top:2.4rem;z-index:5;background:var(--md-primary-fg-color--dark);
  box-shadow:0 2px 8px rgba(0,0,0,.25)}
.tm-inner{max-width:61rem;margin:0 auto;display:flex;flex-wrap:wrap;align-items:stretch;padding:0 .8rem}
@media(min-width:76.25em){ .tm-inner{max-width:none;padding:0 1.2rem} }
.tm-item{position:relative;display:flex}
.tm-link{display:flex;align-items:center;color:#fff;opacity:.92;text-decoration:none;
  font-size:.72rem;font-weight:700;line-height:1;padding:.75rem .85rem;white-space:nowrap;cursor:pointer}
.tm-link:hover{opacity:1}
.tm-has:hover .tm-link{background:rgba(255,255,255,.14)}
.tm-drop{position:absolute;top:100%;left:0;min-width:248px;background:var(--md-default-bg-color);
  border:1px solid var(--md-default-fg-color--lightest);border-radius:.2rem;
  box-shadow:0 8px 26px rgba(0,0,0,.22);padding:.3rem 0;display:none}
.tm-has:hover .tm-drop{display:block}
.tm-drop a{display:block;color:var(--md-default-fg-color);text-decoration:none;
  font-size:.72rem;padding:.5rem 1rem;line-height:1.35}
.tm-drop a:hover{background:var(--md-primary-fg-color);color:#fff}
/* mobile: bar cuộn ngang được, dropdown mở khi chạm (toggle bằng JS) */
@media(max-width:76.1875em){
  .tm-inner{flex-wrap:nowrap;overflow-x:auto}
  .tm-drop{position:static;box-shadow:none;border:0;display:none;background:rgba(255,255,255,.06)}
  .tm-item.tm-open .tm-drop{display:block}
  .tm-drop a{color:#fff}
}

/* ===== LINK / WIKILINK: xanh sáng hơn (dễ thấy trên nền trắng) ===== */
[data-md-color-scheme="default"]{ --md-typeset-a-color:#1e88e5; }
[data-md-color-scheme="slate"]{ --md-typeset-a-color:#64b5f6; }

/* ===== MENU TRÁI: đề mục phụ thụt lề + viền thể hiện là file con ===== */
.md-nav--primary .md-nav__item--nested > nav.md-nav{
  margin-left:.65rem;
  padding-left:.6rem;
  border-left:2px solid var(--md-default-fg-color--lighter);
}
.md-nav--primary .md-nav__item--nested > nav.md-nav .md-nav__link{
  font-size:.7rem;
}
/* đề mục chính: in đậm + mũi tên gập/mở nổi bật để biết bấm được */
.md-nav--primary > .md-nav__list > .md-nav__item--nested > .md-nav__link,
.md-nav--primary > .md-nav__list > .md-nav__item--nested > label.md-nav__link{
  font-weight:700;
  cursor:pointer;
}
.md-nav--primary .md-nav__item--nested > .md-nav__link .md-nav__icon{
  color:var(--md-primary-fg-color);
}
[data-md-color-scheme="slate"] .md-nav--primary .md-nav__item--nested > .md-nav__link .md-nav__icon{
  color:var(--md-accent-fg-color);
}
"""
with open(os.path.join(ASSETS, "extra.css"), "w", encoding="utf-8") as f:
    f.write(EXTRA_CSS)

# ---- dữ liệu menu (gom nhóm, FAQ cuối) ----
def diru(t):
    return "" if t == "index.md" else t[:-3] + "/"

parts_children = []
for folder, label in SECTIONS:
    if folder == "99-templates":
        continue
    fs = sorted([x for x in files if x.startswith(folder + "/")])
    if fs:
        parts_children.append({"label": label, "href": diru(target_of(fs[0]))})

tpl_children = []
for x in sorted([x for x in files if x.startswith("99-templates/")]):
    t = target_of(x)
    tpl_children.append({"label": titles.get(t, t), "href": diru(t)})

MENU = [
    {"label": "🏠 Trang chủ", "href": diru("index.md")},
    {"label": "🚀 Bắt đầu", "href": diru("quick-start.md")},
    {"label": "📚 Giáo trình", "children": parts_children},
    {"label": "📋 Templates", "children": tpl_children},
    {"label": "❓ FAQ", "href": diru("faq.md")},
]

MENU_JS = "const MENU = " + json.dumps(MENU, ensure_ascii=False) + ";\n" + """\
(function () {
  function root() {
    var l = document.querySelector('.md-header .md-logo') || document.querySelector('a.md-logo');
    return l ? l.href : (location.origin + '/');
  }
  function build() {
    var header = document.querySelector('.md-header');
    if (!header || document.querySelector('.tm-bar')) return;
    var base = root();
    var bar = document.createElement('nav'); bar.className = 'tm-bar';
    var inner = document.createElement('div'); inner.className = 'tm-inner';
    MENU.forEach(function (item) {
      var wrap = document.createElement('div');
      wrap.className = 'tm-item' + (item.children ? ' tm-has' : '');
      var a = document.createElement('a'); a.className = 'tm-link';
      a.textContent = item.label + (item.children ? '  ▾' : '');
      a.href = new URL(item.href || '', base).href;
      if (item.children) {
        a.addEventListener('click', function (e) {
          if (window.matchMedia('(max-width: 76.1875em)').matches) { e.preventDefault(); wrap.classList.toggle('tm-open'); }
        });
      }
      wrap.appendChild(a);
      if (item.children) {
        var drop = document.createElement('div'); drop.className = 'tm-drop';
        item.children.forEach(function (c) {
          var ca = document.createElement('a');
          ca.href = new URL(c.href, base).href; ca.textContent = c.label;
          drop.appendChild(ca);
        });
        wrap.appendChild(drop);
      }
      inner.appendChild(wrap);
    });
    bar.appendChild(inner);
    header.insertAdjacentElement('afterend', bar);
  }
  if (document.readyState !== 'loading') build();
  else document.addEventListener('DOMContentLoaded', build);
})();
"""
with open(os.path.join(ASSETS, "menu.js"), "w", encoding="utf-8") as f:
    f.write(MENU_JS)
print("  + assets/extra.css, assets/menu.js")

# ---- sinh mkdocs.yml ----
def nav_lines():
    L = []
    L.append("  - 🏠 Trang chủ: index.md")
    L.append("  - 🚀 Quick Start: quick-start.md")
    for folder, label in SECTIONS:
        fs = sorted([f for f in files if f.startswith(folder + "/")])
        if not fs:
            continue
        L.append(f"  - {label}:")
        for f_ in fs:
            tgt = target_of(f_)
            t = titles.get(tgt, os.path.basename(tgt)).replace('"', "'")
            L.append(f'      - "{t}": {tgt}')
    L.append("  - ❓ FAQ: faq.md")   # FAQ xuống cuối cùng
    return "\n".join(L)

MKDOCS = """\
site_name: Giáo trình Wiki AI
site_description: Xây hệ thống ghi chú AI tự quản lý với Obsidian + Claude — concept-first, multi-vault.
site_author: Son's Brain
site_url: https://sontyphu.github.io/giao-trinh-wiki-ai/
repo_url: https://github.com/sontyphu/giao-trinh-wiki-ai
repo_name: sontyphu/giao-trinh-wiki-ai
edit_uri: edit/main/docs/
docs_dir: docs
not_in_nav: |
  /muc-luc.md

theme:
  name: material
  language: vi
  palette:
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: blue
      accent: light blue
      toggle:
        icon: material/weather-night
        name: Chuyển sang tối
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: blue
      accent: light blue
      toggle:
        icon: material/weather-sunny
        name: Chuyển sang sáng
  font:
    text: Inter
    code: JetBrains Mono
  features:
    - navigation.top
    - navigation.indexes
    - navigation.footer
    - toc.follow
    - search.suggest
    - search.highlight
    - content.code.copy
    - content.action.edit

markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.highlight
  - pymdownx.tasklist:
      custom_checkbox: true
  - attr_list
  - md_in_html
  - tables
  - toc:
      permalink: true

extra_css:
  - assets/extra.css
extra_javascript:
  - assets/menu.js

nav:
""" + nav_lines() + "\n"

with open(os.path.join(ROOT, "mkdocs.yml"), "w", encoding="utf-8") as f:
    f.write(MKDOCS)

print("\nDONE — imported", len(files), "files + mkdocs.yml generated.")
