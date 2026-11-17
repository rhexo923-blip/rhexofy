"""
RHEXOSTATION MASTER SUITE
Vencord Tarzı Tek Tık Enjektör / Kaldırıcı (GUI) + guns.lol Tıklanabilir Buton + Ses & RAM Boost
"""

import os
import sys
import shutil
import zipfile
import subprocess
import time
import threading
import webview
import psutil

# 1. TEMİZLENMİŞ VE GELİŞMİŞ CSS (Kırmızı Hacker + Butonlar + Hover Ses Efekti Hissi)
MASTER_CSS = """
/* ==========================================================================
   RHEXOSTATION ULTRA - MASTER BLOOD RED THEME
   ========================================================================== */

:root {
    --hacker-red: #ff003c !important;
    --hacker-red-glow: #ff0055 !important;
    --hacker-crimson: #990022 !important;
    --hacker-bg: #050102 !important;
    --hacker-card-bg: rgba(20, 3, 7, 0.9) !important;
    --hacker-border: rgba(255, 0, 60, 0.5) !important;
    --hacker-border-bright: #ff003c !important;

    --essential-base: #ff003c !important;
    --essential-positive: #ff003c !important;
    --essential-subdued: #880020 !important;
    --background-base: #050102 !important;
    --background-highlight: #140307 !important;
    --background-press: #ff003c !important;
    --background-elevated-base: #0c0205 !important;
    --background-elevated-highlight: #1a040a !important;
    --text-base: #ffffff !important;
}

html, body, .Root, .Root__top-container,
[data-testid="main-view-container"],
.main-view-container__scroll-node-child,
.Root__nav-bar, .Root__right-sidebar,
aside, section, main {
    background: radial-gradient(circle at 50% 0%, #1a0207 0%, #080103 60%, #020001 100%) !important;
    color: #ffffff !important;
    font-family: 'Consolas', 'Segoe UI', monospace, sans-serif !important;
}

/* 1. SOL ÜST TIKLANABİLİR GUNS.LOL BUTONU VE ORTA GLITCH SLOGAN */
#rhexo-guns-badge {
    position: fixed;
    top: 10px;
    left: 80px;
    background: linear-gradient(135deg, #ff003c 0%, #77001a 100%);
    color: #ffffff !important;
    text-decoration: none !important;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1px;
    padding: 6px 16px;
    border-radius: 8px;
    border: 1px solid #ff3366;
    box-shadow: 0 0 15px rgba(255, 0, 60, 0.8);
    z-index: 999999;
    cursor: pointer !important;
    transition: all 0.25s ease;
    display: flex;
    align-items: center;
    gap: 6px;
}
#rhexo-guns-badge:hover {
    transform: scale(1.08) translateY(-1px);
    box-shadow: 0 0 25px rgba(255, 0, 60, 1);
    background: #ff003c;
}

.Root__top-bar header::after {
    content: "⚡ YOKMU HARBİ HİÇ Bİ DENGİM ⚡";
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    top: 12px;
    font-size: 15px;
    font-weight: 900;
    color: #ff003c;
    letter-spacing: 2px;
    text-shadow: 0 0 12px #ff003c, 0 0 24px #ff003c;
    pointer-events: none;
    z-index: 99999;
    animation: dengimGlitch 2s infinite alternate;
}

@keyframes dengimGlitch {
    0% { transform: translateX(-50%) skew(0deg); text-shadow: 0 0 10px #ff003c; }
    25% { transform: translateX(-50%) skew(-3deg); text-shadow: -2px 0 18px #ff3366; }
    50% { transform: translateX(-50%) skew(2deg); text-shadow: 2px 0 22px #990022; }
    75% { transform: translateX(-50%) skew(-1deg); }
    100% { transform: translateX(-50%) skew(0deg); text-shadow: 0 0 15px #ff003c; }
}

.Root__now-playing-bar::after {
    content: "RHEXO ✖ antiGRAVİTY // SYSTEM INJECTOR 2026";
    position: absolute;
    bottom: -2px;
    left: 50%;
    transform: translateX(-50%);
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 2px;
    color: #ff003c;
    text-shadow: 0 0 10px #ff003c;
    pointer-events: none;
    z-index: 99999;
}

/* 2. REKLAMLARI VE YEŞİL TANITIM KUTULARINI SİL */
[data-testid="upgrade-button"],
[title="Upgrade to Premium"],
a[href*="/upgrade"],
.Root__top-bar aside,
div[data-testid="sponsored-container"],
div[aria-label="Upgrade to Premium"],
div[data-testid="top-bar-upgrade-button"],
div[data-testid="ad-iframe-container"],
#ad-banner,
.ad-iframe,
div[data-testid="hero-card"],
section > div:has(button:contains("Dene")) {
    display: none !important;
    visibility: hidden !important;
    height: 0px !important;
    width: 0px !important;
}

/* 3. KARTLAR VE BUTONLAR (GELİŞMİŞ EVENTLER & 3D TILT) */
div[data-testid="card-container"],
.main-card-card,
[role="gridcell"] > div {
    background: var(--hacker-card-bg) !important;
    border: 1.5px solid var(--hacker-border) !important;
    border-radius: 18px !important;
    padding: 14px !important;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.8) !important;
    transition: all 0.28s cubic-bezier(0.2, 0.8, 0.2, 1) !important;
}

div[data-testid="card-container"]:hover,
.main-card-card:hover,
[role="gridcell"] > div:hover {
    transform: translateY(-8px) scale(1.04) !important;
    border-color: var(--hacker-border-bright) !important;
    box-shadow: 0 16px 40px rgba(255, 0, 60, 0.5), 0 0 30px rgba(255, 0, 60, 0.3) !important;
    background: rgba(36, 5, 12, 0.98) !important;
}

div[data-testid="card-container"] img,
.main-card-card img {
    border-radius: 12px !important;
}

/* 4. ALT OYNATICI (NOW PLAYING BAR) */
footer[data-testid="now-playing-bar"],
.Root__now-playing-bar {
    background: rgba(6, 1, 3, 0.98) !important;
    border-top: 2px solid var(--hacker-red) !important;
    box-shadow: 0 -8px 35px rgba(0, 0, 0, 0.95), 0 0 25px rgba(255, 0, 60, 0.4) !important;
}

button[data-testid="control-button-playpause"] {
    background: linear-gradient(135deg, #ff003c 0%, #660015 100%) !important;
    color: #ffffff !important;
    border: 2px solid rgba(255, 255, 255, 0.5) !important;
    box-shadow: 0 0 26px rgba(255, 0, 60, 1) !important;
    border-radius: 50% !important;
    transform: scale(1.12) !important;
    transition: all 0.2s ease !important;
}
button[data-testid="control-button-playpause"]:hover {
    transform: scale(1.26) !important;
    box-shadow: 0 0 40px rgba(255, 0, 60, 1) !important;
}

.playback-progressbar .progress-bar__slider,
.playback-bar .progress-bar,
.volume-bar .progress-bar {
    --fg-color: #ff003c !important;
    --is-active-fg-color: #ff3366 !important;
    box-shadow: 0 0 16px rgba(255, 0, 60, 0.9) !important;
}

button[data-encore-id="chip"] {
    background: rgba(255, 0, 60, 0.15) !important;
    color: #ffffff !important;
    border: 1px solid var(--hacker-border) !important;
    border-radius: 12px !important;
    transition: all 0.2s ease !important;
}
button[data-encore-id="chip"]:hover {
    background: var(--hacker-red) !important;
    box-shadow: 0 0 16px rgba(255, 0, 60, 0.8) !important;
    transform: translateY(-2px) !important;
}
"""

