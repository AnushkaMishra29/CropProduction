import streamlit as st
import pandas as pd
import joblib

# Load models
model_rf = joblib.load('random_forest_model.pkl')
model_lr = joblib.load('linear_regression_model.pkl')

# Load data with caching
@st.cache_data
def load_data():
    df = pd.read_csv("filtered_crop_dataset.csv")
    return df

df = load_data()

# App Title
st.title("🌾 Crop Production Predictor")
st.write("Predict total crop production (in tons) based on inputs.")

# -------------------------
# Model Selection
# -------------------------
model_choice = st.radio("Select Prediction Model:", ("Random Forest", "Linear Regression"))

# -------------------------
# Input Form
# -------------------------
with st.form("input_form"):
    area = st.selectbox("Select Area (Country/Region)", sorted(df['Area'].dropna().unique()))
    item = st.selectbox("Select Crop", sorted(df['Item'].dropna().unique()))
    year = st.slider("Select Year", int(df['Year'].min()), int(df['Year'].max()), step=1)
    area_ha = st.number_input("Area Harvested (hectares)", min_value=0.0, step=100.0)
    yield_kg_ha = st.number_input("Yield (kg per hectare)", min_value=0.0, step=10.0)

    submitted = st.form_submit_button("Predict")

# -------------------------
# Prediction
# -------------------------
if submitted:
    input_df = pd.DataFrame({
        'Area_Harvested_ha': [area_ha],
        'Yield_kg_ha': [yield_kg_ha],
        'Year': [year]
    })

    # Use selected model
    if model_choice == "Random Forest":
        prediction = model_rf.predict(input_df)[0]
    else:
        prediction = model_lr.predict(input_df)[0]

    st.success(f"🌾 **Predicted Crop Production:** {prediction:.2f} tons")

    # -------------------------
    # Actionable Insights
    # -------------------------
    st.markdown("## 📊 Actionable Insights")

    if prediction < 2000:
        st.warning("⚠️ **Low Production Alert:** Consider increasing the yield via improved seeds or targeted fertilizer use.")
        st.info("""
        **Recommendations:**
        - Introduce better irrigation methods like drip/sprinkler systems.
        - Conduct soil testing to optimize nutrient use.
        - Encourage alternate crops that require less input but yield better in the same conditions.
        """)
    elif prediction >= 2000 and prediction < 5000:
        st.info("ℹ️ **Moderate Production:** The production is reasonable, but there's room for optimization.")
        st.info("""
        **Recommendations:**
        - Monitor weather patterns to align sowing and harvesting cycles.
        - Implement localized training on best agricultural practices.
        - Ensure access to agricultural credits or insurance.
        """)
    else:
        st.success("✅ **High Production Potential:** Great output expected! Focus on sustainability and efficient distribution.")
        st.info("""
        **Recommendations:**
        - Invest in storage facilities to prevent post-harvest losses.
        - Explore export or distribution strategies for surplus.
        - Maintain ecological balance by rotating crops.
        """)
