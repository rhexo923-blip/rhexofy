"""
RHEXOSTATION ULTRA - CLEAN BLOOD RED HACKER THEME
Tüm butonlar, kartlar, guns.lol butonu, DENGİM glitch ve RHEXO & antiGRAVİTY imzası
Yeşil kutular (Mini oynatıcıyı dene dahil) %100 yok edilir.
"""

import os
import sys
import shutil
import zipfile
import subprocess
import time

HACKER_RED_CSS = """
/* ==========================================================================
   RHEXOSTATION ULTRA - BLOOD RED HACKER THEME & ZERO GREEN
   ========================================================================== */

:root {
    --hacker-red: #ff003c !important;
    --hacker-red-glow: #ff0055 !important;
    --hacker-crimson: #990022 !important;
    --hacker-bg: #050102 !important;
    --hacker-card-bg: rgba(20, 3, 7, 0.9) !important;
    --hacker-border: rgba(255, 0, 60, 0.5) !important;
    --hacker-border-bright: #ff003c !important;

    /* Spotify'ı kırmızıya zorlama */
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

/* Tüm Arka Planlar - Kırmızı Gölgelendirme */
html, body, .Root, .Root__top-container,
[data-testid="main-view-container"],
.main-view-container__scroll-node-child,
.Root__nav-bar, .Root__right-sidebar,
aside, section, main {
    background: radial-gradient(circle at 50% 0%, #1a0207 0%, #080103 60%, #020001 100%) !important;
    color: #ffffff !important;
    font-family: 'Consolas', 'Segoe UI', monospace, sans-serif !important;
}

/* 1. ÜST HEADER: GUNS.LOL VE DENGİM BANNER */
#rhexo-hacker-header {
    height: 44px;
    background: rgba(10, 2, 4, 0.95);
    border-bottom: 2px solid var(--hacker-red);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 16px;
    z-index: 99999;
    box-shadow: 0 0 25px rgba(255, 0, 60, 0.5);
}

.gunslol-btn {
    background: linear-gradient(135deg, #ff003c 0%, #77001a 100%);
    color: #fff !important;
    text-decoration: none;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1px;
    padding: 6px 14px;
    border-radius: 8px;
    border: 1px solid #ff3366;
    box-shadow: 0 0 15px rgba(255, 0, 60, 0.8);
    transition: all 0.25s ease;
    display: flex;
    align-items: center;
    gap: 6px;
}
.gunslol-btn:hover {
    transform: scale(1.08);
    box-shadow: 0 0 25px rgba(255, 0, 60, 1);
    background: #ff003c;
}

.dengim-banner {
    font-size: 15px;
    font-weight: 900;
    color: #ff003c;
    letter-spacing: 2px;
    text-transform: uppercase;
    text-shadow: 0 0 10px #ff003c, 0 0 20px #ff003c, 0 0 35px #990022;
    animation: dengimGlitch 2s infinite alternate;
}

@keyframes dengimGlitch {
    0% { transform: skew(0deg); text-shadow: 0 0 10px #ff003c; }
    20% { transform: skew(-2deg); text-shadow: -2px 0 15px #ff3366; }
    40% { transform: skew(1deg); text-shadow: 2px 0 20px #990022; }
    60% { transform: skew(-1deg); }
    80% { transform: skew(3deg); text-shadow: 0 0 25px #ff003c; }
    100% { transform: skew(0deg); text-shadow: 0 0 15px #ff003c; }
}

.dsp-badge {
    background: rgba(255, 0, 60, 0.15);
    border: 1px solid var(--hacker-red);
    color: #ff3366;
    padding: 4px 10px;
    border-radius: 6px;
    font-size: 11px;
    font-weight: bold;
    box-shadow: 0 0 10px rgba(255, 0, 60, 0.4);
}

/* 2. EN ALTTAKİ RHEXO & ANTIGRAVITY İMZA BARI */
#rhexo-footer-signature {
    height: 28px;
    background: #040102;
    border-top: 1px solid rgba(255, 0, 60, 0.4);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 2.5px;
    color: #881122;
    text-shadow: 0 0 8px rgba(255, 0, 60, 0.6);
    z-index: 99999;
}
#rhexo-footer-signature span {
    color: #ff003c;
    text-shadow: 0 0 12px #ff003c;
    margin: 0 6px;
}

/* 3. TÜM YEŞİL TANITIM KUTULARI (MİNİ OYNATICIYI DENE DAHİL) YOK ET */
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
div:has(> div:contains("Mini oynatıcıyı dene")),
section:has(div:contains("Mini oynatıcıyı dene")),
div[data-testid="hero-card"],
.Root__top-container section > div:has(button:contains("Dene")) {
    display: none !important;
    visibility: hidden !important;
    height: 0px !important;
    width: 0px !important;
}

/* 4. KARTLAR VE ÇALMA LİSTELERİ */
div[data-testid="card-container"],
.main-card-card,
[role="gridcell"] > div {
    background: var(--hacker-card-bg) !important;
    border: 1.5px solid var(--hacker-border) !important;
    border-radius: 18px !important;
    padding: 14px !important;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.8) !important;
    transition: all 0.3s cubic-bezier(0.2, 0.8, 0.2, 1) !important;
}

div[data-testid="card-container"]:hover,
.main-card-card:hover,
[role="gridcell"] > div:hover {
    transform: translateY(-8px) scale(1.03) !important;
    border-color: var(--hacker-border-bright) !important;
    box-shadow: 0 16px 40px rgba(255, 0, 60, 0.5), 0 0 30px rgba(255, 0, 60, 0.3) !important;
    background: rgba(36, 5, 12, 0.98) !important;
}

div[data-testid="card-container"] img,
.main-card-card img {
    border-radius: 12px !important;
}

/* 5. ALT OYNATICI (NOW PLAYING BAR) */
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
"""

