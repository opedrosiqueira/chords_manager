import re


def normalizar_linhas(input_file, output_file, max_chars=80, breakline=False):
    breakline = "\n" if breakline else ""
    with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
        outstr = ""
        for linha in infile:
            if breakline and re.match(r"(\d\. )|(\[R\] )", linha):
                outstr += "\n"  # Se a linha começa com número ou "[R] ", adiciona quebra
            while len(linha) > max_chars:
                quebra = list(re.finditer(r"[ .,!?;:|-]", linha[:max_chars]))  # Encontra o último separador antes do limite
                quebra = quebra[-1].start() + 1 if quebra else max_chars  # Se não encontrar separador, quebra no limite
                if linha[quebra:] == breakline:  # Se sobrar só um \n, então acabou a linha
                    outstr += linha[:quebra]
                else:
                    outstr += linha[:quebra] + "\n" + breakline  # Escreve o máximo permitido
                linha = linha[quebra:]  # Remove a parte já escrita
            outstr += linha
        outfile.write(outstr)


if __name__ == "__main__":
    input_file = input("input file (letras.txt): ") or "letras.txt"
    output_file = input(f"output file ({input_file}LinhasCurtas.txt): ") or f"{input_file}LinhasCurtas.txt"
    max_chars = int(input("Máximo de caracteres por linha (padrão 36): ") or 36)

    normalizar_linhas(input_file, output_file, max_chars)
    print(f"Linhas normalizadas foram salvas em {output_file}.")
