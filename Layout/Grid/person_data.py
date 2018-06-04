import tkinter as tk
from Layout.Grid.base import *
from Layout import constant

columns = constant
person_column = columns.person_column
person_column_zh_CN = columns.person_column_zh_CN


class PersonDataGrid(BaseGrid):
    parameter = {
        'text': 'PersonDataGrid',
        'column_array': person_column,
        'column_zh_CN_array': person_column_zh_CN
    }

    column_map = {

    }
