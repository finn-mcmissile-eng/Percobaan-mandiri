import requests

# Nama file tempat menyimpan hasil
nama_file = "laporan_semua_post.txt"

# Melakukan perulangan (loop) dari angka 1 sampai 5
for i in range(1, 6):
    url = f'https://jsonplaceholder.typicode.com/posts/{i}'
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            
            # Membuka file dengan mode 'a' (Append) supaya data lama tidak terhapus
            with open(nama_file, "a") as f:
                f.write(f"--- DATA POST ID: {i} ---\n")
                f.write(f"Judul: {data['title']}\n")
                f.write(f"Isi: {data['body']}\n\n")
            
            print(f"Berhasil mengambil dan menyimpan data ID: {i}")
        else:
            print(f"Gagal mengambil ID {i}. Status: {response.status_code}")
            
    except Exception as e:
        print(f"Terjadi kesalahan pada ID {i}: {e}")

print("\nSelesai! Silakan cek file 'laporan_semua_post.txt' Anda.")
