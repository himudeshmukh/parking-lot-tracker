import unittest

class ParkingLot:
    """
    A class representing a parking lot.
    """
    def __init__(self):
        """
        Initialize the ParkingLot instance.
        """
        self.parking_spots = {}  # Dictionary to store parking spots

    def assign_parking_spot(self, vehicle_number):
        """
        Assign a parking spot to a vehicle.

        Parameters:
            vehicle_number (str): The vehicle number to assign a parking spot to.

        Returns:
            str: A message indicating the result of the assignment.
        """
        if len(self.parking_spots) >= 40:
            return "Parking lot is full"
        
        if vehicle_number in self.parking_spots:
            return "Vehicle already parked"
        
        level = 'A' if len(self.parking_spots) < 20 else 'B'
        spot_number = len(self.parking_spots) % 20 + 1
        self.parking_spots[vehicle_number] = {'level': level, 'spot': spot_number}
        return f"Assigned parking spot: {{'level': {level}, 'spot': {spot_number}}}"

    def retrieve_parking_spot(self, vehicle_number):
        """
        Retrieve the parking spot for a vehicle.

        Parameters:
            vehicle_number (str): The vehicle number to retrieve the parking spot for.

        Returns:
            str: A message indicating the parking spot information for the vehicle.
        """
        if vehicle_number in self.parking_spots:
            return f"Parking spot for {vehicle_number}: {self.parking_spots[vehicle_number]}"
        else:
            return f"No parking spot found for {vehicle_number}"

class ParkingLotTest(unittest.TestCase):
    """
    A class for testing the ParkingLot class.
    """
    def test_parking_allotment(self):
        """
        Test parking spot assignment for a vehicle.
        """
        parking_lot = ParkingLot()
        self.assertEqual(parking_lot.assign_parking_spot('ABC123'), "Assigned parking spot: {'level': A, 'spot': 1}")

    def test_parking_retrieve(self):
        """
        Test retrieving a parking spot for a vehicle.
        """
        parking_lot = ParkingLot()
        parking_lot.assign_parking_spot('ABC123')
        self.assertEqual(parking_lot.retrieve_parking_spot('ABC123'), "Parking spot for ABC123: {'level': 'A', 'spot': 1}")

    def test_parking_allotment_for_already_parked(self):
        """
        Test parking spot assignment for a vehicle that is already parked.
        """
        parking_lot = ParkingLot()
        parking_lot.assign_parking_spot('ABC123')
        self.assertEqual(parking_lot.assign_parking_spot('ABC123'),"Vehicle already parked")

    def test_parking_allotment_when_parking_full(self):
        """
        Test parking spot assignment when the parking lot is full.
        """
        parking_lot = ParkingLot()
        for i in range(40):
            vehicle_number = f"XYZ{i}"
            parking_lot.assign_parking_spot(vehicle_number)
        self.assertEqual(parking_lot.assign_parking_spot('XYZ40'), "Parking lot is full")

    def test_parking_allotment_for_unknown(self):
        """
        Test parking spot retrieval for an unknown vehicle.
        """
        parking_lot = ParkingLot()
        self.assertEqual(parking_lot.retrieve_parking_spot('UNKNOWN'), "No parking spot found for UNKNOWN")


if __name__ == "__main__":
    parking_lot = ParkingLot()

    while True:
        print("Options:")
        print("1. Assign a parking spot to a vehicle")
        print("2. Retrieve parking spot for a vehicle")
        print("3. Run tests")
        print("Type 'exit' to exit the program")

        choice = input("Enter your choice: ")

        if choice == '1':
            vehicle_number = input("Enter the vehicle number: ")
            print(parking_lot.assign_parking_spot(vehicle_number))
        elif choice == '2':
            vehicle_number = input("Enter the vehicle number: ")
            print(parking_lot.retrieve_parking_spot(vehicle_number))
        elif choice == '3':
            print("------------------------Running Tests------------------------")
            unittest.main()
        elif choice.lower() == 'exit':
            break
        else:
            print("Invalid choice. Please try again.")
