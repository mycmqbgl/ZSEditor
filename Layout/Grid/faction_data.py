import tkinter as tk
from Layout.Grid.base import *
from Layout import constant

columns = constant
faction_column = columns.faction_column
faction_column_zh_CN = columns.faction_column_zh_CN


class FactionDataGrid(BaseGrid):
    parameter = {
        'text': 'FactionDataGrid',
        'column_array': faction_column,
        'column_zh_CN_array': faction_column_zh_CN
    }

    column_map = {

    }


