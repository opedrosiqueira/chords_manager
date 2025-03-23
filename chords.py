from chords_manager import is_not_a_chord

'''
coloca cada estrofe em uma linha, com os acordes em cima das letras e os versos separados por |.
'''

if __name__ == "__main__":
    input_file = input("input file (cifras.txt): ") or "cifras.txt"
    output_file = input("output file (cifrasComprimidas.txt): ") or "cifrasComprimidas.txt"
    with open(input_file, encoding="utf8") as file:
        origin = file.readlines()
        newer = []
        prevType = "empty"
        i = 0
        while i < len(origin):
            line = origin[i].rstrip()
            if line.strip() == "":
                newer.append("\n\n")
                prevType = "empty"
            elif is_not_a_chord(line):
                if prevType == "empty":
                    newer.append(line)
                else:
                    newer.append("|" + line)
                prevType = "notChord"
            else:
                chords = "\n"
                verses = ""
                while i < len(origin) - 1 and origin[i].strip() != "" and not is_not_a_chord(origin[i]):
                    line = origin[i].rstrip()
                    nextline = origin[i + 1].rstrip()
                    if is_not_a_chord(nextline):
                        longer = max(len(line), len(nextline))
                        chords += line.ljust(longer) + "|"
                        verses += nextline.ljust(longer) + "|"
                        i += 1
                    else:
                        chords += line + "|"
                        verses += "".ljust(len(line)) + "|"
                    i += 1
                newer.append(chords + "\n" + verses)
                newer.append(origin[i])
                prevType = "empty" if origin[i].strip() == "" else "notChord"
                if prevType == "empty":
                    newer.append("\n")
            i += 1
    with open(output_file, "w", encoding="utf8") as file:
        file.writelines(newer)
