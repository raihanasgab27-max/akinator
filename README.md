# 🔮 Akinator - Game Tanya Jawab Interaktif

Akinator adalah permainan tanya-jawab interaktif berbasis Python yang mencoba menebak apa yang Anda pikirkan melalui serangkaian pertanyaan ya/tidak yang cerdas!

## ✨ Fitur Unggulan

### 🎮 Gameplay
- ❓ Sistem pertanyaan interaktif yang adaptif
- 🧠 Algoritma pembelajaran mesin berbasis pohon keputusan
- 💾 Database yang dapat belajar dan berkembang secara otomatis
- 🎯 Tingkat akurasi yang meningkat seiring waktu

### 📊 Statistik & Analytics
- 📈 Melacak total permainan dimainkan
- ✅ Menghitung tebakan benar/salah
- 📉 Menampilkan tingkat akurasi
- 🧠 Jumlah item baru yang dipelajari

### 🤖 AI Integration (NEW!)
- 🌐 Integrasi dengan Ollama untuk auto-generate database
- 🇮🇩 Focus pada niche Indonesia (makanan, budaya, tokoh, dll)
- 📚 Auto-generate 30-40+ items Indonesia
- 🚀 Support ngrok dari Google Colab
- ✨ Improve existing database dengan AI

### 🎛️ Menu Utama
1. **Mulai Permainan Baru** - Mainkan Akinator
2. **Lihat Statistik** - Tampilkan statistik permainan
3. **Lihat Database** - Visualisasi pohon keputusan
4. **Reset Database** - Kembalikan ke default
5. **Generate Database dengan AI** - Buat database baru pakai Ollama 🆕
6. **Improve Database dengan AI** - Tambah items ke database existing 🆕
7. **Config Ollama URL** - Setup koneksi ke Ollama (lokal/Colab) 🆕
8. **Keluar** - Tutup program

### 🛡️ Error Handling
- Penanganan keyboard interrupt yang baik
- Input validation yang ketat
- Graceful exit pada error

## 📋 Persyaratan

- Python 3.6 atau lebih tinggi
- Tidak ada dependency eksternal! (Requests optional untuk Ollama)
- Untuk AI features: Ollama (lokal atau di cloud)

## 🚀 Quick Start

### Basic (Tanpa AI)
```bash
python akinator.py
```

### Dengan AI (Ollama)
1. **Setup Ollama** - Lihat [OLLAMA_SETUP.md](OLLAMA_SETUP.md) untuk panduan lengkap
2. Jalankan: `python akinator.py`
3. Pilih menu `5. Generate Database dengan AI`
4. Masukkan URL Ollama (lokal atau Colab)
5. Tunggu proses generate selesai
6. Enjoy database Indonesia dengan 30-40+ items! 🎉

**Tidak punya Ollama?** Baca panduan setup di [OLLAMA_SETUP.md](OLLAMA_SETUP.md) (mudah kok!)

## 🎮 Cara Bermain

### Langkah-Langkah:
1. Jalankan program
2. Pilih **"1. Mulai Permainan Baru"** dari menu
3. Pikirkan sesuatu (orang, hewan, benda, atau apa saja)
4. Jawab pertanyaan-pertanyaan dengan jujur
5. Jika Akinator menebak dengan benar → 🎉 Berhasil!
6. Jika Akinator salah → Ajarkan hal baru dengan menjawab pertanyaan pembelajaran

### Contoh Gameplay:

```
==================================================
🎯 SELAMAT DATANG DI AKINATOR!
==================================================
Game Tanya Jawab Interaktif
Saya akan menebak apa yang Anda pikirkan! 🔮
==================================================

==================================================
MENU UTAMA - AKINATOR
==================================================
1. Mulai Permainan Baru
2. Lihat Statistik
3. Lihat Database
4. Reset Database
5. Keluar
==================================================
Pilih opsi (1-5): 1

==================================================
🎮 MULAI PERMAINAN AKINATOR
==================================================

Pikirkan sesuatu (bisa berupa orang, hewan, atau benda)
dan saya akan mencoba menebaknya dengan bertanya.

Tekan Enter ketika Anda sudah siap...

Apakah itu makhluk hidup?
(ya/tidak): ya

Apakah itu hewan?
(ya/tidak): ya

Apakah itu bisa terbang?
(ya/tidak): ya

✨ Saya menebak: ELANG
Apakah tebakan saya benar?
(ya/tidak): tidak

Hmm, saya tidak tahu. Mari kita belajar bersama!
Apa yang Anda pikirkan? burung hantu

Berikan pertanyaan yang membedakan 'burung hantu' dengan 'elang':
apakah dia aktif di malam hari

Untuk 'burung hantu', apakah jawabannya 'ya'?
(ya/tidak): ya

✨ Terima kasih! Saya sekarang tahu tentang 'burung hantu'!
```

## 📁 File & Struktur

