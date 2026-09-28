import json
import asyncio
from telethon import TelegramClient
print("my.telegram.org üzerinden API development tools kısmına gir. Oluşturduğun api_id ve api_hash değerlerini kaydet.")
api_id = input("api_id giriniz:")
api_hash = input("api_hash giriniz:")
girdi = input("Grup adı veya IDsi: ")
dosyaadi = input("Dosya adı giriniz: ")
try:
    hedef = int(girdi)
except ValueError:
    hedef = girdi
async def mesajarsivle():
    async with TelegramClient('kisisel_oturum', api_id, api_hash) as client:
        
        mesajlar = []
        print("Mesajlar çekiliyor...")
        async for message in client.iter_messages(hedef):
            if message.text:
                mesaj_objesi = {
                    "Yazan: ": str(message.sender_id),
                    "Tarih: ": str(message.date),
                    "Mesaj: ": message.text.strip()
                }
                mesajlar.append(mesaj_objesi)
        with open(f'{dosyaadi}.json', 'w', encoding='utf-8') as f:
            json.dump(mesajlar, f, ensure_ascii=False, indent=4)
        print(f"Bitti! {len(mesajlar)} mesaj '{dosyaadi}.json' dosyasına kaydedildi.")
if __name__ == '__main__':
    asyncio.run(mesajarsivle())