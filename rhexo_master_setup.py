"""
RhexoStation 5 — Blood Red Hacker Edition
Spotify CSS Injector + Intro Overlay + Audio Booster
"""
import os, sys, zipfile, shutil, threading, subprocess, time, ctypes, webbrowser, tempfile, struct, math, io
import tkinter as tk
from tkinter import messagebox

# ─── PATHS ────────────────────────────────────────────────────────────────────
APPDATA   = os.environ.get("APPDATA", "")
SPA_PATH  = os.path.join(APPDATA, "Spotify", "Apps", "xpui.spa")
BAK_PATH  = os.path.join(APPDATA, "Spotify", "Apps", "xpui.bak")
SPOTX_DIR = os.path.join(APPDATA, "Spotify")

def resource(name):
    if getattr(sys, '_MEIPASS', None):
        return os.path.join(sys._MEIPASS, name)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), name)

INTRO_MP4 = resource("intro_fast.mp4")

# ─── MASTER CSS ───────────────────────────────────────────────────────────────
MASTER_CSS = """
/* ═══════════════════════════════════════════════════════
   RHEXOSTATION 5 — BLOOD RED HACKER EDITION
   guns.lol/r.h.e.x.o  |  antiGRAVITY 2026
═══════════════════════════════════════════════════════ */

/* Root colour overrides */
:root {
  --spice-main: #0a0000;
  --spice-sidebar: #0d0000;
  --spice-player: #0d0000;
  --spice-button: #ff003c;
  --spice-button-active: #cc0030;
  --spice-text: #ffffff;
  --spice-subtext: #ff6688;
  --spice-highlight: rgba(255,0,60,0.18);
  --spice-card: #160000;
  --spice-shadow: rgba(255,0,60,0.4);
  --spice-selected-row: rgba(255,0,60,0.25);
  --spice-custom-select-background: #160000;
}

/* Global BG */
body, .Root__main-view, .main-view-container,
.Root__top-bar, .Root__nav-bar, .Root__right-panel,
.Root__now-playing-bar {
  background-color: #0a0000 !important;
  color: #ffffff !important;
}

/* Nav sidebar */
.Root__nav-bar, nav[aria-label] {
  background: linear-gradient(180deg,#120000 0%,#0a0000 100%) !important;
  border-right: 1px solid #ff003c33 !important;
}

/* Top bar */
.Root__top-bar {
  background: rgba(10,0,0,0.95) !important;
  border-bottom: 1px solid #ff003c44 !important;
  backdrop-filter: blur(12px);
}

/* Now-playing bar */
.Root__now-playing-bar {
  background: linear-gradient(90deg,#120000 0%,#0a0000 50%,#120000 100%) !important;
  border-top: 2px solid #ff003c !important;
  box-shadow: 0 -4px 30px rgba(255,0,60,0.3) !important;
}

/* Play/pause button */
button[data-testid="control-button-playpause"],
.player-controls__buttons .encore-bright-accent-set button {
  background: radial-gradient(circle,#ff003c 0%,#aa0028 100%) !important;
  box-shadow: 0 0 20px rgba(255,0,60,0.6) !important;
  border-radius: 50% !important;
}

/* Progress bar */
.playback-progressbar .progress-bar__bg,
div[data-testid="progress-bar"] > div:first-child {
  background: #330008 !important;
}
.playback-progressbar .progress-bar__fg,
div[data-testid="progress-bar"] > div:nth-child(2) {
  background: linear-gradient(90deg,#ff003c,#ff6688) !important;
  box-shadow: 0 0 8px #ff003c !important;
}

/* Cards */
.main-card-card, .Card, [data-testid="card-image-hit"] {
  background: #160000 !important;
  border: 1px solid #ff003c22 !important;
  transition: border-color .2s, box-shadow .2s !important;
}
.main-card-card:hover, .Card:hover {
  border-color: #ff003c88 !important;
  box-shadow: 0 4px 24px rgba(255,0,60,0.25) !important;
}

/* Buttons */
.encore-bright-accent-set, [data-encore-id="buttonPrimary"] {
  background: #ff003c !important;
  color: #fff !important;
}
.encore-bright-accent-set:hover, [data-encore-id="buttonPrimary"]:hover {
  background: #cc0030 !important;
  box-shadow: 0 0 16px rgba(255,0,60,0.5) !important;
}

/* Links & accents */
a[href], .encore-text-link {
  color: #ff6688 !important;
}
a[href]:hover, .encore-text-link:hover {
  color: #ff003c !important;
  text-decoration: none !important;
}

/* Search bar */
input[data-testid="search-input"], .x-searchInput-searchInputInput {
  background: #160000 !important;
  border: 1px solid #ff003c55 !important;
  color: #fff !important;
}
input[data-testid="search-input"]:focus {
  border-color: #ff003c !important;
  box-shadow: 0 0 12px rgba(255,0,60,0.3) !important;
}

/* Scrollbars */
::-webkit-scrollbar { width:4px; }
::-webkit-scrollbar-track { background:#0a0000; }
::-webkit-scrollbar-thumb { background:#ff003c55; border-radius:2px; }
::-webkit-scrollbar-thumb:hover { background:#ff003c; }

/* Like / heart */
button[data-testid="add-button"] svg,
button[aria-label*="kaldır"] svg,
button[aria-label*="Beğen"] svg {
  fill: #ff003c !important;
}

/* Volume bar */
.volume-bar .progress-bar__fg,
div[data-testid="volume-bar"] > div:nth-child(2) {
  background: #ff003c !important;
}

/* Selection highlight */
.tracklist-row:hover, .main-trackList-trackListRow:hover {
  background: rgba(255,0,60,0.1) !important;
}
.tracklist-row[aria-selected="true"], .main-trackList-trackListRow[aria-selected="true"] {
  background: rgba(255,0,60,0.2) !important;
}

/* ── YOKMU HARBİ banner (centre-top) ─────────────────── */
#rhexo-denge-banner {
  position: fixed;
  top: 0; left: 50%; transform: translateX(-50%);
  z-index: 99998;
  pointer-events: none;
  font-family: 'Courier New', monospace;
  font-size: 11px;
  font-weight: 900;
  letter-spacing: 4px;
  text-transform: uppercase;
  color: #ff003c;
  text-shadow: 0 0 8px #ff003c, 0 0 20px #ff003c, 0 0 40px #ff003c99;
  animation: rhexo-glitch 2.5s infinite;
  padding: 3px 18px;
  background: rgba(10,0,0,0.75);
  border-bottom: 1px solid #ff003c55;
  white-space: nowrap;
}
@keyframes rhexo-glitch {
  0%,90%,100% { opacity:1; transform:translateX(-50%) skewX(0deg); text-shadow:0 0 8px #ff003c,0 0 20px #ff003c; }
  92%          { opacity:.7; transform:translateX(calc(-50% - 2px)) skewX(-3deg); text-shadow:-2px 0 #00ffff,2px 0 #ff003c; }
  94%          { opacity:1; transform:translateX(calc(-50% + 2px)) skewX(3deg);  text-shadow:2px 0 #00ffff,-2px 0 #ff003c; }
  96%          { opacity:.8; transform:translateX(-50%) skewX(-1deg); }
}

/* ── guns.lol badge (top-left) ────────────────────────── */
#rhexo-guns-badge {
  position: fixed;
  top: 8px; left: 8px;
  z-index: 99999;
  display: flex; align-items: center; gap: 5px;
  padding: 3px 10px;
  background: rgba(10,0,0,0.85);
  border: 1px solid #ff003c;
  border-radius: 3px;
  font-family: 'Courier New', monospace;
  font-size: 10px;
  font-weight: 700;
  color: #ff003c;
  text-decoration: none;
  letter-spacing: 1px;
  cursor: pointer;
  transition: background .2s, box-shadow .2s;
  box-shadow: 0 0 10px rgba(255,0,60,0.3);
  animation: rhexo-pulse-badge 3s ease-in-out infinite;
}
#rhexo-guns-badge:hover {
  background: rgba(255,0,60,0.2);
  box-shadow: 0 0 20px rgba(255,0,60,0.6);
}
@keyframes rhexo-pulse-badge {
  0%,100% { box-shadow:0 0 10px rgba(255,0,60,0.3); }
  50%      { box-shadow:0 0 20px rgba(255,0,60,0.6); }
}

/* ── Footer signature ─────────────────────────────────── */
#rhexo-footer-sig {
  position: fixed;
  bottom: 1px; left: 50%; transform: translateX(-50%);
  z-index: 99997;
  font-family: 'Courier New', monospace;
  font-size: 9px;
  letter-spacing: 3px;
  color: #ff003c77;
  pointer-events: none;
  text-transform: uppercase;
  white-space: nowrap;
}

/* ── Hacker scanline overlay ──────────────────────────── */
body::after {
  content: '';
  position: fixed; inset: 0;
  background: repeating-linear-gradient(
    0deg,
    transparent 0px,
    transparent 2px,
    rgba(255,0,60,0.015) 2px,
    rgba(255,0,60,0.015) 4px
  );
  pointer-events: none;
  z-index: 99990;
}

/* ── PRE-AMP display badge (top-right) ───────────────── */
#rhexo-preamp-badge {
  position: fixed;
  top: 8px; right: 8px;
  z-index: 99999;
  padding: 3px 10px;
  background: rgba(10,0,0,0.85);
  border: 1px solid #ff003c;
  border-radius: 3px;
  font-family: 'Courier New', monospace;
  font-size: 10px;
  color: #ff003c;
  pointer-events: none;
  letter-spacing: 1px;
}

/* ── Visualizer bars (now-playing area) ───────────────── */
#rhexo-visualizer {
  position: fixed;
  bottom: 68px; left: 50%; transform: translateX(-50%);
  z-index: 99993;
  display: flex; align-items: flex-end; gap: 2px;
  pointer-events: none;
  opacity: 0.4;
}
#rhexo-visualizer span {
  display: inline-block;
  width: 3px;
  background: linear-gradient(to top, #ff003c, #ff6688);
  border-radius: 2px 2px 0 0;
  animation: rhexo-bar var(--d,0.8s) ease-in-out infinite alternate;
}
@keyframes rhexo-bar {
  from { height: 4px; opacity:.5; }
  to   { height: var(--h,20px); opacity:1; }
}
"""

