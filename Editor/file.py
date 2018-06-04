import json
import Model.save_data as SaveData
import os
import configparser
from tkinter import filedialog
from Layout.tab_view import *
from Layout import constant
from Editor import edit

tab_view = ShowFrame
save_data = SaveData.SaveDataModel()


class FileView:

    def open_save_data(self):  # 打开存档文件
        root = tk.Tk()
        root.withdraw()
        config = configparser.ConfigParser()
        config.read('Configuration', 'utf-8-sig')
        default_save_path = config.get('defaultPath', 'saveData')
        save_path = os.environ.get('USERPROFILE') + default_save_path
        file_path = filedialog.askopenfilename(title='打开存档文件', filetypes=[('json', '*.json')], initialdir=save_path)
        if not file_path == '':
            file_handler = FileHandler()
            file_handler.analyze_json(file_path)
            summarize_data = file_handler.get_summarize_data()
            tab_view.menu_choose(tab_view, 'summarize', summarize_data)

    def open_scenario_data(self):  # 打开剧本文件
        print("fuck off")

    def save_data(self):  # 保存数据
        print('damn to hell')

    def exit(self):  # 退出
        print('finally...')


class FileHandler:

    def analyze_json(self, path):
        json_file_str = open(path, encoding='utf-8').read()
        result = json.loads(json_file_str)
        save_data.__dict__ = result
        edit.current_save_data=save_data

    def get_summarize_data(self):
        summarize_data = SaveData.SaveDataModel
        for item in constant.summarize_column:
            if item == "PlayerList":
                summarize_data.PlayerList = self.__get_faction_data(save_data.__dict__.get('PlayerList'))
            elif item == "ID":
                exec("summarize_data." + item + " = 1")
            else:
                exec("summarize_data." + item + " = save_data.__dict__.get('" + item + "')")
        return summarize_data

    def __get_faction_data(self, player_list):
        faction_data = save_data.__dict__.get('Factions').get('GameObjects')
        player_zh_CN_list = []
        for player in player_list:
            player_zh_CN = self.__filter_id_func(faction_data, player)
            player_zh_CN_list.append(player_zh_CN)
        return player_zh_CN_list

    def __filter_id_func(self, list, value):
        for element in list:
            if element.get('ID') == value:
                return element.get('Name')



