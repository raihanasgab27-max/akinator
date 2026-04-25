#!/usr/bin/env python3
"""
🎭 Akinator Database Generator - Colab Version
Jalankan langsung di Google Colab untuk menghasilkan database Indonesia MASSIVE!
"""

import requests
import json
from typing import Optional

# ============================================================================
# OLLAMA INTEGRATION (inline, no external import needed)
# ============================================================================

class OllamaIntegration:
    """Integration dengan Ollama untuk generate database AI"""
    
    def __init__(self, base_url: str = "http://localhost:11434"):
        self.base_url = base_url.rstrip('/')
        self.api_endpoint = f"{self.base_url}/api/generate"
        self.model = "llama2"
        self.is_connected = False
        
    def test_connection(self) -> bool:
        """Test koneksi ke Ollama"""
        try:
            response = requests.get(
                f"{self.base_url}/api/tags",
                timeout=5
            )
            self.is_connected = response.status_code == 200
            return self.is_connected
        except Exception as e:
            print(f"❌ Tidak bisa connect ke Ollama: {e}")
            self.is_connected = False
            return False

    def set_model(self, model_name: str):
        """Set model yang digunakan"""
        self.model = model_name

    def _try_fix_json(self, json_str: str, error_pos: int) -> Optional[str]:
        """Try to fix common JSON errors by truncating at error position"""
        try:
            truncated = json_str[:error_pos]
            open_braces = truncated.count('{')
            close_braces = truncated.count('}')
            braces_to_close = open_braces - close_braces
            
            if braces_to_close > 0:
                open_brackets = truncated.count('[')
                close_brackets = truncated.count(']')
                brackets_to_close = open_brackets - close_brackets
                
                truncated += '}' * braces_to_close
                truncated += ']' * brackets_to_close
                
                try:
                    json.loads(truncated)
                    return truncated
                except:
                    pass
            
            return None
        except:
            return None

    def generate_indonesian_database(self, size: str = "medium") -> dict:
        """Generate database Akinator dengan niche Indonesia
        
        size: "small" (30-50), "medium" (100-200), "large" (300-500), "xlarge" (500-1000+)
        """
        print("\n🤖 Generating database Indonesia dengan AI...")
        print(f"📊 Size: {size.upper()}")
        print("⏳ Ini mungkin memakan waktu beberapa menit...\n")
        
        # Customize prompt based on size
        if size == "small":
            item_count = "30-50"
            description = "kecil tapi lengkap"
        elif size == "medium":
            item_count = "100-200"
            description = "medium dengan variety bagus"
        elif size == "large":
            item_count = "300-500"
            description = "besar dengan sub-category detail"
        elif size == "xlarge":
            item_count = "500-1000+"
            description = "MASSIVE dengan banyak sub-branches"
        else:
            item_count = "100-200"
            description = "medium"
        
        prompt = f"""⚠️  OUTPUT ONLY VALID JSON - NO OTHER TEXT!

Generate Akinator binary tree dalam JSON format PURE.
- Niche: INDONESIA (makanan, hewan, budaya, tokoh, landmark, selebriti)
- Items minimum: {item_count}
- Language: Bahasa Indonesia
- OUTPUT: ONLY JSON - NO MARKDOWN, NO EXPLANATION, NO OTHER TEXT!

STRICT JSON RULES:
1. All keys in double quotes: "type", "question", "yes", "no", "guess"
2. All string values in double quotes
3. Escaped quotes in strings: \\" not "
4. Commas between all key-value pairs (NO trailing commas)
5. Valid RFC 7159 JSON format

STRUCTURE (copy exactly):
{{
  "type": "question",
  "question": "Pertanyaan ya atau tidak?",
  "yes": {{ ... }},
  "no": {{ ... }}
}}
atau
{{
  "type": "guess",
  "guess": "Nama item"
}}

EXACT EXAMPLE:
{{
  "type": "question",
  "question": "Apakah dari Indonesia?",
  "yes": {{
    "type": "question",
    "question": "Apakah makanan?",
    "yes": {{"type": "guess", "guess": "soto ayam"}},
    "no": {{"type": "guess", "guess": "batik"}}
  }},
  "no": {{"type": "guess", "guess": "pizza"}}
}}

REQUIREMENTS:
✓ Minimum {item_count} items di leaf nodes
✓ Balanced tree (depth 8-12)
✓ Bahasa Indonesia semua
✓ HANYA JSON OUTPUT!
✓ Valid JSON (python -m json.tool harus pass)
✓ Start: {{ End: }}

CATEGORY IDEAS:
Makanan: soto ayam, rendang, lumpia, nasi kuning, gado-gado, satay, martabak, perkedel, ketoprak, bakso
Hewan: komodo, orangutan, badak jawa, harimau sumatra, gajah, cendrawasih, buaya, python, elang jawa
Budaya: batik, wayang, angklung, ketoprak, tari kecak, gamelan, sarong, ikat, tali temali
Tokoh: sukarno, joko widodo, susi pudjiastuti, bj habibie, megawati, gus dur, suharto
Landmark: borobudur, prambanan, taj mahal, candi ijo, tanah toraja, danau toba, bromo
Selebriti: deddy corbuzier, iko uwais, titi kamal, sienna guillory, gigi hadid

⚠️  FINAL WARNING:
OUTPUT ONLY JSON!
No markdown!
No explanations!
Start with {{ and end with }}
Valid JSON format!
"""

        try:
            response = requests.post(
                self.api_endpoint,
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False,
                    "temperature": 0.3,  # Lower temp untuk JSON lebih valid
                },
                timeout=300  # Timeout 5 menit
            )
            
            if response.status_code == 200:
                result = response.json()
                response_text = result.get('response', '')
                
                # Extract JSON - find first { and parse until first complete JSON object
                first_brace = response_text.find('{')
                
                if first_brace != -1:
                    json_str_partial = response_text[first_brace:]
                    try:
                        # Use raw_decode to extract exactly one complete JSON object
                        database, _ = json.JSONDecoder().raw_decode(json_str_partial)
                        print("✅ Database berhasil di-generate!")
                        return database
                    except json.JSONDecodeError as e:
                        print(f"⚠️  Error parsing JSON dari AI: {e}")
                        print("📝 Raw response (first 500 chars):")
                        print(response_text[:500])
                        print(f"\n🔧 Trying to fix JSON by truncating at error...")
                        
                        # Try to fix by truncating at error position
                        fixed_json = self._try_fix_json(json_str_partial, e.pos)
                        if fixed_json:
                            try:
                                database, _ = json.JSONDecoder().raw_decode(fixed_json)
                                print("✅ Fixed JSON berhasil di-parse!")
                                return database
                            except Exception as fix_error:
                                print(f"❌ Fixed JSON juga error: {fix_error}")
                        
                        return None
                else:
                    print("⚠️  Tidak bisa find '{' dalam response")
                    print("📝 Raw response:")
                    print(response_text[:500])
                    return None
            else:
                print(f"❌ Error dari Ollama: {response.status_code}")
                return None
                
        except requests.exceptions.Timeout:
            print("❌ Timeout - AI memakan waktu terlalu lama")
            return None
        except Exception as e:
            print(f"❌ Error generating database: {e}")
            return None


