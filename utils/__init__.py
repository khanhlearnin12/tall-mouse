#
def load_resource(resource_path):
    # Function to load a resource from the given path
    pass

def get_screen_dimensions():
    # Function to get the current screen dimensions
    return (800, 600)  # Example dimensions (width, height)

def center_element(element_width, element_height):
    # Function to calculate the center position for an element
    screen_width, screen_height = get_screen_dimensions()
    x = (screen_width - element_width) // 2
    y = (screen_height - element_height) // 2
    return (x, y)