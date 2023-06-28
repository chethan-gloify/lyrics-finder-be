import os
import tempfile
import flask
from flask import request
from flask import jsonify
from flask_cors import CORS

import assemblyai as aai


app = flask.Flask(__name__)
CORS(app)


@app.route('/transcribe', methods=['POST'])
def transcribe():
    if request.method == 'POST':
        aai.settings.api_key = "346b2ed2346948dbafcadd645c5e1bb5"

        wav_file = request.files['file']
        temp_dir = tempfile.mkdtemp()
        temp_file_path = os.path.join(temp_dir, 'temp.wav')
        wav_file.save(temp_file_path)

        language_code = request.form['langSelect']

        transcriber = aai.Transcriber()

        transcriber.config = aai.TranscriptionConfig(language_code=language_code, disfluencies=True,
                                                     punctuate=True, format_text=True)

        transcript = transcriber.transcribe(temp_file_path)

        return jsonify(transcript.text)

    else:
        return "This endpoint only processes POST wav blob"
