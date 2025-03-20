import re

"""extrai acordes de um arquivo de cifras. cria um arquivo com os acordes encontrados e outro apenas com as letras das músicas"""

chords = set()


def remove_chord_parts(line: str, ignore_case=True):
    """remove tokens que podem fazer parte de acordes, como dim e maj"""
    chord_parts = [
        "add",
        "dim",
        "int",
        "intr",
        "intro",
        "introd",
        "introducao",
        "introdução",
        "maj",
        "major",
        "minor",
        "riff",
        "solo",
        "sus",
        "tom",
        "vez",
        "vezes",
        "1x",
        "2x",
        "3x",
        "4x",
        "1ª",
        "2ª",
        "3ª",
        "4ª",
        ":",
        "[R]",
        "[1]",
        "[2]",
        "[3]",
        "[4]",
        "[5]",
        "[6]",
        "[7]",
        "[8]",
        "[9]",
        "[Intro]",
        "Final:",
        "M",
        "m",
    ]
    for s in chord_parts:
        line = line.replace(s, "")
    return line


def is_not_a_chord(line: str):
    """retorna o primeiro token que nao seja acorde, dentro de line"""
    line = remove_non_alpha(line)
    if line.strip() == "":
        return line
    tokens = re.split(r"\s|/|\(|\)|\[|\]", line)
    for token in tokens:
        if not re.fullmatch(r"(A|B|C|D|E|F|G|A#|C#|D#|F#|G#|Ab|Bb|Db|Eb|Gb)(-|\+|m|°|º)?([0-9]+(-|\+|m|M|b|#)?)?|([0-9]+(-|\+|m|M|b|#)?)?", token):
            return token
        chords.add(token)
    return None


def remove_non_alpha(line):
    """remove tudo que não for whitespace, barra ou letra (incluíndo letras acentuadas)"""
    # return re.findall(r"[A-Za-zÀ-ÿ]",line)
    return re.sub(r"[^A-Za-zÀ-ÿ/\s]", "", line)


if __name__ == "__main__":
    with open("cifras.txt", encoding="utf8") as file:
        not_chords = set()
        letras = ""
        for line in file:
            not_chord = is_not_a_chord(remove_chord_parts(line))
            not_chords.add(not_chord)
            if not_chord:
                letras += line
    with open("acordes.txt", "w", encoding="utf8") as file:
        file.write(str(chords))
        file.write("\n")
        file.write(str(not_chords))
    with open("letras.txt", "w", encoding="utf8") as file:
        file.write(letras)