# ─── INDEX.HTML INJECTION ─────────────────────────────────────────────────────
INDEX_INJECTION = """
<!-- RhexoStation5 Injection -->
<div id="rhexo-denge-banner">⚡ YOKMU HARBİ HİÇ Bİ DENGİM ⚡</div>
<div id="rhexo-footer-sig">RHEXO ✖ antiGRAVİTY // SYSTEM INJECTOR 2026</div>
<div id="rhexo-preamp-badge">⚡ PRE-AMP: +12dB [BOOST]</div>
<a id="rhexo-guns-badge" href="https://guns.lol/r.h.e.x.o" target="_blank" rel="noopener">
  ⚡ guns.lol/r.h.e.x.o
</a>
<div id="rhexo-visualizer">
  <span style="--d:.6s;--h:18px"></span>
  <span style="--d:.8s;--h:28px"></span>
  <span style="--d:.5s;--h:14px"></span>
  <span style="--d:.9s;--h:32px"></span>
  <span style="--d:.7s;--h:22px"></span>
  <span style="--d:.4s;--h:12px"></span>
  <span style="--d:1.1s;--h:36px"></span>
  <span style="--d:.6s;--h:20px"></span>
  <span style="--d:.8s;--h:26px"></span>
  <span style="--d:.5s;--h:16px"></span>
</div>
<script>
// guns.lol badge click → open browser
document.addEventListener('DOMContentLoaded',function(){
  var badge = document.getElementById('rhexo-guns-badge');
  if(badge){
    badge.addEventListener('click',function(e){
      e.preventDefault();
      // Spotify's CEF uses window.open for external navigation
      window.open('https://guns.lol/r.h.e.x.o','_blank');
    });
  }
});
</script>
"""

