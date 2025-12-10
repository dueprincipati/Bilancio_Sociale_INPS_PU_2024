#!/usr/bin/env python3
"""
Script per rimuovere tutti gli attributi onclick dai bottoni
"""

with open('gdl_inps_patronati.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Rimuovi onclick dai bottoni
content = content.replace('onclick="moveRowUp(this)" ', '')
content = content.replace('onclick="moveRowDown(this)" ', '')
content = content.replace('onclick="deleteRow(this)" ', '')

with open('gdl_inps_patronati.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Tutti gli attributi onclick sono stati rimossi!")
print("✅ Ora i bottoni funzioneranno tramite event delegation")
