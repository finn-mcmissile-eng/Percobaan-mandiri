import requests

url = 'https://jsonplaceholder.typicode.com/posts'
data_baru = {
    'title': 'Belajar API',
    'body': 'Hari ini saya belajar tentang RESTful API.',
    'userId': 1
}

response = requests.post(url, json=data_baru)


if response.status_code == 201: # 201 artinya "Created"
    print("Berhasil:", response.json())
    data = response.json()
    print(f"Judul Post: {data['title']}")
    print(f"Isi: {data['body']}")
else:
    print(f"Gagal mengambil data. Status code: {response.status_code}")
