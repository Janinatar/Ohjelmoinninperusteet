

# Robust: find the text file located in the same folder as this script
text_path = Path(__file__).with_name('sana.txt')

try:
    print(text_path.read_text(encoding='utf-8'))
except FileNotFoundError:
    print(f"Tiedostoa ei löytynyt: {text_path}")
except Exception as e:
    print("Virhe luettaessa tiedostoa:", e)
