╔══════════════════════════════════════════════════════════════════════════╗
║                                                                          ║
║                  🎮 AKINATOR - QUICK REFERENCE GUIDE 🎮                ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝


🎯 APA YANG PERLU KAMU TAHU:
═══════════════════════════════════════════════════════════════════════════

Akinator adalah AI game tanya-jawab yang:
  ✓ Menebak apa yang Anda pikirkan
  ✓ Belajar dari gameplay
  ✓ Focus niche Indonesia
  ✓ Menggunakan Ollama (AI lokal)


🚀 CARA PAKAI (3 LANGKAH SEDERHANA):
═══════════════════════════════════════════════════════════════════════════

STEP 1: GENERATE DATABASE
─────────────────────────────────────────────────────────────────────────

  Command:
  $ python generate_db.py

  Proses:
  1. Input URL Ollama (lokal atau Colab)
  2. Pilih model AI
  3. Tunggu generate (2-5 menit)
  4. Database jadi! ✅

  Output:
  - akinator_db.json (database baru)


STEP 2: PLAY GAME
─────────────────────────────────────────────────────────────────────────

  Command:
  $ python akinator.py

  Pilih menu:
  $ 1. Mulai Permainan Baru

  Proses:
  1. Think of something
  2. Answer AI's yes/no questions
  3. AI tries to guess
  4. AI either wins or learns


STEP 3: ENJOY!
─────────────────────────────────────────────────────────────────────────

  Hasil:
  ✅ AI menebak dengan benar → You win!
  ❌ AI salah → Teach AI → Database grows!

  Setiap kali bermain → AI semakin pintar 🧠


📊 WORKFLOW DIAGRAM:
═══════════════════════════════════════════════════════════════════════════

  Setup Ollama (Colab/Lokal)
         ↓
  python generate_db.py
         ↓
  akinator_db.json created ✅
         ↓
  python akinator.py
         ↓
  Play! Think of something
         ↓
    Answer Questions
         ↓
  AI Makes Guess
         ↓
    ┌─────────────┬──────────────┐
    ↓             ↓
  Correct?    Wrong?
    ✅            ❌
    └─────────────┴──────────────┐
         ↓              ↓
     You win!       Teach AI
                   (Ask question)
                         ↓
                   Database Updated
                         ↓
                    Play Again! 🔄


🔗 OLLAMA SETUP (PILIH 1):
═══════════════════════════════════════════════════════════════════════════

OPSI A: GOOGLE COLAB (RECOMMENDED!) ⭐
─────────────────────────────────────

  Buka Google Colab, jalankan:

  # Cell 1
  !curl https://ollama.ai/install.sh | sh
  !ollama pull llama2

  import subprocess, threading, time

  def run_ollama():
      subprocess.run(['ollama', 'serve'], check=False)

  thread = threading.Thread(target=run_ollama, daemon=True)
  thread.start()
  time.sleep(15)

  # Cell 2
  !pip install pyngrok
  from pyngrok import ngrok

  public_url = ngrok.connect(11434)
  print(f"✨ URL: {public_url}")

  Hasilnya:
  → URL Colab (simpan!)
  → Gunakan di generate_db.py

  Keuntungan:
  ✓ Tidak perlu install apapun
  ✓ Free GPU from Google
  ✓ Cepat dan reliable


OPSI B: LOKAL (Alternative)
─────────────────────────────

  1. Download Ollama: https://ollama.ai
  2. Install & jalankan:
     $ ollama serve

  3. Terminal lain:
     $ ollama pull llama2

  4. Di generate_db.py:
     URL: http://localhost:11434

  Keuntungan:
  ✓ Private (no internet di mid-game)
  ✓ Lebih cepat
  ✓ Offline capable

  Kekurangan:
  ✗ Harus install Ollama
  ✗ Pakai resource PC


🎮 SAAT BERMAIN:
═══════════════════════════════════════════════════════════════════════════

Pertanyaan dari AI:
  "Apakah itu makhluk hidup?"

Jawab jujur:
  "ya" atau "tidak"

AI menebak salah?
  Jawab pertanyaan pembelajaran:
  "Apa yang Anda pikirkan?" → manusia
  "Pertanyaan pembeda?" → "Apakah ia memiliki 2 kaki?"
  "Untuk manusia, jawabannya ya?" → ya

Database terupdate! 🧠

Next time AI lebih pintar!


📊 LIHAT PROGRESS:
═══════════════════════════════════════════════════════════════════════════

Di akinator.py, pilih:

  Menu 2: Lihat Statistik
  ├── Total permainan: 5
  ├── Tebakan benar: 4
  ├── Tebakan salah: 1
  ├── Akurasi: 80%
  ├── Items: 15
  └── Pembelajaran baru: 3

  Menu 3: Lihat Database
  └── Full tree structure dalam terminal


🔧 FITUR LANJUT (OPTIONAL):
═══════════════════════════════════════════════════════════════════════════

