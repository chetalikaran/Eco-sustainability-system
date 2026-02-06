# AI-Eco-Score-Predictor

## GitHub Repository Description
An AI-based sustainability project that predicts an Eco Score, 0 to 100, for products using manufacturing and logistics parameters such as plastic usage, energy consumption, water usage, transport distance, recyclability, and packaging level. The system helps evaluate whether a product is Highly Sustainable, Moderately Sustainable, or Not Sustainable, supporting green decision-making in industry.

---

## Overview
Sustainability has become a key focus for modern industries. This project uses Machine Learning to predict the environmental sustainability of products by analyzing real-world manufacturing factors. The model outputs an Eco Score that helps companies and consumers make environmentally responsible choices.

---

## Objectives
- Predict eco-friendliness of products using AI
- Reduce environmental impact through data-driven decisions
- Provide an automated sustainability evaluation system

---

## Features Used
- Plastic used, grams
- Energy used in production, kWh
- Water usage, litres
- Transport distance, kilometers
- Recyclability percentage, percent
- Packaging level, scale of 1 to 5

---

## Machine Learning Model
**Algorithm:** Random Forest Regressor  

**Reason:**  
Handles non-linear relationships efficiently and provides high prediction accuracy for complex datasets.

---

## Model Performance
- R² Score, approximately 0.86
- Mean Absolute Error, approximately 6

---

## Eco Score Classification
- Eco Score greater than or equal to 75, Highly Sustainable
- Eco Score between 45 and 74, Moderately Sustainable
- Eco Score below 45, Not Sustainable

---

## How It Works
1. User inputs product manufacturing and logistics details
2. Data is processed and passed into the Machine Learning model
3. Model predicts the Eco Score
4. Product sustainability category is displayed

---

## Real-World Applications
- E-commerce eco-rating systems
- Sustainable manufacturing assessment
- Green product certification
- ESG and environmental audits
- Smart factory sustainability monitoring

---

## Future Enhancements
- Integration with real industrial datasets
- Web application using Streamlit
- Deep learning-based sustainability scoring
- ESG metric integration
- Product image-based sustainability analysis

---

## Technologies Used
- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Google Colab

---

## Authors
- Akshat Sahu  
- Chetali Karan  
- Shubham Raut  
- Nikita Lanke  
- Lochan Yadav  

**Program:** AI and Data Science

