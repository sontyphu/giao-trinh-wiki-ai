---
title: Vault 4DX — execution layer
type: huong-dan
created: 2026-05-29
updated: 2026-05-29
phan: 03
---

# Vault 4DX — execution layer

## Trước đó

[02-vault-life-lifestyle](02-vault-life-lifestyle.md) — vault Life chạy được.

---

## 4DX là gì

**4DX** = **4 Disciplines of Execution** (Chris McChesney, Sean Covey, Jim Huling — sách 2012):

1. **mục tiêu tối quan trọng** — Wildly Important Goal (mục tiêu tối thượng)
2. **Lead measures** — Thước đo đòn bẩy (action drive mục tiêu tối quan trọng)
3. **Scoreboard** — Bảng điểm hiển thị
4. **Cadence** — Phiên họp nhịp

Ví dụ 4 mục tiêu tối quan trọng điển hình của chuyên gia đào tạo:

| # | mục tiêu tối quan trọng |
|---|---|
| 1 | Thời gian chất lượng cho gia đình |
| 2 | Cộng đồng thành viên đạt mục tiêu N |
| 3 | Hoàn thành Ironman sub-14 + BQ |
| 4 | Doanh thu đào tạo |

---

## Vault 4DX = META layer

KHÔNG phải knowledge. KHÔNG phải lifestyle. KHÔNG phải production.

Vault 4DX = **trung tâm điều hành** tổng hợp data từ 2-3 vault input → generate báo cáo Xanh/Vàng/Đỏ.

```
Life/4dx/         Marketing/4dx/
   │                  │
   ├── 1-wig.md       ├── 1-wig.md
   ├── 2-lead.md      ├── 2-lead.md
   ├── 3-scoreboard   ├── 3-scoreboard
   ├── 4-cadence      ├── 4-cadence
   └── actions/W22    └── actions/W22
       │                  │
       └───────┬──────────┘
               ▼
        tác vụ lệnh tự động theo lịch đêm CN scan
               │
               ▼
      My 4DX/reviews/weekly/W22.md
        + email + PDF + xlsx
```

---

## Khi nào setup 4DX

Setup 4DX nếu:
- Bạn có 3-5 mục tiêu tối quan trọng 2026 rõ ràng
- Bạn nhập action daily được 4-6 tuần ổn định
- Bạn cần báo cáo tuần tự động, không phải tự tổng hợp

Skip 4DX nếu:
- Bạn không track OKR
- Action đời thường không đo được
- Mới setup vault tuần đầu, chưa cần auto

→ Khuyên: skip lần đầu. Quay lại sau khi vault Brain + Life chạy 3-6 tháng.

---

## Bước 1 — Identify mục tiêu tối quan trọng

Liệt 3-5 mục tiêu tối quan trọng năm nay:

- mục tiêu tối quan trọng 1: ?
- mục tiêu tối quan trọng 2: ?
- ...

Quy tắc mục tiêu tối quan trọng:
- Đo được số (dollar, member, hour, km)
- Có deadline (end of year, Q4)
- Quan trọng nhất — không phải nice-to-have

Vd:
- mục tiêu tối quan trọng 1: "Doanh thu cá nhân $200k năm nay"
- mục tiêu tối quan trọng 2: "Marathon dưới 4 giờ trước 31/12"
- mục tiêu tối quan trọng 3: "Đọc 24 sách hết năm"

---

## Bước 2 — Map mục tiêu tối quan trọng vào vault

Mỗi mục tiêu tối quan trọng nằm ở vault nào tuỳ context:

| mục tiêu tối quan trọng | Vault input |
|---|---|
| mục tiêu tối quan trọng về gia đình / sức khoẻ / hobby | Life |
| mục tiêu tối quan trọng về business / revenue / marketing | Marketing |
| mục tiêu tối quan trọng về knowledge / đọc sách | Brain |

---

## Bước 3 — Setup 4dx/ subfolder mỗi vault input

Trong Life vault:

