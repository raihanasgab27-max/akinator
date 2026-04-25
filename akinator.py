import json
import os
from typing import Optional
from datetime import datetime

try:
    from ollama_integration import OllamaIntegration
    OLLAMA_AVAILABLE = True
except ImportError:
    OLLAMA_AVAILABLE = False
    OllamaIntegration = None

class AkinatorGame:
    def __init__(self, database_file='akinator_db.json', stats_file='akinator_stats.json'):
        self.database_file = database_file
        self.stats_file = stats_file
        self.tree = self.load_database()
        self.current_node = self.tree
        self.question_history = []
        self.stats = self.load_stats()
        
        # Initialize Ollama integration
        self.ollama = None
        if OLLAMA_AVAILABLE:
            self.ollama = OllamaIntegration()
        self.ollama_url = "http://localhost:11434"

    def load_stats(self) -> dict:
        """Load game statistics"""
        if os.path.exists(self.stats_file):
            try:
                with open(self.stats_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return self.create_default_stats()
        else:
            return self.create_default_stats()

    def create_default_stats(self) -> dict:
        """Create default statistics"""
        return {
            "total_games": 0,
            "correct_guesses": 0,
            "wrong_guesses": 0,
            "new_learns": 0,
            "total_items": 0,
            "total_nodes": 0
        }

    def save_stats(self):
        """Save statistics to file"""
        with open(self.stats_file, 'w', encoding='utf-8') as f:
            json.dump(self.stats, f, ensure_ascii=False, indent=2)

    def load_database(self) -> dict:
        """Load the decision tree from JSON file or create default one"""
        if os.path.exists(self.database_file):
            try:
                with open(self.database_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Error loading database: {e}")
                return self.create_default_tree()
        else:
            return self.create_default_tree()

    def create_default_tree(self) -> dict:
        """Create default decision tree with more content"""
        return {
            "type": "question",
            "question": "Apakah itu makhluk hidup?",
            "yes": {
                "type": "question",
                "question": "Apakah itu hewan?",
                "yes": {
                    "type": "question",
                    "question": "Apakah itu bisa terbang?",
                    "yes": {
                        "type": "question",
                        "question": "Apakah itu termasuk burung elang/rajawali?",
                        "yes": {
                            "type": "guess",
                            "guess": "elang"
                        },
                        "no": {
                            "type": "guess",
                            "guess": "burung beo"
                        }
                    },
                    "no": {
                        "type": "question",
                        "question": "Apakah itu berkaki empat?",
                        "yes": {
                            "type": "question",
                            "question": "Apakah itu adalah hewan peliharaan?",
                            "yes": {
                                "type": "guess",
                                "guess": "kucing"
                            },
                            "no": {
                                "type": "guess",
                                "guess": "singa"
                            }
                        },
                        "no": {
                            "type": "guess",
                            "guess": "ular"
                        }
                    }
                },
                "no": {
                    "type": "guess",
                    "guess": "pohon"
                }
            },
            "no": {
                "type": "question",
                "question": "Apakah itu benda yang bisa bergerak?",
                "yes": {
                    "type": "question",
                    "question": "Apakah itu memiliki roda?",
                    "yes": {
                        "type": "guess",
                        "guess": "mobil"
                    },
                    "no": {
                        "type": "guess",
                        "guess": "pesawat terbang"
                    }
                },
                "no": {
                    "type": "question",
                    "question": "Apakah itu tempat tinggal/bangunan?",
                    "yes": {
                        "type": "guess",
                        "guess": "rumah"
                    },
                    "no": {
                        "type": "guess",
                        "guess": "uang"
                    }
                }
            }
        }

    def save_database(self):
        """Save the decision tree to JSON file"""
        with open(self.database_file, 'w', encoding='utf-8') as f:
            json.dump(self.tree, f, ensure_ascii=False, indent=2)
        self.update_stats()

    def count_items_in_tree(self, node: dict = None) -> int:
        """Count total items in the tree"""
        if node is None:
            node = self.tree
        
        if node["type"] == "guess":
            return 1
        else:
            count = 0
            if "yes" in node:
                count += self.count_items_in_tree(node["yes"])
            if "no" in node:
                count += self.count_items_in_tree(node["no"])
            return count

    def count_nodes_in_tree(self, node: dict = None) -> int:
        """Count total nodes in the tree"""
        if node is None:
            node = self.tree
        
        count = 1
        if node["type"] == "question":
            if "yes" in node:
                count += self.count_nodes_in_tree(node["yes"])
            if "no" in node:
                count += self.count_nodes_in_tree(node["no"])
        return count

    def update_stats(self):
        """Update stats based on current tree"""
        self.stats["total_items"] = self.count_items_in_tree()
        self.stats["total_nodes"] = self.count_nodes_in_tree()
        self.save_stats()

    def ask_question(self, question: str) -> bool:
        """Ask user a yes/no question and return their answer"""
        while True:
            try:
                response = input(f"\n{question}\n(ya/tidak): ").strip().lower()
                if response in ['ya', 'y']:
                    return True
                elif response in ['tidak', 't', 'n']:
                    return False
                else:
                    print("❌ Silakan jawab dengan 'ya' atau 'tidak'")
            except KeyboardInterrupt:
                print("\n\n⚠️  Permainan dihentikan oleh pengguna.")
                raise
            except EOFError:
                print("\n\n⚠️  Input error, permainan dihentikan.")
                raise

    def play_menu(self):
        """Show main menu"""
        print("\n" + "=" * 50)
        print("MENU UTAMA - AKINATOR")
        print("=" * 50)
        print("1. Mulai Permainan Baru")
        print("2. Lihat Statistik")
        print("3. Lihat Database")
        print("4. Reset Database")
        
        # Tambah menu Ollama jika available
        if OLLAMA_AVAILABLE:
            print("5. Generate Database dengan AI (Ollama)")
            print("6. Improve Database dengan AI")
            print("7. Config Ollama URL")
            print("8. Keluar")
        else:
            print("5. Keluar")
        
        print("=" * 50)
        
        max_option = '8' if OLLAMA_AVAILABLE else '5'
        
        while True:
            try:
                choice = input("Pilih opsi (1-" + max_option + "): ").strip()
                valid_choices = ['1', '2', '3', '4', '5']
                if OLLAMA_AVAILABLE:
                    valid_choices.extend(['6', '7', '8'])
                
                if choice in valid_choices:
                    return choice
                else:
                    print(f"❌ Pilihan tidak valid! (1-{max_option})")
            except KeyboardInterrupt:
                print("\n\n⚠️  Program dihentikan.")
                return '8' if OLLAMA_AVAILABLE else '5'
            except EOFError:
                print("\n\n⚠️  Input error.")
                return '8' if OLLAMA_AVAILABLE else '5'

    def config_ollama_url(self):
        """Configure Ollama URL"""
        print("\n" + "=" * 50)
        print("⚙️  CONFIG OLLAMA URL")
        print("=" * 50)
        print(f"URL saat ini: {self.ollama_url}")
        print("Contoh: http://localhost:11434")
        print("Atau: https://abc123.ngrok.io (dari Colab)")
        print("=" * 50)
        
        try:
            new_url = input("\nMasukkan URL Ollama (atau Enter untuk skip): ").strip()
            
            if new_url:
                # Normalize URL
                new_url = new_url.rstrip('/')
                
                # Test connection
                if self.ollama:
                    self.ollama.base_url = new_url
                    self.ollama.api_endpoint = f"{new_url}/api/generate"
                    
                    print("\n🔍 Testing connection...")
                    if self.ollama.test_connection():
                        self.ollama_url = new_url
                        print("✅ Koneksi berhasil!")
                        
                        # Ask for model
                        model = input("\nMasukkan model name (default: llama2): ").strip() or "llama2"
                        self.ollama.set_model(model)
                        print(f"✅ Model set ke: {model}")
                    else:
                        print(f"❌ Tidak bisa connect ke {new_url}")
                        print("Pastikan Ollama sudah running!")
            else:
                print("Skipped")
        except (KeyboardInterrupt, EOFError):
            print("\n⚠️  Config dibatalkan")

    def generate_database_with_ai(self):
        """Generate database baru dengan AI"""
        if not self.ollama:
            print("❌ Ollama tidak tersedia. Pastikan ollama_integration.py ada.")
            return
        
        if not self.ollama.is_connected:
            print("\n🔍 Testing koneksi ke Ollama...")
            if not self.ollama.test_connection():
                print("❌ Ollama tidak terhubung.")
                print(f"   Pastikan Ollama running di {self.ollama_url}")
                return
        
        try:
            # Ask for size
            print("\nPilih ukuran database:")
            print("1. small   (30-50 items)")
            print("2. medium  (100-200 items, default)")
            print("3. large   (300-500 items)")
            print("4. xlarge  (500-1000+ items, ~1 juta character!)")
            
            size_choice = input("\nPilih (1-4, default 2): ").strip() or "2"
            
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
            
            print(f"\n🤖 Generating {db_size.upper()} database...")
            
            # Generate database
            database = self.ollama.generate_indonesian_database(size=db_size)
            
            if database:
                # Validate database
                if self._validate_tree(database):
                    self.tree = database
                    self.save_database()
                    print("\n✅ Database baru berhasil disimpan!")
                    print(f"   Size: {db_size.upper()}")
                    print(f"   Total items: {self.count_items_in_tree()}")
                    print(f"   Total nodes: {self.count_nodes_in_tree()}")
                else:
                    print("❌ Database tidak valid")
            else:
                print("❌ Gagal generate database")
        except Exception as e:
            print(f"❌ Error: {e}")

    def improve_database_with_ai(self):
        """Improve existing database dengan AI"""
        if not self.ollama:
            print("❌ Ollama tidak tersedia.")
            return
        
        if not self.ollama.is_connected:
            print("\n🔍 Testing koneksi ke Ollama...")
            if not self.ollama.test_connection():
                print("❌ Ollama tidak terhubung.")
                return
        
        try:
            print("\nImproving database...")
            improved_db = self.ollama.improve_database(self.tree)
            
            if improved_db:
                if self._validate_tree(improved_db):
                    self.tree = improved_db
                    self.save_database()
                    print("✅ Database berhasil ditingkatkan!")
                    print(f"   Total items: {self.count_items_in_tree()}")
                else:
                    print("❌ Database tidak valid")
            else:
                print("❌ Gagal improve database")
        except Exception as e:
            print(f"❌ Error: {e}")

    def _validate_tree(self, tree: dict) -> bool:
        """Validate tree structure"""
        try:
            if "type" not in tree:
                return False
            
            if tree["type"] == "question":
                if "question" not in tree:
                    return False
                if "yes" not in tree or "no" not in tree:
                    return False
                return self._validate_tree(tree["yes"]) and self._validate_tree(tree["no"])
            elif tree["type"] == "guess":
                return "guess" in tree
            else:
                return False
        except:
            return False

        """Display game statistics"""
        print("\n" + "=" * 50)
        print("📊 STATISTIK PERMAINAN")
        print("=" * 50)
        print(f"Total Permainan Dimainkan: {self.stats['total_games']}")
        print(f"Tebakan Benar: {self.stats['correct_guesses']}")
        print(f"Tebakan Salah: {self.stats['wrong_guesses']}")
        
        if self.stats['total_games'] > 0:
            accuracy = (self.stats['correct_guesses'] / self.stats['total_games']) * 100
            print(f"Tingkat Akurasi: {accuracy:.1f}%")
        
        print(f"Total Item Dipelajari: {self.stats['total_items']}")
        print(f"Total Node Dalam Database: {self.stats['total_nodes']}")
        print(f"Pembelajaran Baru: {self.stats['new_learns']}")
        print("=" * 50 + "\n")

    def show_database(self):
        """Display database contents"""
        print("\n" + "=" * 50)
        print("📚 DATABASE AKINATOR")
        print("=" * 50)
        self._print_tree(self.tree, 0)
        print("=" * 50 + "\n")

    def _print_tree(self, node: dict, level: int = 0):
        """Recursively print tree structure"""
        indent = "  " * level
        if node["type"] == "question":
            print(f"{indent}❓ {node['question']}")
            if "yes" in node:
                print(f"{indent}  ✅ Ya:")
                self._print_tree(node["yes"], level + 2)
            if "no" in node:
                print(f"{indent}  ❌ Tidak:")
                self._print_tree(node["no"], level + 2)
        else:
            print(f"{indent}✨ {node['guess']}")

    def reset_database(self):
        """Reset database to default"""
        try:
            response = input("\n⚠️  Apakah Anda yakin ingin reset database? (ya/tidak): ").strip().lower()
            if response in ['ya', 'y']:
                self.tree = self.create_default_tree()
                self.save_database()
                self.stats = self.create_default_stats()
                self.save_stats()
                print("✅ Database berhasil di-reset ke default!")
            else:
                print("❌ Reset dibatalkan.")
        except (KeyboardInterrupt, EOFError):
            print("\n❌ Reset dibatalkan.")


    def play(self):
        """Main game loop with menu"""
        try:
            while True:
                choice = self.play_menu()
                
                if choice == '1':
                    self.start_game()
                elif choice == '2':
                    self.show_stats()
                elif choice == '3':
                    self.show_database()
                elif choice == '4':
                    self.reset_database()
                elif choice == '5':
                    if OLLAMA_AVAILABLE:
                        self.generate_database_with_ai()
                    else:
                        self.exit_game()
                        break
                elif choice == '6' and OLLAMA_AVAILABLE:
                    self.improve_database_with_ai()
                elif choice == '7' and OLLAMA_AVAILABLE:
                    self.config_ollama_url()
                elif choice == '8' and OLLAMA_AVAILABLE:
                    self.exit_game()
                    break
        except KeyboardInterrupt:
            self.exit_game()
        except Exception as e:
            print(f"\n❌ Terjadi kesalahan: {e}")
            self.exit_game()

    def start_game(self):
        """Start a new game"""
        try:
            print("\n" + "=" * 50)
            print("🎮 MULAI PERMAINAN AKINATOR")
            print("=" * 50)
            print("\nPikirkan sesuatu (bisa berupa orang, hewan, atau benda)")
            print("dan saya akan mencoba menebaknya dengan bertanya.\n")
            input("Tekan Enter ketika Anda sudah siap...")

            self.current_node = self.tree
            self.question_history = []
            self.stats['total_games'] += 1
            self.game_loop()
        except KeyboardInterrupt:
            print("\n\n⚠️  Permainan dihentikan oleh pengguna.")
        except Exception as e:
            print(f"\n❌ Terjadi kesalahan dalam permainan: {e}")

    def game_loop(self):
        """Play one round of the game"""
        try:
            while True:
                if self.current_node["type"] == "question":
                    question = self.current_node["question"]
                    self.question_history.append(question)
                    answer = self.ask_question(question)

                    if answer:
                        self.current_node = self.current_node["yes"]
                    else:
                        self.current_node = self.current_node["no"]

                elif self.current_node["type"] == "guess":
                    guess = self.current_node["guess"]
                    print(f"\n✨ Saya menebak: {guess.upper()}")
                    
                    is_correct = self.ask_question("Apakah tebakan saya benar?")
                    
                    if is_correct:
                        print("🎉 Yeay! Saya berhasil!")
                        print(f"Saya tahu Anda sedang memikirkan '{guess}'")
                        self.stats['correct_guesses'] += 1
                        self.save_stats()
                        break
                    else:
                        self.stats['wrong_guesses'] += 1
                        self.learn_new_guess(guess)
                        break
        except KeyboardInterrupt:
            raise
        except EOFError:
            raise

    def learn_new_guess(self, wrong_guess: str):
        """Learn a new guess from the user"""
        try:
            print("\nHmm, saya tidak tahu. Mari kita belajar bersama!")
            correct_answer = input("Apa yang Anda pikirkan? ").strip()
            
            if not correct_answer:
                print("Baik, permainan selesai.")
                return

            distinguishing_question = input(
                f"\nBerikan pertanyaan yang membedakan '{correct_answer}' "
                f"dengan '{wrong_guess}':\n"
            ).strip()

            if not distinguishing_question:
                print("Baik, permainan selesai.")
                return

            # Ensure question is properly formatted
            if not distinguishing_question.endswith('?'):
                distinguishing_question += '?'

            is_correct_answer_yes = self.ask_question(
                f"Untuk '{correct_answer}', apakah jawabannya 'ya'?"
            )

            # Update the tree
            old_guess_node = self.current_node.copy()
            
            if is_correct_answer_yes:
                self.current_node["type"] = "question"
                self.current_node["question"] = distinguishing_question
                self.current_node["yes"] = {"type": "guess", "guess": correct_answer}
                self.current_node["no"] = old_guess_node
            else:
                self.current_node["type"] = "question"
                self.current_node["question"] = distinguishing_question
                self.current_node["yes"] = old_guess_node
                self.current_node["no"] = {"type": "guess", "guess": correct_answer}

            self.save_database()
            self.stats['new_learns'] += 1
            self.save_stats()
            print(f"\n✨ Terima kasih! Saya sekarang tahu tentang '{correct_answer}'!")
        except KeyboardInterrupt:
            print("\n⚠️  Pembelajaran dibatalkan.")
        except EOFError:
            print("\n⚠️  Input error.")

    def exit_game(self):
        """Exit the game gracefully"""
        print("\n" + "=" * 50)
        print("👋 Terima kasih telah bermain Akinator!")
        print(f"   Ada {self.stats['total_items']} item dalam database saya")
        print(f"   Akurasi tebakan: {self.get_accuracy()}%")
        print("=" * 50 + "\n")

    def get_accuracy(self) -> float:
        """Get accuracy percentage"""
        total = self.stats['correct_guesses'] + self.stats['wrong_guesses']
        if total == 0:
            return 0.0
        return round((self.stats['correct_guesses'] / total) * 100, 1)


def main():
    print("\n" + "=" * 50)
    print("🎯 SELAMAT DATANG DI AKINATOR!")
    print("=" * 50)
    print("Game Tanya Jawab Interaktif")
    print("Saya akan menebak apa yang Anda pikirkan! 🔮")
    print("=" * 50 + "\n")
    
    game = AkinatorGame()
    game.play()


if __name__ == "__main__":
    main()
