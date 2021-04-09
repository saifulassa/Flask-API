from flask import Flask, request, jsonify

app = Flask(__name__)

books_list = [
    {
        "id": 0,
        "penulis": "Andrea Hirata",
        "judul": "Sang Pemimpi",
        "tema": "Inspirasi",
    },
    {
        "id": 1,
        "penulis": "Tere Liye",
        "judul": "Tanah Tak Bertuan",
        "tema": "Perjuangan",
    },
    {
        "id": 2,
        "penulis": "Mardiku Wowiek",
        "judul": "Mana NKRImu bung",
        "tema": "Nasionalisme",
    },
    {
        "id": 3,
        "penulis": "Alexandro Ruby",
        "judul": "DO WHAT YOU DO",
        "tema": "Inspirasi",
    },
    {
        "id": 4,
        "penulis": "Raditya Dika",
        "judul": "Malam Minggu Miko : Spesial",
        "tema": "Komedi",
    },
]


@app.route('/', methods=['GET', 'POST'])
def books():
    if request.method == 'GET':
        if len(books_list) > 0:
            return jsonify(books_list)
        else:
            'Not Found', 404
    
    if request.method == 'POST':
        new_penulis = request.form['penulis']
        new_judul = request.form['judul']
        new_tema = request.form['tema']
        iD = books_list[-1]['id']+1

        new_obj = {
            'id' : iD,
            'penulis' : new_penulis,
            'judul' : new_judul,
            'tema' : new_tema
        }
        books_list.append(new_obj)
        return jsonify(books_list), 201


if __name__ == '__main__':
    app.run()



