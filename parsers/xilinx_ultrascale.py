from typing import Dict, List

import pandas as pd
import toml

from db.pin import Pin


def parse_xilinx_ultrascale(fname: str, config: Dict) -> List[Pin]:
    """Parse a Xilinx Ultrascale pinout to a Pin list.

    Args:
        fname: filename as a string

    Returns:
        Pin list of parsed data
    """
    with open(fname, 'r') as f:
        df = pd.read_csv(
            f,
            warn_bad_lines=True,
            error_bad_lines=True,
            header=2,
            skipfooter=2,
            engine='python',
            verbose=True)

    df.loc[df['Pin Name'].str.contains('VCC'), 'I/O Type'] = 'PWR'
    df.loc[df['Pin Name'].str.contains('GND'), 'I/O Type'] = 'GND'

    part_name = fname.split('pkg')[0]
    part_name = part_name.split('/')[-1].upper()
    year = config['year']
    node = config['node']
    manufacturer = config['manufacturer']
    family = config['family']

    pin_list = []
    for idx, row in df.iterrows():
        new_pin = Pin(
            year,
            node,
            manufacturer,
            family,
            part_name,
            row['Pin Name'],
            row['Pin'],
            row['I/O Type'],
        )
        pin_list.append(new_pin)
    return pin_list


if __name__ == '__main__':
    with open('data/xilinx/kintex_ultrascale/overview.toml', 'r') as f:
        config = toml.load(f)

    x = parse_xilinx_ultrascale(
        'data/xilinx/kintex_ultrascale/xcku025ffva1156pkg.csv',
        config,
    )

    print([str(y) for y in x])
