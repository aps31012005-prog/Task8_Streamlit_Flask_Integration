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
# Render deploy hone ke baad apna exact URL yahan paste karna
FLASK_API_URL = "https://task8-flask-api.onrender.com"

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
    health_resp = requests.get(f"{FLASK_API_URL}/", timeout=5)
    if health_resp.status_code == 200:
        st.success("✅ **Flask Backend API Status:** Connected & Live")
    else:
        st.warning("⚠️ **Flask API Status:** Server responding with error")
except Exception:
    st.error("❌ **Flask API Status:** Could not connect to API server")

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
                    files = {"image": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
                    
                    response = requests.post(f"{FLASK_API_URL}/predict", files=files)
                    
                    if response.status_code == 200:
                        result = response.json()
                        st.success("Prediction Received!")
                        st.metric("Predicted Category", result["predicted_class"])
                        st.metric("Confidence Score", f"{result['confidence']}%")
                    else:
                        st.error(f"API Error: {response.json().get('error', 'Unknown Error')}")
                except Exception as e:
                    st.error(f"Failed to communicate with API: {str(e)}")
