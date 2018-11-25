#!/usr/bin/env python3
import csv
from pathlib import Path
from typing import Dict, List

import toml

from db.pin import Pin


def _pin_type_cleanup(ptype: str) -> str:
    if 'VCC' in ptype:
        return 'VCC'
    if 'GND' in ptype:
        return 'GND'
    if 'IO' in ptype:
        return 'IO'
    return ptype


def parse_xilinx_spartan(filepath: Path, config: Dict) -> List[Pin]:
    """Parse a Xilinx Kintex Ultrascale Plus pinout to a Pin list.

    Args:
        fname: filename as a string
        config: dictionary from loaded configuration TOML file

    Returns:
        Pin list of parsed data
    """

    part_name = filepath.stem[:-3].upper()
    year = config['year']
    node = config['node']
    manufacturer = config['manufacturer']
    family = config['family']

    pins = []

    with open(filepath, 'r') as f:
        reader = csv.reader(f)
        *data, _, _ = reader  # removes junk rows
        for row in data:
            print(row)
            if row[0] == '' or row[0][0] == "#":
                continue

            pin_type = _pin_type_cleanup(row[1])
            new_pin = Pin(
                year,
                node,
                manufacturer,
                family,
                part_name,
                row[1],
                row[0],
                pin_type,
            )
            pins.append(new_pin)

    return pins


if __name__ == '__main__':
    with open('data/xilinx/spartan_seven/overview.toml', 'r') as f:
        config = toml.load(f)

    x = parse_xilinx_spartan(
        Path('data/xilinx/spartan_seven/xc7s25csga225pkg.csv'),
        config,
    )

    print([str(y) for y in x])