def patch_spotify_full():
    appdata = os.getenv("APPDATA")
    apps_dir = os.path.join(appdata, "Spotify", "Apps")
    xpui_spa = os.path.join(apps_dir, "xpui.spa")
    backup_spa = os.path.join(apps_dir, "xpui.bak")
    
    webm_src = r"C:\Users\rhexo\.gemini\antigravity\scratch\RhexoInjector\intro.webm"
    mp4_src = r"C:\Users\rhexo\.gemini\antigravity\scratch\RhexoInjector\intro_fast.mp4"

    temp_dir = os.path.join(apps_dir, "xpui_master_patch")
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir, ignore_errors=True)
    os.makedirs(temp_dir, exist_ok=True)

    with zipfile.ZipFile(backup_spa, 'r') as z:
        z.extractall(temp_dir)

    # 1. Videoları kopyala
    if os.path.exists(webm_src):
        shutil.copy2(webm_src, os.path.join(temp_dir, "intro.webm"))
    if os.path.exists(mp4_src):
        shutil.copy2(mp4_src, os.path.join(temp_dir, "intro.mp4"))

    # 2. xpui.css dosyasını güncelle
    css_path = os.path.join(temp_dir, "xpui.css")
    with open(css_path, "a", encoding="utf-8") as f:
        f.write("\n\n" + MASTER_CSS)

    # 3. index.html dosyasını güncelle (guns.lol tıklanabilir buton + kusursuz intro)
    html_path = os.path.join(temp_dir, "index.html")
    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    video_and_guns_tag = """
<a id="rhexo-guns-badge" href="https://guns.lol/r.h.e.x.o" target="_blank">
    🩸 guns.lol/r.h.e.x.o
</a>
<div id="rhexo-video-intro" style="position:fixed;top:0;left:0;width:100vw;height:100vh;background:#000;z-index:99999999;display:flex;align-items:center;justify-content:center;">
    <video id="rhexo-v" autoplay playsinline style="width:100%;height:100%;object-fit:contain;">
        <source src="/intro.webm" type="video/webm">
        <source src="/intro.mp4" type="video/mp4">
    </video>
    <div style="position:fixed;bottom:24px;right:32px;background:rgba(255,0,60,0.5);border:1px solid #ff003c;color:#fff;font-family:sans-serif;font-size:13px;font-weight:bold;padding:8px 18px;border-radius:8px;letter-spacing:1px;box-shadow:0 0 20px #ff003c;pointer-events:none;">ESC BAS VE GEC ⏩</div>
</div>
<script>
    (function(){
        const o = document.getElementById("rhexo-video-intro");
        const v = document.getElementById("rhexo-v");
        function closeIntro() {
            if(o) {
                o.style.opacity = "0";
                o.style.transition = "opacity 0.4s ease";
                setTimeout(() => o.remove(), 400);
            }
        }
        if(v) {
            v.onended = closeIntro;
            v.play().catch(e => { console.log("Autoplay:", e); });
        }
        window.addEventListener("keydown", (e) => {
            if(e.key === "Escape" || e.keyCode === 27 || e.code === "Space") {
                closeIntro();
            }
        });
    })();
</script>
"""
    new_html = html.replace("<body>", "<body>\n" + video_and_guns_tag)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(new_html)

    # 4. Yeniden sıkıştır
    new_spa = os.path.join(apps_dir, "xpui_new.spa")
    with zipfile.ZipFile(new_spa, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                fp = os.path.join(root, file)
                z.write(fp, arcname=os.path.relpath(fp, temp_dir))

    shutil.rmtree(temp_dir, ignore_errors=True)
    if os.path.exists(xpui_spa):
        os.remove(xpui_spa)
    os.rename(new_spa, xpui_spa)
    return True

def restore_spotify_original():
    appdata = os.getenv("APPDATA")
    apps_dir = os.path.join(appdata, "Spotify", "Apps")
    xpui_spa = os.path.join(apps_dir, "xpui.spa")
    backup_spa = os.path.join(apps_dir, "xpui.bak")

    if os.path.exists(backup_spa):
        subprocess.run(["taskkill", "/F", "/IM", "Spotify.exe"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(1)
        shutil.copy2(backup_spa, xpui_spa)
        return True
    return False

# ==============================================================================
# VENCORD TARZI ENJEKTÖR ARAYÜZÜ (HTML + PYWEBVIEW)
# ==============================================================================

VENCORD_STYLE_HTML = """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>RhexoStation Injector</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; user-select: none; }
        body {
            background: #080204;
            color: #ffffff;
            font-family: 'Segoe UI', Inter, sans-serif;
            height: 100vh;
            display: flex;
            flex-direction: column;
            border-radius: 16px;
            border: 1.5px solid rgba(255, 0, 60, 0.4);
            box-shadow: 0 0 35px rgba(255, 0, 60, 0.35);
            overflow: hidden;
        }
        .header {
            height: 44px;
            background: rgba(14, 3, 7, 0.95);
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 16px;
            border-bottom: 1px solid rgba(255, 0, 60, 0.25);
            -webkit-app-region: drag;
        }
        .title {
            display: flex;
            align-items: center;
            gap: 8px;
            font-weight: 700;
            font-size: 13px;
            letter-spacing: 1px;
            color: #ff003c;
        }
        .close-btn {
            background: none;
            border: none;
            color: #aaa;
            font-size: 16px;
            cursor: pointer;
            -webkit-app-region: no-drag;
            transition: 0.2s;
        }
        .close-btn:hover { color: #ff003c; }
        .content {
            flex: 1;
            padding: 24px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
        }
        .logo-box {
            width: 72px;
            height: 72px;
            background: rgba(255, 0, 60, 0.1);
            border: 2px solid #ff003c;
            border-radius: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 32px;
            box-shadow: 0 0 25px rgba(255, 0, 60, 0.5);
            margin-bottom: 16px;
        }
        h2 { font-size: 18px; font-weight: 700; margin-bottom: 6px; }
        p { font-size: 12px; color: #a0707b; max-width: 380px; line-height: 1.4; margin-bottom: 22px; }
        .btn-group {
            display: flex;
            flex-direction: column;
            gap: 10px;
            width: 100%;
            max-width: 340px;
        }
        .btn-install {
            background: linear-gradient(135deg, #ff003c 0%, #88001f 100%);
            color: #fff;
            border: 1px solid rgba(255, 255, 255, 0.3);
            padding: 12px 18px;
            border-radius: 10px;
            font-size: 13px;
            font-weight: 700;
            cursor: pointer;
            box-shadow: 0 4px 18px rgba(255, 0, 60, 0.4);
            transition: all 0.2s ease;
        }
        .btn-install:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(255, 0, 60, 0.7);
            background: #ff003c;
        }
        .btn-uninstall {
            background: rgba(255, 255, 255, 0.05);
            color: #ccc;
            border: 1px solid rgba(255, 255, 255, 0.12);
            padding: 10px 16px;
            border-radius: 10px;
            font-size: 12px;
            cursor: pointer;
            transition: 0.2s;
        }
        .btn-uninstall:hover {
            background: rgba(255, 255, 255, 0.12);
            color: #fff;
        }
        #status {
            margin-top: 14px;
            font-size: 12px;
            min-height: 18px;
            font-weight: 600;
        }
    </style>
</head>
<body>
    <div class="header">
        <div class="title">
            <span>💉</span> RHEXOSTATION INJECTOR
        </div>
        <button class="close-btn" onclick="pywebview.api.close_window()">✕</button>
    </div>

    <div class="content">
        <div class="logo-box">🩸</div>
        <h2>RhexoStation 5 Setup</h2>
        <p>Vencord mantığında tek tıkla yükleyin. Kurulumdan sonra her açılışta doğrudan Spotify çalışır.</p>

        <div class="btn-group">
            <button class="btn-install" onclick="doInstall()">⚡ Yükle / Güncelle (Install)</button>
            <button class="btn-uninstall" onclick="doUninstall()">🔄 Orijinal Spotify'a Dön (Uninstall)</button>
        </div>

        <div id="status"></div>
    </div>

    <script>
        function doInstall() {
            const s = document.getElementById('status');
            s.style.color = '#ff003c';
            s.innerText = '⏳ Yükleniyor ve Spotify yamalanıyor...';
            pywebview.api.install().then(res => {
                s.style.color = res ? '#00ff88' : '#ff4444';
                s.innerText = res ? '✅ Kurulum Başarılı! Spotify Başlatılıyor...' : '❌ Hata oluştu.';
            });
        }
        function doUninstall() {
            const s = document.getElementById('status');
            s.style.color = '#ffcc00';
            s.innerText = '⏳ Orijinal Spotify geri yükleniyor...';
            pywebview.api.uninstall().then(res => {
                s.style.color = res ? '#00ff88' : '#ff4444';
                s.innerText = res ? '✅ Orijinal Spotify Geri Yüklendi!' : '❌ Yedek bulunamadı.';
            });
        }
    </script>
</body>
</html>"""

class InjectorAPI:
    def __init__(self, window):
        self.window = window

    def install(self):
        try:
            subprocess.run(["taskkill", "/F", "/IM", "Spotify.exe"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            time.sleep(1)
            patch_spotify_full()
            
            # Spotify'ı Başlat
            appdata = os.getenv("APPDATA")
            spotify_exe = os.path.join(appdata, "Spotify", "Spotify.exe")
            if os.path.exists(spotify_exe):
                subprocess.Popen([spotify_exe])
            return True
        except Exception as e:
            print("Install error:", e)
            return False

    def uninstall(self):
        return restore_spotify_original()

    def close_window(self):
        self.window.destroy()

def start_injector():
    window = webview.create_window(
        title="RhexoStation Injector",
        html=VENCORD_STYLE_HTML,
        width=480,
        height=420,
        frameless=True,
        easy_drag=True,
        background_color="#080204"
    )
    api = InjectorAPI(window)
    window.expose(api.install, api.uninstall, api.close_window)
    webview.start(debug=False)

if __name__ == "__main__":
    start_injector()
