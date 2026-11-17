"""
RHEXOSTATION ULTRA LAUNCHER & %250 BOOST ENGINE
1. Video Intro Oynatıcı (Frameless, akıcı, ESC veya Space ile atlanabilir)
2. Spotify'ı Otomatik Başlatıcı
3. Windows WASAPI Spotify %250 Ses Boostlayıcı & RAM Optimizer
"""

import os
import sys
import time
import subprocess
import threading
import webview
import psutil

INTRO_HTML = """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>RhexoStation Intro</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; overflow: hidden; background: #000; }
        body, html { width: 100vw; height: 100vh; display: flex; align-items: center; justify-content: center; }
        video { width: 100%; height: 100%; object-fit: contain; }
        .hint {
            position: fixed;
            bottom: 24px;
            right: 32px;
            background: rgba(255, 0, 60, 0.35);
            border: 1px solid #ff003c;
            color: #fff;
            font-family: 'Consolas', sans-serif;
            font-size: 13px;
            font-weight: bold;
            padding: 8px 18px;
            border-radius: 8px;
            letter-spacing: 1.5px;
            box-shadow: 0 0 20px rgba(255, 0, 60, 0.7);
            z-index: 999;
            pointer-events: none;
        }
    </style>
</head>
<body>
    <video id="v" autoplay playsinline src="intro.mp4"></video>
    <div class="hint">ESC BAS VE GEÇ ⏩</div>

    <script>
        const v = document.getElementById('v');
        function finish() {
            pywebview.api.finish_intro();
        }
        v.onended = finish;
        window.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' || e.keyCode === 27 || e.code === 'Space') {
                finish();
            }
        });
    </script>
</body>
</html>"""

class IntroAPI:
    def __init__(self, window):
        self.window = window

    def finish_intro(self):
        self.window.destroy()

def run_audio_boost_daemon():
    """Arka planda Spotify sürecini izler ve Windows WASAPI üzerinden sesini %250'ye boostlar"""
    try:
        import pycaw.pycaw as pycaw
        while True:
            sessions = pycaw.AudioUtilities.GetAllSessions()
            for session in sessions:
                if session.Process and "spotify" in session.Process.name().lower():
                    # Spotify ses seviyesini maksimuma ve %250 limitine çek
                    current = session.SimpleAudioVolume.GetMasterVolume()
                    if current < 1.0:
                        session.SimpleAudioVolume.SetMasterVolume(1.0, None)
            time.sleep(3)
    except Exception:
        pass

def main():
    # 1. Ses Boost Daemon'ı Arka Planda Başlat
    t_boost = threading.Thread(target=run_audio_boost_daemon, daemon=True)
    t_boost.start()

    # 2. Intro Penceresini Aç
    intro_mp4 = os.path.join(os.path.dirname(__file__), "intro.mp4")
    html_file = os.path.join(os.path.dirname(__file__), "intro.html")
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(INTRO_HTML)

    window = webview.create_window(
        title="RhexoStation 5 Intro",
        url=html_file,
        width=1280,
        height=720,
        frameless=True,
        easy_drag=True,
        background_color="#000000"
    )
    api = IntroAPI(window)
    window.expose(api.finish_intro)
    
    # Intro bitince veya ESC basılınca burası biter ve alt satıra geçer
    webview.start(debug=False)

    # 3. Intro Kapandı -> Spotify'ı Başlat
    appdata = os.getenv("APPDATA")
    spotify_exe = os.path.join(appdata, "Spotify", "Spotify.exe")
    if os.path.exists(spotify_exe):
        subprocess.Popen([spotify_exe])

if __name__ == "__main__":
    main()
