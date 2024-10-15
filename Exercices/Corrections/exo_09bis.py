from functools import reduce

def compter_lettre_a(texte: str) -> int:
    upperTexte = texte.upper()
    return reduce(lambda acc, cur: acc+1 if cur == "A" else acc, upperTexte, 0)

print(compter_lettre_a("abba"))
print(compter_lettre_a("mixer"))