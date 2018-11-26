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


def parse_altera_arria_ten(filepath: Path, config: Dict) -> List[Pin]:
    """Parse Altera Arrian-10 pinout to a Pin list.

    Args:
        fname: filename as a string
        config: dictionary from loaded configuration TOML file

    Returns:
        Pin list of parsed data
    """

    part_name = filepath.stem.upper().split('-')[0]
    year = config['year']
    node = config['node']
    manufacturer = config['manufacturer']
    family = config['family']

    pins = []

    with open(filepath, 'r', encoding='cp1252') as f:
        reader = csv.reader(f, delimiter='\t')
        _, _, _, _, *data = reader  # removes junk rows
        for row in data:
            if len(row) < 2 or row[0] == '':
                continue

            try:
                pin_name = row[3]
                pin_id = row[10]
            except IndexError:
                continue

            if pin_name == '' or pin_id == '':
                continue

            pin_type = _pin_type_cleanup(pin_name)
            new_pin = Pin(year, node, manufacturer, family, part_name,
                          pin_name, pin_id, pin_type)
            pins.append(new_pin)

    return pins


if __name__ == '__main__':
    with open('data/altera/arria-10/overview.toml', 'r') as f:
        config = toml.load(f)

    x = parse_altera_arria_ten(
        Path('data/altera/arria-10/10as016-1.txt'),
        config,
    )

    for y in x:
        print(y.as_dict())
    # print([y.as_dict() for y in x])
