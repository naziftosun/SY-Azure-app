from flask import Flask
import os
import psycopg2

app = Flask(__name__) 

@app.route('/hello')
def home():
    try:
       
        conn = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database='postgres'
        )
        conn.close()
        return "<h1>BAŞARILI: Azure Özel Veritabanına tünelsiz erişim sağlandı!</h1>"
    except Exception as e:
        return f"<h1>HATA: Bağlantı başarısız!</h1><p>{str(e)}</p>"

if __name__ == "__main__":
    
    app.run(host='0.0.0.0', port=80)