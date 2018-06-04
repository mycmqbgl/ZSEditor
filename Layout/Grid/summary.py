import tkinter as tk
from Layout.Grid.base import *
from Layout import constant

columns = constant
summarize_column = columns.summarize_column
summarize_column_zh_CN = columns.summarize_column_zh_CN


class SummaryGrid(BaseGrid):
    parameter = {
        'text': 'SummaryGrid',
        'column_array': summarize_column,
        'column_zh_CN_array': summarize_column_zh_CN
    }

    column_map = {

    }
