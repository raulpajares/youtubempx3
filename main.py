
from flask import Flask, request, send_file
import yt_dlp
import tempfile
import os

app = Flask(__name__)

@app.route("/")
def home():
    return '''
    <h2>Descargar MP3 desde YouTube</h2>
    <form action="/download" method="post">
        <input name="url" type="text" placeholder="Enlace de YouTube" style="width: 300px;">
        <button type="submit">Descargar</button>
    </form>
    '''

@app.route("/download", methods=["POST"])
def download():
    url = request.form.get("url")
    if not url:
        return "No se recibió una URL", 400

    with tempfile.TemporaryDirectory() as tmpdir:
        filepath = os.path.join(tmpdir, "audio.mp3")
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": filepath,
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
            "quiet": True,
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            return send_file(filepath, as_attachment=True, download_name="audio.mp3")
        except Exception as e:
            return f"Error: {e}", 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
