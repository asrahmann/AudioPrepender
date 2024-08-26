from flask import Flask, request, send_file, render_template
from pydub import AudioSegment
import io

app = Flask(__name__)

# Set maximum content length to 500 MB
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024  # 500 MB

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Get the uploaded files
        main_file = request.files.get('main_audio')
        append_file = request.files.get('append_audio')

        if not main_file or not append_file:
            return "Both files are required."

        # Load audio files
        main_audio = AudioSegment.from_file(main_file)
        append_audio = AudioSegment.from_file(append_file)
        silence_audio = AudioSegment.silent(duration=1000)

        # Append the second audio file to the first one
        combined_audio = append_audio + silence_audio + main_audio

        # Set audio parameters: 8 kHz, mono, 16-bit (linear PCM)
        combined_audio = combined_audio.set_frame_rate(8000)
        combined_audio = combined_audio.set_channels(1)  # mono
        combined_audio = combined_audio.set_sample_width(2)  # 16-bit audio

        # Save the combined audio to a BytesIO object
        output = io.BytesIO()
        combined_audio.export(output, format="wav")
        output.seek(0)

        # Return the file for download
        return send_file(output, as_attachment=True, download_name="combined_audio.wav", mimetype="audio/wav")

    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