```bash
cd "My Life"
mkdir -p 4dx/actions
cd 4dx
touch 1-wig.md 2-lead-measures.md 3-scoreboard.md 4-cadence.md
```

### `1-wig.md` (Life)

```
---
type: wig-list
updated: 2026-05-29
---

# mục tiêu tối quan trọng — Life vault

| # | mục tiêu tối quan trọng | Target | Deadline |
|---|---|---|---|
| 2 | Marathon dưới 4 giờ | 3h59 | 2026-12-31 |
```

### `2-lead-measures.md` (Life)

```
---
type: lead-measures
updated: 2026-05-29
---

# Lead Measures — Life vault

## mục tiêu tối quan trọng 2 — Marathon

Metric đòn bẩy:

| Metric | Đơn vị | Target/tuần |
|---|---|---|
| training_hours | giờ | 8 |
| long_run_km | km | 25 |
| tempo_run_min | phút | 45 |
| strength_session | session | 2 |
```

### `actions/2026-W22-actions.md` (Life)

```
# Actions — Life W22

## T2 25/05/2026

### Sáng
- [x] 05:00-07:00 | wig=2 | metric=training_hours | val=2 | activity="Long run 25km Z2"

### Chiều
- [x] 14:00-15:30 | wig=1 | metric=family_hours | val=1.5 | activity="Đi siêu thị vợ"

### Tối
- [x] 19:00-20:30 | wig=1 | metric=family_hours | val=1.5 | activity="Cơm tối gia đình"
- [ ] 21:00-23:00 | wig=NONE | val=2 | activity="Xem YouTube" -- off-plan
```

---

## Bước 4 — Tạo vault 4DX

```bash
cd "/Users/$USER/Library/Mobile Documents/iCloud~md~obsidian/Documents"
mkdir "My 4DX"
cd "My 4DX"
mkdir -p wig reviews/weekly scoreboard scripts raw/{from-life,from-marketing}
touch CLAUDE.md README.md index.md log.md now.md
```

---

## Bước 5 — CLAUDE.md cho 4DX

Template:

```
# CLAUDE.md — Luật chơi vault "My 4DX"

Vault này là META layer trên Life + Marketing. Đêm CN tác vụ lệnh tự động theo lịch (tự động theo lịch) tự scan 2 vault → generate báo cáo Xanh/Vàng/Đỏ → output sáng T2.

KHÔNG knowledge. KHÔNG lifestyle. KHÔNG production. **Trung tâm điều hành**.

## 1. Chủ vault

[Tên bạn] — [năm sinh + role].

## 2. Mô hình 2 vault input + 1 vault tổng hợp

[Diagram customize số mục tiêu tối quan trọng của bạn]

## 3. mục tiêu tối quan trọng năm nay — mapping vault

| # | mục tiêu tối quan trọng | Vault input | Lead measure file |
|---|---|---|---|
| 1 | Family time | Life | `Life/4dx/2-lead-measures.md` |
| 2 | Marathon | Life | `Life/4dx/2-lead-measures.md` |
| 3 | Revenue $200k | Marketing | `Marketing/4dx/2-lead-measures.md` |

## 4. Action log convention

Format inline metadata:

```
- [x] HH:MM-HH:MM | wig=N | metric=<name> | val=<number> | activity="..."
```

Tag `wig=`:
- `wig=1` đến `wig=N` → đẩy mục tiêu tối quan trọng
- `wig=NONE` → off-plan
- `wig=whirlwind` → daily ops, không tính

## 5. Logic traffic light

Per mục tiêu tối quan trọng:
- Xanh: lead hit ≥80% target + off-plan ≤10%
- Vàng: lead hit 50-80% hoặc off-plan 10-25%
- Đỏ: lead hit <50% hoặc off-plan >25%

## 6. Cron đêm CN (tác vụ tự động)

CN 23:30 → lệnh tự động theo lịch fire → script scan 2 vault → generate review → email + PDF + xlsx.

T2 04:00 backup lệnh tự động theo lịch nếu CN miss.

## 7. Workflow daily

Tối 21:00 nhập actions (10 phút).
Sáng T2 đọc review (5 phút).
```

