# 🎯 Akinator Workflow & Usage Guide

## 📊 Ada 2 Cara Pake:

### **Way 1️⃣: Standalone (Fastest Way!)**
```
python generate_db.py
  ↓
Input URL Ollama (lokal/Colab)
  ↓
AI generate database (2-5 menit)
  ↓
akinator_db.json created ✅
  ↓
python akinator.py
  ↓
Pilih "1. Mulai Permainan Baru"
  ↓
PLAY! 🎮
```

**Kapan pakai:** Ketika mau langsung generate database, tidak perlu menu yang complex

---

### **Way 2️⃣: Via Menu (More Flexible)**
```
python akinator.py
  ↓
Menu:
  1. Mulai Permainan
  5. Generate Database dengan AI ← Generate baru
  6. Improve Database dengan AI  ← Tambah items ke existing
  7. Config Ollama URL            ← Setup koneksi
  ↓
PLAY! 🎮
```

**Kapan pakai:** Ketika mau lebih banyak opsi (improve, reset, dll)

---

## 🚀 Complete Workflow (from Zero to Play)

### **Step-by-Step dengan Colab:**

#### 1️⃣ Setup Ollama di Colab (5 menit)
```python
# Buka Google Colab, buat notebook baru, jalankan:

# Cell 1
!curl https://ollama.ai/install.sh | sh
!ollama pull llama2

import subprocess
import threading
import time

def run_ollama():
    subprocess.run(['ollama', 'serve'], check=False)

thread = threading.Thread(target=run_ollama, daemon=True)
thread.start()
time.sleep(15)

print("✅ Ollama ready!")

# Cell 2
!pip install pyngrok

from pyngrok import ngrok

public_url = ngrok.connect(11434)
print(f"✨ Public URL: {public_url}")

# COPY URL INI! Jangan close Colab!
```

#### 2️⃣ Generate Database (di PC lokal)
```bash
# Terminal lokal

python generate_db.py

# Masukkan URL dari Colab:
# https://abc123-xyz.ngrok.io

# Pilih model: llama2

# Tunggu 2-5 menit...

# ✅ akinator_db.json created!
```

#### 3️⃣ Play!
```bash
python akinator.py
→ Pilih "1. Mulai Permainan Baru"
→ Enjoy! 🎮
```

**Total time:** ~10 menit dari 0 → play

---

## 📁 File Structure & Punya

```
akinator/
├── akinator.py              # Main game (bisa pakai langsung)
├── ollama_integration.py    # Ollama API (imported by others)
├── generate_db.py           # ⭐ Standalone generator (run this!)
├── akinator_db.json         # Database (auto-created/updated)
├── akinator_stats.json      # Stats (auto-created)
├── README.md               # Full documentation
├── QUICKSTART.md           # Quick setup guide
├── OLLAMA_SETUP.md         # Detailed Ollama setup
├── WORKFLOW.md             # This file
└── requirements.txt        # Dependencies
```

---

## 🎮 Playing Workflow

```
Run Game:
$ python akinator.py

GAME LOOP:
1. Choose "1. Mulai Permainan Baru"
2. Think of something
3. Answer yes/no questions
4. Either:
   a. AI guesses correctly ✅
   b. AI guesses wrong → Teach it new thing!
5. Play again or check stats/database
6. Exit

DATABASE EVOLVES:
- Every time you teach AI something new
- Database saved automatically
- Next game AI is smarter! 🧠
```

---

## ⚙️ Advanced: Improve Workflow

```
Initial Database:
$ python generate_db.py
→ 30-40 items generated ✅

Improve it:
$ python akinator.py
→ Menu "6. Improve Database dengan AI"
→ Add 10-15 more items ✅

Keep improving:
→ Keep using option 6
→ Or teach via gameplay
→ Database grows! 📈
```

---

## 🎯 Recommended Path (for Beginners)

```
1. Setup Ollama (Pick one):
   ✓ Colab (easiest, recommended)
   - Lokal (Ollama di PC)

2. Generate database:
   $ python generate_db.py
   → Answer questions
   → Database created ✅

3. Play game:
   $ python akinator.py
   → Menu 1
   → Have fun! 🎮

4. (Optional) Improve:
   $ python akinator.py
   → Menu 6
   → Add more items

5. (Optional) Check stats:
   $ python akinator.py
   → Menu 2
   → See your progress 📊
```

---

## 🆘 Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| "Connection failed" | Check Ollama running, URL correct |
| "Timeout" | Internet slow? Try smaller model |
| "Invalid JSON" | Try regenerate? Different model? |
| "File permission" | Run from correct folder |
| "No module" | `pip install requests` |

---

## 📊 What Happens Behind the Scenes?

### When you run `generate_db.py`:

```
User input (URL, model)
    ↓
OllamaIntegration object created
    ↓
Test connection to Ollama
    ↓
Send prompt: "Generate Akinator database untuk Indonesia"
    ↓
Ollama AI processes (2-5 min)
    ↓
Response parsed as JSON
    ↓
Validate tree structure
    ↓
Count items/nodes
    ↓
Save to akinator_db.json
    ↓
Database ready! ✅
```

### When you play and teach AI:

```
Game loop:
    Traverse tree based on answers
    ↓
AI makes guess
    ↓
If wrong:
    User provides correct answer
    ↓
    User provides distinguishing question
    ↓
    Tree updated with new node
    ↓
    Database saved (auto)
    ↓
Next time smarter! 🧠
```

---

## 💡 Pro Tips

1. **Colab is best** - No installation, just run Colab code
2. **Generate multiple times** - Pick best result
3. **Teach via gameplay** - Also improves database
4. **Check database structure** - Menu 3 shows tree
5. **Backup your DB** - Copy akinator_db.json before reset

---

## 🚀 Quick Command Reference

```bash
# Generate fresh database with AI
python generate_db.py

# Play the game
python akinator.py

# Check current Python syntax
python -m py_compile akinator.py

# List files
dir

# View database file
type akinator_db.json    # Windows
cat akinator_db.json     # Linux/Mac
```

---

## 📚 More Documentation

- [README.md](README.md) - Full features & mechanics
- [QUICKSTART.md](QUICKSTART.md) - Super quick setup
- [OLLAMA_SETUP.md](OLLAMA_SETUP.md) - Detailed Ollama guide
- [demo_ollama.py](demo_ollama.py) - Test script

---

Enjoy the game! 🎮✨
