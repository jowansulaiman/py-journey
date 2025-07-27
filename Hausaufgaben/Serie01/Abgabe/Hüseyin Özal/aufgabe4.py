import re

text = " Kontakt:info@example.com ,Support:support@test.org ,Admin:admin@domain.net "

# Alle Email Adresse im Text finden. \w = buchstaben/zahlen/_ \. ein Punkt und - Zeichen --> + danach bedeutet = einmal oder öfter 
## Suche nach Text vor und nach einem @ Symbol
find = re.findall(r"[\w\.-]+@[\w\.-]+\.\w+" , text)
print(find)