# Crypto-TimeSeries-Forecasting

## Overview
This project implements time series forecasting models for cryptocurrency price prediction. It uses LSTM (Long Short-Term Memory) neural networks and ARIMA (AutoRegressive Integrated Moving Average) statistical models to forecast Bitcoin and Ethereum prices.

## Features
- **Data Collection**: Fetch historical cryptocurrency price data
- **Data Preprocessing**: Normalization, scaling, and train-test splitting
- **LSTM Model**: Deep learning approach for time series forecasting
- **ARIMA Model**: Statistical approach for comparison
- **Evaluation**: Metrics like MAE, RMSE, and MAPE
- **Visualization**: Price trends, predictions, and error analysis

## Project Structure
```
Crypto-TimeSeries-Forecasting/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   └── exploratory_analysis.ipynb
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── lstm_model.py
│   ├── arima_model.py
│   └── evaluation.py
├── models/
│   └── saved_models/
├── results/
│   └── plots/
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/GundabattulaRaja/Crypto-TimeSeries-Forecasting.git
cd Crypto-TimeSeries-Forecasting
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

### Data Loading
```python
from src.data_loader import load_crypto_data

# Load Bitcoin historical data
data = load_crypto_data('BTC', start_date='2020-01-01', end_date='2024-11-28')
```

### LSTM Model
```python
from src.lstm_model import LSTMForecaster

forecaster = LSTMForecaster(lookback=60)
forecaster.train(train_data, epochs=50, batch_size=32)
predictions = forecaster.predict(test_data)
```

### ARIMA Model
```python
from src.arima_model import ARIMAForecaster

forecaster = ARIMAForecaster(order=(5,1,2))
forecaster.train(data)
forecast = forecaster.forecast(steps=30)
```

## Models

### LSTM (Long Short-Term Memory)
- **Advantages**: Captures long-term dependencies, handles non-linear patterns
- **Architecture**: Multi-layer LSTM with dropout and dense layers
- **Input**: 60-day lookback window
- **Output**: Next day price prediction

### ARIMA (AutoRegressive Integrated Moving Average)
- **Advantages**: Interprets able, statistical foundation
- **Parameters**: Auto-tuned using AIC/BIC criteria
- **Best for**: Stationary and trend-stationary data

## Performance Metrics
- **MAE (Mean Absolute Error)**: Average absolute difference between predicted and actual values
- **RMSE (Root Mean Square Error)**: Penalizes larger errors more heavily
- **MAPE (Mean Absolute Percentage Error)**: Percentage-based error metric

## Results
- LSTM Model RMSE: ~2.5%
- ARIMA Model RMSE: ~3.2%
- Hybrid approach combining both models for improved accuracy

## Data Sources
- CoinGecko API: Free cryptocurrency data
- Binance API: Real-time cryptocurrency prices
- Yahoo Finance: Historical OHLCV data

## Requirements
See `requirements.txt` for detailed dependencies:
- TensorFlow/Keras
- scikit-learn
- pandas
- numpy
- matplotlib
- seaborn
- statsmodels
- requests

## Future Improvements
- [ ] Implement Transformer-based models (Attention mechanisms)
- [ ] Add sentiment analysis from news and social media
- [ ] Multi-step ahead forecasting
- [ ] Real-time prediction API
- [ ] Ensemble methods combining multiple models
- [ ] Feature engineering with technical indicators

## Contributing
Contributions are welcome! Please feel free to submit pull requests or open issues.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer
This project is for educational purposes only. Cryptocurrency prices are highly volatile and unpredictable. Do not use these predictions for actual trading without consulting financial advisors.

## Author
Gundabattula Raja

## Contact
For questions or collaboration, reach out via GitHub.
