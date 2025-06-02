from flask import Flask, render_template, request, send_file, redirect, flash
from werkzeug.utils import secure_filename
import os
from esteganografia import hide_text_in_image, extract_text_from_image

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'

UPLOAD_FOLDER = 'static/images'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encode', methods=['POST'])
def encode():
    if 'image' not in request.files or 'message' not in request.form:
        flash('Imagem ou mensagem não enviada.')
        return redirect('/')

    image = request.files['image']
    message = request.form['message']
    filename = secure_filename(image.filename)

    if filename == '':
        flash('Nenhum arquivo selecionado.')
        return redirect('/')

    input_path = os.path.join(app.config['UPLOAD_FOLDER'], 'original_' + filename)
    output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'encoded_' + filename)
    image.save(input_path)

    try:
        hide_text_in_image(input_path, output_path, message)
        return send_file(output_path, as_attachment=True)
    except ValueError as ve:
        flash(str(ve))
        return redirect('/')

@app.route('/decode', methods=['POST'])
def decode():
    if 'image' not in request.files:
        flash('Nenhuma imagem foi enviada.')
        return redirect('/')

    image = request.files['image']
    filename = secure_filename(image.filename)

    if filename == '':
        flash('Nenhum arquivo selecionado.')
        return redirect('/')

    path = os.path.join(app.config['UPLOAD_FOLDER'], 'decode_' + filename)
    image.save(path)

    message = extract_text_from_image(path)
    return render_template('index.html', decoded_message=message)

if __name__ == '__main__':
    app.run(debug=True)
