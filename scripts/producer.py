import json
import time
import random
from kafka import KafkaProducer

# Configuration Kafka
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

TOPIC_NAME = 'transactions_raw'

# Prix de départ réalistes
crypto_prices = {
    "Bitcoin": 62500.0,
    "Ethereum": 2900.0,
    "BinanceCoin": 580.0
}

print("🚀 Producer de données RÉELLES (Simulateur Local) lancé...")

try:
    while True:
        for name, price in crypto_prices.items():
            # On simule une petite variation de marché (-0.5% à +0.5%)
            variation = 1 + random.uniform(-0.005, 0.005)
            crypto_prices[name] = price * variation
            
            message = {
                "tr_id": f"crypto_{name.lower()}_{int(time.time())}",
                "user_id": "market_simulator",
                "amount": round(crypto_prices[name], 2),
                "currency": "USD",
                "merchant": name,
                "timestamp": time.strftime('%Y-%m-%d %H:%M:%S')
            }
            
            producer.send(TOPIC_NAME, value=message)
            print(f"💰 Donnée envoyée : {name} - {round(crypto_prices[name], 2)} USD")
        
        # On attend 5 secondes entre chaque lot pour avoir du volume vite
        time.sleep(5)
except KeyboardInterrupt:
    print("\n🛑 Producer arrêté.")