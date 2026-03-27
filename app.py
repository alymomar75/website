import streamlit as st
import urllib.parse

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(
    page_title="Dakar Auto & Moto Elite",
    page_icon="🇸🇳",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- IMPORT DES DRAPEAUX & CSS ---
st.markdown("""
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/lipis/flag-icons@7.0.0/css/flag-icons.min.css"/>
    <style>
    [data-testid="stHeader"] { visibility: hidden; }
    .stApp {
        background: linear-gradient(-45deg, #0f0f0f, #232526, #414345, #1a1a1a);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
        color: #e0e0e0;
    }
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    .product-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
        margin-bottom: 20px;
        height: 450px;
    }
    .product-card:hover {
        transform: translateY(-8px);
        border-color: #bdc3c7;
    }
    .product-img {
        width: 100%;
        height: 200px;
        object-fit: cover;
        border-radius: 10px;
    }
    .sn-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(255, 255, 255, 0.1);
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.7rem;
        margin-top: 10px;
    }
    /* Style des Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
        justify-content: center;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: transparent !important;
        border-radius: 4px 4px 0px 0px;
        color: white !important;
        font-weight: bold;
        text-transform: uppercase;
    }
    .stTabs [aria-selected="true"] {
        border-bottom: 2px solid #bdc3c7 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- BASE DE DONNÉES ÉTENDUE ---
inventory = [
    {"type": "Voiture", "marque": "Mercedes", "mod": "Classe G 63 AMG", "px": 95000000, "desc": "V8 Biturbo • 2023 • Noir", "img": "https://images.unsplash.com/photo-1520031441872-265e4ff70366?q=80&w=800"},
    {"type": "Voiture", "marque": "Toyota", "mod": "Land Cruiser 300", "px": 75000000, "desc": "V6 Diesel • Neuf • Full Option", "img": "https://images.unsplash.com/photo-1541899481282-d53bffe3c35d?q=80&w=800"},
    {"type": "Voiture", "marque": "Range Rover", "mod": "Vogue Autobiography", "px": 110000000, "desc": "Hybride • 2024 • Luxe Absolu", "img": "https://images.unsplash.com/photo-1590362891175-3794ef169f24?q=80&w=800"},
    {"type": "Voiture", "marque": "Hyundai", "mod": "Tucson 2023", "px": 195000000, "desc": "Essence • Automatique • Dakar", "img": "https://images.unsplash.com/photo-1620215175664-cb9a6f5b6103?q=80&w=800"},
    {"type": "Moto", "marque": "Yamaha", "mod": "TMAX 560 Tech Max", "px": 8900000, "desc": "Gris Nardo • 2024 • Connectée", "img": "https://images.unsplash.com/photo-1568772585407-9361f9bf3a87?q=80&w=800"},
    {"type": "Moto", "marque": "BMW", "mod": "R 1250 GS Adventure", "px": 14500000, "desc": "Triple Black • Pack Touring", "img": "https://images.unsplash.com/photo-1591637333184-19aa84b3e01f?q=80&w=800"},
    {"type": "Moto", "marque": "Kawasaki", "mod": "Ninja ZX-10R", "px": 12000000, "desc": "Vert KRT • Performance Pure", "img": "https://images.unsplash.com/photo-1444491741275-3747c53c99b4?q=80&w=800"},
    {"type": "Moto", "marque": "Honda", "mod": "Africa Twin", "px": 10500000, "desc": "DCT • Idéal Pistes Sénégal", "img": "https://images.unsplash.com/photo-1558981403-c5f9899a28bc?q=80&w=800"}
]

# --- EN-TÊTE ---
st.markdown("""
    <div style="text-align: center; padding: 10px 0;">
        <h1 style="font-size: 2.5rem; margin:0; letter-spacing: 2px;">DAKAR <span style="color: #bdc3c7;">ELITE</span></h1>
        <p style="opacity: 0.8;"><span class="fi fi-sn"></span> Concessionnaire Multimarque Premium</p>
    </div>
""", unsafe_allow_html=True)

# --- NAVIGATION (CATALOGUE) ---
tab_home, tab_search, tab_brands = st.tabs(["🏠 Accueil", "🔍 Recherche & Filtres", "🏭 Marques proposées"])

# --- TAB : ACCUEIL ---
with tab_home:
    st.markdown("### 🔥 Les Exclusivités du Moment")
    cols = st.columns(2)
    for i, item in enumerate(inventory[:4]): # Affiche les 4 premiers
        with cols[i % 2]:
            st.markdown(f"""<div class="product-card">
                <img src="{item['img']}" class="product-img">
                <div class="sn-badge"><span class="fi fi-sn"></span> DAKAR STOCK</div>
                <h3>{item['mod']}</h3>
                <p>{item['desc']}</p>
                <h4 style="color: #bdc3c7;">{item['px']:,} F CFA</h4>
            </div>""", unsafe_allow_html=True)
            if st.button(f"S'informer sur {item['mod']}", key=f"home_{i}"):
                st.toast(f"Demande envoyée pour {item['mod']}")

# --- TAB : RECHERCHE ---
with tab_search:
    st.markdown("### 🔍 Affiner votre choix")
    col_f1, col_f2, col_f3 = st.columns(3)
    
    with col_f1:
        f_type = st.selectbox("Type de véhicule", ["Tous", "Voiture", "Moto"])
    with col_f2:
        max_px = st.slider("Budget Maximum (F CFA)", 5000000, 150000000, 150000000, step=1000000)
    with col_f3:
        search_query = st.text_input("Modèle spécifique...", "")

    # Filtrage
    results = [i for i in inventory if (f_type == "Tous" or i['type'] == f_type) 
               and i['px'] <= max_px 
               and (search_query.lower() in i['mod'].lower())]

    st.write(f"**{len(results)}** résultats trouvés")
    
    # Affichage grille
    grid_cols = st.columns(3)
    for idx, item in enumerate(results):
        with grid_cols[idx % 3]:
            st.markdown(f"""<div class="product-card">
                <img src="{item['img']}" class="product-img">
                <h3 style="font-size: 1.1rem;">{item['mod']}</h3>
                <p style="font-size: 0.8rem; height: 40px;">{item['desc']}</p>
                <h4 style="color: #bdc3c7;">{item['px']:,} F</h4>
            </div>""", unsafe_allow_html=True)
            if st.button("Réserver via WhatsApp 🇸🇳", key=f"res_{idx}"):
                msg = f"Bonjour Dakar Elite, je suis intéressé par {item['mod']} ({item['px']:,} F)."
                st.markdown(f'<meta http-equiv="refresh" content="0;url=https://wa.me/221770000000?text={urllib.parse.quote(msg)}">', unsafe_allow_html=True)

# --- TAB : MARQUES ---
with tab_brands:
    st.markdown("### 🏆 Nos Partenaires Officiels")
    brands = {
        "Allemandes": ["Mercedes-Benz", "BMW", "Audi", "Porsche"],
        "Japonaises": ["Toyota", "Lexus", "Yamaha", "Honda"],
        "Luxe": ["Range Rover", "Bentley", "Lamborghini"]
    }
    b_col1, b_col2, b_col3 = st.columns(3)
    with b_col1:
        st.write("**🇪🇺 ALLEMANDES**")
        for b in brands["Allemandes"]: st.write(f"• {b}")
    with b_col2:
        st.write("**🇯🇵 JAPONAISES**")
        for b in brands["Japonaises"]: st.write(f"• {b}")
    with b_col3:
        st.write("**💎 PRESTIGE**")
        for b in brands["Luxe"]: st.write(f"• {b}")

# --- FOOTER ---
st.markdown(f"""
    <br><hr>
    <div style="text-align: center; opacity: 0.6; padding: 20px;">
        <span class="fi fi-sn"></span> Dakar Elite - Showroom Almadies | Ouvert du Lundi au Samedi
    </div>
""", unsafe_allow_html=True)
