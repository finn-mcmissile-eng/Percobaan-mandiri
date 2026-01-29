import requests

# Mengambil data post dengan ID 1 (Metode GET)
url = 'https://jsonplaceholder.typicode.com/posts/1'

try:
    response = requests.get(url)
    
    # Memastikan request berhasil (status code 200)
    if response.status_code == 200:
        data = response.json()
        print(f"Judul Post: {data['title']}")
        print(f"Isi: {data['body']}")
    else:
        print(f"Gagal mengambil data. Status code: {response.status_code}")

except Exception as e:
    print(f"Terjadi kesalahan: {e
