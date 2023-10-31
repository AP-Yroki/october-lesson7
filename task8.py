from fuzzywuzzy import fuzz

string1 = 'Плохой код на самом деле не плохой.'
string2 = 'Его просто не так поняли.'
similarity_ratio1 = fuzz.ratio(string1, string2)
print(f"Схожесть строк 1 и 2: {similarity_ratio1}")

string3 = 'Работает? Не трогай.'
string4 = 'Работает? Не трогай.'
similarity_ratio2 = fuzz.ratio(string3, string4)
print(f"Схожесть строк 3 и 4: {similarity_ratio2}")

string5 = 'Работает? Не трогай.'
string6 = 'Работает? Не трогай!'
similarity_ratio3 = fuzz.ratio(string5, string6)
print(f"Схожесть строк 5 и 6: {similarity_ratio3}")