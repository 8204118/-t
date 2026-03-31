#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
洛克王国蛋组数据同步脚本 v2
从 洛克王国蛋组数据.md → 生成 egg-groups-data.js
HTML 通过 <script src="egg-groups-data.js"> 引入，数据与界面完全分离。

用法：
  python update_egg_groups.py
"""

import re
import json
import os
import sys
import datetime
from collections import OrderedDict

# ── 配置 ──────────────────────────────────────────────
MD_FILE = "洛克王国蛋组数据.md"
JS_OUTPUT = "egg-groups-data.js"

# 每个蛋组的 emoji 和颜色，新增蛋组时在这里加一行
GROUP_STYLE = {
    "精灵组": {"emoji": "✨", "color": "#a855f7"},
    "怪兽组": {"emoji": "🐲", "color": "#ef4444"},
    "植物组": {"emoji": "🌿", "color": "#22c55e"},
    "动物组": {"emoji": "🐾", "color": "#f97316"},
    "拟人组": {"emoji": "🎭", "color": "#ec4899"},
    "昆虫组": {"emoji": "🦋", "color": "#84cc16"},
    "飞行组": {"emoji": "🕊️", "color": "#06b6d4"},
    "两栖组": {"emoji": "🐸", "color": "#14b8a6"},
    "海洋组": {"emoji": "🐠", "color": "#3b82f6"},
    "机械组": {"emoji": "⚙️", "color": "#78716c"},
    "矿石组": {"emoji": "💎", "color": "#a78bfa"},
    "妖精组": {"emoji": "🧚", "color": "#f472b6"},
    "巨龙组": {"emoji": "🐉", "color": "#7c3aed"},
    "乖乖组": {"emoji": "🍼", "color": "#fbbf24"},
    "未知组": {"emoji": "❓", "color": "#6b7280"},
}

FALLBACK_STYLE = {"emoji": "🔮", "color": "#64748b"}


# ── 解析 MD ───────────────────────────────────────────
def parse_md(path):
    groups = OrderedDict()
    current_group = None

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            m = re.match(r"^##\s+(.+组)\s*$", line)
            if m:
                current_group = m.group(1)
                groups[current_group] = []
                continue
            if current_group and line and not line.startswith("#"):
                pets = re.split(r"[，,]", line)
                pets = [p.strip() for p in pets if p.strip()]
                groups[current_group].extend(pets)

    return groups


# ── 生成 JS 文件 ──────────────────────────────────────
def build_js_file(groups):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = []
    lines.append("// 此文件由 update_egg_groups.py 自动生成，请勿手动编辑")
    lines.append("// 数据来源：洛克王国蛋组数据.md")
    lines.append(f"// 最后更新：{now}")
    lines.append("")
    lines.append("const EGG_GROUPS = {")

    for name, pets in groups.items():
        style = GROUP_STYLE.get(name, FALLBACK_STYLE)
        pets_json = json.dumps(pets, ensure_ascii=False)
        lines.append(f'  "{name}": {{')
        lines.append(f'    emoji: "{style["emoji"]}",')
        lines.append(f'    color: "{style["color"]}",')
        lines.append(f"    pets: {pets_json},")
        lines.append(f"  }},")

    lines.append("};")
    return "\n".join(lines)


# ── 主流程 ────────────────────────────────────────────
def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    md_path = os.path.join(script_dir, MD_FILE)
    js_path = os.path.join(script_dir, JS_OUTPUT)

    if not os.path.exists(md_path):
        print(f"❌ 找不到 MD 文件：{md_path}")
        sys.exit(1)

    # 解析
    groups = parse_md(md_path)
    print(f"📖 读取 MD 完成，共 {len(groups)} 个蛋组")

    for name, pets in groups.items():
        style = GROUP_STYLE.get(name, FALLBACK_STYLE)
        print(f"   {style['emoji']} {name}：{len(pets)} 只")
        if name not in GROUP_STYLE:
            print(f"   ⚠️  '{name}' 没有在 GROUP_STYLE 中定义，使用了默认样式")

    all_pets = set()
    for pets in groups.values():
        all_pets.update(pets)
    print(f"   📊 精灵总数（去重）：{len(all_pets)}")

    # 写入 JS
    js_content = build_js_file(groups)
    with open(js_path, "w", encoding="utf-8") as f:
        f.write(js_content)

    print(f"\n✅ 已生成 {JS_OUTPUT}，刷新浏览器即可看到新数据！")


if __name__ == "__main__":
    main()
