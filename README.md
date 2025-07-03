
# Conversor YouTube a MP3 en Render

Este proyecto usa Flask + yt-dlp para descargar MP3 desde enlaces de YouTube.

## Cómo desplegar en Render

1. Ve a https://render.com
2. Crea una cuenta gratuita.
3. Sube este proyecto a un repositorio de GitHub.
4. En Render, haz clic en "New + → Web Service".
5. Conecta tu cuenta de GitHub y selecciona este repositorio.
6. Usa estas opciones:
   - Runtime: Python
   - Build Command: pip install -r requirements.txt
   - Start Command: python main.py
7. Espera a que termine el deploy.
8. Abre la URL que Render te da: ahí estará tu app lista y funcionando 24/7.

⚠️ Este servicio está pensado solo para fines educativos y personales.
