# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 13:02:34 2025

@author: nils.rambow
"""

import re

text = " Kontakt : info@example.com , Support : support@test.org , Admin :admin@domain.net "

email_pattern = r'[\w\.-]+@[\w\.-]+\.\w+'


emails = re.findall(email_pattern, text)

print(emails)