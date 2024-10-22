import requests

class Brewery:
    def __init__(self, id: str, name: str, brewery_type: str, address_1: str, address_2: str, address_3: str,  city: str, state_province: str, postal_code: str, country: str, longitude: str, latitude: str, phone: str, website_url: str, state: str, street: str):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.address_1 = address_1
        self.address_2 = address_2
        self.address_3 = address_3
        self.city = city
        self.state_province = state_province
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.website_url = website_url
        self.state = state
        self.street = street

    def __str__(self) -> str:
        return (
            f"Id: {self.id}, Brewery: {self.name}, Type: {self.brewery_type}, Location: {self.address_1}, {self.address_2}, {self.address_3}, "
            f"City: {self.city}, State province: {self.state_province}, Street: {self.street}, Postal Code: {self.postal_code}, Phone: {self.phone}, "
            f"Website: {self.website_url}, Coordinates: ({self.latitude}, {self.longitude})), Country: {self.country}, State: {self.state}, Street: {self.street}")

def get_breweries() -> list:
    url = "https://api.openbrewerydb.org/breweries"
    response = requests.get(url, params={"per_page": 20})
    breweries_data = response.json()

    breweries = []
    for data in breweries_data:
        brewery = Brewery(
            id=data.get("id", ""),
            name=data.get("name", ""),
            brewery_type=data.get("brewery_type", ""),
            address_1=data.get("address_1", ""),
            address_2=data.get("address_2", ""),
            address_3=data.get("address_3", ""),
            city=data.get("city", ""),
            state_province=data.get("state_province", ""),
            postal_code=data.get("postal_code", ""),
            country=data.get("country", ""),
            longitude=data.get("longitude", ""),
            latitude=data.get("latitude", ""),
            phone=data.get("phone", ""),
            website_url=data.get("website_url", ""),
            state=data.get("state", ""),
            street=data.get("street", "")
        )
        breweries.append(brewery)

    return breweries

breweries = get_breweries()
for brewery in breweries:
    print(brewery)