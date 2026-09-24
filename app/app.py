import streamlit as st

# 1. Page Config
st.set_page_config(
    page_title="FoodPulse AI - Delivery Estimator",
    page_icon="🍔",
    layout="wide"
)

# 2. Custom Responsive CSS Injection
st.markdown("""
<style>
    /* Hide Default Streamlit Elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
        max-width: 1300px;
    }

    /* Responsive Navbar Styling */
    .fp-navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: #1E293B;
        padding: 1rem 2rem;
        border-radius: 12px;
        border: 1px solid #334155;
        margin-bottom: 2rem;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
    }
    .fp-brand {
        display: flex;
        align-items: center;
        gap: 12px;
        font-size: 1.4rem;
        font-weight: 700;
        color: #F8FAFC;
    }
    .fp-logo {
        font-size: 1.8rem;
    }
    .fp-nav-links {
        display: flex;
        gap: 1.8rem;
    }
    .fp-nav-links a {
        color: #94A3B8;
        text-decoration: none;
        font-size: 1rem;
        font-weight: 500;
        transition: color 0.2s ease;
    }
    .fp-nav-links a:hover, .fp-nav-links a.active {
        color: #FF5252;
    }
    .fp-status {
        display: flex;
        align-items: center;
        gap: 8px;
        background-color: #064E3B;
        color: #34D399;
        font-size: 0.85rem;
        padding: 6px 14px;
        border-radius: 20px;
        font-weight: 600;
    }
    .status-dot {
        width: 8px;
        height: 8px;
        background-color: #34D399;
        border-radius: 50%;
        display: inline-block;
    }

    /* Hero Banner Styling */
    .hero-container {
        text-align: center;
        margin-bottom: 2.5rem;
    }
    .hero-icon {
        font-size: 3.5rem;
        margin-bottom: 0.5rem;
    }
    .hero-container h1 {
        font-size: 2.5rem;
        font-weight: 800;
        color: #F8FAFC;
        margin-bottom: 0.5rem;
    }
    .hero-container p {
        font-size: 1.1rem;
        color: #94A3B8;
        max-width: 650px;
        margin: 0 auto;
    }

    /* Output Card / Empty Prediction Styling */
    .prediction-card {
        background: #1E293B;
        border: 1px solid #334155;
        border-radius: 16px;
        padding: 2.5rem 1.8rem;
        text-align: center;
        min-height: 380px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
    }
    .empty-icon {
        font-size: 3.5rem;
        margin-bottom: 1rem;
    }
    .empty-title {
        font-size: 1.4rem;
        font-weight: 700;
        color: #F8FAFC;
        margin-bottom: 0.8rem;
    }
    .empty-text {
        color: #94A3B8;
        font-size: 1rem;
        line-height: 1.5;
    }

    /* About Section Styling */
    .about-card {
        background: #1E293B;
        border: 1px solid #334155;
        border-radius: 16px;
        padding: 2rem;
        margin-top: 2rem;
        margin-bottom: 3rem;
    }
    .about-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: #F8FAFC;
        margin-bottom: 0.8rem;
    }
    .about-text {
        color: #94A3B8;
        font-size: 1rem;
        line-height: 1.6;
    }

    /* Separated Responsive Footer Styling */
    .footer-wrapper {
        margin-top: 4rem;
        border-top: 1px solid #334155;
        padding-top: 2rem;
        background-color: #0F172A;
    }
    .footer-main {
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 1.5rem;
        margin-bottom: 1.5rem;
    }
    .footer-brand {
        font-size: 1.3rem;
        font-weight: 700;
        color: #FF5252;
    }
    .footer-sub {
        font-size: 0.9rem;
        color: #64748B;
        margin-top: 4px;
    }
    .footer-links {
        display: flex;
        gap: 1.5rem;
    }
    .footer-links a {
        color: #94A3B8;
        text-decoration: none;
        font-size: 0.95rem;
        transition: color 0.2s ease;
    }
    .footer-links a:hover {
        color: #FF5252;
    }
    .footer-bottom {
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 1rem;
        padding-top: 1rem;
        border-top: 1px solid #1E293B;
        color: #64748B;
        font-size: 0.88rem;
    }
    .footer-stats span {
        margin: 0 4px;
    }

    /* Responsive Adjustments for Mobile and Tablets */
    @media (max-width: 768px) {
        .fp-navbar, .footer-main, .footer-bottom {
            flex-direction: column;
            text-align: center;
            gap: 1rem;
        }
        .fp-nav-links, .footer-links {
            flex-wrap: wrap;
            justify-content: center;
        }
    }
</style>
""", unsafe_allow_html=True)

# ----------------- 3. NAVBAR SECTION -----------------
st.markdown("""
<div class="fp-navbar">
    <div class="fp-brand">
        <div class="fp-logo">🍔</div>
        <span>FoodPulse AI</span>
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
    <div class="hero-icon">🍔</div>
    <h1>Food Delivery Time Prediction</h1>
    <p>Configure delivery parameters and let our machine learning model estimate the expected delivery time in real time.</p>
</div>
""", unsafe_allow_html=True)

