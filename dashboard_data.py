
def get_weather_data():
    """
    Returns the current weather snapshot for the dashboard.
    Must always include: temp, condition, humidity.
    """
    weather = {
        "temp": "24°C",
        "condition": "Light Showers Expected",
        "humidity": "78%"
    }
    return weather


def get_market_prices():
    """
    Returns current commodity prices for common crops.
    Keys are crop names, values are display-ready price strings.
    """
    prices = {
        "Maize": "$25 / Bag",
        "Beans": "$45 / Bag",
        "Potatoes": "$18 / Crate"
    }
    return prices


if __name__ == "__main__":
    print("Weather data:", get_weather_data())
    print("Market prices:", get_market_prices())