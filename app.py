import streamlit as st
import urllib.parse

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(
    page_title="Dakar Auto & Moto Elite",
    page_icon="🇸🇳",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CSS PERSONNALISÉ (STYLE ANTHRACITE PREMIUM) ---
st.markdown("""
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/lipis/flag-icons@7.0.0/css/flag-icons.min.css"/>
    <style>
    [data-testid="stHeader"] { visibility: hidden; }
    
    .stApp {
        background: linear-gradient(135deg, #111111 0%, #2c3e50 100%);
        color: #e0e0e0;
    }
    
    .product-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
        margin-bottom: 25px;
    }
    
    .product-card:hover {
        transform: translateY(-5px);
        border-color: #bdc3c7;
        box-shadow: 0 10px 25px rgba(0,0,0,0.5);
    }

    .product-img {
        width: 100%;
        height: 220px;
        object-fit: cover;
        border-radius: 10px;
        background-color: #222; /* Fond de secours */
    }

    .sn-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(0, 133, 63, 0.2);
        color: #00ff88;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.75rem;
        margin-top: 10px;
        border: 1px solid rgba(0, 255, 136, 0.3);
    }

    .price-text {
        color: #ffffff;
        font-weight: 800;
        font-size: 1.3rem;
        margin-top: 5px;
    }
    
    .stTabs [data-baseweb="tab-list"] { justify-content: center; }
    .stButton>button { width: 100%; font-weight: bold; border-radius: 8px; }
    </style>
""", unsafe_allow_html=True)

# --- BASE DE DONNÉES CORRIGÉE ---
inventory = [
    {
        "type": "Voiture", 
        "mod": "Hyundai Tucson 2023", 
        "px": "22.500.000 F", 
        "desc": "Neuf • Automatique • Toit Ouvrant • Garantie 2 ans", 
        "img": "https://images.unsplash.com/photo-1669811400262-9e9095697669?q=80&w=1000"
    },
    {
        "type": "Voiture", 
        "mod": "Range Rover Vogue", 
        "px": "85.000.000 F", 
        "desc": "Luxe Absolu • Pivi Pro • Suspension Pneumatique", 
        "img": "https://images.unsplash.com/photo-1606148632349-564e8c8ada42?q=80&w=1000"
    },
    {
        "type": "Moto", 
        "mod": "Yamaha TMAX 560", 
        "px": "8.500.000 F", 
        "desc": "Tech Max • Full Option • 2024", 
        "img": "https://images.unsplash.com/photo-1591123120675-6f7f1aae0e5b?q=80&w=1000"
    },
    {
        "type": "Moto", 
        "mod": "Scooter NMAX 155", 
        "px": "1.950.000 F", 
        "desc": "Idéal Dakar • Consommation Faible • Neuf", 
        "img": "https://images.unsplash.com/photo-1611082590912-3255dfb82813?q=80&w=1000"
    }
]

# --- EN-TÊTE ---
st.markdown("""
    <div style="text-align: center; padding: 20px 0;">
        <h1 style="font-size: 2.8rem; margin:0; letter-spacing: 2px;">DAKAR <span style="color: #bdc3c7;">ELITE</span></h1>
        <p style="opacity: 0.8;"><span class="fi fi-sn"></span> Votre Partenaire Automobile au Sénégal</p>
    </div>
""", unsafe_allow_html=True)

# --- NAVIGATION ---
tab_acc, tab_rech = st.tabs(["🏠 Accueil", "🔍 Catalogue Complet"])

with tab_acc:
    st.markdown("### ✨ Sélection Premium")
    col1, col2 = st.columns(2)
    
    for i, item in enumerate(inventory):
        with (col1 if i % 2 == 0 else col2):
            st.markdown(f"""
                <div class="product-card">
                    <img src="{item['img']}" class="product-img">
                    <div class="sn-badge"><span class="fi fi-sn"></span> DISPONIBLE DAKAR</div>
                    <h3 style="margin:10px 0 0 0; color:#bdc3c7;">{item['mod']}</h3>
                    <p style="margin:5px 0; font-size:0.9rem; opacity:0.7;">{item['desc']}</p>
                    <p class="price-text">{item['px']}</p>
                </div>
            """, unsafe_allow_html=True)
            
            msg = f"Bonjour Dakar Elite 🇸🇳, je suis intéressé par le modèle {item['mod']}."
            whatsapp_url = f"https://wa.me/221770000000?text={urllib.parse.quote(msg)}"
            st.markdown(f'<a href="{whatsapp_url}" target="_blank" style="text-decoration:none;"><button style="width:100%; padding:10px; background:#25D366; color:white; border:none; border-radius:8px; cursor:pointer; font-weight:bold; margin-bottom:20px;">CONTACTER VIA WHATSAPP</button></a>', unsafe_allow_html=True)

with tab_rech:
    st.info("Utilisez les filtres pour trouver votre prochain véhicule (En cours de développement)")

# --- FOOTER ---
st.markdown("<br><hr><center>Dakar Elite 🇸🇳 - Showroom ouvert aux Almadies</center>", unsafe_allow_html=True)
