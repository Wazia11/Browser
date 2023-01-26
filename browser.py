import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow, QPushButton, QVBoxLayout, QWidget, QToolBar, QTabWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView 
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont





class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        app.setStyleSheet(open("style.css").read())


        

       
        self.setWindowFlag(Qt.FramelessWindowHint)
        icon = QIcon("ikon.png")
        self.setWindowIcon(icon)
        self.setWindowTitle("Webstroke")
        self.view = QWebEngineView(self)

        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)
        font = QFont("Arial", 9)
        app.setFont(font)
       
        self.url_bar = QLineEdit(self)
        self.url_bar.setPlaceholderText("Enter URL here...")

        self.view = QWebEngineView(self)
        self.view.setUrl(QUrl("https://www.google.com"))
        self.view.loadFinished.connect(self.update_urlbar)

        self.navigate_btn = QPushButton("Go", self)
        self.navigate_btn.clicked.connect(self.navigate_to_url)
        self.navigate_btn.setObjectName("navigate-dssbutton")

        self.back_btn = QPushButton("<", self)
        self.back_btn.setObjectName("navigateButton")
        self.back_btn.clicked.connect(self.view.back)

        self.forward_btn = QPushButton(">", self)
        self.forward_btn.setStyleSheet(".button2 { display: inline-block;transition: all 0.2s ease-in;position: relative;overflow: hidden;z-index: 1;color: #090909;padding: 0.7em 1.7em;font-size: 18px;border-radius: 0.5em;background: #e8e8e8;border: 1px solid #e8e8e8;box-shadow: 6px 6px 12px #c5c5c5,-6px -6px 12px #ffffff;}.button2:active {color: #666;box-shadow: inset 4px 4px 12px #c5c5c5,inset -4px -4px 12px #ffffff;}.button2:before {content: "";position: absolute;left: 50%;transform: translateX(-50%) scaleY(1) scaleX(1.25);top: 100%;width: 140%;height: 180%;background-color: rgba(0, 0, 0, 0.05);border-radius: 50%;display: block;transition: all 0.5s 0.1s cubic-bezier(0.55, 0, 0.1, 1);z-index: -1;}.button2:after {content: ""; position: absolute;left: 55%;transform: translateX(-50%) scaleY(1) scaleX(1.45);top: 180%;width: 160%;height: 190%;background-color: #009087;border-radius: 50%;display: block;transition: all 0.5s 0.1s cubic-bezier(0.55, 0, 0.1, 1);z-index: -1;}.button2:hover {color: #ffffff;border: 1px solid #009087;}.button2:hover:before {top: -35%;")
        self.forward_btn.clicked.connect(self.view.forward)

        self.reload_btn = QPushButton("F5", self)
        self.reload_btn.setStyleSheet(".button2 { display: inline-block;transition: all 0.2s ease-in;position: relative;overflow: hidden;z-index: 1;color: #090909;padding: 0.7em 1.7em;font-size: 18px;border-radius: 0.5em;background: #e8e8e8;border: 1px solid #e8e8e8;box-shadow: 6px 6px 12px #c5c5c5,-6px -6px 12px #ffffff;}.button2:active {color: #666;box-shadow: inset 4px 4px 12px #c5c5c5,inset -4px -4px 12px #ffffff;}.button2:before {content: "";position: absolute;left: 50%;transform: translateX(-50%) scaleY(1) scaleX(1.25);top: 100%;width: 140%;height: 180%;background-color: rgba(0, 0, 0, 0.05);border-radius: 50%;display: block;transition: all 0.5s 0.1s cubic-bezier(0.55, 0, 0.1, 1);z-index: -1;}.button2:after {content: ""; position: absolute;left: 55%;transform: translateX(-50%) scaleY(1) scaleX(1.45);top: 180%;width: 160%;height: 190%;background-color: #009087;border-radius: 50%;display: block;transition: all 0.5s 0.1s cubic-bezier(0.55, 0, 0.1, 1);z-index: -1;}.button2:hover {color: #ffffff;border: 1px solid #009087;}.button2:hover:before {top: -35%;")
        self.reload_btn.clicked.connect(self.view.reload)

       

        toolbar = QToolBar(self)
        self.setObjectName("QToolBar")
        toolbar.addWidget(self.back_btn)
        toolbar.addWidget(self.forward_btn)
        toolbar.addWidget(self.reload_btn)
       
        self.new_tab_btn = QPushButton("New Tab", self)
        self.new_tab_btn.setStyleSheet("QPushButton { background-color: #0000FF; margin: 10px; color: white; border: 1px solid #0000FF; border-radius: 3px; padding: 3px; text-align: center; box-shadow: 2px 2px 2px #888888; } QPushButton:pressed { background-color: #0000CC; border: 1px solid #0000CC; }")

        toolbar.addWidget(self.new_tab_btn)
        toolbar.addSeparator()
        self.minimize_btn = QPushButton("-", self)
        self.minimize_btn.setStyleSheet("QPushButton { background-color: #0000FF; margin: 10px; color: white; border: 1px solid #0000FF; border-radius: 3px; padding: 3px; text-align: center; box-shadow: 2px 2px 2px #888888; } QPushButton:pressed { background-color: #0000CC; border: 1px solid #0000CC; }")
        self.minimize_btn.clicked.connect(self.showMinimized)
        toolbar.addWidget(self.minimize_btn)
        self.maximize_btn = QPushButton("[]", self)
        self.maximize_btn.setStyleSheet("QPushButton { background-color: #0000FF; margin: 10px; color: white; border: 1px solid #0000FF; border-radius: 3px; padding: 3px; text-align: center; box-shadow: 2px 2px 2px #888888; } QPushButton:pressed { background-color: #0000CC; border: 1px solid #0000CC; }")
        self.maximize_btn.clicked.connect(self.showMaximized)
        toolbar.addWidget(self.maximize_btn)
        self.close_btn = QPushButton("X", self)
        self.close_btn.setStyleSheet("QPushButton { float: right; }QPushButton { background-color: #0000FF; margin: 10px; color: white; border: 1px solid #0000FF; border-radius: 3px; padding: 3px; text-align: center; box-shadow: 2px 2px 2px #888888; } QPushButton:pressed { background-color: #0000CC; border: 1px solid #0000CC; }")
        self.close_btn.clicked.connect(self.close)
        toolbar.addWidget(self.close_btn)
        self.tabs = []
        self.tabs.append(self.view)
        self.current_tab_index = 0
        self.tab_btns = []
        self.new_tab_btn.clicked.connect(self.open_new_tab)
        self.addToolBar(toolbar)

        layout = QVBoxLayout() 
        layout.addWidget(self.url_bar)
        layout.addWidget(self.view)
        layout.addWidget(self.navigate_btn)

        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.show()
 
    def navigate_to_url(self):
        url = QUrl(self.url_bar.text())
        self.view.load(url)
        self.view.setFocus()

    def create_new_tab(self):
        new_view = QWebEngineView(self)
        new_view.setUrl(QUrl("https://www.google.com"))
        self.tab_widget.addTab(new_view, "New Tab")
        self.tab_widget.setCurrentWidget(new_view)

    def open_new_tab(self):
        new_tab = QWebEngineView()
        new_tab.setUrl(QUrl("https://www.google.com"))
        if self.tab_widget:
            self.tab_widget.addTab(new_tab, "New Tab")
        else:
            print("Tab widget has been deleted.")

    def update_urlbar(self, q):
        if q:
            self.url_bar.setText(self.view.url().toString())
            self.url_bar.setCursorPosition(0)

    def switch_tab(self, new_view):
        self.view.setVisible(False)
        self.view = new_view
        self.view.setVisible(True)

    def close_tab(self):
        current_index = self.tabs.index(self.view)
        self.tabs.remove(self.view)
        self.tab_btns[current_index].deleteLater()
        self.tab_btns.remove(self.tab_btns[current_index])
        if self.tabs:
            self.switch_tab(self.tabs[-1])
        else:
            self.close()

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec_())

