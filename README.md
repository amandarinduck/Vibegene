# ⬡ VibeGene

DNA sequence editor and plasmid viewer — runs as a PWA on Android.

## Project structure

```
vibegene/
├── public/
│   ├── favicon.svg
│   ├── apple-touch-icon.png
│   └── icons/
│       ├── icon-192.png
│       └── icon-512.png
├── src/
│   ├── main.jsx        ← React entry point
│   └── App.jsx         ← Main app component
├── index.html
├── vite.config.js      ← Vite + PWA plugin config
├── vercel.json         ← Zero-config Vercel deployment
└── package.json
```

---

## Deploy to Vercel (recommended — free, ~5 min)

### 1. Install dependencies locally (one-time)
You need [Node.js](https://nodejs.org) (v18+) installed.

```bash
npm install
npm run build   # verify it builds without errors
```

### 2. Push to GitHub
```bash
git init
git add .
git commit -m "init VibeGene"
# Create a new repo on github.com, then:
git remote add origin https://github.com/YOUR_USERNAME/vibegene.git
git push -u origin main
```

### 3. Deploy on Vercel
1. Go to [vercel.com](https://vercel.com) and sign in with GitHub
2. Click **"Add New Project"** → import your `vibegene` repo
3. Vercel auto-detects Vite — just click **Deploy**
4. Your app is live at `https://vibegene-xxx.vercel.app`

---

## Install on Android as a PWA

1. Open your Vercel URL in **Chrome for Android**
2. Tap the **⋮ menu** (top right) → **"Add to Home screen"**
3. Tap **"Add"** — VibeGene appears on your home screen like a native app
4. Open it — it runs fullscreen with no browser UI

> **Tip:** After the first load, the app works fully offline thanks to the service worker.

---

## Local development

```bash
npm install
npm run dev      # starts at http://localhost:5173
```

---

## Alternative: Netlify

```bash
npm run build
# Drag the `dist/` folder to app.netlify.com/drop
```

Done — no CLI needed.
