import os  # Importa a Biblioteca OS

ROOT_FOLDER = r"C:\Users\vinic\Downloads\Spoofs"  # Caminho raiz
total_itens = 0
for subdir, dirs, _ in os.walk(ROOT_FOLDER):  # Aqui vou iterar entre subpastas

    for dir in dirs:  # Para cada subpasta
        current_itens = len(os.listdir(os.path.join(ROOT_FOLDER, dir)))  # Número de itens dentro de uma subpasta
        print("Dir %s - Count %s" % (dir, current_itens))  # Exibo o número de itens dentro das subpastas
        total_itens += current_itens

print("Total itens %s " % total_itens)
