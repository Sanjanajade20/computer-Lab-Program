# Create a class Weather that has a list containing weather parameters. Define an overloaded in operator that checks whether an item is present in the list.

class Weather:
    def __init__(self, parameters):
        self.parameters = parameters
    
    def __contains__(self, item):
        return item in self.parameters

weather = Weather(['temperature', 'humidity', 'precipitation', 'wind speed', 'pressure'])
print('temperature' in weather)  # Output: True
print('cloud cover' in weather)  # Output: False
