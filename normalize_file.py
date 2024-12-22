import re
import unicodedata
import sys


def to_pascal_case(phrase: str):
    words = phrase.lower().split()
    pascal_case_words = [word.capitalize() for word in words]
    return "".join(pascal_case_words)


def strip_accents(s):
    """https://stackoverflow.com/a/518232"""
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


def keep_only_letters(s):
    """https://stackoverflow.com/a/72478014/4072641"""
    return re.sub(r"[\W\d_]", "", s)


input_file = input("input file (empty to scan lines): ")
output_file = input("output file (empty to print to stdout): ")

if input_file:
    input_file = open(input_file, "r", encoding="utf8")
    sys.stdin = input_file

if output_file:
    output_file = open(output_file, "w", encoding="utf8")
    sys.stdout = output_file

for line in sys.stdin:
    normalized = strip_accents(keep_only_letters(to_pascal_case(line)))
    print(f"{normalized}→{line.strip()}")

if input_file:
    input_file.close()

if output_file:
    output_file.close()
