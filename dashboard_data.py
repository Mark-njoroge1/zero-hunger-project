def get_weather_data():
    weather = {
        "temp": "24°C",
        "condition": "Light Showers Expected",
        "humidity": "78%"
    }
    return weather


def get_market_prices():
    prices = {
        "Maize": "$25 / Bag",
        "Beans": "$45 / Bag",
        "Potatoes": "$18 / Crate"
    }
    return prices


if __name__ == "__main__":
    print("Weather data:", get_weather_data())
    print("Market prices:", get_market_prices())