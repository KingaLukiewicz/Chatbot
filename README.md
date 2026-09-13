# Chatbot AI z analizą danych

Aplikacja webowa łącząca czat z Claude z mozliwością wykorzystania go do streszczania tekstu lub analizy wysłanych plików CSV.

# Funkcje

- Czat z Claude z obsługą historii rozmowy
- Upload plików CSV i automatyczna analiza z wykresem
- Streszczanie tekstu z Claude
- System logowania (hasła hashowane przez bcrypt)
- Rate limiting i ochrona przed prompt injection

# Wymagania

- Python 3.10 lub nowszy
- Konto na console.anthropic.com z kluczem API

# Instalacja lokalna

1. Sklonuj repozytorium:

```bash
git clone https://github.com/KingaLukiewicz/Chatbot.git
cd nazwa-repo
```

2. Stwórz i aktywuj wirtualne środowisko:

```bash
python -m venv venv
source venv/bin/activate
```

3. Zainstaluj zależności:

```bash
pip install -r requirements.txt
```

4. Stwórz plik .env i uzupełnij ANTHROPIC_API_KEY oraz SECRET_KEY
5. Uruchom appkę: `python app.py`

# Zmienne środowiskowe

| Nazwa             | Opis                                                 | Wymagane |
| ----------------- | ---------------------------------------------------- | -------- |
| ANTHROPIC_API_KEY | Klucz API do Claude                                  | Tak      |
| SECRET_KEY        | Sekret do podpisywania sesji Flaska                  | Tak      |
| PORT              | Port appki (ustawiane automatycznie przez platformę) | Nie      |

# Struktura projektu

```
app.py - główny plik appki (routes, logika)
templates/ - szablony HTML (Jinja2)
static/ - CSS i wygenerowane raporty
requirements.txt - lista zależności Pythona
Procfile - instrukcja uruchomienia dla platformy hostingowej
```

# Autor

KingaLukiewicz, projekt stworzony w ramach kursu.
