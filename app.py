import streamlit as st
import urllib.parse

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(
    page_title="Dakar Elite Auto & Moto",
    page_icon="🇸🇳",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- BLOC CSS (CORRIGÉ POUR NE PAS S'AFFICHER) ---
st.markdown("""
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/lipis/flag-icons@7.0.0/css/flag-icons.min.css"/>
    <style>
    /* Cache le menu Streamlit par défaut */
    [data-testid="stHeader"] { visibility: hidden; }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Fond du site */
    .stApp {
        background-color: #1a1a1a;
        color: #ffffff;
    }

    /* Style des Cartes */
    .product-card {
        background: #262626;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #333;
        margin-bottom: 10px;
        transition: 0.3s ease;
    }
    
    .product-card:hover {
        border-color: #bdc3c7;
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.5);
    }

    /* Images des produits */
    .product-img {
        width: 100%;
        height: 250px;
        object-fit: cover;
        border-radius: 10px;
        background: #000;
    }

    /* Badge Sénégal */
    .sn-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(0, 255, 100, 0.1);
        color: #00ff88;
        padding: 6px 12px;
        border-radius: 5px;
        font-size: 0.85rem;
        margin: 15px 0;
        font-weight: bold;
    }

    /* Prix */
    .price-text {
        color: #ffffff;
        font-weight: 900;
        font-size: 1.6rem;
        margin: 10px 0;
    }

    /* Bouton WhatsApp Vert */
    .wa-button {
        display: block;
        text-align: center;
        background-color: #25D366;
        color: white !important;
        padding: 12px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        margin-top: 10px;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        justify-content: center;
        gap: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# --- BASE DE DONNÉES PRODUITS ---
inventory = [
    {
        "mod": "Range Rover Vogue SV 2022",
        "px": "95.000.000 F",
        "desc": "V8 Special Vehicle Operations • Gris Satin • Intérieur Executive",
        "img": "https://images.unsplash.com/photo-1645731504302-601934960960?q=80&w=1000"
    },
    {
        "mod": "Hyundai Tucson 2023",
        "px": "24.500.000 F",
        "desc": "Modèle 2023 • Calandre Paramétrique • Neuf 0km",
        "img": "https://images.unsplash.com/photo-1669811400262-9e9095697669?q=80&w=1000"
    },
    {
        "mod": "KTM Duke 125/200",
        "px": "2.200.000 F",
        "desc": "Style KTM 110 Ready-to-race • Performance & Agilité",
        "img": "https://images.unsplash.com/photo-1599819811279-d5ad9cccf838?q=80&w=1000"
    },
    {
        "mod": "Yamaha NMAX 155",
        "px": "2.150.000 F",
        "desc": "Scooter Urbain • ABS • Éclairage LED • Neuf",
        "img": "https://images.unsplash.com/photo-1611082590912-3255dfb82813?q=80&w=1000"
    }
]

# --- EN-TÊTE ---
st.markdown("""
    <div style="text-align: center; padding: 20px 0;">
        <h1 style="font-size: 3rem; margin:0; letter-spacing: 2px;">DAKAR <span style="color: #bdc3c7;">ELITE</span></h1>
        <p style="font-size: 1.2rem;"><span class="fi fi-sn"></span> Showroom Almadies - Excellence Automobile</p>
    </div>
""", unsafe_allow_html=True)

# --- NAVIGATION ---
tab1, tab2, tab3 = st.tabs(["🏠 ACCUEIL", "🔍 RECHERCHE", "📞 CONTACT"])

with tab1:
    col1, col2 = st.columns(2)
    
    for i, item in enumerate(inventory):
        with (col1 if i % 2 == 0 else col2):
            msg = f"Bonjour Dakar Elite 🇸🇳, je suis intéressé par le modèle {item['mod']}."
            wa_url = f"https://wa.me/221770000000?text={urllib.parse.quote(msg)}"
            
            st.markdown(f"""
                <div class="product-card">
                    <img src="{item['img']}" class="product-img">
                    <div class="sn-badge"><span class="fi fi-sn"></span> DISPONIBLE À DAKAR</div>
                    <h2 style="margin:0; font-size:1.6rem; color: #bdc3c7;">{item['mod']}</h2>
                    <p style="opacity:0.8; font-size: 0.95rem; margin: 10px 0;">{item['desc']}</p>
                    <p class="price-text">{item['px']}</p>
                    <a href="{wa_url}" target="_blank" class="wa-button">RÉSERVER SUR WHATSAPP</a>
                </div>
            """, unsafe_allow_html=True)
            st.write("") # Espaceur

with tab2:
    st.write("### Filtres de recherche")
    st.multiselect("Marques disponibles", ["Toyota", "Mercedes", "Hyundai", "Range Rover", "Yamaha", "KTM"])
    st.slider("Budget Maximum (F CFA)", 1000000, 100000000, 50000000)

with tab3:
    st.markdown("""
        <div style="background: #262626; padding: 40px; border-radius: 15px; text-align: center;">
            <h2>📍 Retrouvez-nous</h2>
            <p>Route des Almadies, en face de la banque SG.</p>
            <p>Dakar, Sénégal</p>
            <hr style="border-color: #444;">
            <h3>🕘 Horaires</h3>
            <p>Lundi - Samedi : 09h00 - 19h00</p>
        </div>
    """, unsafe_allow_html=True)

# --- PIED DE PAGE ---
st.markdown("<br><center>Dakar Elite © 2026 - Le prestige au Sénégal 🇸🇳</center>", unsafe_allow_html=True)
