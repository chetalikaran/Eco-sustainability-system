import streamlit as st
import numpy as np
import pickle

# Load trained model
model = pickle.load(open("eco_model.pkl", "rb"))

st.set_page_config(
    page_title="AI Eco‑Score Predictor",
    layout="centered"
)

st.title("🌱 AI Eco‑Score Predictor")
st.write("Predict product sustainability using AI")

st.subheader("Enter Product Details")

plastic = st.number_input("Plastic used (grams)", min_value=0, step=10)
energy = st.number_input("Energy used (kWh)", min_value=0, step=10)
water = st.number_input("Water usage (litres)", min_value=0, step=10)
transport = st.number_input("Transport distance (km)", min_value=0, step=10)
recycle = st.slider("Recyclability (%)", 0, 100, 50)
packaging = st.selectbox("Packaging level (1–5)", [1, 2, 3, 4, 5])

if st.button("Predict Eco Score"):
    input_data = np.array([[plastic, energy, water, transport, recycle, packaging]])
    score = model.predict(input_data)[0]

    st.markdown(f"## 🌍 Eco Score: **{round(score, 2)}**")

    if score >= 75:
        st.success("✅ Highly Sustainable Product")
    elif score >= 45:
        st.warning("⚠️ Moderately Sustainable Product")
    else:
        st.error("❌ Not Sustainable Product")
