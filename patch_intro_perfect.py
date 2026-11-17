import os
import zipfile
import shutil
import subprocess

def patch_perfect_intro():
    appdata = os.getenv("APPDATA")
    apps_dir = os.path.join(appdata, "Spotify", "Apps")
    xpui_spa = os.path.join(apps_dir, "xpui.spa")
    
    webm_src = r"C:\Users\rhexo\.gemini\antigravity\scratch\RhexoInjector\intro.webm"
    mp4_src = r"C:\Users\rhexo\.gemini\antigravity\scratch\RhexoInjector\intro_fast.mp4"

    temp_dir = os.path.join(apps_dir, "xpui_intro_perfect")
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir, ignore_errors=True)
    os.makedirs(temp_dir, exist_ok=True)

    with zipfile.ZipFile(xpui_spa, 'r') as z:
        z.extractall(temp_dir)

    # 1. Her iki optimize formatı da köke kopyala
    shutil.copy2(webm_src, os.path.join(temp_dir, "intro.webm"))
    shutil.copy2(mp4_src, os.path.join(temp_dir, "intro.mp4"))

    # 2. index.html içine hem WebM hem MP4 fallback ile video göm
    html_path = os.path.join(temp_dir, "index.html")
    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Eski rhexo-video-intro varsa temizle
    if "rhexo-video-intro" in html:
        import re
        html = re.sub(r'<div id="rhexo-video-intro".*?</script>', '', html, flags=re.DOTALL)

    video_tag = """
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
    new_html = html.replace("<body>", "<body>\n" + video_tag)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(new_html)

    # 3. Paketle
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
    print("WebM ve FastStart MP4 Başarıyla Gömüldü!")

if __name__ == "__main__":
    patch_perfect_intro()
