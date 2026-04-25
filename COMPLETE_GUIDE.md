# 🎮 AKINATOR - COMPLETE GUIDE

Panduan lengkap untuk memahami dan menggunakan Akinator dengan AI!

---

## 🤔 Apa itu Akinator?

**Akinator** adalah game tanya-jawab interaktif di mana:
- 🎯 AI bertanya ya/tidak untuk menebak apa yang Anda pikirkan
- 🧠 Database terus berkembang saat Anda bermain
- 🇮🇩 Niche Indonesia (makanan, budaya, tokoh, hewan lokal)
- 🤖 Powered by Ollama (local LLM)

---

## 🚀 Quick Start (3 Steps!)

### Step 1: Generate Database
```bash
python generate_db.py
```
- Input URL Ollama (lokal atau Colab)
- Tunggu 2-5 menit
- Database Indonesia siap! ✅

### Step 2: Play
```bash
python akinator.py
```
- Pilih "1. Mulai Permainan Baru"
- Think of something
- Answer yes/no questions
- AI tries to guess! 🎯

### Step 3: Enjoy!
- Jika AI benar → 🎉
- Jika AI salah → Teach it! 📚

---

## 📊 System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     AKINATOR SYSTEM                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Frontend (Terminal UI)                                     │
│  ├── akinator.py (Main game loop)                          │
│  ├── Menu system (Play, Stats, Database, Reset)            │
│  ├── Game loop (Questions → Guesses → Learning)            │
│  └── Error handling (Graceful exit, input validation)      │
│                                                             │
│  Backend (Database & Logic)                                │
│  ├── Binary Decision Tree (pohon keputusan biner)          │
│  ├── Tree traversal (Yes/No → next node)                   │
│  ├── Tree update (Add new nodes when learning)             │
│  └── Persistence (Save to JSON)                            │
│                                                             │
│  AI Module                                                  │
│  ├── ollama_integration.py (Ollama API client)             │
│  ├── generate_db.py (Standalone generator)                 │
│  ├── Prompt engineering (Custom prompts untuk Indonesia)   │
│  └── JSON parsing (Parse AI responses)                     │
│                                                             │
│  Storage                                                    │
│  ├── akinator_db.json (Binary tree)                        │
│  └── akinator_stats.json (Game statistics)                 │
│                                                             │
│  External Services                                          │
│  └── Ollama API (Local atau Cloud via ngrok)               │
│      ├── Lokal: http://localhost:11434                     │
│      └── Cloud: https://xxx.ngrok.io                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 📁 File Structure

| File | Purpose | Run? |
|------|---------|------|
| `akinator.py` | Main game with full menu | ✅ YES |
| `generate_db.py` | Standalone DB generator | ✅ YES |
| `ollama_integration.py` | Ollama API client (lib) | ❌ No |
| `demo_ollama.py` | Demo/testing script | ✅ Optional |
| `akinator_db.json` | Database (auto-created) | ❌ No |
| `akinator_stats.json` | Stats (auto-created) | ❌ No |
| `README.md` | Feature documentation | 📖 Read |
| `QUICKSTART.md` | Quick setup guide | 📖 Read |
| `OLLAMA_SETUP.md` | Detailed Ollama setup | 📖 Read |
| `WORKFLOW.md` | Workflow & usage patterns | 📖 Read |
| `requirements.txt` | Dependencies list | Install |

---

## 🎯 Two Main Workflows

### **Workflow A: Standalone Generator (Fastest)**

```
generate_db.py
    ↓
[Interactive prompts]
    ↓
Config Ollama + Choose model
    ↓
AI generates database
    ↓
akinator_db.json created
    ↓
python akinator.py
    ↓
Start playing! 🎮
```

**Pros:** Fast, focused, simple
**Cons:** Only generates, doesn't have menu options

**When to use:** Just want to generate DB and play

---

### **Workflow B: Menu-Based (Flexible)**

```
akinator.py
    ↓
MENU:
  1. Play game
  2. View stats
  3. View database
  4. Reset database
  5. Generate new DB with AI
  6. Improve existing DB with AI
  7. Config Ollama URL
  8. Exit
    ↓
Many options available
```