# ============================================================================
# DATABASE GENERATOR
# ============================================================================

def count_items_in_tree(node):
    """Count total items (leaf nodes) dalam tree"""
    if not node:
        return 0
    if node.get("type") == "guess":
        return 1
    
    count = 0
    if node.get("yes"):
        count += count_items_in_tree(node["yes"])
    if node.get("no"):
        count += count_items_in_tree(node["no"])
    return count


def count_nodes_in_tree(node):
    """Count total nodes dalam tree"""
    if not node:
        return 0
    
    count = 1
    if node.get("yes"):
        count += count_nodes_in_tree(node["yes"])
    if node.get("no"):
        count += count_nodes_in_tree(node["no"])
    return count


def get_tree_depth(node):
    """Get depth of tree"""
    if not node:
        return 0
    
    if node.get("type") == "guess":
        return 1
    
    yes_depth = get_tree_depth(node.get("yes"))
    no_depth = get_tree_depth(node.get("no"))
    
    return 1 + max(yes_depth, no_depth)


def fix_incomplete_tree(node, default_guess="Unknown"):
    """Fix incomplete tree nodes by filling missing branches with dummy guesses"""
    if not node:
        return {"type": "guess", "guess": default_guess}
    
    if node.get("type") == "guess":
        if not node.get("guess"):
            node["guess"] = default_guess
        return node
    
    if node.get("type") == "question":
        if not node.get("question"):
            # Incomplete question, convert to guess
            return {"type": "guess", "guess": default_guess}
        
        # Fix missing branches
        if not node.get("yes"):
            node["yes"] = {"type": "guess", "guess": "Something"}
        else:
            node["yes"] = fix_incomplete_tree(node["yes"], default_guess)
        
        if not node.get("no"):
            node["no"] = {"type": "guess", "guess": "Something else"}
        else:
            node["no"] = fix_incomplete_tree(node["no"], default_guess)
        
        return node
    
    # Unknown type, convert to guess
    return {"type": "guess", "guess": default_guess}


