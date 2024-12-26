from flask import Flask,render_template

app = Flask(__name__)

# Ana sayfa
@app.route('/')
def home():
    return render_template('index.html')

# Hakkımızda sayfası
@app.route('/hakkımızda')
def about():
    return render_template('hakkımızda.html')

# İletişim sayfası
@app.route('/iletisim')
def contact():
    return render_template('iletisim.html')

# Slider sayfası
@app.route('/slider')
def slider():
    return render_template('slider.html')

if __name__ == '__main__':
    app.run(debug=True)