# ─── PATCH HELPERS ────────────────────────────────────────────────────────────
def kill_spotify():
    subprocess.run(["taskkill","/F","/IM","Spotify.exe"],
                   capture_output=True, creationflags=0x08000000)
    time.sleep(2)

def restore_backup():
    if os.path.exists(BAK_PATH):
        shutil.copy2(BAK_PATH, SPA_PATH)
        return True
    return False

def apply_patch():
    """Apply CSS + HTML injection to xpui.spa (never touch xpui.js)"""
    if not os.path.exists(BAK_PATH):
        if os.path.exists(SPA_PATH):
            shutil.copy2(SPA_PATH, BAK_PATH)
        else:
            return False, "xpui.spa bulunamadı!"

    # Always start from clean backup
    shutil.copy2(BAK_PATH, SPA_PATH)

    tmp = SPA_PATH + ".tmp"
    with zipfile.ZipFile(SPA_PATH, 'r') as zin:
        with zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                data = zin.read(item.filename)

                if item.filename == "xpui.css":
                    data = data + b"\n" + MASTER_CSS.encode("utf-8")

                elif item.filename == "index.html":
                    html = data.decode("utf-8", errors="replace")
                    # Remove any previous injection
                    if "RhexoStation5 Injection" in html:
                        start = html.find("<!-- RhexoStation5 Injection -->")
                        end   = html.rfind("</script>", 0, start + 3000) + len("</script>")
                        if end > start:
                            html = html[:start] + html[end:]
                    # Inject before </body>
                    html = html.replace("</body>", INDEX_INJECTION + "\n</body>")
                    data = html.encode("utf-8")

                zout.writestr(item, data)

    os.replace(tmp, SPA_PATH)
    return True, "OK"