def validate_database(database):
    """Validate database structure"""
    if not database:
        return False, "Database kosong"
    
    if database.get("type") not in ["question", "guess"]:
        return False, "Invalid type"
    
    if database.get("type") == "question":
        if not database.get("question"):
            return False, "Question kosong"
        if not database.get("yes") or not database.get("no"):
            return False, "Missing yes/no branches"
        
        yes_valid, yes_msg = validate_database(database["yes"])
        if not yes_valid:
            return False, f"Yes branch: {yes_msg}"
        
        no_valid, no_msg = validate_database(database["no"])
        if not no_valid:
            return False, f"No branch: {no_msg}"
        
        return True, "OK"
    else:  # type == "guess"
        if not database.get("guess"):
            return False, "Guess kosong"
        return True, "OK"


def main():
    """Main function"""
    print("\n" + "="*60)
    print("  🎭 AKINATOR DATABASE GENERATOR - COLAB VERSION")
    print("="*60)
    
    print("\n📍 Ollama URL:")
    print("   Untuk Colab: http://localhost:11434 (default)")
    print("   Untuk lokal: http://localhost:11434")
    print("   Untuk custom: ketik URL-nya")
    
    ollama_url = input("\nInput Ollama URL (default: http://localhost:11434): ").strip()
    if not ollama_url:
        ollama_url = "http://localhost:11434"
    
    print(f"\n🔗 Testing connection ke {ollama_url}...")
    ollama = OllamaIntegration(ollama_url)
    
    if not ollama.test_connection():
        print("❌ Tidak bisa connect ke Ollama!")
        print("⚠️  Make sure Ollama is running on Colab!")
        return
    
    print("✅ Connected to Ollama!")
    
    # Get available models
    print("\n📦 Fetching available models...")
    try:
        response = requests.get(f"{ollama_url}/api/tags", timeout=5)
        if response.status_code == 200:
            models_data = response.json()
            models = [m.get("name", "") for m in models_data.get("models", [])]
            
            if models:
                print(f"\n✅ Available models ({len(models)}):")
                for i, model in enumerate(models, 1):
                    print(f"   {i}. {model}")
                
                model_choice = input(f"\nPilih model (1-{len(models)}, default: 1): ").strip()
                try:
                    model_idx = int(model_choice) - 1
                    if 0 <= model_idx < len(models):
                        selected_model = models[model_idx]
                        ollama.set_model(selected_model)
                        print(f"✅ Selected: {selected_model}")
                    else:
                        print(f"❌ Invalid choice, using default")
                        ollama.set_model(models[0])
                except:
                    ollama.set_model(models[0])
            else:
                print("⚠️  No models available!")
                model_name = input("Input model name: ").strip()
                if model_name:
                    ollama.set_model(model_name)
                else:
                    return
    except Exception as e:
        print(f"⚠️  Error fetching models: {e}")
        model_name = input("Input model name: ").strip()
        if model_name:
            ollama.set_model(model_name)
        else:
            return
    
    # Size selection
    print("\n" + "="*60)
    print("  STEP 3.5️⃣: Pilih Ukuran Database")
    print("="*60)
    
    print("\nDatabase size options:")
    print("1. small   (30-50 items, ~50KB)      - Quick generate")
    print("2. medium  (100-200 items, ~200KB)   - Balanced (default)")
    print("3. large   (300-500 items, ~500KB)   - Comprehensive")
    print("4. xlarge  (500-1000+ items, ~2MB+)  - MASSIVE (untuk 1 juta character!)")
    
    size_choice = input("\nPilih (1-4, default 2): ").strip()
    
    size_map = {
        "1": "small",
        "2": "medium",
        "3": "large",
        "4": "xlarge"
    }
    
    db_size = size_map.get(size_choice, "medium")
    print(f"✅ Size: {db_size.upper()}")
    
    # Confirm
    print("\n" + "="*60)
    print("  STEP 4️⃣: Generate Database Indonesia")
    print("="*60)
    
    print("\n⚠️  PERHATIAN:")
    print("- Proses ini bisa memakan waktu sesuai size database")
    print(f"- Size {db_size.upper()}:")
    size_times = {
        "small": "1-2 menit",
        "medium": "2-4 menit",
        "large": "4-8 menit",
        "xlarge": "8-15+ menit"
    }
    print(f"  • {size_times[db_size]}")
    print("- Internet speed mempengaruhi!")
    print("- Jangan tutup script sampai selesai!")
    
    confirm = input("\nMulai generate? (y/n): ").strip().lower()
    
    if confirm != 'y':
        print("\n⚠️  Dibatalkan oleh user.")
        return
    
    # Generate
    database = ollama.generate_indonesian_database(size=db_size)
    
    if not database:
        print("\n❌ GAGAL GENERATE!")
        print("\nKemungkinan:")
        print("1. Model tidak tersedia")
        print("2. Timeout (internet/server lambat)")
        print("3. Ollama error")
        return
    
    # Fix incomplete tree nodes
    print("\n🔧 Fixing incomplete tree nodes...")
    database = fix_incomplete_tree(database)
    print("✅ Tree fixed!")
    
    # Validate
    is_valid, msg = validate_database(database)
    
    if not is_valid:
        print(f"\n❌ Database structure still invalid: {msg}")
        print("⚠️  Trying with more aggressive fixing...")
        # Try again with default guess
        database = fix_incomplete_tree(database, "Unknown Item")
        is_valid, msg = validate_database(database)
        
        if not is_valid:
            print(f"❌ Still invalid: {msg}")
            return
        else:
            print("✅ Fixed successfully!")
    
    # Count stats
    items = count_items_in_tree(database)
    nodes = count_nodes_in_tree(database)
    depth = get_tree_depth(database)
    
    print("\n" + "="*60)
    print("  ✅ GENERATION SUCCESSFUL!")
    print("="*60)
    
    print(f"\n📊 Database Statistics:")
    print(f"   • Items (guesses): {items}")
    print(f"   • Nodes (questions + guesses): {nodes}")
    print(f"   • Depth: {depth}")
    
    # Estimate file size
    json_str = json.dumps(database, ensure_ascii=False, indent=2)
    file_size_kb = len(json_str.encode('utf-8')) / 1024
    
    print(f"   • File size: ~{file_size_kb:.1f} KB")
    print(f"   • Characters: ~{len(json_str):,}")
    
    # Save to file
    filename = f"akinator_db_{db_size}_{items}_items.json"
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(database, f, ensure_ascii=False, indent=2)
        
        print(f"\n💾 Saved to: {filename}")
        print(f"   Download file dari Colab!")
    except Exception as e:
        print(f"\n❌ Error saving file: {e}")
        print(f"\n📝 Database JSON:")
        print(json_str[:500] + "...")


if __name__ == "__main__":
    main()
