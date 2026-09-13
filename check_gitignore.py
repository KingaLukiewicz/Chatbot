def check_gitignore():
    try:
        with open('.gitignore', "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print("BRAK pliku .gitignore! Stwórz go jak najszybciej.")
        return
    if ".env" in content:
        print("OK: .env jest wymienione w .gitignore.")
    else:
        print("UWAGA: .env NIE jest wymienione w .gitignore!")


check_gitignore()
