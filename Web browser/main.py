import sys
import os
import json

from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                            QPushButton, QLabel, QLineEdit, QTabBar,
                            QFrame, QStackedLayout, QTabWidget, QShortcut, QKeySequenceEdit)

from PyQt5.QtGui import QIcon, QWindow, QImage, QKeySequence
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


class AddressBar(QLineEdit):

    def __init__(self):
        super().__init__()

    def mousePressEvent(self, event):
        self.selectAll()


class App(QFrame):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Web Browser by RafaelxFernandes")
        self.setBaseSize(1366, 768)
        self.create_app()


    def create_app(self):
        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)

        # Create tabs
        self.tab_bar = QTabBar(movable=True, tabsClosable=True)
        self.tab_bar.tabCloseRequested.connect(self.close_tab)
        self.tab_bar.tabBarClicked.connect(self.switch_tab)
        self.tab_bar.setDrawBase(False)

        # Keep track of tabs
        self.tab_count = 0
        self.tabs = []

        # Set toolbar buttons
        # Back
        self.back_button = QPushButton("<")
        self.back_button.clicked.connect(self.go_back)

        # Forward
        self.forward_button = QPushButton(">")
        self.forward_button.clicked.connect(self.go_forward)

        # Reload
        self.reload_button = QPushButton("⟲")
        self.reload_button.clicked.connect(self.reload)

        # Create address bar
        self.tool_bar = QWidget()
        self.tool_bar.setObjectName("Toolbar")
        self.tool_bar_layout = QHBoxLayout()
        self.tool_bar.setLayout(self.tool_bar_layout)
        self.address_bar = AddressBar()
        self.address_bar.returnPressed.connect(self.browse_to)

        # New tab button
        self.add_tab_button = QPushButton("+")
        self.add_tab_button.clicked.connect(self.add_tab)

        # Build tool bar
        self.tool_bar_layout.addWidget(self.back_button)
        self.tool_bar_layout.addWidget(self.forward_button)
        self.tool_bar_layout.addWidget(self.reload_button)
        self.tool_bar_layout.addWidget(self.address_bar)
        self.tool_bar_layout.addWidget(self.add_tab_button)

        # Set main view
        self.container = QWidget()
        self.container.layout = QStackedLayout()
        self.container.setLayout(self.container.layout)

        self.layout.addWidget(self.tab_bar)
        self.layout.addWidget(self.tool_bar)
        self.layout.addWidget(self.container)

        # Shortcuts
        # New tab
        self.shortcut_new_tab = QShortcut(QKeySequence("Ctrl+T"), self)
        self.shortcut_new_tab.activated.connect(self.add_tab)

        # Reload
        self.shortcut_reload = QShortcut(QKeySequence("Ctrl+R"), self)
        self.shortcut_reload.activated.connect(self.reload)

        self.setLayout(self.layout)

        self.add_tab()

        self.show()


    def close_tab(self, index):
        # print(index)
        self.tab_bar.removeTab(index)

    
    def add_tab(self):
        index = self.tab_count

        # Set self.tabs<#> = QWidget 
        self.tabs.append(QWidget())
        self.tabs[index].layout = QVBoxLayout()
        self.tabs[index].layout.setContentsMargins(0, 0, 0, 0)
        
        # For tab switching
        self.tabs[index].setObjectName("Tab" + str(index))

        # Create webview within the tabs top level widget
        self.tabs[index].content = QWebEngineView()
        self.tabs[index].content.load(QUrl.fromUserInput("http://google.com"))

        self.tabs[index].content.titleChanged.connect(lambda: self.set_tab_content(index, "title"))
        self.tabs[index].content.iconChanged.connect(lambda: self.set_tab_content(index, "icon"))
        self.tabs[index].content.urlChanged.connect(lambda: self.set_tab_content(index, "url"))

        # Add webview to tab.layout
        self.tabs[index].layout.addWidget(self.tabs[index].content)

        # Set tab_layout to layout
        self.tabs[index].setLayout(self.tabs[index].layout)

        # Add and set new tabs content to stack widget
        self.container.layout.addWidget(self.tabs[index])
        self.container.layout.setCurrentWidget(self.tabs[index])

        # Create tab on tab_bar, representing this tab,
        # Set tab_data to tab<#> so it knows what self.tabs[#] it needs to control
        self.tab_bar.addTab("New Tab")
        self.tab_bar.setTabData(index, {"object": "Tab" + str(index), "initial": index})
        self.tab_bar.setCurrentIndex(index)

        self.tab_count += 1

    
    def switch_tab(self, index):
        if(self.tab_bar.tabData(index)):
            tab_data = self.tab_bar.tabData(index)["object"]
            # print("Tab: " + str(tab_data))
            tab_widget = self.findChild(QWidget, tab_data)

            self.container.layout.setCurrentWidget(tab_widget)

            new_url = tab_widget.content.url().toString()
            self.address_bar.setText(new_url)


    def browse_to(self):
        text = self.address_bar.text()
        
        index = self.tab_bar.currentIndex()
        tab = self.tab_bar.tabData(index)["object"]
        window_view = self.findChild(QWidget, tab).content

        if("http" not in text):
            if("." not in text):
                url = "https://www.google.com/search?q=" + text
            else:
                url = "http://" + text
        else:
            url = text

        window_view.load(QUrl.fromUserInput(url))


    def set_tab_content(self, index, type):
        tab_object_name = self.tabs[index].objectName()

        count = 0
        running = True

        current_tab = self.tab_bar.tabData(self.tab_bar.currentIndex())["object"]
        
        if(current_tab == tab_object_name and type == "url"):
            new_url = self.findChild(QWidget, tab_object_name).content.url().toString()
            self.address_bar.setText(new_url)
            return False             

        while running:
            tab_data_name = self.tab_bar.tabData(count)

            if(count >= 99):
                running = False

            if(tab_object_name == tab_data_name["object"]):
                if(type == "title"):    
                    new_title = self.findChild(QWidget, tab_object_name).content.title()
                    self.tab_bar.setTabText(count, new_title)
                elif(type == "icon"):
                    new_icon = self.findChild(QWidget, tab_object_name).content.icon()
                    self.tab_bar.setTabIcon(count, new_icon)

                running = False
            else:
                count += 1


    def go_back(self):
        activate_index = self.tab_bar.currentIndex()
        tab_name = self.tab_bar.tabData(activate_index)["object"]
        tab_content = self.findChild(QWidget, tab_name).content

        tab_content.back()


    def go_forward(self):
        activate_index = self.tab_bar.currentIndex()
        tab_name = self.tab_bar.tabData(activate_index)["object"]
        tab_content = self.findChild(QWidget, tab_name).content

        tab_content.forward()


    def reload(self):
        activate_index = self.tab_bar.currentIndex()
        tab_name = self.tab_bar.tabData(activate_index)["object"]
        tab_content = self.findChild(QWidget, tab_name).content

        tab_content.reload()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = App()

    with open("style.css", "r") as style:
        app.setStyleSheet(style.read())

    sys.exit(app.exec_())