import socket
import time



# Güvenlik duvarı kuralları
# İzin verilen ve engellenen IP ve portlar listesi
izinli_ipler = ['127.0.0.1' ]
engellenen_ipler = ['10.0.0.5']
izinli_portlar = [80, 443, 61]
engellenen_portlar = [23]

# Güvenlik duvarı fonksiyonu
def guvenlik_duvari(ip, port):
    if ip in engellenen_ipler:
        print(f"{ip} adresinden gelen bağlantı engellendi!")
        return False
    if port in engellenen_portlar:
        print(f"{port} portundan gelen bağlantı engellendi!")
        return False
    if ip in izinli_ipler or port in izinli_portlar:
        print(f"{ip} adresinden {port} portuna gelen bağlantıya izin verildi.")
        return True
    print(f"{ip} adresi ve {port} portu bilinmiyor, bağlantı reddedildi.")
    return False

# Sunucu soketi oluşturalım (örneğin bir web sunucusu gibi)
sunucu = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sunucu.bind(('0.0.0.0', 8080))
sunucu.listen(10)

print("Güvenlik duvarı çalışıyor...")

while True:
    istemci, adres = sunucu.accept()
    ip_adresi, port = adres
    print(f"Yeni bağlantı: {ip_adresi}:{port}")
    
    if guvenlik_duvari(ip_adresi, port):
        istemci.send(b"Baglanti kabul edildi.")
        time.sleep(0.3)
    else:
        istemci.send(b"Baglanti reddedildi.")
        time.sleep(0.3)
    
    