Dari akinator.py:

  Menu 4: Reset Database
  → Kembali ke database default

  Menu 5: Generate Ulang dengan AI
  → Buat database baru dari nol

  Menu 6: Improve Database dengan AI
  → Tambah 10-15 items baru

  Menu 7: Config Ollama URL
  → Ubah koneksi Ollama


📁 FILE YANG ADA:
═══════════════════════════════════════════════════════════════════════════

  RUN THESE:
  ✅ generate_db.py       - Generate database
  ✅ akinator.py          - Play the game

  OPTIONAL:
  ⭐ demo_ollama.py       - Test Ollama connection

  LIBRARIES (auto-imported):
  📚 ollama_integration.py - Ollama API client

  AUTO-CREATED:
  💾 akinator_db.json     - Database
  📊 akinator_stats.json  - Statistics

  DOCUMENTATION:
  📖 README.md            - Full features
  📖 QUICKSTART.md        - Quick setup
  📖 OLLAMA_SETUP.md      - Ollama guide
  📖 WORKFLOW.md          - Workflow details
  📖 COMPLETE_GUIDE.md    - Everything explained
  📖 QUICK_REFERENCE.md   - This file!


❓ COMMON QUESTIONS:
═══════════════════════════════════════════════════════════════════════════

Q: Apa bedanya generate_db.py dan akinator.py?
A: 
  generate_db.py  → Hanya untuk generate database (simple & fast)
  akinator.py     → Game lengkap dengan menu (flexible)

Q: Harus online terus saat bermain?
A: 
  Tidak! Setelah database generated, game bisa offline.
  Online hanya saat generate/improve database.

Q: Database bisa hilang?
A: 
  Aman! Disimpan di akinator_db.json
  Backup dengan copy file kalau takut.

Q: Bisa modify database manual?
A: 
  Bisa! Edit akinator_db.json dengan text editor.
  Tapi harus valid JSON format.

Q: AI selalu salah?
A: 
  Normal di awal! Setelah 20+ games, accuracy naik.
  Atau improve database dengan AI.

Q: Model LLM mana yang terbaik?
A: 
  llama2   → balanced (recommended)
  mistral  → lebih akurat (lebih lambat)
  neural   → lebih cepat (kurang akurat)


⚡ TROUBLESHOOTING:
═══════════════════════════════════════════════════════════════════════════

Problem                      Solution
──────────────────────────────────────────────────────────────────────────
"No module named requests"   $ pip install requests

"Connection failed"          - Pastikan Ollama running
                            - URL benar?
                            - Firewall?

"Timeout"                    - Coba model lebih kecil
                            - Internet lebih stabil
                            - Timeout lama (5 menit)

"Invalid JSON"               - Regenerate database
                            - Coba model lain
                            - Restart Ollama

"File permission error"      - Run dari folder yang tepat
                            - Pastikan write permission

"Memory full"                - Ollama gunakan RAM
                            - Ada aplikasi lain running?
                            - Restart Ollama


🎯 RECOMMENDED WORKFLOW (First Time):
═══════════════════════════════════════════════════════════════════════════

Time: ~15 minutes total

  0-5 min    → Setup Ollama di Colab
  5-10 min   → Run generate_db.py (generate database)
  10-15 min  → Run akinator.py (play!)

Hasil:
  ✅ Database Indonesia siap
  ✅ AI game functional
  ✅ Ready to improve iteratively


💡 PRO TIPS:
═══════════════════════════════════════════════════════════════════════════

  1. Generate MULTIPLE TIMES
     → Coba generate 2-3x, pilih yang terbaik

  2. Improve ITERATIVELY
     → Jangan reset, improve terus (database grows)

  3. Play OFTEN
     → Semakin sering main, AI semakin pintar

  4. Check DATABASE structure
     → Menu 3 shows full tree (understand algorithm)

  5. Backup your data
     → Copy akinator_db.json sebelum reset


📚 BELAJAR LEBIH LANJUT:
═══════════════════════════════════════════════════════════════════════════

File                    Untuk
──────────────────────────────────────────────────────────────────────────
README.md              Fitur lengkap & mechanics
QUICKSTART.md          Setup super cepat
OLLAMA_SETUP.md        Detail Ollama setup
WORKFLOW.md            Detailed workflows & architecture
COMPLETE_GUIDE.md      Everything explained!


🚀 SIAP MAIN?
═══════════════════════════════════════════════════════════════════════════

Quick Start Checklist:

  ☐ Setup Ollama (Colab atau lokal)
  ☐ Dapatkan URL Ollama
  ☐ $ python generate_db.py
  ☐ Input URL Ollama
  ☐ Tunggu database generate
  ☐ $ python akinator.py
  ☐ Menu 1: Mulai Permainan
  ☐ PLAY! 🎮

Go! 🚀✨


╔══════════════════════════════════════════════════════════════════════════╗
║                                                                          ║
║    Enjoy AI Akinator! Semakin sering main, semakin pintar AI kami! 🧠   ║
║                                                                          ║
║                          Happy Gaming! 🎮✨                              ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
