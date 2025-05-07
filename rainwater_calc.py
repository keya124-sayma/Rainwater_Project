def calculate_rainwater(catchment_area_m2, rainfall_mm, efficiency=0.85):
    """
    Calculate collected rainwater in liters.

    Parameters:
    - catchment_area_m2: Area of the rooftop (in square meters)
    - rainfall_mm: Total rainfall (in millimeters)
    - efficiency: Collection efficiency (between 0 and 1)

    Returns:
    - Estimated rainwater collected in liters.
    """
    volume_liters = catchment_area_m2 * rainfall_mm * efficiency
    return volume_liters
