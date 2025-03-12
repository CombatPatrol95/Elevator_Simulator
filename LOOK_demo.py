class Elevator:
    def __init__(self, num_floors):
        self.current_floor = 0
        self.direction = 1  # 1 for up, -1 for down
        self.num_floors = num_floors
        self.requests = []
        self.stops_made = []

    def add_request(self, floor):
        """Add a floor request to the elevator system"""
        if 0 <= floor < self.num_floors and floor not in self.requests:
            self.requests.append(floor)

    def has_requests_above(self):
        """Check if there are any pending requests above current floor"""
        return any(floor > self.current_floor for floor in self.requests)

    def has_requests_below(self):
        """Check if there are any pending requests below current floor"""
        return any(floor < self.current_floor for floor in self.requests)

    def next_destination(self):
        """Determine next floor to visit using LOOK algorithm"""
        if not self.requests:
            return None

        # Moving up
        if self.direction == 1:
            # Get all requests above current floor
            upper_floors = [f for f in self.requests if f > self.current_floor]
            if upper_floors:
                # If there are requests above, go to the nearest upper floor
                return min(upper_floors)
            # If no requests above, get all requests below
            lower_floors = [f for f in self.requests if f < self.current_floor]
            if lower_floors:
                # Change direction and go to highest lower floor
                self.direction = -1
                return max(lower_floors)

        # Moving down
        else:
            # Get all requests below current floor
            lower_floors = [f for f in self.requests if f < self.current_floor]
            if lower_floors:
                # If there are requests below, go to the nearest lower floor
                return max(lower_floors)
            # If no requests below, get all requests above
            upper_floors = [f for f in self.requests if f > self.current_floor]
            if upper_floors:
                # Change direction and go to lowest upper floor
                self.direction = 1
                return min(upper_floors)

        return None

    def run(self):
        """Run the elevator until all requests are processed"""
        while self.requests:
            next_floor = self.next_destination()
            if next_floor is None:
                break

            # Move to next floor and record the stop
            self.current_floor = next_floor
            self.stops_made.append(next_floor)

            # Remove the request once served
            self.requests.remove(next_floor)

        return self.stops_made


# Example usage
def demonstrate_look():
    # Create elevator for a 10-floor building
    elevator = Elevator(10)

    # Add sample requests
    sample_requests = [2, 5, 7, 1, 8, 3]
    print("Floor requests:", sample_requests)

    for floor in sample_requests:
        elevator.add_request(floor)

    # Run the elevator and get the sequence of stops
    stops = elevator.run()
    print("\nElevator starts at floor", 0)
    print("Stops made in order:", stops)

    # Calculate total distance traveled
    total_distance = 0
    current = 0  # Start from ground floor

    for stop in stops:
        distance = abs(stop - current)
        total_distance += distance
        current = stop

    print("Total floors traveled:", total_distance)


if __name__ == "__main__":
    demonstrate_look()