from pathlib import Path

# This script finds 'sana.txt' in the same folder as the script and prints it.
text_path = Path(__file__).with_name('sana.txt')

try:
    print(text_path.read_text(encoding='utf-8'))
except FileNotFoundError:
    print(f"Tiedostoa ei löytynyt: {text_path}")
except Exception as e:
    print("Virhe luettaessa tiedostoa:", e)
