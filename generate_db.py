#!/usr/bin/env python3
"""
Standalone script untuk generate Akinator database dengan Ollama
Jalankan: python generate_db.py
"""

import os
import json
import sys
from ollama_integration import OllamaIntegration

def print_header(text):
    """Print header dengan styling"""
    print("\n" + "=" * 60)
    print(f"  {text}")
    print("=" * 60)

def main():
    print_header("🚀 AKINATOR - DATABASE GENERATOR")
    
    print("""
Workflow:
1. Setup koneksi ke Ollama
2. Generate database Indonesia dengan AI
3. Simpan ke akinator_db.json
4. Ready to play! 🎮

Persiapan:
✓ Ollama sudah running? (lokal atau di Colab)
✓ Public URL sudah siap? (kalau pakai ngrok dari Colab)
""")
    
    # === STEP 1: Input Ollama URL ===
    print_header("STEP 1️⃣: Koneksi ke Ollama")
    
    print("""
Pilih:
1. Lokal (http://localhost:11434)
2. Colab dengan ngrok (https://...)
3. Custom URL
    """)
    
    choice = input("Pilih (1-3): ").strip()
    
    if choice == '1':
        ollama_url = "http://localhost:11434"
        print(f"✅ URL: {ollama_url}")
    elif choice == '2':
        ollama_url = input("\nPaste public URL dari Colab ngrok: ").strip()
        if not ollama_url:
            print("❌ URL kosong!")
            return
        ollama_url = ollama_url.rstrip('/')
    elif choice == '3':
        ollama_url = input("\nMasukkan custom URL: ").strip().rstrip('/')
        if not ollama_url:
            print("❌ URL kosong!")
            return
    else:
        print("❌ Pilihan tidak valid!")
        return
    
    # === STEP 2: Init Ollama ===
    print_header("STEP 2️⃣: Testing Koneksi")
    
    ollama = OllamaIntegration(base_url=ollama_url)
    
    print(f"🔍 Coba connect ke {ollama_url}...")
    
    if not ollama.test_connection():
        print(f"""
❌ KONEKSI GAGAL!

Pastikan:
1. Ollama sudah running
   - Lokal: jalankan 'ollama serve'
   - Colab: cell sudah running
   
2. URL benar: {ollama_url}

3. Internet stabil

Coba lagi? (y/n): """, end="")
        if input().lower() != 'y':
            return
        
        if not ollama.test_connection():
            print("❌ Masih gagal. Exit.")
            return
    
    print("✅ Koneksi berhasil!\n")
    
    # === STEP 3: Pilih model ===
    print_header("STEP 3️⃣: Pilih Model")
    
    print("""
Model options:
1. llama2 (balanced, recommended)
2. neural-chat (faster)
3. mistral (higher quality, slower)
4. Custom model
    """)
    
    model_choice = input("Pilih (1-4): ").strip()
    
    if model_choice == '1':
        model = "llama2"
    elif model_choice == '2':
        model = "neural-chat"
    elif model_choice == '3':
        model = "mistral"
    elif model_choice == '4':
        model = input("Model name: ").strip() or "llama2"
    else:
        model = "llama2"
    
    ollama.set_model(model)
    print(f"✅ Model: {model}\n")
    
    # === STEP 3.5: Pilih size ===
    print_header("STEP 3.5️⃣: Pilih Ukuran Database")
    
    print("""
Database size options:
1. small   (30-50 items, ~50KB)      - Quick generate
2. medium  (100-200 items, ~200KB)   - Balanced (default)
3. large   (300-500 items, ~500KB)   - Comprehensive
4. xlarge  (500-1000+ items, ~2MB+)  - MASSIVE (untuk 1 juta character!)
    """)
    
    size_choice = input("Pilih (1-4, default 2): ").strip() or "2"
    
    if size_choice == '1':
        db_size = "small"
    elif size_choice == '2':
        db_size = "medium"
    elif size_choice == '3':
        db_size = "large"
    elif size_choice == '4':
        db_size = "xlarge"
    else:
        db_size = "medium"
    
    print(f"✅ Size: {db_size.upper()}\n")
    
    # === STEP 4: Generate Database ===
    print_header("STEP 4️⃣: Generate Database Indonesia")
    
    print(f"""
⚠️  PERHATIAN:
- Proses ini bisa memakan waktu sesuai size database
- Size {db_size.upper()}:
  • small:  1-2 menit
  • medium: 2-4 menit
  • large:  4-8 menit
  • xlarge: 8-15+ menit
- Internet speed mempengaruhi!
- Jangan tutup script sampai selesai!

Mulai generate? (y/n): """, end="")
    
    if input().lower() != 'y':
        print("Dibatalkan.")
        return
    
    print(f"""
🤖 Generating database Indonesia ({db_size.upper()})...
⏳ Processing dengan AI...\n""")
    
    database = ollama.generate_indonesian_database(size=db_size)
    
    if not database:
        print("""
❌ GAGAL GENERATE!

Kemungkinan:
1. Model tidak tersedia
2. Timeout (internet/server lambat)
3. Ollama error

Coba lagi? (y/n): """, end="")
        if input().lower() == 'y':
            main()
        return
    
    # === STEP 5: Validate & Save ===
    print_header("STEP 5️⃣: Validasi & Simpan")
    
    print("🔍 Validating database structure...")
    
    # Validate
    def validate_tree(node):
        if "type" not in node:
            return False
        if node["type"] == "question":
            return "question" in node and "yes" in node and "no" in node
        elif node["type"] == "guess":
            return "guess" in node
        return False
    
    if not validate_tree(database):
        print("❌ Database structure tidak valid!")
        return
    
    print("✅ Database valid!\n")
    
    # Count items
    def count_items(node):
        if node["type"] == "guess":
            return 1
        count = 0
        if "yes" in node:
            count += count_items(node["yes"])
        if "no" in node:
            count += count_items(node["no"])
        return count
    
    def count_nodes(node):
        count = 1
        if node["type"] == "question":
            if "yes" in node:
                count += count_nodes(node["yes"])
            if "no" in node:
                count += count_nodes(node["no"])
        return count
    
    items = count_items(database)
    nodes = count_nodes(database)
    
    print(f"📊 Database stats:")
    print(f"   - Total items: {items}")
    print(f"   - Total nodes: {nodes}")
    print(f"   - Tree depth: {_get_depth(database)}")
    
    # Save to file
    db_file = 'akinator_db.json'
    
    try:
        with open(db_file, 'w', encoding='utf-8') as f:
            json.dump(database, f, ensure_ascii=False, indent=2)
        
        print(f"\n✅ Disimpan ke: {db_file}")
    except Exception as e:
        print(f"\n❌ Error saat menyimpan: {e}")
        return
    
    # === SELESAI ===
    print_header("✨ SELESAI!")
    
    print(f"""
DATABASE BERHASIL DI-GENERATE! 🎉

File: {db_file}
Items: {items}
Nodes: {nodes}

SELANJUTNYA:
$ python akinator.py
→ Pilih menu "1. Mulai Permainan Baru"
→ Nikmati game dengan database Indonesia! 🎮

Tips:
- Jika ingin improve, gunakan menu 6 di akinator.py
- Jika ingin reset, bisa gunakan menu 4
- Database disimpan otomatis saat ada pembelajaran baru

Enjoy! 🚀✨
""")

def _get_depth(node, current=0):
    """Get tree depth"""
    if node["type"] == "guess":
        return current + 1
    
    max_depth = current + 1
    if "yes" in node:
        max_depth = max(max_depth, _get_depth(node["yes"], current + 1))
    if "no" in node:
        max_depth = max(max_depth, _get_depth(node["no"], current + 1))
    
    return max_depth

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Dibatalkan oleh user.")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
