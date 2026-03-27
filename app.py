import streamlit as st
import urllib.parse

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(
    page_title="Dakar Auto Elite",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CSS PERSONNALISÉ (STYLE AUTOMOBILE PREMIUM) ---
st.markdown("""
    <style>
    [data-testid="stHeader"] { visibility: hidden; }
    
    /* Arrière-plan animé type "Asphalte & Nuit" */
    .stApp {
        background: linear-gradient(-45deg, #0f0f0f, #1a1a2e, #16213e, #0f3460);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
        color: white;
    }
    
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Cartes Produits */
    .car-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 20px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        text-align: left;
        transition: transform 0.3s;
        margin-bottom: 20px;
    }
    .car-card:hover {
        transform: translateY(-5px);
        border-color: #00d2ff;
    }
    .car-img {
        width: 100%;
        height: 200px;
        object-fit: cover;
        border-radius: 15px;
        margin-bottom: 15px;
    }
    
    /* Carte VIP Auto */
    .vip-card {
        background: linear-gradient(135deg, #000000 0%, #434343 100%);
        color: #ffffff;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #00d2ff;
        box-shadow: 0 0 20px rgba(0, 210, 255, 0.2);
        position: relative;
        overflow: hidden;
    }
    .vip-card::after {
        content: "DRIVE";
        position: absolute;
        bottom: -10px;
        right: 10px;
        font-size: 40px;
        opacity: 0.05;
        font-weight: 900;
    }
    
    /* Boutons personnalisés */
    .stButton>button {
        border-radius: 10px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# --- EN-TÊTE ---
st.markdown("""
    <div style="text-align: center; padding: 30px 0;">
        <h1 style="font-size: 2.5rem; margin:0; letter-spacing: 2px;">DAKAR <span style="color: #00d2ff;">AUTO</span> ELITE</h1>
        <p style="letter-spacing: 5px; opacity: 0.6; font-size: 0.9rem; text-transform: uppercase;">Véhicules d'Exception & Services Premium</p>
    </div>
""", unsafe_allow_html=True)

# --- INVENTAIRE DES VOITURES ---
st.markdown("### 🏎️ Sélection du Moment")

cars = [
    {
        "modele": "SUV Hybride 2022", 
        "prix": "18.500.000 F", 
        "info": "Automatique • Essence • 45k km",
        "img": "https://images.unsplash.com/photo-1533473359331-0135ef1b58bf?q=80&w=800"
    },
    {
        "modele": "Berline Luxe", 
        "prix": "12.000.000 F", 
        "info": "Automatique • Diesel • 60k km",
        "img": "https://images.unsplash.com/photo-1503376780353-7e6692767b70?q=80&w=800"
    }
]

# Initialisation session state
if 'voiture_selectionnee' not in st.session_state:
    st.session_state.voiture_selectionnee = None

col1, col2 = st.columns(2)
for i, c in enumerate(cars):
    target_col = col1 if i % 2 == 0 else col2
    with target_col:
        st.markdown(f"""
            <div class="car-card">
                <img src="{c['img']}" class="car-img">
                <h3 style="margin:0; color: #00d2ff;">{c['modele']}</h3>
                <p style="opacity:0.8; font-size: 0.9rem; margin-top:5px;">{c['info']}</p>
                <h4 style="color: white; font-weight: bold;">{c['prix']}</h4>
            </div>
        """, unsafe_allow_html=True)
        if st.button(f"Réserver ce véhicule", key=f"car_{i}", use_container_width=True):
            st.session_state.voiture_selectionnee = c['modele']
            st.session_state.prix_voiture = c['prix']

if st.session_state.voiture_selectionnee:
    st.info(f"🚘 Véhicule choisi : **{st.session_state.voiture_selectionnee}**")

    # Bouton WhatsApp pour confirmer la réservation
    message = f"Bonjour, je souhaite réserver le véhicule {st.session_state.voiture_selectionnee} au prix de {st.session_state.prix_voiture}."
    whatsapp_url = f"https://wa.me/221771234567?text={urllib.parse.quote(message)}"
    st.markdown(f"[📲 Confirmer via WhatsApp]({whatsapp_url})", unsafe_allow_html=True)

# --- SERVICES & LIVRAISON ---
st.divider()
st.subheader("🛠️ Services & Livraison")

col_left, col_right = st.columns(2)

with col_left:
    st.markdown("""
        <div class="vip-card">
            <h3>🚚 Livraison Premium</h3>
            <p>Transport sécurisé et rapide partout au Sénégal.</p>
        </div>
    """, unsafe_allow_html=True)

with col_right:
    st.markdown("""
        <div class="vip-card">
            <h3>🛠️ Service VIP</h3>
            <p>Entretien, assistance et suivi personnalisé pour votre véhicule.</p>
        </div>
    """, unsafe_allow_html=True)
