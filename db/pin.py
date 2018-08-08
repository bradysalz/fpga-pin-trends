from typing import Dict

from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Pin(Base):
    """Pin class for holding info on a single FPGA pin

    Fields:
        id: Primary key, autogen int
        year: Year the device came out, stored as int for simplicity
            example - 2012
        process: Device process node in nm
            example - 130
        manufacturer: Device manufacturer
            example - "MyFpgaCompany"
        family: Device family
            example - "UltraStratex IV"
        part: Specific part name
            example - "XCEP4KU-CGX060"
        pin_name: Listed device pin name. if a pin has functions, they are
            joined with underscores to create one name
            example - "IO_LT2_GXB4_P"
        pin_id: The ID of the pin on the footprint. Can be either numeric or
            alphanumeric (but shouldn't be purely alphabetical)
            example - "AM13", "112"
        pin_type: What kind of pin it is
            #TODO more documentation here
            example - "IO", "VDD"
    """
    __tablename__ = 'pin_outs'

    id = Column(Integer, primary_key=True)
    year = Column(Integer)
    process = Column(Integer)
    manufacturer = Column(Text)
    family = Column(Text)
    part = Column(Text)
    pin_name = Column(Text)
    pin_id = Column(Text)
    pin_type = Column(Text)

    def __init__(self, year, process, manufacturer, family, part, pin_name,
                 pin_id, pin_type):
        """Create the Pin row

        This is currently a no-op, but there might be a need for parsing,
        later so might as well have it in now.
        """
        self.year = year
        self.process = process
        self.manufacturer = manufacturer
        self.family = family
        self.part = part
        self.pin_name = pin_name
        self.pin_id = pin_id
        self.pin_type = pin_type

    def as_dict(self) -> Dict:
        """Turn row of data into dict and return it

        Returns:
            Dict of attr, attr_value pairs
        """
        return {
            'year': self.year,
            'process': self.process,
            'manufacturer': self.manufacturer,
            'family': self.family,
            'part': self.part,
            'pin_name': self.pin_name,
            'pin_id': self.pin_id,
            'pin_type': self.pin_type,
        }

    def __str__(self):
        return f"<Pin {self.part} {self.pin_id}>"
