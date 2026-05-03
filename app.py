import streamlit as st

# ─── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Portafolio de apps de interfaces multimodales",
    layout="wide",
)

# ─── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Mono:wght@400;500&family=Syne:wght@400;600;700&display=swap');

html, body, [class*="css"] { font-family: 'Syne', sans-serif; }

#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 2rem; padding-bottom: 4rem; max-width: 1100px; }

.hero { padding: 48px 0 32px; border-bottom: 1px solid rgba(255,255,255,0.08); margin-bottom: 16px; }
.hero-tag { font-family: 'DM Mono', monospace; font-size: 11px; letter-spacing: 0.2em; text-transform: uppercase; color: #c8f04d; margin-bottom: 16px; display: flex; align-items: center; gap: 10px; }
.hero h1 { font-family: 'DM Serif Display', serif; font-size: clamp(36px, 5vw, 64px); font-weight: 400; line-height: 1.1; }
.hero h1 em { font-style: italic; color: #c8f04d; }
.hero-desc { color: #888; font-size: 15px; line-height: 1.7; max-width: 480px; }

.section-hdr { display: flex; align-items: center; gap: 20px; margin: 56px 0 28px; padding-bottom: 16px; border-bottom: 1px solid rgba(255,255,255,0.08); }
.section-num { font-family: 'DM Serif Display'; font-size: 56px; opacity: 0.08; }
.section-label { font-family: 'DM Mono'; font-size: 10px; text-transform: uppercase; }
.section-name { font-family: 'DM Serif Display'; font-size: 24px; }
.section-badge { margin-left: auto; font-family: 'DM Mono'; font-size: 10px; padding: 4px 10px; border-radius: 100px; border: 1px solid rgba(255,255,255,0.15); color: #888; }

.app-card { background: #1a1a1a; border: 1px solid #2a2a2a; border-radius: 12px; overflow: hidden; transition: 0.2s; display: flex; flex-direction: column; height: 100%; }
.app-card:hover { transform: translateY(-4px); }

.app-thumb { aspect-ratio: 16/10; background: #111; display: flex; align-items: center; justify-content: center; flex-direction: column; gap: 8px; border-bottom: 1px solid #2a2a2a; }
.thumb-icon { font-size: 28px; opacity: 0.3; }
.thumb-label { font-family: 'DM Mono'; font-size: 9px; color: #555; }

.app-body { padding: 14px 16px; display: flex; flex-direction: column; flex: 1; }
.app-name { font-size: 13px; font-weight: 600; margin-bottom: 6px; }
.app-desc { font-size: 11px; color: #777; flex: 1; }

.app-btns { display: flex; gap: 6px; margin-top: 14px; }
.btn-app { flex: 1; padding: 7px; text-align: center; font-size: 10px; text-decoration: none; border-radius: 7px; }
.btn-primary-6 { background: #c8f04d; color: black; }
.btn-primary-7 { background: #4df0b4; color: black; }
.btn-primary-8 { background: #f0a84d; color: black; }
.btn-primary-9 { background: #c44df0; color: white; }
.btn-primary-11 { background: #4db8f0; color: black; }
.btn-primary-12 { background: #f04d4d; color: white; }
.btn-primary-13 { background: #f0e44d; color: black; }

.btn-ghost { border: 1px solid #333; color: #aaa; }
</style>
""", unsafe_allow_html=True)

# ─── DATA ──────────────────────────────────────────────────────────────────────
CLASSES = {
    6: {
        "color": "#c8f04d",
        "label": "cl6",
        "title": "Desarrollo de aplicaciones web para interfaces multimodales.",
        "apps": [
            {
                "name": "Mi primera app",
                "desc": "Mi primera app en Streamlit.",
                "icon": "📊",
                "streamlit": "https://natilladearequipe.streamlit.app",
                "github": "https://github.com/laugc2407-bit/Natilla",
            },
            {
                "name": "Cuento",
                "desc": "Generador de cuentos interactivos.",
                "icon": "📖",
                "streamlit": "https://amarillacomogato.streamlit.app",
                "github": "https://github.com/laugc2407-bit/amarilla",
            },
        ],
    },
    11: {
        "color": "#4db8f0",
        "label": "cl11",
        "title": "Aplicaciones con LLMs",
        "apps": [
            {
                "name": "Generador de LSTM",
                "icon": "🔷",
                "streamlit": "https://lstmnlp-zqkveafyjlpavwottgpeka.streamlit.app",
                "github": "https://github.com/laugc2407-bit/lstmnlp",
            },
            {
                "name": "Chatea con tu pdf",
                "icon": "🔷",
                "streamlit": "https://chatiandopdf.streamlit.app",
                "github": "https://github.com/laugc2407-bit/Chatiandopdf",
            },
        ],
    },
}

# ─── HERO ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-tag">Portafolio de aplicaciones</div>
  <h1>Portafolio de apps de interfaces multimodales</h1>
  <p class="hero-desc">
    Colección de aplicaciones interactivas desarrolladas durante el curso.
  </p>
</div>
""", unsafe_allow_html=True)

# ─── FUNCTIONS ────────────────────────────────────────────────────────────────
def render_card(app, class_num):
    name = app.get("name", "Sin nombre")
    desc = app.get("desc", "Sin descripción")
    icon = app.get("icon", "📦")
    streamlit = app.get("streamlit", "#")
    github = app.get("github", "#")

    return f"""
    <div class="app-card">
        <div class="app-thumb">
            <div class="thumb-icon">{icon}</div>
            <div class="thumb-label">preview</div>
        </div>
        <div class="app-body">
            <div class="app-name">{name}</div>
            <div class="app-desc">{desc}</div>
            <div class="app-btns">
                <a class="btn-app btn-primary-{class_num}" href="{streamlit}" target="_blank">Ver app</a>
                <a class="btn-app btn-ghost" href="{github}" target="_blank">Código</a>
            </div>
        </div>
    </div>
    """

# ─── RENDER ────────────────────────────────────────────────────────────────────
for class_num, info in CLASSES.items():
    apps = info["apps"]

    st.markdown(f"""
    <div class="section-hdr">
        <div class="section-num">{class_num}</div>
        <div>
            <div class="section-label">Clase {class_num}</div>
            <div class="section-name">{info["title"]}</div>
        </div>
        <div class="section-badge">{len(apps)} apps</div>
    </div>
    """, unsafe_allow_html=True)

    cols = st.columns(min(len(apps), 3))
    for i, app in enumerate(apps):
        with cols[i % len(cols)]:
            st.markdown(render_card(app, class_num), unsafe_allow_html=True)
