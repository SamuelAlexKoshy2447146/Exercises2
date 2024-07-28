"""
5.Write a Python program to analyze and process weather data for New York City from 1st
August to 10th July in 2024.

1. Each day's data includes:
    o Date
    o Maximum temperature (in Celsius)
    o Minimum temperature (in Celsius)
    o Humidity (in percentage)
2. Write a function to find the highest and lowest temperatures recorded during the week.
3. Write a function to determine the number of days with temperatures above 30°C.
4. Write a function to compute the average humidity over the specified period."""

weather_data = [
    {"date": "2024-08-01", "max_temp": 27, "min_temp": 20, "humidity": 68},
    {"date": "2024-08-02", "max_temp": 26, "min_temp": 19, "humidity": 70},
    {"date": "2024-08-03", "max_temp": 28, "min_temp": 21, "humidity": 63},
    {"date": "2024-08-04", "max_temp": 29, "min_temp": 22, "humidity": 59},
    {"date": "2024-08-05", "max_temp": 30, "min_temp": 23, "humidity": 57},
    {"date": "2024-08-06", "max_temp": 31, "min_temp": 24, "humidity": 54},
    {"date": "2024-08-07", "max_temp": 30, "min_temp": 23, "humidity": 56},
    {"date": "2024-08-08", "max_temp": 29, "min_temp": 22, "humidity": 58},
    {"date": "2024-08-09", "max_temp": 28, "min_temp": 21, "humidity": 60},
    {"date": "2024-08-10", "max_temp": 27, "min_temp": 20, "humidity": 62},
]


def highest_temp(weather_data):
    """Find the highest temperature in a period

    Args:
        weather_data (list): The weather data available

    Returns:
        int: The maximum temperature recorded
    """

    max_temp = weather_data[0]["max_temp"]
    for day in weather_data[1:]:
        max_temp = max_temp if max_temp > day["max_temp"] else day["max_temp"]
    return max_temp


def lowest_temp(weather_data):
    """Find the lowest temperature in a period

    Args:
        weather_data (list): The weather data available

    Returns:
        int: The lowest temperature recorded
    """

    min_temp = weather_data[0]["min_temp"]
    for day in weather_data[1:]:
        min_temp = min_temp if min_temp < day["min_temp"] else day["min_temp"]
    return min_temp


def temp_above_30(weather_data):
    """Find the number of days temperature exceeded 30 Celsius

    Args:
        weather_data (list): The weather data available

    Returns:
        int: The number of days
    """

    count = 0
    for day in weather_data:
        if day["max_temp"] > 30:
            count += 1
    return count


def average_humidity(weather_data):
    """Find average humidity in the given period

    Args:
        weather_data (list): The weather data available

    Returns:
        float: The average humidity
    """

    total_humidity = 0
    for day in weather_data:
        total_humidity += day["humidity"]
    return total_humidity / len(weather_data)


if __name__ == "__main__":
    print("Highest temperature:", highest_temp(weather_data))
    print("Lowest temperature:", lowest_temp(weather_data))
    print("No. of days with temperature above 30:", temp_above_30(weather_data))
    print("Average humidity:", average_humidity(weather_data))
