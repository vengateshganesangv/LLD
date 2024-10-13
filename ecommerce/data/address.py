class Address:
    def __init__(self, address_line1: str, address_line2: str, address_line3: str,
                 city: str, state: str, country: str, zip_code: str):
        self.address_line1 = address_line1
        self.address_line2 = address_line2
        self.address_line3 = address_line3
        self.city = city
        self.state = state
        self.country = country
        self.zip_code = zip_code