```
akinator/
├── akinator.py              # Program utama
├── ollama_integration.py    # Integration dengan Ollama 🆕
├── akinator_db.json         # Database pohon keputusan (auto-generated)
├── akinator_stats.json      # Statistik permainan (auto-generated)
├── README.md               # File ini
├── OLLAMA_SETUP.md         # Panduan setup Ollama 🆕
└── requirements.txt        # Dependencies (optional)
```

## 🤖 AI Features (Ollama Integration) 🆕

### Apa itu Ollama?
Ollama adalah tool untuk menjalankan Large Language Model (LLM) lokal atau di cloud. Kita gunakan untuk auto-generate dan improve database Akinator!

### Keuntungan
- ✅ Generate database Indonesia dengan **30-40+ items**
- ✅ Tidak perlu manual isi satu-satu
- ✅ AI buat pertanyaan yang smart dan relevant
- ✅ Bisa improve database yang ada
- ✅ Bisa pakai Ollama lokal ATAU dari Google Colab

### Setup (Super Simple!)

**Opsi 1: Lokal**
```bash
# 1. Download Ollama dari https://ollama.ai
# 2. Run: ollama serve
# 3. Di Akinator pilih menu 7, input: http://localhost:11434
done!
```

**Opsi 2: Google Colab (Recommended)**
```python
# Di Colab, setup Ollama + ngrok
# Dapat public URL: https://abc123.ngrok.io
# Di Akinator pilih menu 7, input URL tersebut
done!
```

Baca panduan lengkap di: [OLLAMA_SETUP.md](OLLAMA_SETUP.md)

### Cara Pakai
```
Menu Utama
5. Generate Database dengan AI  ← Buat database baru
6. Improve Database dengan AI   ← Tambah items ke database existing
7. Config Ollama URL            ← Setup koneksi ke Ollama
```

## 💾 Database

### Lokasi
- **akinator_db.json** - Menyimpan pohon keputusan
- **akinator_stats.json** - Menyimpan statistik permainan

### Struktur Pohon Keputusan
```json
{
  "type": "question",
  "question": "Pertanyaan di sini?",
  "yes": {
    "type": "question atau guess",
    ...
  },
  "no": {
    "type": "question atau guess",
    ...
  }
}
```

### Struktur Statistik
```json
{
  "total_games": 5,
  "correct_guesses": 4,
  "wrong_guesses": 1,
  "new_learns": 3,
  "total_items": 15,
  "total_nodes": 28
}
```

## 🎯 Tips & Trik

### Untuk Pemain
- ✅ Jawab pertanyaan dengan **jujur** untuk hasil terbaik
- ✅ Berikan pertanyaan yang **spesifik** saat mengajar
- ✅ Semakin sering bermain = Akinator semakin **pintar**
- ✅ Lihat database untuk melihat apa yang sudah dipelajari

### Untuk Mengajar Akinator
- Pastikan pertanyaan Anda **membedakan** item baru dari yang salah ditebak
- Gunakan pertanyaan yang **tidak ambigu**
- Jangan gunakan nama spesifik dalam pertanyaan
- Contoh baik: "Apakah ia hidup di laut?" vs Contoh buruk: "Apakah ia paus?"

## 📊 Melihat Statistik

Pilih **"2. Lihat Statistik"** untuk melihat:
- Total permainan yang dimainkan
- Jumlah tebakan benar/salah
- Persentase akurasi
- Total item yang dipelajari
- Berapa kali Akinator belajar hal baru

## 🔄 Reset Database

Jika ingin memulai dari awal, pilih **"4. Reset Database"** untuk:
- Mengembalikan semua pertanyaan ke default
- Menghapus semua pembelajaran sebelumnya
- Mereset statistik permainan

## 🐛 Troubleshooting

| Masalah | Solusi |
|---------|--------|
| KeyboardInterrupt | Program akan keluar dengan baik, tekan Ctrl+C |
| Database error | Hapus file `.json` dan jalankan ulang |
| Input tidak terbaca | Pastikan terminal support UTF-8 |

## 📊 Contoh Statistik

```
==================================================
📊 STATISTIK PERMAINAN
==================================================
Total Permainan Dimainkan: 5
Tebakan Benar: 4
Tebakan Salah: 1
Tingkat Akurasi: 80.0%
Total Item Dipelajari: 12
Total Node Dalam Database: 24
Pembelajaran Baru: 3
==================================================
```

## 🎓 Cara Kerja Algoritma

1. **Pohon Keputusan Biner** - Setiap pertanyaan membagi kemungkinan menjadi 2
2. **Learning Tree** - Ketika penebakan salah, tree berkembang dengan node baru
3. **Traversal** - Program melintasi tree berdasarkan jawaban user
4. **Persistance** - Database disimpan dalam JSON untuk pembelajaran berkelanjutan

## 📝 Lisensi

Bebas digunakan dan dimodifikasi untuk keperluan apapun.

---

## 🎮 Selamat Bermain!

Nikmati pengalaman bermain Akinator! Semakin sering bermain, semakin pintar AI kami! 🧠✨

Punya saran? Modifikasi kode sesuai kebutuhan Anda!