# Initialize Session State for Dynamic Prediction Reset
if 'predicted' not in st.session_state:
    st.session_state.predicted = False
if 'last_prediction' not in st.session_state:
    st.session_state.last_prediction = None

def reset_prediction():
    st.session_state.predicted = False

# ----------------- 5. MAIN INPUT & PREDICTION GRID -----------------
col1, col2, col3 = st.columns([1.1, 1.1, 1], gap="large")

with col1:
    st.subheader("🛵 Rider & Order Details")
    st.caption("Enter delivery person and order information.")
    
    age = st.slider("Delivery Person Age", 18, 50, 30, on_change=reset_prediction)
    rating = st.number_input("Delivery Person Rating", 1.0, 5.0, 4.5, step=0.1, on_change=reset_prediction)
    vehicle = st.selectbox("Type of Vehicle", ["Motorcycle", "Scooter", "Bicycle", "Electric Bike"], on_change=reset_prediction)
    order_type = st.selectbox("Type of Order", ["Snack", "Meal", "Drinks", "Buffet"], on_change=reset_prediction)

with col2:
    st.subheader("🌦️ Environment & Trip Parameters")
    st.caption("Add traffic, weather and trip conditions.")
    
    distance = st.number_input("Distance (km)", 0.5, 50.0, 10.0, step=0.5, on_change=reset_prediction)
    traffic = st.selectbox("Traffic Level", ["Low", "Medium", "High", "Jam"], on_change=reset_prediction)
    weather = st.selectbox("Weather", ["Clear Sky", "Cloudy", "Windy", "Foggy", "Moderate Rain", "Heavy Rain"], on_change=reset_prediction)
    temp = st.number_input("Temperature (°C)", -10.0, 50.0, 23.0, step=1.0, on_change=reset_prediction)
    humidity = st.number_input("Humidity (%)", 0.0, 100.0, 66.0, step=1.0, on_change=reset_prediction)
    precipitation = st.number_input("Precipitation", 0.0, 10.0, 0.0, step=0.1, on_change=reset_prediction)

with col3:
    st.subheader("📊 Delivery Estimate")
    st.write("") # Layout spacer
    
    # Calculate Button
    predict_btn = st.button("🚀 Predict Delivery Time", use_container_width=True, type="primary")
    
    if predict_btn:
        # NOTE: Place your actual Machine Learning model .predict() code here
        # Example calculation placeholder using model logic:
        estimated_time = round(15 + (distance * 1.5) + (5 if traffic in ['High', 'Jam'] else 1), 1)
        st.session_state.last_prediction = estimated_time
        st.session_state.predicted = True

    # Prediction Card State Logic
    if st.session_state.predicted:
        st.markdown(f"""
        <div class="prediction-card" style="border-color: #34D399;">
            <div style="color: #34D399; font-weight: bold; font-size: 0.9rem; margin-bottom: 0.5rem;">✓ PREDICTION CALCULATED</div>
            <h1 style="color: #FF5252; font-size: 3.5rem; margin: 0.5rem 0;">{st.session_state.last_prediction}</h1>
            <div style="font-size: 1.2rem; font-weight: 600; color: #F8FAFC;">MINUTES</div>
            <p style="color: #94A3B8; font-size: 0.9rem; margin-top: 1.5rem;">Estimated for {weather.lower()} conditions and {traffic.lower()} traffic level.</p>
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

st.divider()

# ----------------- 6. MODEL PERFORMANCE SECTION -----------------
st.markdown("<div id='model-info'></div>", unsafe_allow_html=True)
st.subheader("📈 Model Performance")

m1, m2, m3, m4 = st.columns(4)
m1.metric("MODEL", "Random Forest")
m2.metric("R² SCORE", "0.88")
m3.metric("MAE", "3.04 min")
m4.metric("RMSE", "5.42")

# ----------------- 7. ABOUT SECTION -----------------
st.markdown("""
<div class="about-card" id="about">
    <div class="about-title">About This Project</div>
    <div class="about-text">
        FoodPulse AI uses a Random Forest Regression model to estimate food delivery time using delivery person details,
        distance, traffic, weather and environmental conditions. The application combines a trained machine learning model
        with an interactive Streamlit interface for real-time predictions.
    </div>
</div>
""", unsafe_allow_html=True)

# ----------------- 8. FOOTER SECTION -----------------
st.markdown("""
<div class="footer-wrapper">
    <div class="footer-main">
        <div>
            <div class="footer-brand">🍔 FoodPulse AI</div>
            <div class="footer-sub">Machine Learning · Food Delivery Prediction</div>
        </div>
        <div class="footer-links">
            <a href="#predictor">Predictor</a>
            <a href="#model-info">Model Info</a>
            <a href="#about">About</a>
            <a href="https://github.com/Shrutir09/Food-Delivery-Time-Prediction" target="_blank">GitHub ↗</a>
        </div>
    </div>
    <div class="footer-bottom">
        <div>© 2026 FoodPulse AI · Built with Streamlit</div>
        <div class="footer-stats">
            <span>Random Forest</span>
            <span>•</span>
            <span>R² 0.88</span>
            <span>•</span>
            <span>MAE 3.04 min</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)