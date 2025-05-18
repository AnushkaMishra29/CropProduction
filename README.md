# 🌾 Crop Production Predictor

A machine learning-powered Streamlit web application that predicts total crop production (in tons) based on agricultural parameters such as area harvested and yield. This tool helps stakeholders make informed decisions in agricultural planning and resource allocation.

---

## 🚀 Features

- Predict crop production using:
  - ✅ Random Forest Regressor
  - ✅ Linear Regression
- Input parameters:
  - 🌍 Region (Country/Area)
  - 🌱 Crop Type
  - 📅 Year
  - 🌾 Area Harvested (in hectares)
  - 📈 Yield (kg per hectare)
- Actionable insights based on prediction:
  - 📊 Resource optimization
  - 📍 Strategic planning
  - 🛠 Policy and investment guidance

---

## 🧠 Use Cases

### ✅ Case 1: Low Production Alert  
> If predicted production is low, consider:
- Diversifying crop types in the region
- Investing in better irrigation or fertilization methods
- Analyzing soil health and environmental factors

### ✅ Case 2: High Production Potential  
> If predicted production is significantly high:
- Focus on improving post-harvest storage and logistics
- Consider market linkage for surplus crop
- Plan export strategies (for global demand)

### ✅ Case 3: Sub-optimal Yield Despite High Area  
> When area is large but yield is low:
- Conduct training for best farming practices
- Introduce high-yield variety seeds
- Monitor climate and disease factors

---

## 🏗️ Project Structure

├── app.py # Streamlit app code
├── filtered_crop_dataset.csv # Cleaned dataset
├── CropProductionModel.ipynb # Model training notebook
├── linear_regression_model.pkl
├── random_forest_model.pkl
├── .gitignore
└── README.md

▶️ Run the App
-streamlit run app.py
-Open in your browser at http://localhost:8502

💡 Future Enhancements
-Add location-based filtering using maps
-Integrate real-time weather data
-Enable model retraining with new user data
