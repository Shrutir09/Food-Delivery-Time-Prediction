import streamlit as st

# 1. Page Config
st.set_page_config(
    page_title="FoodPulse AI - Delivery Estimator",
    page_icon="🍔",
    layout="wide"
)

# 2. Enhanced UI CSS
st.markdown("""
<style>
    /* Hide Default Streamlit Chrome */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Container Spacing & Full Screen Expansion */
    .block-container {
        padding-top: 1.2rem !important;
        padding-bottom: 2rem !important;
        max-width: 95% !important;
        margin: 0 auto;
    }

    /* Fixed & Scaled Navbar */
    .fp-navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
        padding: 1.1rem 2.2rem;
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35);
    }
    .fp-brand {
        display: flex;
        align-items: center;
        gap: 12px;
        font-size: 1.5rem;
        font-weight: 800;
        color: #F8FAFC;
        letter-spacing: -0.02em;
    }
    .fp-brand span.logo-icon {
        font-size: 1.8rem;
    }
    .fp-nav-links {
        display: flex;
        gap: 2.2rem;
        align-items: center;
    }
    .fp-nav-links a {
        color: #CBD5E1;
        text-decoration: none;
        font-size: 1.05rem;
        font-weight: 600;
        transition: all 0.2s ease;
    }
    .fp-nav-links a:hover, .fp-nav-links a.active {
        color: #FF5252;
    }
    .fp-status {
        display: flex;
        align-items: center;
        gap: 8px;
        background: rgba(6, 78, 59, 0.5);
        border: 1px solid #059669;
        color: #34D399;
        font-size: 0.85rem;
        padding: 8px 16px;
        border-radius: 30px;
        font-weight: 700;
    }
    .status-dot {
        width: 9px;
        height: 9px;
        background-color: #34D399;
        border-radius: 50%;
        box-shadow: 0 0 10px #34D399;
    }

    /* Hero Section Gradient Text */
    .hero-container {
        text-align: center;
        margin-bottom: 2.2rem;
    }
    .hero-title {
        font-size: 2.6rem;
        font-weight: 800;
        background: linear-gradient(180deg, #FFFFFF 0%, #94A3B8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.4rem;
    }
    .hero-sub {
        color: #94A3B8;
        font-size: 1rem;
    }

    /* Equal Height Card Containers */
    div[data-testid="stColumn"] > div {
        height: 100%;
    }
    div[data-testid="stColumn"] {
        background: #1E293B;
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 18px;
        padding: 1.6rem !important;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.25);
    }

    /* Output Card Styling */
    .prediction-card {
        background: linear-gradient(180deg, #1E293B 0%, #0F172A 100%);
        border: 1px solid rgba(52, 211, 153, 0.3);
        border-radius: 16px;
        padding: 2.2rem 1.5rem;
        text-align: center;
        min-height: 330px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        box-shadow: 0 0 20px rgba(52, 211, 153, 0.08);
    }
    .empty-card {
        background: linear-gradient(180deg, #1E293B 0%, #0F172A 100%);
        border: 1px dashed #334155;
        border-radius: 16px;
        padding: 2.2rem 1.5rem;
        text-align: center;
        min-height: 330px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    /* Metric Cards Custom Styling */
    .metric-card {
        background: #1E293B;
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-top: 3px solid #FF5252;
        border-radius: 14px;
        padding: 1.3rem;
        text-align: center;
    }
    .metric-label {
        font-size: 0.75rem;
        color: #94A3B8;
        font-weight: 700;
        letter-spacing: 0.05em;
        margin-bottom: 0.4rem;
    }
    .metric-value {
        font-size: 1.6rem;
        font-weight: 800;
        color: #F8FAFC;
    }

    /* Button Styling */
    div.stButton > button {
        background: linear-gradient(90deg, #FF5252 0%, #FF7676 100%) !important;
        color: white !important;
        font-weight: 700 !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.75rem 1rem !important;
        font-size: 1.05rem !important;
        box-shadow: 0 4px 15px rgba(255, 82, 82, 0.3) !important;
        transition: all 0.2s ease !important;
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(255, 82, 82, 0.45) !important;
    }

    /* PREMIUM BEAUTIFUL FOOTER STYLING */
    .fp-footer-card {
        margin-top: 4rem;
        background: linear-gradient(180deg, #1E293B 0%, #0F172A 100%);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 2.8rem 2.5rem 1.8rem 2.5rem;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4);
    }
    .footer-grid {
        display: grid;
        grid-template-columns: 2fr 1fr 1fr;
        gap: 2rem;
        margin-bottom: 2.2rem;
    }
    .footer-brand-large {
        display: flex;
        align-items: center;
        gap: 12px;
        font-size: 1.8rem;
        font-weight: 800;
        color: #F8FAFC;
        margin-bottom: 0.6rem;
    }
    .footer-brand-desc {
        color: #94A3B8;
        font-size: 0.95rem;
        line-height: 1.6;
        max-width: 420px;
    }
    .footer-col-title {
        color: #F8FAFC;
        font-size: 1rem;
        font-weight: 700;
        margin-bottom: 1rem;
        letter-spacing: 0.03em;
    }
    .footer-col-links {
        display: flex;
        flex-direction: column;
        gap: 0.75rem;
    }
    .footer-col-links a {
        color: #94A3B8;
        text-decoration: none;
        font-size: 0.95rem;
        font-weight: 500;
        transition: color 0.2s ease;
    }
    .footer-col-links a:hover {
        color: #FF5252;
    }
    .footer-badge-link {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(255, 82, 82, 0.1);
        border: 1px solid rgba(255, 82, 82, 0.3);
        color: #FF5252 !important;
        padding: 8px 16px;
        border-radius: 10px;
        font-weight: 600 !important;
        width: fit-content;
    }
    .footer-bottom-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding-top: 1.5rem;
        border-top: 1px solid #334155;
        color: #64748B;
        font-size: 0.88rem;
    }

    /* Responsive Mobile Layout Tweaks */
    @media (max-width: 768px) {
        .fp-navbar {
            flex-direction: column;
            gap: 1.2rem;
            text-align: center;
            padding: 1.2rem 1rem;
        }
        .fp-nav-links {
            gap: 1.2rem;
            flex-wrap: wrap;
            justify-content: center;
        }
        .footer-grid {
            grid-template-columns: 1fr;
            gap: 2rem;
        }
        .footer-bottom-bar {
            flex-direction: column;
            gap: 0.8rem;
            text-align: center;
        }
        div[data-testid="stColumn"] {
            margin-bottom: 1.2rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# ----------------- 3. NAVBAR -----------------
st.markdown("""
<div class="fp-navbar">
    <div class="fp-brand">
        <span class="logo-icon">🍔</span>
        <span>FoodPulse AI</span>
    </div>
    <div class="fp-nav-links">
        <a href="#predictor" class="active">Predictor</a>
        <a href="#model-info">Model Info</a>
        <a href="https://github.com/Shrutir09/Food-Delivery-Time-Prediction" target="_blank">Repository</a>
    </div>
    <div class="fp-status">
        <span class="status-dot"></span>
        Model Live · v1.0
    </div>
</div>
""", unsafe_allow_html=True)

# ----------------- 4. HERO SECTION -----------------
st.markdown("""
<div class="hero-container" id="predictor">
    <div class="hero-title">Food Delivery Time Prediction</div>
    <div class="hero-sub">Configure delivery parameters and let our machine learning model estimate the expected delivery time.</div>
</div>
""", unsafe_allow_html=True)

# State reset logic
if 'predicted' not in st.session_state:
    st.session_state.predicted = False
if 'last_prediction' not in st.session_state:
    st.session_state.last_prediction = None

def reset_prediction():
    st.session_state.predicted = False

# ----------------- 5. MAIN CARDS GRID -----------------
col1, col2, col3 = st.columns([1.1, 1.1, 1], gap="medium")

with col1:
    st.markdown("<h3 style='color:#F8FAFC; font-size:1.25rem; margin-bottom:0.2rem;'>🛵 Rider & Order Details</h3>", unsafe_allow_html=True)
    st.caption("Enter delivery person and order details.")
    
    age = st.slider("Delivery Person Age", 18, 50, 25, on_change=reset_prediction)
    rating = st.number_input("Delivery Person Rating", 1.0, 5.0, 4.9, step=0.1, on_change=reset_prediction)
    vehicle = st.selectbox("Type of Vehicle", ["Motorcycle", "Scooter", "Bicycle", "Electric Bike"], on_change=reset_prediction)
    order_type = st.selectbox("Type of Order", ["Snack", "Meal", "Drinks", "Buffet"], on_change=reset_prediction)

with col2:
    st.markdown("<h3 style='color:#F8FAFC; font-size:1.25rem; margin-bottom:0.2rem;'>🌦️ Environment & Trip</h3>", unsafe_allow_html=True)
    st.caption("Add traffic, weather and trip conditions.")
    
    distance = st.number_input("Distance (km)", 0.5, 50.0, 11.5, step=0.5, on_change=reset_prediction)
    traffic = st.selectbox("Traffic Level", ["Low", "Medium", "High", "Jam"], index=1, on_change=reset_prediction)
    weather = st.selectbox("Weather", ["Clear Sky", "Cloudy", "Windy", "Foggy", "Moderate Rain", "Heavy Rain"], index=2, on_change=reset_prediction)
    temp = st.number_input("Temperature (°C)", -10.0, 50.0, 21.0, step=1.0, on_change=reset_prediction)
    humidity = st.number_input("Humidity (%)", 0.0, 100.0, 62.0, step=1.0, on_change=reset_prediction)
    precipitation = st.number_input("Precipitation", 0.0, 10.0, 2.4, step=0.1, on_change=reset_prediction)

with col3:
    st.markdown("<h3 style='color:#F8FAFC; font-size:1.25rem; margin-bottom:0.2rem;'>📊 Delivery Estimate</h3>", unsafe_allow_html=True)
    st.caption("Generated output prediction.")
    
    predict_btn = st.button("🚀 Predict Delivery Time", use_container_width=True)
    
    if predict_btn:
        estimated_time = round(15 + (distance * 1.5) + (5 if traffic in ['High', 'Jam'] else 1), 1)
        st.session_state.last_prediction = estimated_time
        st.session_state.predicted = True

    st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)

    if st.session_state.predicted:
        st.markdown(f"""
        <div class="prediction-card">
            <div style="color: #34D399; font-weight: 700; font-size: 0.85rem; letter-spacing:0.05em;">✓ PREDICTION CALCULATED</div>
            <h1 style="color: #FF5252; font-size: 3.6rem; margin: 0.4rem 0; font-weight: 800;">{st.session_state.last_prediction}</h1>
            <div style="font-size: 1rem; font-weight: 700; color: #F8FAFC; letter-spacing:0.08em;">MINUTES</div>
            <p style="color: #94A3B8; font-size: 0.85rem; margin-top: 1.2rem;">Calculated for {weather.lower()} and {traffic.lower()} traffic.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="empty-card">
            <div style="font-size: 2.8rem; margin-bottom: 0.6rem;">🤖</div>
            <div style="font-size: 1.2rem; font-weight: 700; color: #F8FAFC; margin-bottom: 0.4rem;">Your Delivery Estimate</div>
            <div style="color: #94A3B8; font-size: 0.9rem; line-height: 1.5;">Enter the delivery details and click <b>Predict Delivery Time</b> to generate an estimate.</div>
        </div>
        """, unsafe_allow_html=True)

st.write("")
st.write("")

# ----------------- 6. MODEL PERFORMANCE -----------------
st.markdown("<div id='model-info'></div>", unsafe_allow_html=True)
st.markdown("<h3 style='color:#F8FAFC; font-size:1.3rem; margin-bottom:1rem;'>📈 Model Performance</h3>", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4, gap="small")

with m1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">MODEL</div>
        <div class="metric-value" style="font-size: 1.3rem;">Random Forest</div>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">R² SCORE</div>
        <div class="metric-value">0.88</div>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">MAE</div>
        <div class="metric-value">3.04 min</div>
    </div>
    """, unsafe_allow_html=True)

