import streamlit as st
import urllib.parse

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(
    page_title="Dakar Auto & Moto Elite",
    page_icon="🇸🇳",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CSS PERSONNALISÉ (STYLE GRIS MÉTALLIQUE & PREMIUM SÉNÉGAL) ---
st.markdown("""
    <style>
    [data-testid="stHeader"] { visibility: hidden; }
    
    /* Arrière-plan dégradé Gris Anthracite / Acier */
    .stApp {
        background: linear-gradient(-45deg, #121212, #2c3e50, #1a1a1a, #434343);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
        color: #e0e0e0;
    }
    
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Cartes Produits (Effet Verre Dépoli Gris) */
    .product-card {
        background: rgba(255, 255, 255, 0.07);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        text-align: left;
        transition: all 0.3s ease;
        margin-bottom: 20px;
    }
    .product-card:hover {
        transform: translateY(-8px);
        border-color: #bdc3c7;
        box-shadow: 0 10px 20px rgba(0,0,0,0.5);
    }
    .product-img {
        width: 100%;
        height: 180px;
        object-fit: cover;
        border-radius: 10px;
        margin-bottom: 15px;
        border-bottom: 2px solid #34495e;
    }
    
    /* Badge Sénégal */
    .sn-badge {
        background-color: #00853f;
        color: white;
        padding: 2px 8px;
        border-radius: 5px;
        font-size: 0.7rem;
        font-weight: bold;
        margin-right: 5px;
    }

    /* Titres et Boutons */
    h1, h2, h3 { font-family: 'Inter', sans-serif; color: #ffffff; }
    .stButton>button {
        background-color: #ffffff !important;
        color: #1a1a1a !important;
        border-radius: 8px;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #bdc3c7 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- EN-TÊTE ---
st.markdown("""
    <div style="text-align: center; padding: 20px 0;">
        <p style="letter-spacing: 3px; color: #00853f; font-weight: bold; margin-bottom: 0;">🇸🇳 LE PRESTIGE AU SÉNÉGAL</p>
        <h1 style="font-size: 3rem; margin:0; letter-spacing: 1px;">DAKAR <span style="color: #bdc3c7;">ELITE</span></h1>
        <p style="opacity: 0.7; font-size: 1rem;">L'excellence automobile et deux-roues au cœur de la capitale.</p>
    </div>
""", unsafe_allow_html=True)

# --- LOGIQUE DE SÉLECTION ---
if 'selection' not in st.session_state:
    st.session_state.selection = None

# --- SECTION VOITURES ---
st.markdown("## 🚗 Véhicules de Prestige")
cars = [
    {"mod": "Range Rover Sport 2023", "px": "65.000.000 F", "desc": "V8 • Full Options • Neuf", "img": "https://images.unsplash.com/photo-1590362891175-3794ef169f24?q=80&w=800"},
    {"mod": "Mercedes Classe G", "px": "85.000.000 F", "desc": "AMG • Noir Obsidienne • Dakar Ready", "img": "https://images.unsplash.com/photo-1520031441872-265e4ff70366?q=80&w=800"}
]

c1, c2 = st.columns(2)
for i, c in enumerate(cars):
    with (c1 if i==0 else c2):
        st.markdown(f"""<div class="product-card">
            <img src="{c['img']}" class="product-img">
            <span class="sn-badge">DISPONIBLE DAKAR</span>
            <h3 style="margin:5px 0;">{c['mod']}</h3>
            <p style="opacity:0.7;">{c['desc']}</p>
            <h4 style="color: #bdc3c7;">{c['px']}</h4>
        </div>""", unsafe_allow_html=True)
        if st.button(f"Réserver {c['mod']}", key=f"car_{i}"):
            st.session_state.selection = c

# --- SECTION MOTOS ---
st.divider()
st.markdown("## 🏍️ Univers Deux-Roues")
motos = [
    {"mod": "Yamaha TMAX 560", "px": "8.500.000 F", "desc": "Série Tech MAX • 2024 • Neuf", "img": "https://images.unsplash.com/photo-1568772585407-9361f9bf3a87?q=80&w=800"},
    {"mod": "BMW R 1250 GS", "px": "14.000.000 F", "desc": "Adventure Edition • Idéal Routes Sénégal", "img": "https://images.unsplash.com/photo-1591637333184-19aa84b3e01f?q=80&w=800"}
]

m1, m2 = st.columns(2)
for i, m in enumerate(motos):
    with (m1 if i==0 else m2):
        st.markdown(f"""<div class="product-card">
            <img src="{m['img']}" class="product-img">
            <span class="sn-badge">STOCK LOCAL</span>
            <h3 style="margin:5px 0;">{m['mod']}</h3>
            <p style="opacity:0.7;">{m['desc']}</p>
            <h4 style="color: #bdc3c7;">{m['px']}</h4>
        </div>""", unsafe_allow_html=True)
        if st.button(f"Réserver {m['mod']}", key=f"moto_{i}"):
            st.session_state.selection = m

# --- CONTACT WHATSAPP ---
if st.session_state.selection:
    sel = st.session_state.selection
    st.success(f"✅ Vous avez sélectionné : **{sel['mod']}**")
    msg = f"Bonjour Dakar Elite, je suis intéressé par le modèle {sel['mod']} affiché à {sel['px']}. Est-il disponible pour une visite ?"
    whatsapp_url = f"https://wa.me/221770000000?text={urllib.parse.quote(msg)}"
    st.markdown(f"""
        <a href="{whatsapp_url}" target="_blank" style="text-decoration: none;">
            <div style="background-color: #25D366; color: white; padding: 15px; border-radius: 10px; text-align: center; font-weight: bold;">
                CONTACTER NOTRE SHOWROOM SUR WHATSAPP 🇸🇳
            </div>
        </a>
    """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<br><hr><center>Dakar Elite © 2026 - Almadies, Dakar, Sénégal</center>", unsafe_allow_html=True)
