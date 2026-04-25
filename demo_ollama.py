"""
Demo script untuk menggunakan Ollama Integration
Jalankan: python demo_ollama.py
"""

from ollama_integration import OllamaIntegration
import json

def demo_local():
    """Demo dengan Ollama lokal"""
    print("=" * 50)
    print("DEMO: Ollama Integration (Lokal)")
    print("=" * 50)
    
    # Init Ollama
    ollama = OllamaIntegration()
    
    # Test connection
    print("\n1️⃣  Testing connection ke http://localhost:11434...")
    if ollama.test_connection():
        print("✅ Koneksi berhasil!")
    else:
        print("❌ Ollama tidak running di lokal")
        print("   Jalankan: ollama serve")
        return
    
    # Set model
    ollama.set_model("llama2")
    print(f"2️⃣  Model set ke: {ollama.model}")
    
    # Generate database
    print("\n3️⃣  Generate database Indonesia...")
    print("⏳ Tunggu (ini bisa sampai 5 menit)...\n")
    
    database = ollama.generate_indonesian_database()
    
    if database:
        print("✅ Database berhasil di-generate!")
        print(f"   Contoh struktur:")
        print(json.dumps(database, ensure_ascii=False, indent=2)[:500] + "...")
    else:
        print("❌ Gagal generate database")

def demo_colab():
    """Demo dengan Ollama dari Colab"""
    print("=" * 50)
    print("DEMO: Ollama Integration (Colab)")
    print("=" * 50)
    
    # Assume ngrok public URL
    public_url = input("\nMasukkan public URL dari Colab (e.g., https://abc123.ngrok.io): ").strip()
    
    if not public_url:
        print("URL kosong, skipping...")
        return
    
    # Init dengan custom URL
    ollama = OllamaIntegration(base_url=public_url)
    
    print(f"\n🔍 Testing connection ke {public_url}...")
    if ollama.test_connection():
        print("✅ Koneksi berhasil!")
    else:
        print("❌ Tidak bisa connect")
        print("   Pastikan:")
        print("   1. ngrok tunnel masih aktif")
        print("   2. Ollama masih running di Colab")
        print("   3. URL benar")
        return
    
    # Set model
    model = input("Model name (default: llama2): ").strip() or "llama2"
    ollama.set_model(model)
    
    # Generate
    print(f"\n🤖 Generate database dengan {model}...")
    print("⏳ Tunggu...\n")
    
    database = ollama.generate_indonesian_database()
    
    if database:
        print("✅ Database berhasil di-generate!")
        print(f"   Preview:")
        print(json.dumps(database, ensure_ascii=False, indent=2)[:500] + "...")
    else:
        print("❌ Gagal generate")

def demo_custom_prompt():
    """Demo generate dengan custom prompt"""
    print("=" * 50)
    print("DEMO: Custom Prompt Generation")
    print("=" * 50)
    
    ollama = OllamaIntegration()
    
    print("\n🔍 Testing connection...")
    if not ollama.test_connection():
        print("❌ Ollama tidak connected")
        return
    
    print("✅ Connected!\n")
    
    # Custom prompt
    custom_prompt = """
Buatkan 5 pertanyaan ya/tidak untuk membedakan:
1. Kupu-kupu vs Lalat
2. Nasi Goreng vs Mie Goreng
3. Kucing vs Bulan

Return sebagai JSON list: {"questions": ["q1", "q2", ...]}
"""
    
    print("📝 Sending custom prompt...")
    print("\n⏳ Generating...\n")
    
    try:
        import requests
        response = requests.post(
            ollama.api_endpoint,
            json={
                "model": "llama2",
                "prompt": custom_prompt,
                "stream": False,
            },
            timeout=60
        )
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Response dari AI:")
            print(result.get('response', '')[:500])
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("\n🎯 AKINATOR - OLLAMA INTEGRATION DEMO\n")
    
    print("Pilih demo:")
    print("1. Demo Lokal (Ollama di komputer)")
    print("2. Demo Colab (Ollama dengan ngrok)")
    print("3. Demo Custom Prompt")
    print("0. Exit")
    
    choice = input("\nPilih (0-3): ").strip()
    
    if choice == '1':
        demo_local()
    elif choice == '2':
        demo_colab()
    elif choice == '3':
        demo_custom_prompt()
    else:
        print("Exit")
    
    print("\n" + "=" * 50)
    print("Done!")
    print("=" * 50 + "\n")
