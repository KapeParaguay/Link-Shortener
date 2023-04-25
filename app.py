from flask import Flask, render_template, request, redirect
import uuid

app = Flask(__name__)

urls = {}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        short_url = str(uuid.uuid4())[:8]
        urls[short_url] = url
        return render_template('index.html', short_url=request.host_url + short_url)
    else: 
        return render_template('index.html')

@app.route('/<short_url>')
def redirect_to_url(short_url):
    url = urls.get(short_url)
    if url:
        return redirect(url)
    else:
        return 'URL no encontrada'

if __name__ == '__main__':
    app.run(debug=True)
