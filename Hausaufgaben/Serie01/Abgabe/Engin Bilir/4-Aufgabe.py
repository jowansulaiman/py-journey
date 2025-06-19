# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 12:51:48 2025

@author: engin.bilir

1. E-Mail-Adressen extrahieren (4 Punkte): Schreiben Sie ein Python-Skript, das
die Funktion re.findall() verwendet, um alle E-Mail-Adressen aus dem gegebenen 
textString zu extrahieren. Geben Sie die gefundene Liste von E-Mail-Adressen 
auf der Konsole aus.
"""

import re

text = "Kontakt: info@example.com, Support: support@test.org, Admin: admin@domain.net"

# Übung Nr. 1
zeigeMAILS = re.findall(r"[\w\.]+@[\w\.]+\.\w+", text)
print(zeigeMAILS)