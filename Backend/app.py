# filepath: /c:/Users/nilsc/OneDrive - Ecoles - Schulen Valais-Wallis/Arbeit/EMVs/EMVs Unterricht/EMVs1/3D-Modell-Scanning/3D-Scanning-Modell/Backend/app.py
from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename
import subprocess

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def process_file(filename):
    # Hier kommt die Logik zur Weiterverarbeitung der Datei hin
    print(f"Verarbeite Datei: {filename}")
    # Beispiel: Aufruf eines externen Skripts
    subprocess.run(["python", "process_script.py", filename])

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        process_file(filepath)  # Datei direkt nach dem Speichern verarbeiten
        return jsonify({'message': 'File uploaded and processed successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)