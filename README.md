# 🥚 洛克王国蛋组图鉴

<p align="center">
  <img src="https://img.shields.io/badge/洛克王国-蛋组查询-blue?style=flat-square" alt="洛克王国">
  <img src="https://img.shields.io/badge/纯前端-零依赖-green?style=flat-square" alt="纯前端">
  <img src="https://img.shields.io/badge/TailwindCSS-样式-orange?style=flat-square" alt="TailwindCSS">
</p>

<p align="center">
  <b>孵蛋配对查询工具 | 精灵蛋组数据可视化 | 智能筛选与搜索</b>
</p>

---

## 📖 项目简介

**洛克王国蛋组图鉴**是一个专为《洛克王国》玩家设计的网页工具，帮助玩家快速查询精灵的蛋组信息，找到可以孵蛋配对的精灵组合。

### ✨ 核心功能

- 🔍 **智能搜索** - 支持按精灵名称、蛋组类型快速查找
- 🥚 **蛋组分类** - 15 种蛋组分类，一目了然
- 🔗 **配对查询** - 自动计算可配对的精灵组合
- 📊 **数据可视化** - 清晰的卡片式布局，美观易用
- 📱 **响应式设计** - 完美适配手机、平板、电脑
- ⚡ **纯前端实现** - 无需后端，打开即用

### 🎯 支持的蛋组

| 蛋组 | 图标 | 蛋组 | 图标 |
|------|------|------|------|
| 精灵组 | ✨ | 怪兽组 | 🐲 |
| 植物组 | 🌿 | 动物组 | 🐾 |
| 拟人组 | 🎭 | 昆虫组 | 🦋 |
| 飞行组 | 🕊️ | 两栖组 | 🐸 |
| 海洋组 | 🐠 | 机械组 | ⚙️ |
| 矿石组 | 💎 | 妖精组 | 🧚 |
| 巨龙组 | 🐉 | 乖乖组 | 🍼 |
| 未知组 | ❓ | | |

---

## 🚀 快速开始

### 在线访问

直接打开 `roco-egg-groups.html` 文件即可使用：

```bash
# 方式一：直接双击打开
roco-egg-groups.html

# 方式二：使用本地服务器（推荐）
python -m http.server 8080
# 然后访问 http://localhost:8080/roco-egg-groups.html
```

### 项目结构

```
.
├── roco-egg-groups.html    # 主页面（蛋组图鉴）
├── egg-groups-data.js      # 蛋组数据文件
├── update_egg_groups.py    # 数据更新脚本
├── pet-img/                # 精灵图片资源
├── design-system/          # 设计系统文档
└── .cursor/                # Cursor 编辑器配置
```

---

## 🛠️ 技术栈

- **HTML5** - 语义化结构
- **Tailwind CSS** - 原子化 CSS 框架（CDN 引入）
- **Vanilla JavaScript** - 原生 JS，零依赖
- **Python 3** - 数据同步脚本

---

## 📝 数据更新

如需更新蛋组数据，请编辑 `洛克王国蛋组数据.md` 文件，然后运行：

```bash
python update_egg_groups.py
```

脚本会自动生成新的 `egg-groups-data.js` 文件。

### 数据格式

```javascript
const EGG_GROUPS = {
  "精灵组": {
    emoji: "✨",
    color: "#a855f7",
    pets: ["幽冥眼", "火神", "梦悠悠", ...]
  },
  // ... 其他蛋组
};
```

---

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 Pull Request

---

## 📄 开源协议

本项目采用 [MIT](LICENSE) 协议开源。

---

## 🙏 致谢

- 数据来源：《洛克王国》游戏官方
- 样式框架：[Tailwind CSS](https://tailwindcss.com/)
- 字体：[Inter](https://fonts.google.com/specimen/Inter)

---

<p align="center">
  Made with ❤️ for 洛克王国玩家
</p>
