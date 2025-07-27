import re
# Vorgegebener String:

text = "Kontakt: info@example.com , Support: support@test.org , Admin: admin@domain.net"

# 1. E-Mail-Adressen extrahieren

mails = re.findall(r"[\w\.-]+@[\w\.-]+\.\w+",text)
print(mails)