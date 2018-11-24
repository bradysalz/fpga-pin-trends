#!/usr/bin/env python3
import os
from pathlib import Path
from typing import List

import toml
from tqdm import tqdm

from db import database
from db import pin
from parsers.parse_table import PARSE_TABLE


def file_to_pins(filepath: Path) -> List[pin.Pin]:
    """Parses a single file to a list of Pin types.

    Args:
        filepath: Path with relative path to current file

    Returns:
        List of Pins from parsed file
    """
    config_file = Path(filepath).parent / 'overview.toml'

    if not config_file.is_file():
        raise FileNotFoundError(
            f"No 'overview.toml' found for {config_file.parent}")

    with open(config_file) as f:
        config = toml.load(f)

    parse_func = PARSE_TABLE[config['parser']]
    pins = parse_func(filepath, config)
    return pins


def add_all_files(root_dir: str = 'data/') -> List[Path]:
    """Recursively iterates over a directory and returns all files with paths

    Args:
        root_dir: the starting directory to search from

    Returns:
        List of all files found, with paths relative to the root_dir
    """
    root_path = Path(root_dir)
    files = [f for f in root_path.glob('**/*.csv')]
    files = files + [f for f in root_path.glob('**/*.txt')]

    manager = database.DbManager()
    session = manager.open_session()

    total_pins = 0
    print("Parsing files...")
    for f in tqdm(files):
        pins = file_to_pins(f)
        total_pins += len(pins)
        for p in pins:
            session.add(p)
    print(f"Added {total_pins} pins.")

    print("Commiting to database...")
    session.commit()
    session.close()
    print("Done!")


if __name__ == '__main__':
    if os.path.exists('pin_out.db'):
        os.remove('pin_out.db')
        # raise FileExistsError(
        # "'pin_out.db' already exists, please delete and retry")

    print("Creating database...")
    manager = database.DbManager()
    manager._create_db()
    print("Database created.")

    add_all_files()
