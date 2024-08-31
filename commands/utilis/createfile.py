import sys

def create_file(file_name):
    try:
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write('')  # Crează un fișier gol
        print(f"Fișier creat: {file_name}")
    except Exception as e:
        print(f"A apărut o eroare la crearea fișierului: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Utilizare: cfile {name of file}.{extension}")
    else:
        create_file(sys.argv[1])
