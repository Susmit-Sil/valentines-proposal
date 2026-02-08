# 💕 Valentine's Proposal Website

A beautiful, interactive Valentine's Day proposal website built with Streamlit.

## ✨ Features

- 🔐 **Password Protected** - Date picker with hint: "The date on which we first met" (02/01/2026)
- 📖 **Story Montage** - 3-page journey of your relationship
- 👸 **Her Spotlight** - A page dedicated to her beauty
- 💕 **The Proposal** - Interactive Yes/No with a playful moving "No" button!
- 🎉 **Celebration** - Confetti, hearts rain, and romantic messages
- 📸 **Photo Slideshow** - Your memories displayed in a gallery
- 🎬 **Video Player** - Muted videos with background music
- 🎵 **Background Music** - "Gone Gone Gone" plays at low volume

---

## 📁 Folder Structure

```
c:\Users\HP\Documents\valentines\
├── app.py                    # Main application
├── requirements.txt          # Dependencies
├── README.md                 # This file
├── gone_gone_gone.mp3        # 🎵 Background music (YOU ADD THIS)
├── images/                   # Story section photos
│   ├── story_1.jpg
│   ├── story_2.jpg
│   ├── story_3.jpg
│   ├── her_portrait.jpg
│   └── us_final.jpg
└── gallery/                  # 📸🎬 Celebration media
    ├── images/               # Photo slideshow
    │   ├── photo1.jpg
    │   ├── photo2.jpg
    │   └── ...
    └── videos/               # Video player (muted)
        ├── video1.mp4
        ├── video2.mp4
        └── ...
```

---

## 🖼️ Setup Your Photos

### Story Section (`images/` folder)
| File | Description | Size |
|------|-------------|------|
| `story_1.jpg` | Memory #1 | 600×600 |
| `story_2.jpg` | Memory #2 | 600×600 |
| `story_3.jpg` | Memory #3 | 600×600 |
| `her_portrait.jpg` | Solo photo of her | 400×500 |
| `us_final.jpg` | Couple photo | 800×450 |

### Celebration Gallery (`gallery/` folder)
| Folder | Content | Format |
|--------|---------|--------|
| `gallery/images/` | Photo slideshow | JPG, PNG (9:16 mobile) |
| `gallery/videos/` | Video player | MP4 (muted, loops) |

---

## 🎵 Setup Music

1. Download "Gone Gone Gone" by Phillip Phillips as MP3
2. Rename to `gone_gone_gone.mp3`
3. Place in: `c:\Users\HP\Documents\valentines\`

---

## 🚀 Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

Made with 💕 for your special someone!
