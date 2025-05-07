# Dictionary of cities and their average annual rainfall in mm
rainfall_database = {
    "Dhaka": 2100,
    "Chittagong": 2900,
    "Khulna": 1800,
    "Sylhet": 4200,
    "Rajshahi": 1600
}

def get_rainfall(city):
    """
    Returns the average annual rainfall (in mm) for the given city.
    If the city is not found, returns a default value (2000 mm).
    """
    return rainfall_database.get(city, 2000)
