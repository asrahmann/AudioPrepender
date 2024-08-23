# Python Audio Project

This project is a Flask application that allows users to upload and process audio files. The application uses the `pydub` library to manipulate audio files and `ffmpeg` for audio processing.

## Features

- Upload audio files
- Append one audio file to another
- Convert audio to 8 kHz, mono, 16-bit format
- Download the processed audio file

## Requirements

- Python 3.x
- Flask 2.0.1
- pydub 0.25.1
- ffmpeg

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   
2. Create and activate a virtual environment:
    python3 -m venv myenv
    source myenv/bin/activate

3. Install the dependencies:
    pip install -r requirements.txt

4. Ensure ffmpeg is installed on your system. For example
   on Amazon Linux
   sudo amazon-linux-extras install epel -y
   sudo yum install -y ffmpeg

## Usage

1. Run the Flask application:
FLASK_APP=app.py flask run --host=0.0.0.0

2. Open your web browser and navigate to http://localhost:5000.

3. Upload your audio files and process them as needed.

## Acknowledgments
- Flask
- pydub
- ffmpeg

## License
This project is licensed under the MIT License. See the LICENSE file for details.