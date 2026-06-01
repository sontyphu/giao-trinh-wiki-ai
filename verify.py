# -*- coding: utf-8 -*-
import os
VAULT = r"C:\Users\Thanh Son\Documents\Obsidian Vault\Son's Brain\wiki\work\Đào tạo\giao-trinh-wiki-ai"
DOCS  = r"E:\Agent Claude\ai-agent-business-kit\giao-trinh-wiki-ai\docs"
REMAP = {"README.md":"index.md","index.md":"muc-luc.md","QUICK-START.md":"quick-start.md","FAQ.md":"faq.md"}

def walk(base):
    out = {}
    for dp, _, fns in os.walk(base):
        for fn in fns:
            rel = os.path.relpath(os.path.join(dp, fn), base).replace("\\", "/")
            out[rel] = os.path.getsize(os.path.join(dp, fn))
    return out

v = walk(VAULT); d = walk(DOCS)
v_md = [f for f in v if f.endswith(".md")]
v_other = [f for f in v if not f.endswith(".md")]
print(f"VAULT: {len(v)} file ({len(v_md)} .md, {len(v_other)} khác)")
print(f"DOCS : {len(d)} file")
print(f"File KHÁC .md trong vault: {v_other if v_other else 'KHONG CO (chi toan .md)'}")

missing = []; short = []
for f in v_md:
    tgt = REMAP[f] if ("/" not in f and f in REMAP) else f
    p = os.path.join(DOCS, tgt.replace("/", os.sep))
    if not os.path.exists(p):
        missing.append(f); continue
    src = open(os.path.join(VAULT, f.replace("/", os.sep)), encoding="utf-8").read()
    dst = open(p, encoding="utf-8").read()
    sl = src.count("\n"); dl = dst.count("\n")
    if dl < sl - 2:
        short.append((f, sl, dl))

print("\n=== FILE THIEU tren web:", missing if missing else "KHONG - du het 100%")
print("=== FILE nghi bi cat ngan:", short if short else "KHONG - so dong khop het")
extra = [f for f in d if f.endswith(".md") and f not in [REMAP.get(x, x) if "/" not in x else x for x in v_md]]
print("=== FILE THUA tren web (khong co trong vault):", extra if extra else "KHONG")
print(f"\nKET LUAN: {len(v_md)-len(missing)}/{len(v_md)} file .md cua vault da co tren web.")
