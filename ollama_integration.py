import requests
import json
from typing import Optional, List, Dict
import time

class OllamaIntegration:
    """Integration dengan Ollama untuk generate database AI"""
    
    def __init__(self, base_url: str = "http://localhost:11434"):
        self.base_url = base_url.rstrip('/')
        self.api_endpoint = f"{self.base_url}/api/generate"
        self.model = "llama2"  # Default model, bisa diganti
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
            
            # Count braces to figure out how many to close
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
        
        size: "small" (30-50), "medium" (100-200), "large" (500+), "xlarge" (1000+)
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
                import re
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

    def improve_database(self, current_database: dict) -> dict:
        """Improve existing database dengan AI"""
        print("\n🤖 Improving database dengan AI...")
        print("⏳ Processing...\n")
        
        db_str = json.dumps(current_database, ensure_ascii=False, indent=2)
        
        prompt = f"""
Perhatikan struktur pohon keputusan berikut:

{db_str[:2000]}

Tingkatkan dengan:
1. Tambahkan 10-15 item baru yang relevan dengan Indonesia
2. Perbaiki pertanyaan agar lebih distinguishing
3. Pastikan benar-benar pohon keputusan biner
4. Tambahkan lebih banyak kategori Indonesia (makanan, budaya, tokoh)

Return HANYA JSON yang valid dan lengkap, tidak ada teks lain.
"""

        try:
            response = requests.post(
                self.api_endpoint,
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False,
                },
                timeout=300
            )
            
            if response.status_code == 200:
                result = response.json()
                response_text = result.get('response', '')
                
                first_brace = response_text.find('{')
                
                if first_brace != -1:
                    json_str_partial = response_text[first_brace:]
                    try:
                        database, _ = json.JSONDecoder().raw_decode(json_str_partial)
                        print("✅ Database berhasil ditingkatkan!")
                        return database
                    except json.JSONDecodeError as e:
                        print(f"⚠️  Error parsing JSON: {e}")
                        return None
            return None
        except Exception as e:
            print(f"❌ Error: {e}")
            return None

    def generate_question_pair(self, item1: str, item2: str) -> Optional[str]:
        """Generate pertanyaan pembeda untuk 2 item"""
        prompt = f"""
Buatkan 1 pertanyaan ya/tidak yang membedakan:
- {item1}
- {item2}

Pertanyaan harus:
- Dalam bahasa Indonesia
- Singkat dan jelas
- Bukan pertanyaan yang terlalu spesifik

Return hanya pertanyaan saja, tanpa penjelasan.
"""
        try:
            response = requests.post(
                self.api_endpoint,
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False,
                },
                timeout=60
            )
            
            if response.status_code == 200:
                result = response.json()
                question = result.get('response', '').strip()
                if not question.endswith('?'):
                    question += '?'
                return question
            return None
        except Exception as e:
            print(f"Error generating question: {e}")
            return None