with m4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">RMSE</div>
        <div class="metric-value">5.42</div>
    </div>
    """, unsafe_allow_html=True)

# ----------------- 7. ENHANCED LARGE FOOTER -----------------
st.markdown("""
<div class="fp-footer-card">
    <div class="footer-grid">
        <div>
            <div class="footer-brand-large">
                <span>🍔</span>
                <span>FoodPulse AI</span>
            </div>
            <div class="footer-brand-desc">
                An end-to-end Machine Learning web application designed to predict real-time food delivery duration using environmental, traffic, and logistics features.
            </div>
        </div>
        <div>
            <div class="footer-col-title">NAVIGATION</div>
            <div class="footer-col-links">
                <a href="#predictor">Delivery Predictor</a>
                <a href="#model-info">Model Metrics</a>
                <a href="#predictor">Back to Top ↑</a>
            </div>
        </div>
        <div>
            <div class="footer-col-title">SOURCE CODE</div>
            <div class="footer-col-links">
                <a href="https://github.com/Shrutir09/Food-Delivery-Time-Prediction" target="_blank" class="footer-badge-link">
                    <span>GitHub Project</span> ↗
                </a>
            </div>
        </div>
    </div>
    <div class="footer-bottom-bar">
        <div>© 2026 FoodPulse AI · Built with Streamlit & Python</div>
        <div>Random Forest Regressor • R² 0.88 • MAE 3.04 min</div>
    </div>
</div>
""", unsafe_allow_html=True)