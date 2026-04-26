def frequency_map(s: str) -> dict:
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq


attempt = frequency_map("abacate")
attempt2 = frequency_map("Davi")
attempt3 = frequency_map("a a a a a a a")

# como esperado, ele também leva em conta os espaços em branco
print(attempt)
print(attempt2)
print(attempt3)

# COMPARANDO IGUALDADES EM ANAGRAMAS
item1 = frequency_map("BANANA")
item2 = frequency_map("AAANNB")

print(item1 == item2)
