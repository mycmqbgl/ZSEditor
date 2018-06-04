import tkinter as tk
from Layout import constant
from Layout.Grid import adapter

tabs = constant
tabArray = tabs.tabArray
adapter = adapter.TypeAdapter


class ShowFrame:

    def __init__(self, root):
        self.__create_frame(self, root)

    def __create_frame(self, root):
        self.frm = tk.Frame(root)
        self.frm.pack(fill="both", expand=1)
        self.__create_frm_show(self)

    def __create_frm_show(self):
        for i in range(0, len(tabArray)):
            var_name = tabArray[i]
            exec('self.' + var_name + '_frame=tk.Frame(self.frm)')
            exec('self.' + var_name + '=adapter.adapt_draw_grid(adapter, self.' + var_name + '_frame, var_name)')
            if i == 0:
                exec('self.' + var_name + '_frame.pack(fill="both", expand=1, padx=2, pady=2)')
            else:
                exec('self.' + var_name + '_frame.pack_forget()')

    def menu_choose(self, menu_name, data):
        for i in range(0, len(tabArray)):
            var_name = tabArray[i]
            if not (var_name == menu_name):
                exec('self.' + var_name + '_frame.pack_forget()')
            else:
                adapter.adapt_show_data(adapter, menu_name, data)
                exec('self.' + var_name + '_frame.pack(fill="both", expand=1, padx=2, pady=2)')
