from Layout.Grid.summary import *
from Layout.Grid.person_data import *
from Layout.Grid.faction_data import *
from Layout.Grid.military_data import *
from Layout.Grid.architecture_data import *
from Layout.Grid.facility_data import *
from Layout.Grid.treasure_data import *
from Layout.Grid.military_event_data import *
from Layout.Grid.new_person import *
from Layout.Grid.new_title import *


class TypeAdapter:

    def adapt_draw_grid(self, frame, grid_type):
        grid = self.switch(grid_type)
        grid_instance = grid
        grid_instance.set_frame(grid_instance, frame)
        grid_instance.draw_grid(grid_instance)

    def adapt_forget_grid(self, frame, grid_type):
        grid = self.switch(grid_type)
        grid_instance = grid
        grid_instance.set_frame(grid_instance, frame)
        grid_instance.forget_grid(grid_instance)

    def adapt_show_data(self, grid_type, data):
        grid = self.switch(grid_type)
        grid_instance = grid
        grid_instance.set_data(grid_instance, data)

    @staticmethod
    def switch(grid_type):
        type_switcher = {
            'summarize': SummaryGrid,
            'persondata': PersonDataGrid,
            'factiondata': FactionDataGrid,
            'militarydata': MilitaryDataGrid,
            'architecturedata': ArchitectureDataGrid,
            'facilitydata': FacilityDataGrid,
            'treasuredata': TreasureDataGrid,
            'militaryeventdata': MilitaryEventDataGrid,
            'newperson': NewPersonGrid,
            'newtitle': NewTitleGrid,
        }
        return type_switcher.get(grid_type)
