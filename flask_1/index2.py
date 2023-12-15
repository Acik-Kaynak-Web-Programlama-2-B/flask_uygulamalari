

# paket içe aktarma
from flask import Flask

# flask uygulama oluşturma başlatma
app = Flask(__name__)

# / yolu için rota belirleme ve istekleri işleme
@app.route('/')
def anasayfa():
    # tarayıcıda görüntülenecek içerik
    return "<font color='red'><b><i>Merhaba Dünya</i></b></font>"

# proje çalıştırıldıysa
if __name__ == '__main__':
    # uygulamayı debug modunda çalıştır
    app.run(debug=True)
 