---

## Bước 6 — Script scan (Python)

Tạo `scripts/scan_4dx.py`:

```python
#!/usr/bin/env python3
"""Scan Life + Marketing 4dx/actions/ → generate review tuần."""

import re
import os
from datetime import datetime, timedelta
from pathlib import Path
from collections import defaultdict

VAULT_LIFE = Path("/Users/<you>/Library/Mobile Documents/iCloud~md~obsidian/Documents/My Life")
VAULT_MKT = Path("/Users/<you>/Library/Mobile Documents/iCloud~md~obsidian/Documents/My Marketing")
VAULT_4DX = Path("/Users/<you>/Library/Mobile Documents/iCloud~md~obsidian/Documents/My 4DX")

def current_week():
    """Trả về string 'YYYY-Www'."""
    now = datetime.now()
    iso = now.isocalendar()
    return f"{iso.year}-W{iso.week:02d}"

def parse_actions(path):
    """Parse file actions, trả list dict {wig, metric, val, activity}."""
    actions = []
    if not path.exists():
        return actions
    pattern = re.compile(
        r'- \[(x| )\] .*?\| wig=(\w+) \| metric=([\w_]+) \| val=([\d.]+) \| activity="(.*)"'
    )
    for line in path.read_text().splitlines():
        m = pattern.search(line)
        if m:
            done, wig, metric, val, activity = m.groups()
            actions.append({
                'done': done == 'x',
                'wig': wig,
                'metric': metric,
                'val': float(val),
                'activity': activity,
            })
    return actions

def aggregate(actions):
    """Aggregate theo wig + metric."""
    agg = defaultdict(lambda: defaultdict(float))
    off_plan = 0
    total = 0
    for a in actions:
        if not a['done']:
            continue
        total += 1
        if a['wig'] == 'NONE':
            off_plan += 1
        elif a['wig'] != 'whirlwind':
            agg[a['wig']][a['metric']] += a['val']
    off_plan_ratio = off_plan / total if total > 0 else 0
    return agg, off_plan_ratio

def traffic_light(agg, off_plan_ratio, targets):
    """Trả về xanh/vàng/đỏ per mục tiêu tối quan trọng."""
    results = {}
    for wig, metrics in agg.items():
        hit_count = 0
        total_metrics = len(targets.get(wig, {}))
        for metric, target in targets.get(wig, {}).items():
            actual = metrics.get(metric, 0)
            if actual >= target * 0.8:
                hit_count += 1
        hit_ratio = hit_count / total_metrics if total_metrics > 0 else 0
        if hit_ratio >= 0.8 and off_plan_ratio <= 0.1:
            results[wig] = 'XANH'
        elif hit_ratio >= 0.5 or off_plan_ratio <= 0.25:
            results[wig] = 'VANG'
        else:
            results[wig] = 'DO'
    return results

def generate_review(week):
    """Generate review markdown."""
    life_actions = parse_actions(VAULT_LIFE / "4dx/actions" / f"2026-{week}-actions.md")
    mkt_actions = parse_actions(VAULT_MKT / "4dx/actions" / f"2026-{week}-actions.md")
    
    all_actions = life_actions + mkt_actions
    agg, off_plan = aggregate(all_actions)
    
    # Targets — customize
    targets = {
        '1': {'family_hours': 14},
        '2': {'training_hours': 8, 'long_run_km': 25},
        '3': {'revenue_usd': 4000},
    }
    lights = traffic_light(agg, off_plan, targets)
    
    output_path = VAULT_4DX / "reviews/weekly" / f"2026-{week}-review.md"
    content = f"""# Review {week}

Generated: {datetime.now().isoformat()}

## Traffic light per mục tiêu tối quan trọng

| mục tiêu tối quan trọng | Màu |
|---|---|
"""
    for wig in sorted(lights.keys()):
        content += f"| mục tiêu tối quan trọng {wig} | {lights[wig]} |\n"
    
    content += f"\n## Off-plan ratio: {off_plan*100:.1f}%\n"
    content += "\n## Aggregate metrics\n\n"
    for wig in sorted(agg.keys()):
        content += f"### mục tiêu tối quan trọng {wig}\n"
        for metric, val in agg[wig].items():
            content += f"- {metric}: {val:.1f}\n"
        content += "\n"
    
    output_path.write_text(content)
    print(f"Wrote {output_path}")

if __name__ == '__main__':
    week = current_week()
    generate_review(week)
```

