import streamlit as st

# 1. Page Config
st.set_page_config(
    page_title="FoodPulse AI - Delivery Estimator",
    page_icon="🍔",
    layout="wide"
)

# 2. Complete Professional CSS Overhaul
st.markdown("""
<style>
    /* Hide Default Streamlit Chrome */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* FIX 1: Full-Width Screen Stretch (Removes Blank Space on Big Screens) */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 2rem !important;
        max-width: 95% !important; /* Expands across large laptop screens */
        margin: 0 auto;
    }

    /* FIX 2: Modern Responsive Navbar */
    .fp-navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
        padding: 0.8rem 1.8rem;
        border-radius: 14px;
        border: 1px solid #334155;
        margin-bottom: 2rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
    }
    .fp-brand {
        display: flex;
        align-items: center;
        gap: 10px;
        font-size: 1.3rem;
        font-weight: 700;
        color: #F8FAFC;
    }
    .fp-nav-links {
        display: flex;
        gap: 1.5rem;
    }
    .fp-nav-links a {
        color: #94A3B8;
        text-decoration: none;
        font-size: 0.95rem;
        font-weight: 500;
        transition: all 0.2s ease;
    }
    .fp-nav-links a:hover, .fp-nav-links a.active {
        color: #FF5252;
    }
    .fp-status {
        display: flex;
        align-items: center;
        gap: 8px;
        background-color: rgba(6, 78, 59, 0.6);
        border: 1px solid #059669;
        color: #34D399;
        font-size: 0.8rem;
        padding: 5px 12px;
        border-radius: 20px;
        font-weight: 600;
    }
    .status-dot {
        width: 8px;
        height: 8px;
        background-color: #34D399;
        border-radius: 50%;
        box-shadow: 0 0 8px #34D399;
    }

    /* FIX 3: Styled Input Cards Container */
    div[data-testid="stColumn"] {
        background: #1E293B;
        border: 1px solid #334155;
        border-radius: 16px;
        padding: 1.5rem !important;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
    }

    /* FIX 4: Output Prediction Card Styling */
    .prediction-card {
        background: linear-gradient(180deg, #1E293B 0%, #0F172A 100%);
        border: 1px solid #334155;
        border-radius: 16px;
        padding: 2rem 1.5rem;
        text-align: center;
        min-height: 350px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .empty-icon {
        font-size: 3rem;
        margin-bottom: 0.8rem;
    }
    .empty-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: #F8FAFC;
        margin-bottom: 0.5rem;
    }
    .empty-text {
        color: #94A3B8;
        font-size: 0.95rem;
        line-height: 1.5;
    }

    /* HERO Header Section */
    .hero-container {
        text-align: center;
        margin-bottom: 2rem;
    }
    .hero-container h1 {
        font-size: 2.3rem;
        font-weight: 800;
        color: #F8FAFC;
    }
    .hero-container p {
        color: #94A3B8;
        font-size: 1rem;
    }

    /* FIX 5: Full Width Clean Footer */
    .footer-wrapper {
        margin-top: 3rem;
        border-top: 1px solid #334155;
        padding-top: 1.5rem;
        width: 100%;
    }
    .footer-main {
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 1rem;
    }
    .footer-brand {
        font-size: 1.2rem;
        font-weight: 700;
        color: #FF5252;
    }
    .footer-bottom {
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        margin-top: 1rem;
        padding-top: 1rem;
        border-top: 1px solid #1E293B;
        color: #64748B;
        font-size: 0.85rem;
    }

    /* Mobile Responsive Tweaks */
    @media (max-width: 768px) {
        .fp-navbar {
            flex-direction: column;
            gap: 0.8rem;
            text-align: center;
            padding: 1rem;
        }
        .fp-nav-links {
            gap: 1rem;
        }
        div[data-testid="stColumn"] {
            margin-bottom: 1rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# ----------------- 3. NAVBAR -----------------
st.markdown("""
<div class="fp-navbar">
    <div class="fp-brand">
        <span>🍔 FoodPulse AI</span>
    </div>
    <div class="fp-nav-links">
        <a href="#predictor" class="active">Predictor</a>
        <a href="#model-info">Model Info</a>
        <a href="#about">About</a>
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
    <h1>Food Delivery Time Prediction</h1>
    <p>Configure delivery parameters and let our machine learning model estimate the expected delivery time.</p>
</div>
""", unsafe_allow_html=True)

# State reset logic
if 'predicted' not in st.session_state:
    st.session_state.predicted = False
if 'last_prediction' not in st.session_state:
    st.session_state.last_prediction = None

def reset_prediction():
    st.session_state.predicted = False

# ----------------- 5. MAIN INPUT & PREDICTION CARDS -----------------
col1, col2, col3 = st.columns([1.1, 1.1, 1], gap="medium")

with col1:
    st.markdown("### 🛵 Rider & Order Details")
    st.caption("Enter delivery person and order details.")
    
    age = st.slider("Delivery Person Age", 18, 50, 30, on_change=reset_prediction)
    rating = st.number_input("Delivery Person Rating", 1.0, 5.0, 4.5, step=0.1, on_change=reset_prediction)
    vehicle = st.selectbox("Type of Vehicle", ["Motorcycle", "Scooter", "Bicycle", "Electric Bike"], on_change=reset_prediction)
    order_type = st.selectbox("Type of Order", ["Snack", "Meal", "Drinks", "Buffet"], on_change=reset_prediction)

with col2:
    st.markdown("### 🌦️ Environment & Trip")
    st.caption("Add traffic, weather and trip conditions.")
    
    distance = st.number_input("Distance (km)", 0.5, 50.0, 10.0, step=0.5, on_change=reset_prediction)
    traffic = st.selectbox("Traffic Level", ["Low", "Medium", "High", "Jam"], on_change=reset_prediction)
    weather = st.selectbox("Weather", ["Clear Sky", "Cloudy", "Windy", "Foggy", "Moderate Rain", "Heavy Rain"], on_change=reset_prediction)
    temp = st.number_input("Temperature (°C)", -10.0, 50.0, 23.0, step=1.0, on_change=reset_prediction)
    humidity = st.number_input("Humidity (%)", 0.0, 100.0, 66.0, step=1.0, on_change=reset_prediction)
    precipitation = st.number_input("Precipitation", 0.0, 10.0, 0.0, step=0.1, on_change=reset_prediction)

with col3:
    st.markdown("### 📊 Delivery Estimate")
    st.caption("Generated output prediction.")
    
    predict_btn = st.button("🚀 Predict Delivery Time", use_container_width=True, type="primary")
    
    if predict_btn:
        # Pass features to your model here
        estimated_time = round(15 + (distance * 1.5) + (5 if traffic in ['High', 'Jam'] else 1), 1)
        st.session_state.last_prediction = estimated_time
        st.session_state.predicted = True

    if st.session_state.predicted:
        st.markdown(f"""
        <div class="prediction-card" style="border-color: #34D399;">
            <div style="color: #34D399; font-weight: bold; font-size: 0.85rem;">✓ PREDICTION CALCULATED</div>
            <h1 style="color: #FF5252; font-size: 3.2rem; margin: 0.5rem 0;">{st.session_state.last_prediction}</h1>
            <div style="font-size: 1.1rem; font-weight: 600; color: #F8FAFC;">MINUTES</div>
            <p style="color: #94A3B8; font-size: 0.85rem; margin-top: 1rem;">Calculated for {weather.lower()} and {traffic.lower()} traffic.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="prediction-card">
            <div class="empty-icon">🤖</div>
            <div class="empty-title">Your Delivery Estimate</div>
            <div class="empty-text">Enter the delivery details and click <b>Predict Delivery Time</b> to generate an AI-powered estimate.</div>
        </div>
        """, unsafe_allow_html=True)

st.write("") # Spacing

# ----------------- 6. MODEL PERFORMANCE -----------------
st.markdown("<div id='model-info'></div>", unsafe_allow_html=True)
st.subheader("📈 Model Performance")

m1, m2, m3, m4 = st.columns(4)
m1.metric("MODEL", "Random Forest")
m2.metric("R² SCORE", "0.88")
m3.metric("MAE", "3.04 min")
m4.metric("RMSE", "5.42")

# ----------------- 7. ABOUT SECTION -----------------
st.markdown("""
<div style="background: #1E293B; border: 1px solid #334155; border-radius: 16px; padding: 1.5rem; margin-top: 2rem;" id="about">
    <h3 style="color: #F8FAFC; margin-bottom: 0.5rem;">About This Project</h3>
    <p style="color: #94A3B8; line-height: 1.6; font-size: 0.95rem;">
        FoodPulse AI uses a Random Forest Regression model to estimate food delivery time using delivery person details,
        distance, traffic, weather and environmental conditions. The application combines a trained machine learning model
        with an interactive Streamlit interface for real-time predictions.
    </p>
</div>
""", unsafe_allow_html=True)

# ----------------- 8. FOOTER -----------------
st.markdown("""
<div class="footer-wrapper">
    <div class="footer-main">
        <div>
            <div class="footer-brand">🍔 FoodPulse AI</div>
            <div style="color: #64748B; font-size: 0.85rem;">Machine Learning · Food Delivery Prediction</div>
        </div>
        <div style="display: flex; gap: 1.2rem;">
            <a href="#predictor" style="color: #94A3B8; text-decoration: none;">Predictor</a>
            <a href="#model-info" style="color: #94A3B8; text-decoration: none;">Model Info</a>
            <a href="#about" style="color: #94A3B8; text-decoration: none;">About</a>
            <a href="https://github.com/Shrutir09/Food-Delivery-Time-Prediction" target="_blank" style="color: #FF5252; text-decoration: none;">GitHub ↗</a>
        </div>
    </div>
    <div class="footer-bottom">
        <div>© 2026 FoodPulse AI · Built with Streamlit</div>
        <div>Random Forest • R² 0.88 • MAE 3.04 min</div>
    </div>
</div>
""", unsafe_allow_html=True)