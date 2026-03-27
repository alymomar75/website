import streamlit as st
import urllib.parse

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(
    page_title="Dakar Elite Auto & Moto",
    page_icon="🇸🇳",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CSS CORRECTEMENT ENCAPSULÉ ---
st.markdown("""
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/lipis/flag-icons@7.0.0/css/flag-icons.min.css"/>
    <style>
    /* Masquer le header Streamlit */
    [data-testid="stHeader"] { visibility: hidden; }
    
    /* Fond Gris Anthracite */
    .stApp {
        background: #1a1a1a;
        color: #ffffff;
    }
    
    /* Cartes Produits */
    .product-card {
        background: #262626;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #333;
        margin-bottom: 20px;
        transition: 0.3s;
    }
    
    .product-card:hover {
        border-color: #bdc3c7;
        transform: translateY(-5px);
    }

    .product-img {
        width: 100%;
        height: 250px;
        object-fit: contain; /* Pour voir toute la voiture sans coupure */
        border-radius: 8px;
        background: #000;
    }

    .sn-badge {
        display: inline-flex;
        align-items: center;
        gap: 5px;
        background: rgba(0, 255, 100, 0.1);
        color: #00ff88;
        padding: 5px 10px;
        border-radius: 5px;
        font-size: 0.8rem;
        margin: 10px 0;
    }

    .price-text {
        color: #ffffff;
        font-weight: bold;
        font-size: 1.4rem;
    }
    
    /* Navigation */
    .stTabs [data-baseweb="tab-list"] { justify-content: center; gap: 50px; }
    button[kind="secondary"] { background: #25D366 !important; color: white !important; border: none !important; }
    </style>
""", unsafe_allow_html=True)

# --- BASE DE DONNÉES PRODUITS (PHOTOS RÉELLES) ---
inventory = [
    {
        "cat": "Voiture",
        "mod": "Range Rover Vogue SV 2022",
        "px": "95.000.000 F",
        "desc": "Édition SV • Gris Flux • Intérieur Cuir étendu",
        "img": "https://images.unsplash.com/photo-1645731504302-601934960960?q=80&w=1000"
    },
    {
        "cat": "Voiture",
        "mod": "Hyundai Tucson 2023",
        "px": "24.500.000 F",
        "desc": "Finition Prestige • Full LED • Caméra 360°",
        "img": "https://images.unsplash.com/photo-1669811400262-9e9095697669?q=80&w=1000"
    },
    {
        "cat": "Moto",
        "mod": "KTM 110 (SX/Duke Style)",
        "px": "1.850.000 F",
        "desc": "Moteur monocylindre • Très agile • Parfait pour débuter",
        "img": "https://images.unsplash.com/photo-1599819811279-d5ad9cccf838?q=80&w=1000"
    },
    {
        "cat": "Moto",
        "mod": "Yamaha NMAX 155",
        "px": "2.100.000 F",
        "desc": "ABS • Start & Stop • Stock limité Dakar",
        "img": "https://images.unsplash.com/photo-1611082590912-3255dfb82813?q=80&w=1000"
    }
]

# --- ENTÊTE ---
st.markdown("""
    <div style="text-align: center; padding-bottom: 20px;">
        <h1 style="margin:0; letter-spacing: 3px;">DAKAR <span style="color: #bdc3c7;">ELITE</span></h1>
        <p><span class="fi fi-sn"></span> Showroom Premium - Almadies</p>
    </div>
""", unsafe_allow_html=True)

# --- CATALOGUE ---
tab1, tab2 = st.tabs(["ACCUEIL", "RECHERCHE"])

with tab1:
    col1, col2 = st.columns(2)
    for i, item in enumerate(inventory):
        target_col = col1 if i % 2 == 0 else col2
        with target_col:
            st.markdown(f"""
                <div class="product-card">
                    <img src="{item['img']}" class="product-img">
                    <div class="sn-badge"><span class="fi fi-sn"></span> DISPONIBLE AU SHOWROOM</div>
                    <h2 style="margin:0; font-size:1.5rem;">{item['mod']}</h2>
                    <p style="opacity:0.8;">{item['desc']}</p>
                    <p class="price-text">{item['px']}</p>
                </div>
            """, unsafe_allow_html=True)
            
            # Bouton de contact
            msg = f"Bonjour, je souhaite réserver la {item['mod']}."
            wa_url = f"https://wa.me/221770000000?text={urllib.parse.quote(msg)}"
            st.link_button("RESERVER SUR WHATSAPP 🇸🇳", wa_url, use_container_width=True)

with tab2:
    st.write("Le catalogue complet des marques (Toyota, Mercedes, Yamaha...) arrive bientôt.")

# --- FOOTER ---
st.markdown("<br><hr><center>Dakar Elite Auto & Moto © 2026</center>", unsafe_allow_html=True)