**Pros:** Flexible, many features, can improve DB
**Cons:** Slightly more complex

**When to use:** Want more control, improve DB iteratively

---

## 🌳 Database: Binary Decision Tree

### Structure
```json
{
  "type": "question",
  "question": "Apakah itu makhluk hidup?",
  "yes": {
    "type": "question",
    "question": "Apakah itu hewan?",
    "yes": {
      "type": "guess",
      "guess": "kucing"
    },
    "no": {
      "type": "guess",
      "guess": "pohon"
    }
  },
  "no": {
    "type": "guess",
    "guess": "mobil"
  }
}
```

### How it works
```
Start at root
    ↓
Ask question
    ↓
User says YES → Go to "yes" branch
User says NO → Go to "no" branch
    ↓
Repeat until reach leaf node
    ↓
Leaf node contains "guess"
    ↓
Ask: "Correct?"
    ↓
If NO → Learn new node
```

### Learning (Auto Tree Update)
```
Wrong guess: "kucing"
Correct answer: "singa"
Distinguishing Q: "Apakah ia hewan buas?"

Tree updated:
Old leaf "kucing" becomes:
{
  "type": "question",
  "question": "Apakah ia hewan buas?",
  "yes": {"type": "guess", "guess": "singa"},
  "no": {"type": "guess", "guess": "kucing"}
}

Next time AI is smarter! 🧠
```

---

## 🤖 Ollama Integration

### What is Ollama?
- Local LLM (Language Model) runner
- Can run local atau di cloud
- Good for generating, improving database
- No API key needed (lokal)

### Connection Options

**Option 1: Lokal**
```
Ollama di PC yang sama
✓ Private, no internet needed
✗ Need to install Ollama
✗ Uses PC resources (RAM/GPU)
```

**Option 2: Cloud (Google Colab)**
```
Ollama di Colab, accessed via ngrok
✓ No local installation
✓ Free GPU from Google
✓ Easy to share
✗ Need active Colab session
```

### Database Generation
```
You provide:
- URL to Ollama
- Model name (llama2, mistral, etc)

Ollama provides:
- Indonesian-focused database
- 30-40+ items auto-generated
- Smart yes/no questions
```

---

## 🎮 Playing the Game

### Game Loop
```
1. Think of something
2. Answer yes/no questions honestly
3. AI narrows down possibilities
4. AI makes a guess

Outcome:
A) Correct guess → 🎉 AI wins!
B) Wrong guess → 📚 Teach AI

If teaching:
- Tell correct answer
- Give distinguishing question
- Answer whether new answer would be "yes"
- Tree is updated! 📈
```

### Example Game
```
Q: Apakah itu makhluk hidup?
A: Ya

Q: Apakah itu hewan?
A: Tidak

Q: Apakah ia memiliki daun?
A: Ya

Guess: Pohon
A: Tidak, itu pohon pisang!

Q: Pohon dengan daun kecil atau besar?
A: Daun besar

Contoh pembeda: "Apakah ia buah-buahan?"
A: Ya

Tree updated! Next time lebih pintar 🧠
```

---

## 📊 Statistics Tracking

### Auto-tracked metrics
- `total_games` - Total permainan dimainkan
- `correct_guesses` - Tebakan AI yang benar
- `wrong_guesses` - Tebakan AI yang salah
- `accuracy` - Persentase akurasi
- `new_learns` - Berapa kali AI belajar hal baru
- `total_items` - Jumlah items dalam database
- `total_nodes` - Jumlah nodes di tree

### View stats
```
python akinator.py
→ Menu 2: Lihat Statistik
```

---

## ⚙️ Advanced Features

### Improve Existing Database
```
AI sudah punya 30 items?
Mau tambah lebih banyak?

python akinator.py
→ Menu 6: Improve Database dengan AI

AI akan:
✓ Analyze existing tree
✓ Add 10-15 new items
✓ Keep existing structure
✓ Expand possibilities!
```

### Reset to Default
```
Database jadi berantakan?
Mau reset?

python akinator.py
→ Menu 4: Reset Database

Will restore default tree:
- 15-20 items saja
- Balik ke awal
- Stats direset
```

### View Database Structure
```
Penasaran database lo gimana?

python akinator.py
→ Menu 3: Lihat Database

Shows full tree dalam terminal!
```

