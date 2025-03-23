def normalizar_linhas(input_file, output_file, max_chars=80):
    with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
        for linha in infile:
            while len(linha) > max_chars:
                outfile.write(linha[:max_chars] + "\n")  # Escreve o máximo permitido
                linha = linha[max_chars:]  # Remove a parte já escrita
            outfile.write(linha)


if __name__ == "__main__":
    input_file = input("input file (letras.txt): ") or "letras.txt"
    output_file = input(f"output file ({input_file}LinhasCurtas.txt): ") or f"{input_file}LinhasCurtas.txt"
    max_chars = int(input("Máximo de caracteres por linha (padrão 36): ") or 36)

    normalizar_linhas(input_file, output_file, max_chars)
    print(f"Linhas normalizadas foram salvas em {output_file}.")
