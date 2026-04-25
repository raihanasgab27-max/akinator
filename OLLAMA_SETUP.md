# 🤖 Setup Ollama Integration untuk Akinator

Panduan lengkap untuk setup Ollama dan menggunakan AI untuk auto-generate database Indonesia!

## 📋 Persyaratan

- Python 3.6+
- Requests library (sudah included)
- Ollama (lokal atau di cloud seperti Colab)
- Internet connection

## 🚀 Setup Ollama Lokal

### 1. Install Ollama
```bash
# Windows/Mac/Linux
# Download dari: https://ollama.ai

# Atau menggunakan package manager:
# Windows (Chocolatey):
choco install ollama

# macOS (Homebrew):
brew install ollama

# Linux:
curl https://ollama.ai/install.sh | sh
```

### 2. Jalankan Ollama
```bash
ollama serve
```

Ollama akan running di `http://localhost:11434`

### 3. Pull Model
```bash
# Gunakan model pilihan Anda
ollama pull llama2
# atau
ollama pull neural-chat
# atau
ollama pull mistral
```

## ☁️ Setup Ollama di Google Colab

Ini adalah cara terbaik untuk mendapatkan API publik!

### 1. Buka Google Colab
```bash
# Buat notebook baru atau gunakan yang ada
```

### 2. Install dan Setup Ollama di Colab
```python
# Cell 1: Install Ollama
!curl https://ollama.ai/install.sh | sh

# Cell 2: Download dan setup
!ollama pull llama2

# Cell 3: Jalankan Ollama dengan ngrok
!pip install pyngrok

import subprocess
import threading

# Jalankan Ollama di background
def run_ollama():
    subprocess.run(['ollama', 'serve'], check=False)

thread = threading.Thread(target=run_ollama, daemon=True)
thread.start()

import time
time.sleep(10)  # Tunggu Ollama start

# Setup ngrok untuk public URL
from pyngrok import ngrok

public_url = ngrok.connect(11434)
print(f"✅ Ollama public URL: {public_url}")
```

**Simpan URL ini!** Contohnya: `https://abc123.ngrok.io`

## 🎮 Menggunakan Akinator dengan Ollama

### Langkah 1: Jalankan Akinator
```bash
python akinator.py
```

### Langkah 2: Dari Menu, Pilih Config
```
1. Mulai Permainan Baru
2. Lihat Statistik
3. Lihat Database
4. Reset Database
5. Generate Database dengan AI (Ollama)
6. Improve Database dengan AI
7. Config Ollama URL
8. Keluar

Pilih opsi (1-8): 7  # Config Ollama URL
```

### Langkah 3: Masukkan URL Ollama
```
⚙️  CONFIG OLLAMA URL
==================================================
URL saat ini: http://localhost:11434
Contoh: http://localhost:11434
Atau: https://abc123.ngrok.io (dari Colab)
==================================================

Masukkan URL Ollama (atau Enter untuk skip): https://abc123.ngrok.io
```

### Langkah 4: Pilih Model
```
Masukkan model name (default: llama2): llama2
✅ Model set ke: llama2
```

### Langkah 5: Generate Database
```
Pilih opsi (1-8): 5  # Generate Database dengan AI

🤖 Generating database Indonesia dengan AI...
⏳ Ini mungkin memakan waktu beberapa menit...

[Tunggu proses selesai]

✅ Database baru berhasil disimpan!
   Total items: 45
   Total nodes: 89
```

## ⚙️ Model Recommendations

### Untuk Speed (Fast)
```
ollama pull neural-chat
```
- Cepat dan ringkas
- Cocok untuk demo

### Untuk Quality (Medium)
```
ollama pull llama2
```
- Balance speed dan quality
- Recommended untuk production

### Untuk Kualitas Terbaik (Slow)
```
ollama pull mistral
```
- Response paling baik
- Lebih lambat

## 🔧 Advanced Configuration

### Set Model Secara Manual
Edit `akinator.py` dan ubah:
```python
self.ollama.set_model("mistral")  # Ganti dengan model pilihan
```

### Customize Prompt
Edit `ollama_integration.py` - ubah prompt di bagian:
```python
def generate_indonesian_database(self) -> dict:
    prompt = """
    [Customize prompt di sini]
    """
```

## 📊 Database Options

### Generate Database Baru
- Membuat database dari nol dengan AI
- Fokus pada niche Indonesia
- 30-40+ items auto-generated

### Improve Database Existing
- Menambah items ke database yang ada
- Memperbaiki pertanyaan
- Tetap maintain struktur sebelumnya

## 🐛 Troubleshooting

### Error: "Cannot connect to Ollama"
```
✅ Solusi:
1. Pastikan Ollama sudah running
2. Cek URL yang benar
3. Test di browser: http://localhost:11434/api/tags
4. Jika Colab, pastikan ngrok public URL masih aktif
```

### Error: "Timeout"
```
✅ Solusi:
1. Timeout default 5 menit
2. Coba model yang lebih kecil (neural-chat)
3. Pastikan internet connection stabil
```

### Error: "Invalid JSON response"
```
✅ Solusi:
1. Try model yang berbeda
2. Adjust temperature di ollama_integration.py
3. Check Ollama version terbaru
```

### Model Not Found
```
✅ Solusi:
# List available models
ollama list

# Pull model baru
ollama pull [model_name]
```

## 📝 Contoh Database yang Dihasilkan

Berikut struktur database yang akan di-generate:

```json
{
  "type": "question",
  "question": "Apakah itu makhluk hidup?",
  "yes": {
    "type": "question",
    "question": "Apakah itu hewan?",
    "yes": {
      "type": "question",
      "question": "Apakah itu adalah burung?",
      "yes": {
        "type": "guess",
        "guess": "elang jawa"
      },
      "no": {
        "type": "guess",
        "guess": "harimau sumatra"
      }
    },
    "no": {
      "type": "guess",
      "guess": "pohon kelapa"
    }
  },
  "no": {
    "type": "question",
    "question": "Apakah itu makanan?",
    "yes": {
      "type": "guess",
      "guess": "rendang"
    },
    "no": {
      "type": "guess",
      "guess": "batik"
    }
  }
}
```

## 🎓 Tips untuk Hasil Terbaik

1. **Gunakan model terbaru** - Testing dengan beberapa model
2. **Customize prompt** - Modifikasi prompt sesuai kebutuhan
3. **Multiple generations** - Generate berkali-kali dan pilih yang terbaik
4. **Validate manually** - Cek database yang di-generate sebelum digunakan
5. **Improve iteratively** - Gunakan "Improve Database" untuk add items

## 🔗 Links Berguna

- Ollama: https://ollama.ai
- ngrok: https://ngrok.com
- Models: https://ollama.ai/library

---

Enjoy generating database Akinator dengan AI! 🚀✨
