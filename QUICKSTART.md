# 🚀 Quick Start Guide - Akinator dengan AI

## Pilihan 1️⃣: Tanpa AI (Vanilla)

Super simple! Just run:
```bash
python akinator.py
```

Pilih menu "1. Mulai Permainan Baru" dan enjoy!

---

## Pilihan 2️⃣: Dengan AI dari Google Colab (RECOMMENDED!) ⭐

### Step 1: Setup Ollama di Colab (5 menit)

Buka Google Colab dan jalankan code ini:

```python
# Cell 1: Install dan setup
!curl https://ollama.ai/install.sh | sh
!ollama pull llama2

import subprocess
import threading
import time

# Jalankan Ollama di background
def run_ollama():
    subprocess.run(['ollama', 'serve'], check=False)

thread = threading.Thread(target=run_ollama, daemon=True)
thread.start()
time.sleep(15)  # Tunggu Ollama start

print("✅ Ollama ready!")

# Cell 2: Setup ngrok untuk public URL
!pip install pyngrok

from pyngrok import ngrok

public_url = ngrok.connect(11434)
print(f"✨ Public URL: {public_url}")
print("Copy URL ini!")
```

### Step 2: Dapatkan Public URL

Dari output Colab, copy URL yang mirip:
```
https://abc123-xyz.ngrok.io
```

**Jangan di-close Colab! Biarkan dia running!**

### Step 3: Setup di Akinator

```bash
python akinator.py
```

Pilih menu:
```
Pilih opsi (1-8): 7
```

Masukkan public URL:
```
Masukkan URL Ollama: https://abc123-xyz.ngrok.io
Masukkan model name: llama2
```

### Step 4: Generate Database

Kembali ke menu utama:
```
Pilih opsi (1-8): 5
```

**Tunggu proses generate (2-5 menit)**

```
🤖 Generating database Indonesia dengan AI...
⏳ Ini mungkin memakan waktu beberapa menit...

[Processing...]

✅ Database baru berhasil disimpan!
   Total items: 45
   Total nodes: 89
```

### Step 5: Play!

```
Pilih opsi (1-8): 1
```

Enjoy game dengan database Indonesia yang di-generate AI! 🎉

---

## Pilihan 3️⃣: Dengan AI Lokal

### Step 1: Install Ollama

Download dari https://ollama.ai

### Step 2: Run Ollama

```bash
ollama serve
```

Akan running di: `http://localhost:11434`

### Step 3: Pull Model

Di terminal lain:
```bash
ollama pull llama2
```

### Step 4: Setup di Akinator

```bash
python akinator.py
```

Menu:
```
7. Config Ollama URL
http://localhost:11434
llama2
```

### Step 5: Generate

```
5. Generate Database dengan AI
```

Done!

---

## 📋 Quick Comparison

| Feature | Vanilla | Lokal | Colab |
|---------|---------|-------|-------|
| Setup | 0 min | 10 min | 5 min |
| Speed | - | Fast | Med |
| Dependency | None | Ollama | Colab |
| Quality | Good | Good | Good |
| Rekomendasi | Demo | Prod | Learning |

---

## 🆘 Troubleshooting

### "Connection failed"
```
✅ Cek:
1. Ollama running? (ollama serve)
2. URL benar?
3. Colab ngrok masih active?
```

### "Timeout"
```
✅ Coba:
1. Model lebih kecil (neural-chat)
2. Internet lebih stabil
3. Tunggu lebih lama
```

### "Invalid JSON"
```
✅ Solusi:
1. Coba generate lagi
2. Ganti model
3. Restart Ollama
```

---

## 🎮 Next Steps

Setelah setup, explore:

```
Menu Utama
1. Play game! 🎮
2. Lihat stats
3. Lihat database (tree structure)
6. Improve database (add more items)
```

---

## 📚 Learn More

- Baca [README.md](README.md) untuk lengkap
- Baca [OLLAMA_SETUP.md](OLLAMA_SETUP.md) untuk detail
- Run [demo_ollama.py](demo_ollama.py) untuk demo

---

## 💡 Pro Tips

1. **Gunakan Colab** - Paling simple dan tidak perlu install apapun
2. **Multiple generations** - Generate database beberapa kali, pilih yang terbaik
3. **Improve iteratively** - Mulai dari generate, terus improve dengan "Improve Database"
4. **Test connection** - Selalu test koneksi dulu sebelum generate

---

Enjoy! 🚀✨
