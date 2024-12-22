import os

# Nome do arquivo original
input_filename = 'letras.txt'

# Cria uma pasta para salvar as músicas, se ainda não existir
output_folder = 'musicas'
os.makedirs(output_folder, exist_ok=True)

# Lê o conteúdo do arquivo original
with open(input_filename, 'r', encoding='utf-8') as file:
    # Divide o conteúdo pelas músicas, considerando que cada nova música começa com '@'
    content = file.read().split('→')

# Para cada música no conteúdo dividido
for song in content:
    # Remove espaços extras do início e do fim
    song = song.strip()
    
    # Ignora blocos vazios
    if not song:
        continue
    
    # Extrai o título da música (primeira linha)
    lines = song.splitlines()
    title = lines[0].strip()
    
    # Extrai o conteúdo da música (resto do texto)
    lyrics = "\n".join(lines[1:]).strip()
    
    # Define o nome do arquivo com o título da música
    filename = os.path.join(output_folder, f"{title}.txt")
    
    # Salva a música em um arquivo com o nome extraído do título
    with open(filename, 'w', encoding='windows-1252') as song_file:
        song_file.write(lyrics)

print("Arquivos de músicas foram criados com sucesso!")
