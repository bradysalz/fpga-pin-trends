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


def parse_xilinx_virtex_four(filepath: Path, config: Dict) -> List[Pin]:
    """Parse a Xilinx Virtex-4 pinout to a Pin list.

    Args:
        fname: filename as a string
        config: dictionary from loaded configuration TOML file

    Returns:
        Pin list of parsed data
    """

    part_name = filepath.stem.upper()
    year = config['year']
    node = config['node']
    manufacturer = config['manufacturer']
    family = config['family']

    pins = []

    with open(filepath, 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        _, _, _, _, _, _, *data = reader  # removes junk rows
        for row in data:
            if len(row) == 0 or row[0] == '':
                continue

            pin_name = row[len(row) - 1]
            pin_id = row[len(row) - 3]
            pin_type = _pin_type_cleanup(pin_name)

            new_pin = Pin(
                year,
                node,
                manufacturer,
                family,
                part_name,
                pin_name,
                pin_id,
                pin_type,
            )
            pins.append(new_pin)

    return pins


if __name__ == '__main__':
    with open('data/xilinx/virtex_four/overview.toml', 'r') as f:
        config = toml.load(f)

    x = parse_xilinx_virtex_four(
        Path('data/xilinx/virtex_four/4vlx80ff1148.txt'),
        config,
    )

    for y in x:
        print(y.as_dict())
    # print([y.as_dict() for y in x])