---

## 🐛 Troubleshooting

### "ImportError: No module named requests"
```
Solution:
pip install requests
```

### "Connection refused"
```
Check:
✓ Ollama running? (ollama serve)
✓ URL correct?
✓ Port 11434 open?
```

### "Timeout during generation"
```
Try:
✓ Smaller model (neural-chat)
✓ Better internet
✓ Longer timeout
✓ Check Ollama logs
```

### "JSON parse error"
```
Try:
✓ Regenerate DB
✓ Different model
✓ Adjust temperature in code
```

### "Wrong answers from AI"
```
Normal! AI learns via gameplay.
After playing 10+ games, accuracy improves.
```

---

## 💡 Tips & Tricks

### For Better Accuracy
1. ✅ Teach via gameplay (not just reset)
2. ✅ Give precise distinguishing questions
3. ✅ Play multiple games
4. ✅ Use improve feature to add more items

### For Better Performance
1. ✅ Use lokal Ollama (faster than Colab)
2. ✅ Choose fast model (neural-chat)
3. ✅ Keep database < 100 items (faster traversal)
4. ✅ Cache results

### For Development
1. ✅ Examine akinator_db.json structure
2. ✅ Run demo_ollama.py for testing
3. ✅ Check akinator_stats.json for metrics
4. ✅ Modify prompts in ollama_integration.py

---

## 🔗 Recommended Learning Path

### For Beginners
```
1. Read QUICKSTART.md (5 min)
2. Setup Ollama via Colab (5 min)
3. Run generate_db.py (5 min)
4. Run akinator.py (play!)
5. Check statistics (understand system)
6. Read WORKFLOW.md (understand flows)
```

### For Intermediate
```
1. Understand tree structure (WORKFLOW.md)
2. Play 20 games (AI learns)
3. Use improve feature (expand DB)
4. Check database structure (Menu 3)
5. Modify prompts (advanced)
```

### For Advanced
```
1. Understand ollama_integration.py code
2. Customize prompts for different topics
3. Add new features (API server, web UI)
4. Optimize tree traversal
5. Experiment with different models
```

---

## 🎓 Learning Outcomes

After using Akinator, you'll understand:
- 🌳 Binary decision trees
- 🤖 Local LLMs (Ollama)
- 💾 JSON data persistence
- 🧠 Machine learning via gameplay
- 🔄 Tree traversal algorithms
- 🎮 Game loop design
- 📊 Statistics tracking

---

## 🚀 Next Steps

1. **Install Ollama** (Choose: Lokal or Colab)
2. **Generate DB**: `python generate_db.py`
3. **Play game**: `python akinator.py`
4. **Improve**: Use menu or teach via gameplay
5. **Share**: Show friends your AI game!

---

## 📚 Documentation Map

```
COMPLETE_GUIDE.md (This file)
├── High-level concepts
├── System architecture
├── Workflows overview
└── Learning resources

README.md
├── Feature list
├── Basic usage
└── File structure

QUICKSTART.md
├── Setup instructions
├── Step-by-step guide
└── Troubleshooting

OLLAMA_SETUP.md
├── Detailed Ollama setup
├── Colab instructions
├── Model options

WORKFLOW.md
├── Workflow diagrams
├── Architecture flow
└── Command reference
```

---

## 📞 Support & Resources

### Check these if stuck:
1. QUICKSTART.md - Quick answers
2. OLLAMA_SETUP.md - Ollama issues
3. WORKFLOW.md - Architecture questions
4. demo_ollama.py - Test connection
5. akinator_db.json - Check database structure

### Common commands:
```bash
# Generate
python generate_db.py

# Play
python akinator.py

# Test Ollama
python demo_ollama.py

# Check syntax
python -m py_compile akinator.py

# View database
type akinator_db.json    # Windows
cat akinator_db.json     # Linux
```

---

## 🎉 You're Ready!

Semua sudah siap! Sekarang:

```bash
python generate_db.py  # Generate database
python akinator.py     # Play the game!
```

Enjoy! 🚀✨

---

**Last Updated:** April 2026
**Version:** 1.0
**Status:** ✅ Production Ready
