import streamlit as st
import pandas as pd
import joblib


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Food Delivery AI",
    page_icon="🍔",
    layout="wide"
)


# =========================================================
# LOAD MODEL
# =========================================================

@st.cache_resource
def load_model():
    return joblib.load("models/delivery_model.pkl")


model = load_model()


# =========================================================
# SESSION STATE
# =========================================================

if "prediction" not in st.session_state:
    st.session_state.prediction = None


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    /* ---------- MAIN BACKGROUND ---------- */

    .stApp {
        background:
            radial-gradient(
                circle at 10% 0%,
                rgba(255, 100, 70, 0.08),
                transparent 30%
            ),
            radial-gradient(
                circle at 90% 0%,
                rgba(70, 130, 255, 0.08),
                transparent 30%
            ),
            #0c121c;
    }

    .block-container {
        max-width: 1180px;
        padding-top: 1.2rem;
        padding-bottom: 2rem;
    }


    /* ---------- NAVBAR ---------- */

    .nav-box {
        background: rgba(30, 35, 47, 0.95);
        border: 1px solid rgba(255,255,255,0.10);
        border-radius: 15px;
        padding: 13px 20px;
        margin-bottom: 35px;
    }

    .brand {
        font-size: 1.25rem;
        font-weight: 800;
        color: #f7f0df;
    }

    .nav-item {
        color: #aeb6c3;
        font-size: 0.86rem;
        text-align: center;
        padding-top: 5px;
    }


    /* ---------- HERO ---------- */

    .hero {
        text-align: center;
        padding: 8px 0 25px 0;
    }

    .hero-icon {
        font-size: 3rem;
    }

    .hero-subtitle {
        color: #9ba5b5;
        font-size: 0.95rem;
    }


    /* ---------- CARDS ---------- */

    div[data-testid="stVerticalBlockBorderWrapper"] {
        background:
            linear-gradient(
                145deg,
                rgba(34,39,51,0.96),
                rgba(24,29,40,0.96)
            );

        border: 1px solid rgba(255,255,255,0.10);
        border-radius: 18px;

        box-shadow:
            0 12px 35px rgba(0,0,0,0.22);
    }


    /* ---------- SECTION HEADINGS ---------- */

    .section-heading {
        font-size: 1.15rem;
        font-weight: 750;
        color: #f1f3f6;
    }

    .section-text {
        color: #8d97a7;
        font-size: 0.80rem;
        margin-bottom: 18px;
    }


    /* ---------- BUTTON ---------- */

    div.stButton > button {
        width: 100%;
        min-height: 54px;

        border-radius: 12px;
        border: none;

        background:
            linear-gradient(
                135deg,
                #ff7154,
                #ff8968
            );

        color: white;
        font-size: 1rem;
        font-weight: 750;

        box-shadow:
            0 8px 25px rgba(255,105,76,0.25);

        transition: all 0.2s ease;
    }

    div.stButton > button:hover {
        transform: translateY(-2px);
        color: white;
        box-shadow:
            0 12px 30px rgba(255,105,76,0.38);
    }


    /* ---------- RESULT PANEL ---------- */

    .result-title {
        text-align: center;
        color: #8ce3a8;
        font-size: 0.95rem;
        font-weight: 700;
    }

    .result-number {
        text-align: center;
        color: #ffd66f;
        font-size: 3.4rem;
        font-weight: 850;
        margin: 10px 0;
    }

    .result-unit {
        text-align: center;
        color: #a9b2bf;
        font-size: 0.9rem;
    }


    /* ---------- ABOUT ---------- */

    .about-title {
        text-align: center;
        font-size: 1.1rem;
        font-weight: 750;
        color: #edf0f4;
    }

    .about-text {
        text-align: center;
        color: #919baa;
        font-size: 0.84rem;
        line-height: 1.7;
        max-width: 760px;
        margin: auto;
    }


    /* ---------- FOOTER ---------- */

    .footer-line {
        margin-top: 40px;
        border-top: 1px solid rgba(255,255,255,0.10);
        padding-top: 18px;
    }

    .footer-text {
        color: #7f8998;
        font-size: 0.76rem;
    }

    .footer-link {
        color: #9da7b5;
        text-decoration: none;
    }


    /* ---------- MOBILE ---------- */

    @media (max-width: 700px) {

        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }

        .brand {
            font-size: 1rem;
        }

        .nav-item {
            font-size: 0.70rem;
        }

        .hero-icon {
            font-size: 2.5rem;
        }

        .result-number {
            font-size: 2.6rem;
        }
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# NAVBAR
# =========================================================

