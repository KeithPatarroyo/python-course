def get_available_brands():
    return ["chiquita"]


class Banana:
    def __init__(self, brand="chiquita"):
        if brand not in get_available_brands():
            raise ValueError(f"Unknown brand: {brand}")
        self._brand = brand