from tkinter import *
from Editor import file
from Editor import edit
from Editor import new_person
from Editor import new_title
from Layout import tab_view

file_view = file.FileView
edit_view = edit.EditView
new_person_view = new_person.NewPersonView
new_title_view = new_title.NewTitleView

root = Tk()
root.title("Editor")
menu_bar = Menu(root)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='打开存档文件', command=lambda: file_view.open_save_data(file_view))
file_menu.add_command(label='打开剧本文件', command=lambda: file_view.open_scenario_data(file_view))
file_menu.add_command(label='保存数据', command=lambda: file_view.save_data(file_view))
file_menu.add_command(label='退出', command=lambda: file_view.exit(file_view))
menu_bar.add_cascade(label="文件", menu=file_menu)

edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label='编辑人物', command=lambda: edit_view.edit_person(edit_view))
edit_menu.add_command(label='编辑势力', command=lambda: edit_view.edit_faction(edit_view))
edit_menu.add_command(label='编辑部队', command=lambda: edit_view.edit_military(edit_view))
edit_menu.add_command(label='编辑建筑', command=lambda: edit_view.edit_architecture(edit_view))
edit_menu.add_command(label='编辑编队', command=lambda: edit_view.edit_facility(edit_view))
edit_menu.add_command(label='编辑宝物', command=lambda: edit_view.edit_treasure(edit_view))
edit_menu.add_command(label='编辑部队事件', command=lambda: edit_view.edit_military_event(edit_view))
menu_bar.add_cascade(label="编辑", menu=edit_menu)

menu_bar.add_command(label='制作新武将', command=lambda: new_person_view.add_person(new_person_view))

menu_bar.add_command(label='制作新称号', command=lambda: new_title_view.add_title(new_title_view))

tab_view = tab_view.ShowFrame
tab_view.__init__(tab_view, root)

root.config(menu=menu_bar)
root.geometry('800x600')
root.mainloop()
