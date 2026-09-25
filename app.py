import streamlit as st
import requests
from PIL import Image

# ==========================================
# Page Configuration & Styling
# ==========================================

st.set_page_config(
    page_title="CIFAR-10 Deep Learning App",
    page_icon="🧠",
    layout="wide"
)

# Custom Styling
st.markdown(
    """
    <style>
    [data-testid="stMetricValue"] { font-size: 28px; font-weight: 700; color: #4CAF50; }
    .class-badge { background-color: #1E222D; border: 1px solid #313745; border-radius: 8px; padding: 10px; text-align: center; font-weight: 600; color: #E0E0E0; }
    [data-testid="stHeader"], #MainMenu, footer, header { display: none !important; }
    </style>
    """,
    unsafe_allow_html=True
)

# ==========================================
# API Configuration (Render Live Link)
# ==========================================

FLASK_API_URL = "https://cifar10-flask-api-pwux.onrender.com"

class_names = [
    "Airplane ✈️", "Automobile 🚗", "Bird 🐦", "Cat 🐱", "Deer 🦌",
    "Dog 🐶", "Frog 🐸", "Horse 🐴", "Ship 🚢", "Truck 🚚"
]

# Sidebar
st.sidebar.title("🧠 CIFAR-10 AI Platform")
st.sidebar.info("Connected to Flask REST API Backend")
st.sidebar.markdown("---")

st.title("🧠 CIFAR-10 Image Classification Suite")
st.caption("Interactive Frontend connected with Flask API")

# Check API Health
try:
    health_resp = requests.get(f"{FLASK_API_URL}/", timeout=10)
    if health_resp.status_code == 200:
        st.success("✅ **Flask Backend API Status:** Connected & Live")
    else:
        st.warning(f"⚠️ **Flask API Status:** Server responding with status code {health_resp.status_code}")
except Exception as e:
    st.error(f"❌ **Flask API Status:** Could not connect to API server ({str(e)})")

st.markdown("---")

# Prediction Section
st.subheader("📤 Real-time Image Inference")
uploaded_file = st.file_uploader("Upload an Image for Classification", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    col1, col2 = st.columns(2)
    
    with col1:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)
        
    with col2:
        if st.button("🚀 Predict Class via Flask API"):
            with st.spinner("Sending image to Flask API..."):
                try:
                    # Convert file to bytes for POST request
                    uploaded_file.seek(0)
                    files = {
                        "image": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)
                    }
                    
                    # POST Request to Flask API /predict endpoint
                    response = requests.post(f"{FLASK_API_URL}/predict", files=files, timeout=30)
                    
                    if response.status_code == 200:
                        try:
                            result = response.json()
                            st.success("Prediction Received!")
                            st.metric("Predicted Category", result.get("predicted_class", "N/A"))
                            st.metric("Confidence Score", f"{result.get('confidence', 0)}%")
                        except Exception as json_err:
                            st.error(f"Failed to parse JSON response: {str(json_err)}")
                            st.text(f"Raw Response: {response.text}")
                    else:
                        st.error(f"API Error (Status {response.status_code}): {response.text}")

                except Exception as e:
                    st.error(f"Failed to communicate with API: {str(e)}")
