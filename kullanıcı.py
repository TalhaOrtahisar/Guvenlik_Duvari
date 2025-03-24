import socket

# Sunucu IP ve port bilgileri
sunucu_ip = '127.0.0.1'  # Sunucunun IP adresi
sunucu_port = 8080       # Sunucunun dinlediği port

# İstemci soketi oluşturalım
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Sunucuya bağlanmayı dene
    client.connect((sunucu_ip, sunucu_port))
    print("Sunucuya bağlanıldı.")
    
    # Sunucudan mesaj bekle
    mesaj = client.recv(1024)  # Sunucudan gelen yanıtı al
    print("Sunucudan gelen mesaj:", mesaj.decode())
    
except Exception as e:
    print("Bağlantı hatası:", e)

finally:
    client.close()  # Bağlantıyı kapat

