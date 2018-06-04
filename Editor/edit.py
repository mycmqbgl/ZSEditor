from Layout.tab_view import *
from Layout import constant
from Model import person_data as PersonData
from Model import faction_data as FactionData

tab_view = ShowFrame
current_save_data = ""


class EditView:

    def edit_person(self):  # 编辑人物
        tab_view.menu_choose(tab_view,
                             'persondata',
                             data=EditHandler.get_data(
                                 self,
                                 PersonData.PersonDataModel,
                                 constant.person_column,
                                 "Persons"
                                )
                             )

    def edit_faction(self):  # 编辑势力
        tab_view.menu_choose(tab_view,
                             'factiondata',
                             data=EditHandler.get_data(
                                 self,
                                 FactionData.FactionDataModel,
                                 constant.faction_column,
                                 "Factions"
                                )
                             )

    def edit_military(self):  # 编辑部队
        tab_view.menu_choose(tab_view, 'militarydata')

    def edit_architecture(self):  # 编辑建筑
        tab_view.menu_choose(tab_view, 'architecturedata')

    def edit_facility(self):  # 编辑编队
        tab_view.menu_choose(tab_view, 'facilitydata')

    def edit_treasure(self):  # 编辑宝物
        tab_view.menu_choose(tab_view, 'treasuredata')

    def edit_military_event(self):  # 编辑部队事件
        tab_view.menu_choose(tab_view, 'militaryeventdata')


class EditHandler:

    def get_data(self, data_model, constant_column, data_name):
        data = data_model
        GameObjects = current_save_data.__dict__.get(data_name).get('GameObjects')
        for item in constant_column:
            if item == "ArchitecturesString":
                exec("data." + item + " = [len(game_object.get('" + item + "')) for game_object in GameObjects]")
            else:
                exec("data." + item + " = [game_object.get('" + item + "') for game_object in GameObjects]")
        return data

""" sample , don't delete 
def get_faction_data(self):
    faction_data = FactionData.FactionDataModel
    GameObjects = current_save_data.__dict__.get("Factions").get('GameObjects')
    for item in constant.faction_column:
        if item == "ArchitecturesString":
            exec("faction_data." + item + " = [len(game_object.get('" + item + "')) for game_object in GameObjects]")
        else:
            exec("faction_data." + item + " = [game_object.get('" + item + "') for game_object in GameObjects]")
    return faction_data"""