st.markdown('<div class="nav-box">', unsafe_allow_html=True)

nav1, nav2, nav3, nav4 = st.columns([3, 1, 1, 1])

with nav1:
    st.markdown(
        '<div class="brand">🍔 Food Delivery AI</div>',
        unsafe_allow_html=True
    )

with nav2:
    st.markdown(
        '<div class="nav-item">Predictor</div>',
        unsafe_allow_html=True
    )

with nav3:
    st.markdown(
        '<div class="nav-item">Model Info</div>',
        unsafe_allow_html=True
    )

with nav4:
    st.markdown(
        '<div class="nav-item">About</div>',
        unsafe_allow_html=True
    )

st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# HERO
# =========================================================

st.markdown(
    """
    <div class="hero">
        <div class="hero-icon">🍔</div>
    </div>
    """,
    unsafe_allow_html=True
)

st.title("Food Delivery Time Prediction")

st.markdown(
    """
    <div class="hero-subtitle">
        Configure delivery parameters to get an estimated delivery time.
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")


# =========================================================
# MAIN AREA
# =========================================================

input_col, result_col = st.columns(
    [1.15, 0.85],
    gap="large"
)


# =========================================================
# INPUT AREA
# =========================================================

with input_col:

    left_col, right_col = st.columns(2, gap="medium")


    # -----------------------------------------------------
    # RIDER & ORDER
    # -----------------------------------------------------

    with left_col:

        with st.container(border=True):

            st.markdown(
                '<div class="section-heading">🛵 Rider & Order Details</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                '<div class="section-text">'
                'Enter delivery person and order information.'
                '</div>',
                unsafe_allow_html=True
            )

            age = st.slider(
                "Delivery Person Age",
                min_value=15,
                max_value=50,
                value=30
            )

            rating = st.number_input(
                "Delivery Person Rating",
                min_value=1.0,
                max_value=6.0,
                value=4.5,
                step=0.1
            )

            vehicle = st.selectbox(
                "Type of Vehicle",
                [
                    "motorcycle",
                    "scooter",
                    "electric_scooter",
                    "bicycle"
                ],
                format_func=lambda x: {
                    "motorcycle": "🏍️ Motorcycle",
                    "scooter": "🛵 Scooter",
                    "electric_scooter": "⚡ Electric Scooter",
                    "bicycle": "🚲 Bicycle"
                }[x]
            )

            order_type = st.selectbox(
                "Type of Order",
                [
                    "Snack",
                    "Meal",
                    "Drinks",
                    "Buffet"
                ],
                format_func=lambda x: {
                    "Snack": "🍟 Snack",
                    "Meal": "🍱 Meal",
                    "Drinks": "🥤 Drinks",
                    "Buffet": "🍽️ Buffet"
                }[x]
            )


    # -----------------------------------------------------
    # ENVIRONMENT
    # -----------------------------------------------------

    with right_col:

        with st.container(border=True):

            st.markdown(
                '<div class="section-heading">'
                '🌦️ Environment & Trip Parameters'
                '</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                '<div class="section-text">'
                'Add traffic, weather and trip conditions.'
                '</div>',
                unsafe_allow_html=True
            )

            distance = st.number_input(
                "Distance (km)",
                min_value=0.0,
                max_value=100.0,
                value=10.0,
                step=0.1
            )

            traffic = st.selectbox(
                "Traffic Level",
                [
                    "Low",
                    "Moderate",
                    "High",
                    "Very High",
                    "Very Low"
                ]
            )

            weather = st.selectbox(
                "Weather",
                [
                    "clear sky",
                    "haze",
                    "mist",
                    "broken clouds",
                    "light rain",
                    "smoke",
                    "scattered clouds",
                    "overcast clouds",
                    "fog",
                    "few clouds",
                    "moderate rain"
                ],
                format_func=lambda x: {
                    "clear sky": "☀️ Clear Sky",
                    "haze": "🌫️ Haze",
                    "mist": "🌫️ Mist",
                    "broken clouds": "⛅ Broken Clouds",
                    "light rain": "🌦️ Light Rain",
                    "smoke": "💨 Smoke",
                    "scattered clouds": "🌤️ Scattered Clouds",
                    "overcast clouds": "☁️ Overcast Clouds",
                    "fog": "🌫️ Fog",
                    "few clouds": "🌤️ Few Clouds",
                    "moderate rain": "🌧️ Moderate Rain"
                }[x]
            )

            temperature = st.number_input(
                "Temperature (°C)",
                min_value=0.0,
                max_value=50.0,
                value=23.0,
                step=0.1
            )

            humidity = st.number_input(
                "Humidity (%)",
                min_value=0.0,
                max_value=100.0,
                value=66.0,
                step=0.1
            )

            precipitation = st.number_input(
                "Precipitation",
                min_value=0.0,
                value=0.0,
                step=0.01
            )


    # -----------------------------------------------------
    # PREDICT BUTTON
    # -----------------------------------------------------

    st.write("")

    if st.button("🚀 Predict Delivery Time"):

        input_data = pd.DataFrame({
            "Delivery_person_Age": [age],
            "Delivery_person_Ratings": [rating],
            "temperature": [temperature],
            "humidity": [humidity],
            "precipitation": [precipitation],
            "Distance (km)": [distance],
            "Traffic_Level": [traffic],
            "weather_description": [weather],
            "Type_of_order": [order_type],
            "Type_of_vehicle": [vehicle]
        })

        prediction = model.predict(input_data)[0]

        st.session_state.prediction = prediction


# =========================================================
# RESULT AREA
# =========================================================

with result_col:

    with st.container(border=True):

        if st.session_state.prediction is None:

            st.subheader("📊 Your Delivery Estimate")

            st.info(
                "Enter the delivery details and click "
                "**Predict Delivery Time** to see the estimated time."
            )

            st.write("")

            st.metric(
                label="Estimated Time",
                value="-- min"
            )

            st.caption(
                "Your prediction will appear here."
            )

        else:

            prediction = st.session_state.prediction

            st.markdown(
                '<div class="result-title">'
                '✓ PREDICTION CALCULATED'
                '</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div class="result-number">'
                f'{prediction:.1f}'
                f'</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                '<div class="result-unit">'
                'MINUTES'
                '</div>',
                unsafe_allow_html=True
            )

            st.divider()

            if prediction <= 20:
                status = "🟢 Fast Delivery"
                message = "The estimated delivery time is relatively short."

            elif prediction <= 40:
                status = "🟡 Average Delivery"
                message = "The estimated delivery time is within the average range."

            else:
                status = "🔴 Longer Delivery"
                message = "The estimated delivery time is relatively longer."

            st.subheader(status)

            st.caption(message)

            st.write("")

            st.metric(
                "Estimated Delivery Time",
                f"{prediction:.1f} min"
            )


# =========================================================
# MODEL PERFORMANCE
# =========================================================

st.write("")
st.write("")

st.subheader("Model Performance")

metric1, metric2, metric3, metric4 = st.columns(4)

with metric1:
    st.metric(
        "Model",
        "Random Forest"
    )

with metric2:
    st.metric(
        "R² Score",
        "0.88"
    )

with metric3:
    st.metric(
        "MAE",
        "3.04 min"
    )

with metric4:
    st.metric(
        "RMSE",
        "5.42"
    )


# =========================================================
# ABOUT
# =========================================================

st.write("")
st.write("")

with st.container(border=True):

    st.markdown(
        '<div class="about-title">About This Project</div>',
        unsafe_allow_html=True
    )

    st.write("")

    st.markdown(
        """
        <div class="about-text">
        This application uses a Random Forest Regression model to estimate
        food delivery time using delivery person details, distance,
        traffic, weather and other environmental conditions.
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    '<div class="footer-line"></div>',
    unsafe_allow_html=True
)

footer_left, footer_right = st.columns(2)

with footer_left:
    st.markdown(
        """
        <div class="footer-text">
        © 2026 <strong>Food Delivery AI</strong>
        · Machine Learning Project
        </div>
        """,
        unsafe_allow_html=True
    )

with footer_right:
    st.markdown(
        """
        <div class="footer-text" style="text-align:right;">
        Random Forest · R² 0.88 ·
        <a
            class="footer-link"
            href="https://github.com/Shrutir09/Food-Delivery-Time-Prediction"
            target="_blank"
        >
        GitHub
        </a>
        </div>
        """,
        unsafe_allow_html=True
    )