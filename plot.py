#!/usr/bin/env python3

import click
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sqlalchemy import func

from db import database
from db.pin import Pin

VALID_PLOTS = {
    'PINS_VS_PROCESS',
    'PINS_VS_YEAR',
    'VCC_VS_GND_DIST',
    'VCC_VS_GND',
}
VALID_PLOTS_STR = ', '.join(VALID_PLOTS)


@click.command()
@click.option(
    '-n',
    '--name',
    type=str,
    help='Which plot to show, case insensitive. '
    f'Valid options are:\n{VALID_PLOTS_STR}')
def plot(name: str):
    name = name.upper()
    if name.upper() not in VALID_PLOTS:
        raise KeyError(
            f"Invalid plot name '{name}'. Try one of: {VALID_PLOTS_STR}")

    manager = database.DbManager()
    session = manager.open_session()

    if name == 'PINS_VS_PROCESS':
        query = session.query(Pin.family, Pin.part, func.count(Pin.pin_id),
                              Pin.process).group_by(Pin.part)
        df = pd.read_sql_query(query.statement, session.bind)

        ax = sns.swarmplot(x="process", y="count_1", data=df)
        ax.set_xlabel('Process Node [nm]')
        ax.set_ylabel('Pin Count [#]')

    if name == 'PINS_VS_YEAR':
        query = session.query(Pin.family, Pin.part, func.count(Pin.pin_id),
                              Pin.year).group_by(Pin.part)
        df = pd.read_sql_query(query.statement, session.bind)

        ax = sns.swarmplot(x="year", y="count_1", data=df)
        ax.set_xlabel('Year')
        ax.set_ylabel('Pin Count [#]')

    if name == 'VCC_VS_GND_DIST':
        query = session.query(Pin.family, Pin.part, Pin.pin_type, func.count(
                Pin.pin_id)) \
            .filter(Pin.pin_type.in_(['VCC', 'GND'])) \
            .group_by(Pin.part, Pin.pin_type)
        df = pd.read_sql_query(query.statement, session.bind)

        # You can probably do this in SQL but I wasn't sure how to do that
        df['ratio'] = df.count_1 / df.count_1.shift(1)

        ax = sns.distplot(df[df['pin_type'] == 'VCC']['ratio'])
        ax.set_xlabel('(# of VCC Pins) / (# of GND Pins)')
        ax.set_yticks([])

    if name == 'VCC_VS_GND':
        query = session.query(Pin.family, Pin.part, Pin.pin_type, func.count(
                Pin.pin_id)) \
            .filter(Pin.pin_type.in_(['VCC', 'GND'])) \
            .group_by(Pin.part, Pin.pin_type)
        df = pd.read_sql_query(query.statement, session.bind)

        ax = sns.scatterplot(
            x=df[df['pin_type'] == 'VCC']['count_1'].values,
            y=df[df['pin_type'] == 'GND']['count_1'].values)

        ax.set_xlabel('# of VCC Pins')
        ax.set_ylabel('# of GND Pins')
    session.close()
    plt.show()


if __name__ == '__main__':
    plot()
