import tkinter as tk


class BaseGrid:

    frame = None
    column_array = None
    column_zh_CN_array = None

    parameter = {
        'text': 'BaseGrid',
    }

    column_map = {

    }

    def set_frame(self, frame):
        self.frame = frame

    def draw_grid(self):
        self.column_array = self.parameter.get('column_array')
        self.column_zh_CN_array = self.parameter.get('column_zh_CN_array')
        for i in range(0, len(self.column_array)):
            exec('self.'+self.column_array[i]+'_label = tk.Label(self.frame, text="'+self.column_zh_CN_array[i]+'")')
            exec('self.'+self.column_array[i]+'_label.grid(column='+str(i)+', row = 0)')
            exec('self.column_map["' + self.column_array[i] + '"] = str(i)')

    def forget_grid(self):
        self.column_array = self.parameter.get('column_array')
        for i in range(0, len(self.column_array)):
            exec('self.'+self.column_array[i]+'_label.grid_forget()')

    def set_data(self, data):
        for key in self.column_map:
            column = self.column_map.get(key)
            i = 0
            for row_data in [data.get_value(data, key)]:
                if type(row_data) == list:
                    for d in list(row_data):
                        i += 1
                        tk.Label(self.frame, text=d).grid(column=column, row=i)
                else:
                    for d in [row_data]:
                        i += 1
                        tk.Label(self.frame, text=d).grid(column=column, row=i)