HACKER_RED_JS = """
// ==========================================================================
// RHEXOSTATION ULTRA - SAFE DOM ENHANCER
// ==========================================================================
(function() {
    function injectUI() {
        if (!document.getElementById("rhexo-hacker-header")) {
            const header = document.createElement("div");
            header.id = "rhexo-hacker-header";
            header.innerHTML = `
                <a href="https://guns.lol/r.h.e.x.o" target="_blank" class="gunslol-btn">
                    🩸 guns.lol/r.h.e.x.o
                </a>
                <div class="dengim-banner">
                    ⚡ yokmu harbi hiç bi DENGİM ⚡
                </div>
                <div class="dsp-badge">
                    🔊 PRE-AMP: %250 [CORE BOOST]
                </div>
            `;
            document.body.prepend(header);
        }

        if (!document.getElementById("rhexo-footer-signature")) {
            const footer = document.createElement("div");
            footer.id = "rhexo-footer-signature";
            footer.innerHTML = `RHEXO <span>✖</span> antiGRAVİTY // SYSTEM INJECTOR 2026`;
            document.body.appendChild(footer);
        }

        // Yeşil "Mini oynatıcıyı dene" kartını DOM'dan sök
        document.querySelectorAll('div').forEach(el => {
            if (el.innerText && el.innerText.includes("Mini oynatıcıyı dene")) {
                let p = el;
                for (let i = 0; i < 4; i++) {
                    if (p && p.parentElement) p = p.parentElement;
                }
                if (p) p.style.display = "none";
            }
        });
    }

    setInterval(injectUI, 600);
})();
"""

def inject_clean_theme():
    appdata = os.getenv("APPDATA")
    apps_dir = os.path.join(appdata, "Spotify", "Apps")
    xpui_spa = os.path.join(apps_dir, "xpui.spa")
    backup_spa = os.path.join(apps_dir, "xpui.bak")

    temp_dir = os.path.join(apps_dir, "xpui_clean_build")
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir, ignore_errors=True)
    os.makedirs(temp_dir, exist_ok=True)

    with zipfile.ZipFile(backup_spa, 'r') as z:
        z.extractall(temp_dir)

    css_path = os.path.join(temp_dir, "xpui.css")
    with open(css_path, "a", encoding="utf-8") as f:
        f.write("\n\n" + HACKER_RED_CSS)

    js_path = os.path.join(temp_dir, "xpui.js")
    with open(js_path, "a", encoding="utf-8") as f:
        f.write("\n\n" + HACKER_RED_JS)

    new_spa = os.path.join(apps_dir, "xpui_temp.spa")
    with zipfile.ZipFile(new_spa, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                full_f = os.path.join(root, file)
                rel = os.path.relpath(full_f, temp_dir)
                z.write(full_f, arcname=rel)

    if os.path.exists(xpui_spa):
        os.remove(xpui_spa)
    os.rename(new_spa, xpui_spa)
    shutil.rmtree(temp_dir, ignore_errors=True)
    print("Tema basariyla xpui.spa icine enjekte edildi!")

if __name__ == "__main__":
    inject_clean_theme()
