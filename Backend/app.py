



# NICHT BENUTZT WORDEN!!!!!!!!!!!!!!





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

def process_files(filepaths):
    # Hier kommt die Logik zur Weiterverarbeitung der Dateien hin
    print(f"Verarbeite Dateien: {filepaths}")
    # Beispiel: Aufruf eines externen Skripts
    subprocess.run(["python", "process_script.py"] + filepaths)

@app.route('/upload', methods=['POST'])
def upload_files():
    if 'files' not in request.files:
        return jsonify({'message': 'No file part'}), 400

    files = request.files.getlist('files')
    if not files:
        return jsonify({'message': 'No selected files'}), 400

    filepaths = []
    for file in files:
        if file.filename == '':
            continue
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        filepaths.append(filepath)

    if filepaths:
        process_files(filepaths)  # Dateien direkt nach dem Speichern verarbeiten
        return jsonify({'message': 'Files uploaded and processed successfully'}), 200
    else:
        return jsonify({'message': 'No valid files uploaded'}), 400

if __name__ == '__main__':
    app.run(debug=True)