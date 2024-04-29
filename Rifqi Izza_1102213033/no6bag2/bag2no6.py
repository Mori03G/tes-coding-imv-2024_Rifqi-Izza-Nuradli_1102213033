def adlh_anagrams(str1, str2):
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    return sorted_str1 == sorted_str2

# Input strings
string1 = (input("Masukan Kata Pertama : "))
string2 = (input("Masukan kata Kedua : "))

if adlh_anagrams(string1, string2):
    print(f"{string1} dan {string2} adalah  anagrams.")
else:
    print(f"{string1} dan {string2} bukan anagrams.")