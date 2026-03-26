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

/* Global */
html, body, [class*="css"] { font-family: 'Syne', sans-serif; }

/* Hide Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 2rem; padding-bottom: 4rem; max-width: 1100px; }

/* ── Hero ─────────────────────────────────── */
.hero {
    padding: 48px 0 32px;
    border-bottom: 1px solid rgba(255,255,255,0.08);
    margin-bottom: 16px;
}
.hero-tag {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #c8f04d;
    margin-bottom: 16px;
    display: flex;
    align-items: center;
    gap: 10px;
}
.hero-tag::before {
    content: '';
    display: inline-block;
    width: 20px;
    height: 1px;
    background: #c8f04d;
}
.hero h1 {
    font-family: 'DM Serif Display', serif;
    font-size: clamp(36px, 5vw, 64px);
    font-weight: 400;
    letter-spacing: -0.02em;
    line-height: 1.1;
    margin-bottom: 16px;
}
.hero h1 em { font-style: italic; color: #c8f04d; }
.hero-desc {
    color: #888;
    font-size: 15px;
    line-height: 1.7;
    max-width: 480px;
    font-weight: 400;
}

/* ── Section header ───────────────────────── */
.section-hdr {
    display: flex;
    align-items: center;
    gap: 20px;
    margin: 56px 0 28px;
    padding-bottom: 16px;
    border-bottom: 1px solid rgba(255,255,255,0.08);
}
.section-num {
    font-family: 'DM Serif Display', serif;
    font-size: 56px;
    font-weight: 400;
    opacity: 0.08;
    line-height: 1;
    user-select: none;
}
.section-label {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 0.2em;
    margin-bottom: 4px;
}
.section-name {
    font-family: 'DM Serif Display', serif;
    font-size: 24px;
    font-weight: 400;
    letter-spacing: -0.01em;
}
.section-badge {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    padding: 4px 10px;
    border-radius: 100px;
    border: 1px solid rgba(255,255,255,0.15);
    color: #888;
    margin-left: auto;
}

/* Color accents per class */
.cl6 .section-label { color: #c8f04d; }
.cl7 .section-label { color: #4df0b4; }
.cl8 .section-label { color: #f0a84d; }
.cl9 .section-label { color: #c44df0; }

/* ── App card ─────────────────────────────── */
.app-card {
    background: #1a1a1a;
    border: 1px solid #2a2a2a;
    border-radius: 12px;
    overflow: hidden;
    transition: transform 0.2s, border-color 0.2s;
    height: 100%;
    display: flex;
    flex-direction: column;
}
.app-card:hover { transform: translateY(-4px); border-color: #3a3a3a; }

.app-thumb {
    aspect-ratio: 16/10;
    background: #111;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    gap: 8px;
    border-bottom: 1px solid #2a2a2a;
    overflow: hidden;
}
.app-thumb img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
}
.thumb-icon { font-size: 28px; opacity: 0.3; }
.thumb-label {
    font-family: 'DM Mono', monospace;
    font-size: 9px;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #555;
}

.app-body { padding: 14px 16px; flex: 1; display: flex; flex-direction: column; }
.app-name { font-size: 13px; font-weight: 600; margin-bottom: 6px; letter-spacing: -0.01em; }
.app-desc { font-size: 11px; color: #666; line-height: 1.6; flex: 1; font-weight: 400; }

.app-btns { display: flex; gap: 6px; margin-top: 14px; }
.btn-app {
    flex: 1;
    padding: 7px 8px;
    border-radius: 7px;
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    text-align: center;
    text-decoration: none;
    display: block;
    transition: opacity 0.15s;
    font-weight: 500;
}
.btn-app:hover { opacity: 0.8; text-decoration: none; }
.btn-primary-6  { background: #c8f04d; color: #0d0d0d; }
.btn-primary-7  { background: #4df0b4; color: #0d0d0d; }
.btn-primary-8  { background: #f0a84d; color: #0d0d0d; }
.btn-primary-9  { background: #c44df0; color: #fff; }
.btn-ghost {
    background: transparent;
    border: 1px solid #2a2a2a;
    color: #666;
}
.btn-ghost:hover { border-color: #666; color: #ccc; }

/* Bg per class */
.thumb-bg-6 { background: #161f03 !important; }
.thumb-bg-7 { background: #031f16 !important; }
.thumb-bg-8 { background: #1f1003 !important; }
.thumb-bg-9 { background: #110318 !important; }
</style>
""", unsafe_allow_html=True)

# ─── Data ──────────────────────────────────────────────────────────────────────
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
                "github": "https://github.com/TU-USUARIO/TU-REPO",
                "screenshot": None,
            },
            {
                "name": "Cuento",
                "desc": "Generador de cuentos interactivos.",
                "icon": "📖",
                "streamlit": "https://amarillacomogato.streamlit.app",
                "github": "https://github.com/TU-USUARIO/TU-REPO",
                "screenshot": None,
            },
        ],
    },
    7: {
        "color": "#4df0b4",
        "label": "cl7",
        "title": "Interfaces de voz a texto.",
        "apps": [
            {
                "name": "Traductor",
                "desc": "App de traducción de texto.",
                "icon": "🌐",
                "streamlit": "https://traduciendooo.streamlit.app",
                "github": "https://github.com/TU-USUARIO/TU-REPO",
                "screenshot": None,
            },
            {
                "name": "Reconocimiento óptico de caracteres con audio",
                "desc": "OCR combinado con síntesis de voz.",
                "icon": "🎙️",
                "streamlit": "https://audicionandopara.streamlit.app",
                "github": "https://github.com/TU-USUARIO/TU-REPO",
                "screenshot": None,
            },
            {
                "name": "Reconocimiento óptico de caracteres",
                "desc": "Extracción de texto desde imágenes.",
                "icon": "🔍",
                "streamlit": "https://reconociendocaracter.streamlit.app",
                "github": "https://github.com/TU-USUARIO/TU-REPO",
                "screenshot": None,
            },
        ],
    },
    8: {
        "color": "#f0a84d",
        "label": "cl8",
        "title": "Procesamiento de lenguaje Natural.",
        "apps": [
            {
                "name": "Análisis de sentimientos",
                "desc": "Clasificación de emociones en textos.",
                "icon": "😶",
                "streamlit": "https://tristepqnomepagan.streamlit.app",
                "github": "https://github.com/TU-USUARIO/TU-REPO",
                "screenshot": None,
            },
            {
                "name": "WordCloud Studio",
                "desc": "Generador de nubes de palabras.",
                "icon": "☁️",
                "streamlit": "https://cuandopagan.streamlit.app",
                "github": "https://github.com/TU-USUARIO/TU-REPO",
                "screenshot": None,
            },
            {
                "name": "Demo de TF-IDF con Preguntas y Respuestas",
                "desc": "Búsqueda semántica con TF-IDF.",
                "icon": "❓",
                "streamlit": "https://todavianomepagan.streamlit.app",
                "github": "https://github.com/TU-USUARIO/TU-REPO",
                "screenshot": None,
            },
        ],
    },
    9: {
        "color": "#c44df0",
        "label": "cl9",
        "title": "Aplicaciones con visión artificial.",
        "apps": [
            {
                "name": "Reconocimiento de Imágenes",
                "desc": "Clasificación de imágenes con IA.",
                "icon": "🖼️",
                "streamlit": "https://tamalitootabueno.streamlit.app",
                "github": "https://github.com/TU-USUARIO/TU-REPO",
                "screenshot": None,
            },
            {
                "name": "Detección de Objetos en Imágenes",
                "desc": "Detección de objetos con YOLO.",
                "icon": "🎯",
                "streamlit": "https://yolooenel2013.streamlit.app",
                "github": "https://github.com/TU-USUARIO/TU-REPO",
                "screenshot": None,
            },
        ],
    },
}

# ─── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-tag">Portafolio de aplicaciones</div>
  <h1>Portafolio <br>de apps de <em>interfaces</em> multimodales</h1>
  <p class="hero-desc">
    Colección de aplicaciones interactivas desarrolladas durante el curso,
    desplegadas en Streamlit y con código abierto en GitHub.
  </p>
</div>
""", unsafe_allow_html=True)

# ─── Render cards per class ────────────────────────────────────────────────────
def render_thumb(app, class_num):
    bg_class = f"thumb-bg-{class_num}"
    if app["screenshot"]:
        return f'<div class="app-thumb"><img src="{app["screenshot"]}" alt="{app["name"]}"></div>'
    return f"""
    <div class="app-thumb {bg_class}">
        <span class="thumb-icon">{app["icon"]}</span>
        <span class="thumb-label">screenshot</span>
    </div>"""

def render_card(app, class_num):
    thumb = render_thumb(app, class_num)
    return f"""
    <div class="app-card">
        {thumb}
        <div class="app-body">
            <div class="app-name">{app["name"]}</div>
            <div class="app-desc">{app["desc"]}</div>
            <div class="app-btns">
                <a class="btn-app btn-primary-{class_num}" href="{app["streamlit"]}" target="_blank">▲ Ver app</a>
                <a class="btn-app btn-ghost" href="{app["github"]}" target="_blank">⌥ Código</a>
            </div>
        </div>
    </div>"""

for class_num, info in CLASSES.items():
    label = info["label"]
    color = info["color"]
    n = len(info["apps"])

    st.markdown(f"""
    <div class="section-hdr {label}">
        <div class="section-num">{class_num}</div>
        <div>
            <div class="section-label">Clase {class_num}</div>
            <div class="section-name">{info["title"]}</div>
        </div>
        <div class="section-badge">{n} apps</div>
    </div>
    """, unsafe_allow_html=True)

    cols = st.columns(min(n, 3), gap="small")
    for i, app in enumerate(info["apps"]):
        with cols[i % 3]:
            st.markdown(render_card(app, class_num), unsafe_allow_html=True)

# ─── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center; margin-top:60px; padding-top:32px;
            border-top:1px solid rgba(255,255,255,0.08);
            font-family:'DM Mono',monospace; font-size:11px; color:#555;">
  Hecho con Python &amp; Streamlit &nbsp;·&nbsp;
  <a href="https://github.com/TU-USUARIO" target="_blank"
     style="color:#c8f04d; text-decoration:none;">GitHub</a>
</div>
""", unsafe_allow_html=True)
