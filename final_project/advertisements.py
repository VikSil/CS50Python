# This module stores all the classes that are used for scraping advertisement data from www.ss.lv


# GENERIC AD CLASS
class Ad:
    def __init__(
        self,
        url: str,
        adtype: int,
        price: float,
        ccy: str,
        description: str,
        fprice: float = 0,
        fract: str = "",
    ):
        self.url = url
        # ad types: 1 - Sell, 2 - Buy, 3 - Lease out, 4 - Lease in, 5 - Other
        self.adtype = adtype
        self.price = price
        self.ccy = ccy
        self.description = description
        self.fprice = fprice
        self.fract = fract

    def __str__(self):
        match self.adtype:
            case 1:
                adtype_str = "Sell"
            case 2:
                adtype_str = "Buy"
            case 3:
                adtype_str = "Lease out"
            case 4:
                adtype_str = "Lease_In"
            case _:
                adtype_str = "Other"

        output = (
            "The properties of this ad are:"
            + "\n"
            + "URL: "
            + self.url
            + "\n"
            + "Ad type: "
            + adtype_str
            + "\n"
            + "Price: "
            + str(self.price)
            + "\n"
            + "Currency: "
            + self.ccy
            + "\n"
        )
        if self.fprice > 0:
            output = (
                output
                + "Fracional price: "
                + str(self.fprice)
                + " per "
                + self.fract
                + "\n"
            )

        output = output + "The description of the ad: \n"
        output = output + self.descr

        return output

    # function to return all class data as a list
    def listmyself(self):
        match self.adtype:
            case 1:
                adtype_str = "Sell"
            case 2:
                adtype_str = "Buy"
            case 3:
                adtype_str = "Lease out"
            case 4:
                adtype_str = "Lease_In"
            case _:
                adtype_str = "Other"

        listself = [
            self.url,
            adtype_str,
            self.price,
            self.ccy,
            self.description,
            self.fprice,
            self.fract,
        ]
        return listself


# EXTENDED CLASS OF A REAL ESTATE - FLAT AD
class Flat(Ad):
    def __init__(
        self,
        url: str,
        adtype: int,
        price: float,
        ccy: str,
        description: str,
        city: str,
        area: float,
        rooms: int,
        fprice: float = 0,
        fract: str = "",
        parish: str = "",
        village: str = "",
        street: str = "",
        level: str = "",
        series: str = "",
        buildingtype: str = "",
    ):
        super().__init__(url, adtype, price, ccy, description, fprice, fract)

        self.city = city
        self.area = area
        self.rooms = rooms
        self.parish = parish
        self.village = village
        self.street = street
        self.level = level
        self.series = series
        self.buildingtype = buildingtype

    def __str__(self):
        match self.adtype:
            case 1:
                adtype_str = "Sell"
            case 2:
                adtype_str = "Buy"
            case 3:
                adtype_str = "Lease out"
            case 4:
                adtype_str = "Lease_In"
            case _:
                adtype_str = "Other"

        output = (
            "The properties of this ad are:"
            + "\n"
            + "URL: "
            + self.url
            + "\n"
            + "Ad type: "
            + adtype_str
            + "\n"
            + "Price: "
            + str(self.price)
            + "\n"
            + "Currency: "
            + self.ccy
            + "\n"
            + "City: "
            + self.city
            + "\n"
            + "Area: "
            + str(self.area)
            + "\n"
            + "Rooms: "
            + str(self.rooms)
            + "\n"
        )

        if self.fprice > 0:
            output = (
                output
                + "Fracional price: "
                + str(self.fprice)
                + " per "
                + self.fract
                + "\n"
            )
        if len(self.parish) > 0:
            output = output + "Parish: " + self.parish + "\n"
        if len(self.village) > 0:
            output = output + "Village: " + self.village + "\n"
        if len(self.street) > 0:
            output = output + "Street: " + self.street + "\n"
        if len(self.level) > 0:
            output = output + "Level: " + self.level + "\n"
        if len(self.series) > 0:
            output = output + "Era of a building: " + self.series + "\n"
        if len(self.buildingtype) > 0:
            output = output + "Type of a building: " + self.buildingtype + "\n"

        output = output + "The description of the ad: \n"
        output = output + self.description

        return output

    # function to return all class data as a list
    def listmyself(self):
        listself = super().listmyself()
        listself_add = [
            self.area,
            self.rooms,
            self.city,
            self.parish,
            self.village,
            self.street,
            self.level,
            self.series,
            self.buildingtype,
        ]
        listself.extend(listself_add)
        # move the description to the end - looks better when output to Excel
        listself.append(listself.pop(4))

        return listself
