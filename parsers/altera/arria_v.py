#!/usr/bin/env python3
import csv
from pathlib import Path
from typing import Dict, List, Tuple

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


def find_part_start(rows: List[str]) -> Tuple[int, str]:
    """Find the starting row for all parts in a file.

    Altera is dumb and concats what should be independent CSVs into one file,
    which makes it incredibly hard to parse. This helps us find the starting
    points for each one.
    """
    parts = []
    for idx_row, row in enumerate(rows):
        if row and row[0].startswith('Bank'):
            for idx_col, val in enumerate(row):
                if val[0] in ['F', 'U']:  # lol
                    try:
                        # Trying to find "1152" in "F1152 "
                        val = val.split(' ')[0]
                        int(val[1:])
                        parts.append((idx_row, idx_col, val))
                    except ValueError:
                        continue
    print(parts)
    return parts


def parse_altera_arria_v(filepath: Path, config: Dict) -> List[Pin]:
    """Parse Altera Arrian GX pinout to a Pin list.

    Args:
        fname: filename as a string
        config: dictionary from loaded configuration TOML file

    Returns:
        Pin list of parsed data
    """
    part_root = filepath.stem.upper().split('-')[0]
    year = config['year']
    node = config['node']
    manufacturer = config['manufacturer']
    family = config['family']

    pins = []

    with open(filepath, 'r', encoding='cp1252') as f:
        reader = csv.reader(f, delimiter='\t')
        header, *data = reader  # removes junk rows

        parts = []
        for idx, val in enumerate(header):
            val = val.split(' ')[0]
            if val and val[0] in ['F', 'U']:  # lol
                try:
                    int(val[1:])
                    parts.append((idx, val))
                except ValueError:
                    continue

        for part in parts:
            pin_id_idx, part_tail = part
            part_name = part_root + part_tail
            for row in data:
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
    with open('data/altera/arria-v/overview.toml', 'r') as f:
        config = toml.load(f)

    x = parse_altera_arria_v(
        Path('data/altera/arria-v/5asxmb5-1.txt'),
        config,
    )

    for y in x:
        # print(y.as_dict())
        pass
    print(len(x))
