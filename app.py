from flask import Flask, request, send_file, render_template, redirect, url_for, flash
from pydub import AudioSegment
import io

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with your actual secret key

# Set maximum content length to 500 MB
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024  # 500 MB

# Read the correct password from password.txt
with open('password.txt', 'r') as file:
    CORRECT_PASSWORD = file.read().strip()

@app.route('/', methods=['GET', 'POST'])
def password_page():
    return render_template('password.html')

@app.route('/check_password', methods=['POST'])
def check_password():
    password = request.form.get('password')
    if password == CORRECT_PASSWORD:
        return redirect(url_for('upload_file'))
    else:
        flash('Incorrect password. Please try again.')
        return redirect(url_for('password_page'))

@app.route('/upload', methods=['GET', 'POST'])
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

@app.route('/convert_single', methods=['POST'])
def convert_single():
    single_file = request.files.get('single_audio')

    if not single_file:
        return "A file is required."

    # Load the single audio file
    single_audio = AudioSegment.from_file(single_file)

    # Set audio parameters: 8 kHz, mono, 16-bit (linear PCM)
    single_audio = single_audio.set_frame_rate(8000)
    single_audio = single_audio.set_channels(1)  # mono
    single_audio = single_audio.set_sample_width(2)  # 16-bit audio

    # Save the converted audio to a BytesIO object
    output = io.BytesIO()
    single_audio.export(output, format="wav")
    output.seek(0)

    # Return the file for download
    return send_file(output, as_attachment=True, download_name="converted_audio.wav", mimetype="audio/wav")

if __name__ == '__main__':
    app.run(debug=True)