def launch_spotify():
    exe = os.path.join(SPOTX_DIR, "Spotify.exe")
    if os.path.exists(exe):
        subprocess.Popen([exe], creationflags=0x08000000)
    else:
        subprocess.Popen(["start", "spotify:"], shell=True)

# ─── INTRO OVERLAY (OpenCV window over Spotify) ───────────────────────────────
def play_intro_overlay():
    """Play intro video in a borderless window on top of everything."""
    try:
        import cv2
        import numpy as np

        cap = cv2.VideoCapture(INTRO_MP4)
        if not cap.isOpened():
            return

        fps   = cap.get(cv2.CAP_PROP_FPS) or 30
        total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        sw    = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        sh    = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # Get screen size
        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()
        SCREEN_W = user32.GetSystemMetrics(0)
        SCREEN_H = user32.GetSystemMetrics(1)

        WIN = "RhexoIntro"
        cv2.namedWindow(WIN, cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
        cv2.setWindowProperty(WIN, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        # Always on top via WinAPI
        try:
            hwnd = ctypes.windll.user32.FindWindowW(None, WIN)
            HWND_TOPMOST = -1
            SWP_NOMOVE   = 0x0002
            SWP_NOSIZE   = 0x0001
            ctypes.windll.user32.SetWindowPos(hwnd, HWND_TOPMOST, 0, 0, 0, 0,
                                               SWP_NOMOVE | SWP_NOSIZE)
        except Exception:
            pass

        frame_ms = int(1000 / fps)
        idx = 0

        # ESC button overlay parameters
        btn_text  = "ESC BAS VE GEC  >>"
        btn_x     = SCREEN_W - 260
        btn_y     = SCREEN_H - 60

        skip = False
        def on_key(event, x, y, flags, param):
            nonlocal skip
            # mouse click on ESC button area
            if event == cv2.EVENT_LBUTTONDOWN:
                if btn_x - 10 <= x <= SCREEN_W - 20 and btn_y - 36 <= y <= btn_y + 10:
                    skip = True

        cv2.setMouseCallback(WIN, on_key)

        while cap.isOpened() and not skip:
            t0 = time.time()
            ret, frame = cap.read()
            if not ret:
                break

            # Fade-in first 0.5s, fade-out last 0.5s
            fade_frames = int(fps * 0.5)
            alpha = 1.0
            if idx < fade_frames:
                alpha = idx / fade_frames
            elif idx > total - fade_frames:
                alpha = (total - idx) / fade_frames
            alpha = max(0.0, min(1.0, alpha))

            if alpha < 1.0:
                frame = (frame.astype(float) * alpha).astype("uint8")

            # Resize to screen
            if frame.shape[1] != SCREEN_W or frame.shape[0] != SCREEN_H:
                frame = cv2.resize(frame, (SCREEN_W, SCREEN_H), interpolation=cv2.INTER_LINEAR)

            # Draw ESC button
            overlay = frame.copy()
            cv2.rectangle(overlay, (btn_x - 10, btn_y - 36), (SCREEN_W - 20, btn_y + 10),
                          (0, 0, 180), -1)
            cv2.addWeighted(overlay, 0.8, frame, 0.2, 0, frame)
            cv2.rectangle(frame, (btn_x - 10, btn_y - 36), (SCREEN_W - 20, btn_y + 10),
                          (0, 0, 220), 2)
            cv2.putText(frame, btn_text, (btn_x, btn_y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 1, cv2.LINE_AA)

            # RHEXO watermark
            cv2.putText(frame, "RHEXO x antiGRAVITY 2026",
                        (20, SCREEN_H - 20), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (60, 0, 160), 1, cv2.LINE_AA)

            cv2.imshow(WIN, frame)

            key = cv2.waitKey(1) & 0xFF
            if key == 27 or key == ord(' '):  # ESC or Space
                skip = True

            idx += 1
            elapsed = time.time() - t0
            wait = frame_ms / 1000.0 - elapsed
            if wait > 0:
                time.sleep(wait)

        cap.release()
        cv2.destroyAllWindows()
    except Exception as e:
        print(f"Intro error: {e}")

# ─── AUDIO BOOSTER DAEMON ─────────────────────────────────────────────────────
_boost_active  = False
_boost_thread  = None
_current_boost = 1.5   # default: 150%

def audio_boost_daemon():
    global _boost_active, _current_boost
    try:
        from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
    except ImportError:
        return

    while _boost_active:
        try:
            sessions = AudioUtilities.GetAllSessions()
            for sess in sessions:
                if sess.Process and "spotify" in sess.Process.name().lower():
                    vol = sess._ctl.QueryInterface(ISimpleAudioVolume)
                    # Clamp to [0,1] — Windows won't go above 1.0 per session
                    target = min(1.0, _current_boost)
                    vol.SetMasterVolume(target, None)
        except Exception:
            pass
        time.sleep(1.5)

def start_audio_boost():
    global _boost_active, _boost_thread
    _boost_active = True
    _boost_thread = threading.Thread(target=audio_boost_daemon, daemon=True)
    _boost_thread.start()

def stop_audio_boost():
    global _boost_active
    _boost_active = False

# ─── GUI ──────────────────────────────────────────────────────────────────────
class RhexoApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("RhexoStation 5 — Blood Red Hacker Edition")
        self.root.geometry("520x600")
        self.root.configure(bg="#0a0000")
        self.root.resizable(False, False)

        # Try icon
        try:
            ico = resource("blood_syringe.ico")
            if os.path.exists(ico):
                self.root.iconbitmap(ico)
        except Exception:
            pass

        self._build_ui()
        self.root.mainloop()

    def _build_ui(self):
        r = self.root
        RED    = "#ff003c"
        DARK   = "#0a0000"
        CARD   = "#160000"
        MONO   = ("Courier New", 10)
        MONO_L = ("Courier New", 9)

        # ── Title ──────────────────────────────────────────
        tk.Label(r, text="⚡ RhexoStation 5", bg=DARK, fg=RED,
                 font=("Courier New", 20, "bold")).pack(pady=(18,2))
        tk.Label(r, text="BLOOD RED HACKER EDITION", bg=DARK, fg="#ff006688",
                 font=("Courier New", 9, "bold"), letter_spacing=4).pack()
        tk.Frame(r, bg=RED, height=1).pack(fill="x", padx=20, pady=8)

        # ── Status ─────────────────────────────────────────
        self.status_var = tk.StringVar(value="● Hazır")
        tk.Label(r, textvariable=self.status_var, bg=DARK, fg="#aaffaa",
                 font=MONO).pack()

        # ── Main buttons ───────────────────────────────────
        btn_frame = tk.Frame(r, bg=DARK)
        btn_frame.pack(pady=14)

        def rbtn(parent, text, cmd, fg=RED, bg=CARD):
            b = tk.Button(parent, text=text, command=cmd,
                          bg=bg, fg=fg, activebackground="#330000",
                          activeforeground="#ff6688",
                          font=("Courier New", 10, "bold"),
                          relief="flat", bd=0, padx=16, pady=8,
                          cursor="hand2")
            b.pack(side="left", padx=6)
            return b

        rbtn(btn_frame, "⚡  INSTALL & LAUNCH", self.do_install)
        rbtn(btn_frame, "🗑  UNINSTALL",         self.do_uninstall, fg="#888")

        # ── Audio booster ──────────────────────────────────
        tk.Frame(r, bg=RED, height=1).pack(fill="x", padx=20, pady=(10,6))
        tk.Label(r, text="🔊 SES BOOSTER (PRE-AMP)", bg=DARK, fg=RED,
                 font=("Courier New", 10, "bold")).pack()

        self.boost_var = tk.DoubleVar(value=150)
        self.boost_lbl = tk.Label(r, text="150%", bg=DARK, fg="#ff6688",
                                  font=("Courier New", 10, "bold"))
        self.boost_lbl.pack()

        sl = tk.Scale(r, variable=self.boost_var, from_=100, to=250,
                      orient="horizontal", length=340,
                      bg=DARK, fg=RED, troughcolor="#330000",
                      activebackground=RED, highlightthickness=0,
                      command=self._on_boost_change, resolution=5,
                      showvalue=False)
        sl.pack(pady=2)

        self.boost_on = tk.BooleanVar(value=False)
        tk.Checkbutton(r, text="Boost Aktif", variable=self.boost_on,
                       command=self._toggle_boost,
                       bg=DARK, fg=RED, selectcolor=CARD,
                       activebackground=DARK, activeforeground=RED,
                       font=MONO).pack()

        # ── guns.lol link ──────────────────────────────────
        tk.Frame(r, bg=RED, height=1).pack(fill="x", padx=20, pady=(10,6))
        link = tk.Label(r, text="⚡ guns.lol/r.h.e.x.o", bg=DARK, fg=RED,
                        font=("Courier New", 10, "bold"), cursor="hand2")
        link.pack()
        link.bind("<Button-1>", lambda e: webbrowser.open("https://guns.lol/r.h.e.x.o"))

        # ── Info ───────────────────────────────────────────
        info = (
            "• Tema: Blood Red (#ff003c)\n"
            "• Intro: OpenCV overlay (ESC ile geç)\n"
            "• Ses Booster: pycaw WASAPI session\n"
            "• Hedef: xpui.css + index.html ONLY\n"
            "• xpui.js'ye DOKUNULMAZ (SHA crash)"
        )
        tk.Label(r, text=info, bg=DARK, fg="#666666",
                 font=MONO_L, justify="left").pack(padx=24, pady=6, anchor="w")

        # ── Footer ─────────────────────────────────────────
        tk.Frame(r, bg=RED, height=1).pack(fill="x", padx=20, pady=(4,0))
        tk.Label(r, text="RHEXO ✖ antiGRAVİTY // SYSTEM INJECTOR 2026",
                 bg=DARK, fg="#ff003c55",
                 font=("Courier New", 8)).pack(pady=6)

    # ── Callbacks ──────────────────────────────────────────
    def _on_boost_change(self, val):
        global _current_boost
        pct = float(val)
        self.boost_lbl.config(text=f"{int(pct)}%")
        _current_boost = pct / 100.0

    def _toggle_boost(self):
        if self.boost_on.get():
            start_audio_boost()
            self.status_var.set("● Ses Boost AKTİF")
        else:
            stop_audio_boost()
            self.status_var.set("● Ses Boost durduruldu")

    def do_install(self):
        self.status_var.set("⏳ Spotify kapatılıyor...")
        self.root.update()
        kill_spotify()

        self.status_var.set("⏳ Patch uygulanıyor...")
        self.root.update()
        ok, msg = apply_patch()
        if not ok:
            messagebox.showerror("Hata", msg)
            self.status_var.set("❌ Hata: " + msg)
            return

        # Start audio boost if enabled
        if self.boost_on.get():
            start_audio_boost()

        self.status_var.set("▶ Spotify başlatılıyor...")
        self.root.update()
        launch_spotify()
        time.sleep(2.5)  # Let Spotify start

        # Play intro overlay in separate thread
        self.status_var.set("🎬 Intro oynatılıyor...")
        self.root.update()
        t = threading.Thread(target=play_intro_overlay, daemon=True)
        t.start()

        self.status_var.set("✅ Kurulum tamam! Intro oynuyor...")

    def do_uninstall(self):
        self.status_var.set("⏳ Geri yükleniyor...")
        self.root.update()
        kill_spotify()
        stop_audio_boost()
        if restore_backup():
            self.status_var.set("✅ Orijinal xpui.spa geri yüklendi")
        else:
            self.status_var.set("❌ Backup bulunamadı (xpui.bak yok)")

# ─── ENTRY ────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    RhexoApp()
