#!/usr/bin/env python
"""
Main entry point for Crypto Time Series Forecasting Application
"""

import logging
import argparse
from datetime import datetime, timedelta

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    """
    Main function to run the cryptocurrency forecasting pipeline
    """
    parser = argparse.ArgumentParser(
        description='Cryptocurrency Time Series Forecasting'
    )
    parser.add_argument(
        '--crypto',
        type=str,
        default='BTC',
        help='Cryptocurrency to forecast (BTC, ETH, etc.)'
    )
    parser.add_argument(
        '--model',
        type=str,
        default='lstm',
        choices=['lstm', 'arima', 'hybrid'],
        help='Forecasting model to use'
    )
    parser.add_argument(
        '--days',
        type=int,
        default=30,
        help='Number of days to forecast'
    )
    
    args = parser.parse_args()
    
    logger.info(f'Starting forecast for {args.crypto} using {args.model} model')
    logger.info(f'Forecasting {args.days} days ahead')
    
    # TODO: Implement actual forecasting pipeline
    logger.info('Forecast complete!')


if __name__ == '__main__':
    main()
