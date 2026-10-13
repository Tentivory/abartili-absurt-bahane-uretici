#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Absürt Bahane Üretici
Dünyanın en gereksiz ama en eğlenceli scripti.
"""

import random

bahaneler = [
    "Kedi benim klavyemi yedi, sonra pişman olup kusunca bilgisayarım kısa devre yaptı.",
    "Asansörün içinde mahsur kaldım, ama asansör yoktu, sadece hayal ediyordum.",
    "WiFi'nin ruhu beni terk etti, modemi ağlayarak sakinleştirmeye çalışıyordum.",
    "Kahve makinesi bana isyan etti ve 'bugün çalışmıyorum' diye bağırdı.",
    "Zaman yolculuğu yapmaya çalışırken 3 dakika geriye gittim, o yüzden geç kaldım.",
    "Komşunun ördeği benim ödevimi yedi, sonra ödev ördek gibi ses çıkarmaya başladı.",
    "Güneş doğarken o kadar şaşırdım ki 2 saat boyunca sadece baktım.",
    "Bilgisayarım beni ghost'ladı, mesajlarımı okudu ama cevap vermedi.",
    "Ayakkabı bağcıklarım birbirine küstü, barıştırmak 45 dakika sürdü.",
    "Rüzgar o kadar sert esti ki düşüncelerim dağıldı, toplayana kadar geçti."
]

def bahane_uret():
    return random.choice(bahaneler)

if __name__ == "__main__":
    print("\n=== ABSÜRT BAHANE ÜRETİCİ ===")
    print("Bugünkü bahaneniz:")
    print(f"\"{bahane_uret()}\"")
    print("\nBaşarılar, gerçekten! (Ciddi ciddi absürt)")
