# 🥚 Roco Kingdom Egg Group Guide

<p align="center">
  <img src="https://img.shields.io/badge/Roco%20Kingdom-Egg%20Group%20Query-blue?style=flat-square" alt="Roco Kingdom">
  <img src="https://img.shields.io/badge/Pure%20Frontend-Zero%20Dependencies-green?style=flat-square" alt="Pure Frontend">
  <img src="https://img.shields.io/badge/TailwindCSS-Styling-orange?style=flat-square" alt="TailwindCSS">
</p>

<p align="center">
  <b>Egg Breeding Pair Query Tool | Pet Egg Group Data Visualization | Smart Filter & Search</b>
</p>

---

## 📖 Introduction

**Roco Kingdom Egg Group Guide** is a web tool designed specifically for Roco Kingdom players to quickly query pet egg group information and find compatible breeding pairs.

### ✨ Key Features

- 🔍 **Smart Search** - Search by pet name or egg group type
- 🥚 **Egg Group Categories** - 15 egg groups at a glance
- 🔗 **Pairing Query** - Automatically calculate compatible breeding pairs
- 📊 **Data Visualization** - Clean card-based layout, beautiful and user-friendly
- 📱 **Responsive Design** - Perfectly adapted for mobile, tablet, and desktop
- ⚡ **Pure Frontend** - No backend required, works out of the box

### 🎯 Supported Egg Groups

| Egg Group | Icon | Egg Group | Icon |
|-----------|------|-----------|------|
| Spirit | ✨ | Monster | 🐲 |
| Plant | 🌿 | Animal | 🐾 |
| Humanoid | 🎭 | Insect | 🦋 |
| Flying | 🕊️ | Amphibian | 🐸 |
| Ocean | 🐠 | Mechanical | ⚙️ |
| Mineral | 💎 | Fairy | 🧚 |
| Dragon | 🐉 | Baby | 🍼 |
| Unknown | ❓ | | |

---

## 🚀 Quick Start

### Online Access

Simply open the `roco-egg-groups.html` file:

```bash
# Method 1: Double-click to open
roco-egg-groups.html

# Method 2: Use local server (recommended)
python -m http.server 8080
# Then visit http://localhost:8080/roco-egg-groups.html
```

### Project Structure

```
洛克王国世界/
├── roco-egg-groups.html    # Main page (Egg Group Guide)
├── egg-groups-data.js      # Egg group data file
├── update_egg_groups.py    # Data update script
├── pet-img/                # Pet image resources
│   └── example.PNG
├── design-system/          # Design system documentation
└── .cursor/                # Cursor editor configuration
```

---

## 🛠️ Tech Stack

- **HTML5** - Semantic structure
- **Tailwind CSS** - Atomic CSS framework (CDN)
- **Vanilla JavaScript** - Native JS, zero dependencies
- **Python 3** - Data synchronization script

---

## 📝 Data Update

To update egg group data, edit the `洛克王国蛋组数据.md` file, then run:

```bash
python update_egg_groups.py
```

The script will automatically generate a new `egg-groups-data.js` file.

### Data Format

```javascript
const EGG_GROUPS = {
  "Spirit": {
    emoji: "✨",
    color: "#a855f7",
    pets: ["幽冥眼", "火神", "梦悠悠", ...]
  },
  // ... other egg groups
};
```

---

## 🤝 Contributing

Issues and Pull Requests are welcome!

1. Fork this repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the [MIT](LICENSE) License.

---

## 🙏 Acknowledgments

- Data Source: Roco Kingdom Official Game
- Styling Framework: [Tailwind CSS](https://tailwindcss.com/)
- Font: [Inter](https://fonts.google.com/specimen/Inter)

---

<p align="center">
  Made with ❤️ for Roco Kingdom Players
</p>

<p align="center">
  <a href="https://gitee.com/stevec_gitee/RocoKingdom">🔗 Gitee Repository</a>
</p>
