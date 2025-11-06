BASE_FARE = 50
FARE_PER_KM = 10
def calculate_fare(distance):
    return BASE_FARE + (FARE_PER_KM * distance)
def total_fare(trips):
    total = 0
    for i, dist in enumerate(trips, start=1):
        fare = calculate_fare(dist)
        print(f"Trip {i}: ${fare}")
        total += fare
        print(f"Total Fare: ${total}")
if __name__ == "__main__":
    trips = [5, 10, 3]
    total_fare(trips)
