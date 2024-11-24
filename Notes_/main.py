from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import(QApplication, QWidget, QPushButton, QLabel, QHBoxLayout, QTextEdit, QListWidget, QVBoxLayout, QLineEdit, )

import json

app = QApplication([])
window = QWidget()
text_note = QTextEdit()
h_main = QHBoxLayout()
h_main.addWidget(text_note)

v1 = QVBoxLayout()
lbl_notelist = QLabel("список заміток")
list_note = QListWidget()
v1.addWidget(lbl_notelist)
v1.addWidget(list_note)

btn_create = QPushButton("створити замітку")
btn_delete = QPushButton("видалити замітку")
btn_save = QPushButton("зберегти замітку")
h2 = QHBoxLayout()
h2.addWidget(btn_create)
h2.addWidget(btn_delete)
v1.addLayout(h2)
v1.addWidget(btn_save)

lbl_taglist = QLabel("Список тегів")
list_tag = QListWidget()
line_tag = QLineEdit()
line_tag.setPlaceholderText("Введіть тег...")

btn_append = QPushButton("додати до замітки")
btn_clear = QPushButton("відкріпити від замітки")
btn_search = QPushButton("шукати змітки за тегом")
h3 = QHBoxLayout()
h3.addWidget(btn_append)
h3.addWidget(btn_clear)

v1.addWidget(lbl_taglist)
v1.addWidget(list_tag)
v1.addWidget(line_tag)
v1.addLayout(h3)
v1.addWidget(btn_search)

"""замітки в json"""
notes = {
    "ласк просимо!":{
        "текст" : "Це найкращ додаток для заміток у світі", 
        "теги" : ["ласкаво", "інструкція"] 
              }
}
with open("notes_data.json", "w", encoding = "utf-8") as file:
    json.dump(notes, file)

"""функція програми"""
def show_note():
    key = list_note.selectedItems()[0].text()
    print(key)
    text_note.setText(notes[key]["текст"])
    list_tag.clear()
    list_tag.addItems(notes[key]["теги"])

"""запуск програми"""
#підключення обробки подій
list_note.itemClicked.connect(show_note)


with open("notes_data.json", "r") as file:
    notes = json.load(file)
list_note.addItems(notes)




h_main.addLayout(v1)
window.setLayout(h_main)
window.show()
app.exec_()