Test thủ công:

```bash
python scripts/scan_4dx.py
```

---

## Bước 7 — Setup lệnh tự động theo lịch (launchd macOS)

Tác vụ tự động theo lịch (lệnh tự động theo lịch) trên macOS dùng launchd. Tạo `scripts/com.you.4dx-weekly.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" 
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>com.you.4dx-weekly</string>
  
  <key>ProgramArguments</key>
  <array>
    <string>/usr/bin/env</string>
    <string>python3</string>
    <string>/Users/you/Library/Mobile Documents/iCloud~md~obsidian/Documents/My 4DX/scripts/scan_4dx.py</string>
  </array>
  
  <key>StartCalendarInterval</key>
  <dict>
    <key>Weekday</key>
    <integer>0</integer>
    <key>Hour</key>
    <integer>23</integer>
    <key>Minute</key>
    <integer>30</integer>
  </dict>
  
  <key>StandardOutPath</key>
  <string>/Users/you/Library/Logs/4dx-weekly.log</string>
  <key>StandardErrorPath</key>
  <string>/Users/you/Library/Logs/4dx-weekly.error.log</string>
</dict>
</plist>
```

Install:

```bash
cp scripts/com.you.4dx-weekly.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.you.4dx-weekly.plist
```

Verify:

```bash
launchctl list | grep com.you.4dx
```

Disable tạm:

```bash
launchctl unload ~/Library/LaunchAgents/com.you.4dx-weekly.plist
```

---

## Bước 8 — Output 4 channel

Sau khi lệnh tự động theo lịch generate review markdown, script còn:

1. **Markdown** trong vault (done)
2. **Email** gửi qua Gmail (cần MCP Gmail hoặc Python smtplib)
3. **PDF** in giấy (pandoc convert md → PDF)
4. **xlsx** dashboard (openpyxl)

Code email + PDF + xlsx — phức tạp hơn, xem script mẫu để tham khảo full.

---

## Bước 9 — Workflow daily

Tối 21:00 (10 phút):
- Mở `My Life/4dx/actions/2026-W22-actions.md` hoặc `My Marketing/4dx/actions/2026-W22-actions.md`
- Thêm action đã làm hôm nay

Sáng T2 (5 phút):
- Mở `My 4DX/reviews/weekly/2026-W22-review.md`
- Đọc traffic light
- Xanh → tiếp tục
- Vàng → adjust DMO
- Đỏ → reflection + hỏi accountability partner

---

## Bước 10 — Khi không chắc

- Action không biết mục tiêu tối quan trọng → `wig=whirlwind` (daily ops)
- Tuần lỡ không nhập → lệnh tự động theo lịch vẫn chạy, flag "data sparse" + treat as đỏ
- Metric mới → thêm vào `2-lead-measures.md` trước, rồi log action

---

## 📖 Chú thích

- **vault** = kho ghi chú — một folder thông thường trên máy tính được Obsidian nhận diện và quản lý đặc biệt (tạo liên kết giữa file, tìm kiếm toàn văn, hiển thị sơ đồ mạng lưới).
- **MCP Server** (Model Context Protocol) = phần mềm cầu nối giúp AI Claude kết nối và làm việc trực tiếp với ứng dụng khác (Gmail, Google Drive, Slack, lịch...) mà không cần copy-paste thủ công.

## Tiếp theo

Đọc tiếp: [04-vault-marketing](04-vault-marketing.md) — Build vault Marketing.
