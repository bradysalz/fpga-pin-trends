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


def parse_altera_arria_gx(filepath: Path, config: Dict) -> List[Pin]:
    """Parse Altera Arrian GX pinout to a Pin list.

    Args:
        fname: filename as a string
        config: dictionary from loaded configuration TOML file

    Returns:
        Pin list of parsed data
    """

    year = config['year']
    node = config['node']
    manufacturer = config['manufacturer']
    family = config['family']

    pins = []

    with open(filepath, 'r', encoding='cp1252') as f:
        reader = csv.reader(f, delimiter='\t')
        _, _, _, headers, _, *data = reader  # removes junk rows

        parts = []
        for idx, val in enumerate(headers):
            if val.startswith('EP'):
                parts.append((idx, val))

        for part in parts:
            pin_id_idx, part_name = part
            for row in data:
                if len(row) < 2:
                    continue

                try:
                    pin_name = row[2]
                    pin_id = row[pin_id_idx]
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
    with open('data/altera/arria-gx/overview.toml', 'r') as f:
        config = toml.load(f)

    x = parse_altera_arria_gx(
        Path('data/altera/arria-gx/ep1agx60.txt'),
        config,
    )

    for y in x:
        print(y.as_dict())
    # print([y.as_dict() for y in x])
