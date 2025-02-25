# Delivery Time Prediction 📦

This is a Streamlit web application that utilizes a pre-trained **Gradient Boosting Regressor (GBR)** model to predict delivery times based on various input features such as location details, time information, GPS data, and distance. Simply enter the required values, and the app will provide a predicted delivery time along with a summary of the input features.

## Features
✅ User-friendly interface with organized input fields grouped by category.  
✅ Real-time prediction of delivery times using a pre-trained GBR model.  
✅ Detailed input feature descriptions for better user understanding.  
✅ Expandable sections for input features and additional information.  
✅ **Error handling** for model loading and prediction processes.  

## Requirements
Ensure you have the following dependencies installed:
- Python 3.x
- Streamlit
- scikit-learn
- numpy
- pandas
- joblib

## Installation
### 1. Clone the repository:
```sh
git clone https://github.com/your-username/delivery-time-predictor.git
cd delivery-time-predictor
```

### 2. Install the required dependencies:
```sh
pip install -r requirements.txt
```

### 3. Ensure the pre-trained model file (`best_gbr_model_v1.pkl`) is in the root directory.

## Usage
Run the Streamlit app with the following command:
```sh
streamlit run app.py
```

## Live Demo
Check out the live version of the app here: [Delivery Time Prediction](https://deliveryprediction-sapna-95-git.streamlit.app/)

## Deployment
You can deploy this Streamlit app using **Streamlit Cloud** or other cloud platforms. Ensure all dependencies are included in `requirements.txt`.

## Contributing
Pull requests are welcome! Feel free to open an issue for feature requests or bug reports.

---
### Built with ❤️ using [Streamlit](https://streamlit.io/)
