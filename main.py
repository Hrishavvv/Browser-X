import sys
import platform
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QLineEdit, QPushButton, QToolBar,
    QAction, QComboBox, QWidget, QStatusBar, QLabel, QDialog, QListWidget, QDialogButtonBox,
    QTabWidget, QShortcut
)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QKeySequence

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Browser X")
        self.setGeometry(100, 100, 1000, 600)
        self.default_search_engine = "https://www.google.com/search?q="
        self.homepage = self.default_search_engine
        self.dark_mode = False
        self.history = []

        self.tab_widget = QTabWidget()
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.close_tab)
        self.setCentralWidget(self.tab_widget)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        self.search_engine_box = QComboBox()
        self.search_engine_box.addItems(["Google", "Bing", "DuckDuckGo"])
        self.search_engine_box.setCurrentText("Google")
        self.search_engine_box.currentTextChanged.connect(self.set_search_engine)

        self.theme_button = QPushButton("Toggle Theme")
        self.theme_button.clicked.connect(self.toggle_theme)

        self.history_button = QPushButton("History")
        self.history_button.clicked.connect(self.show_history)

        self.burn_button = QPushButton("Burn")
        self.burn_button.clicked.connect(self.clear_history_and_cookies)

        self.new_tab_button = QPushButton("New Tab")
        self.new_tab_button.clicked.connect(self.add_new_tab)

        new_tab_shortcut = QShortcut(QKeySequence("Ctrl+T"), self)
        new_tab_shortcut.activated.connect(self.add_new_tab)

        toolbar = QToolBar()

        back_action = QAction("Back", self)
        back_action.triggered.connect(self.navigate_back)

        forward_action = QAction("Forward", self)
        forward_action.triggered.connect(self.navigate_forward)

        reload_action = QAction("Reload", self)
        reload_action.triggered.connect(self.reload_page)

        home_action = QAction("Home", self)
        home_action.triggered.connect(self.go_home)

        toolbar.addAction(back_action)
        toolbar.addAction(forward_action)
        toolbar.addAction(reload_action)
        toolbar.addAction(home_action)
        toolbar.addWidget(self.url_bar)
        toolbar.addWidget(self.search_engine_box)
        toolbar.addWidget(self.theme_button)
        toolbar.addWidget(self.history_button)
        toolbar.addWidget(self.burn_button)
        toolbar.addWidget(self.new_tab_button)

        self.addToolBar(toolbar)
        self.setStatusBar(QStatusBar())
        self.add_new_tab()
        self.update_theme()
        self.show_title_screen()

    def add_new_tab(self):
        browser = QWebEngineView()
        browser.setUrl(QUrl(self.homepage))
        browser.loadStarted.connect(self.on_loading_started)
        browser.loadFinished.connect(self.on_loading_finished)
        browser.titleChanged.connect(self.update_tab_title)
        index = self.tab_widget.addTab(browser, "New Tab")
        self.tab_widget.setCurrentIndex(index)

    def close_tab(self, index):
        if self.tab_widget.count() > 1:
            self.tab_widget.removeTab(index)
        else:
            self.close()

    def navigate_to_url(self):
        current_tab = self.tab_widget.currentWidget()
        if isinstance(current_tab, QWebEngineView):
            url = self.url_bar.text()
            keyword = url
            if not url.startswith(("http://", "https://")) and "." not in url:
                url = self.default_search_engine + url
            elif not url.startswith(("http://", "https://")):
                url = "http://" + url

            self.history.append((keyword, url))
            current_tab.setUrl(QUrl(url))

    def set_search_engine(self, engine):
        search_engines = {
            "Google": "https://www.google.com/search?q=",
            "Bing": "https://www.bing.com/search?q=",
            "DuckDuckGo": "https://duckduckgo.com/?q="
        }
        self.default_search_engine = search_engines.get(engine, self.default_search_engine)
        self.homepage = self.default_search_engine

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self.update_theme()

    def update_theme(self):
        if self.dark_mode:
            self.setStyleSheet("background-color: #2e2e2e; color: white;")
            self.url_bar.setStyleSheet("background-color: #555555; color: white;")
        else:
            self.setStyleSheet("")
            self.url_bar.setStyleSheet("")

    def navigate_back(self):
        current_tab = self.tab_widget.currentWidget()
        if isinstance(current_tab, QWebEngineView):
            current_tab.back()

    def navigate_forward(self):
        current_tab = self.tab_widget.currentWidget()
        if isinstance(current_tab, QWebEngineView):
            current_tab.forward()

    def reload_page(self):
        current_tab = self.tab_widget.currentWidget()
        if isinstance(current_tab, QWebEngineView):
            current_tab.reload()

    def go_home(self):
        current_tab = self.tab_widget.currentWidget()
        if isinstance(current_tab, QWebEngineView):
            current_tab.setUrl(QUrl(self.homepage))

    def show_title_screen(self):
        self.title_screen = QDialog(self)
        self.title_screen.setWindowTitle("Browser X - Welcome")
        self.title_screen.setGeometry(300, 200, 400, 200)

        layout = QVBoxLayout()
        title_label = QLabel("Browser X", self)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 36px; color: #444444;")

        developer_label = QLabel("Made with QTWebEngine", self)
        developer_label.setAlignment(Qt.AlignCenter)
        developer_label.setStyleSheet("font-size: 18px; color: #888888;")

        python_version_label = QLabel(f"Python {platform.python_version()}", self)
        python_version_label.setAlignment(Qt.AlignCenter)
        python_version_label.setStyleSheet("font-size: 14px; color: #888888;")

        dive_in_button = QPushButton("Dive In", self)
        dive_in_button.clicked.connect(self.launch_browser)

        layout.addWidget(title_label)
        layout.addWidget(developer_label)
        layout.addWidget(python_version_label)
        layout.addWidget(dive_in_button)

        self.title_screen.setLayout(layout)
        self.title_screen.exec_()

    def launch_browser(self):
        self.title_screen.accept()
        self.show()

    def on_loading_started(self):
        self.url_bar.setText("Loading...")

    def on_loading_finished(self):
        current_tab = self.tab_widget.currentWidget()
        if isinstance(current_tab, QWebEngineView):
            current_url = current_tab.url().toString()
            self.url_bar.setText(current_url)
            if current_url not in [url[1] for url in self.history]:
                self.history.append((current_url, current_url))

    def update_tab_title(self, title):
        current_index = self.tab_widget.currentIndex()
        self.tab_widget.setTabText(current_index, title)

    def show_history(self):
        history_dialog = QDialog(self)
        history_dialog.setWindowTitle("History")
        history_dialog.setGeometry(200, 150, 400, 300)

        layout = QVBoxLayout()
        history_list = QListWidget()
        history_list.addItems([keyword for keyword, _ in self.history])

        history_list.itemClicked.connect(self.navigate_from_history)

        close_button = QPushButton("Close")
        close_button.clicked.connect(history_dialog.accept)

        layout.addWidget(history_list)
        layout.addWidget(close_button)

        history_dialog.setLayout(layout)
        history_dialog.exec_()

    def navigate_from_history(self, item):
        keyword = item.text()
        url = next(url for keyword_history, url in self.history if keyword_history == keyword)
        current_tab = self.tab_widget.currentWidget()
        if isinstance(current_tab, QWebEngineView):
            current_tab.setUrl(QUrl(url))
            self.url_bar.setText(url)

    def clear_history_and_cookies(self):
        self.history.clear()
        for i in range(self.tab_widget.count()):
            tab = self.tab_widget.widget(i)
            if isinstance(tab, QWebEngineView):
                tab.page().profile().cookieStore().deleteAllCookies()
                tab.page().profile().clearHttpCache()
        self.show_burn_message()

    def show_burn_message(self):
        burn_message_dialog = QDialog(self)
        burn_message_dialog.setWindowTitle("History and Cookies Cleared")
        burn_message_dialog.setGeometry(300, 200, 300, 150)

        layout = QVBoxLayout()
        burn_message_label = QLabel("All history, cookies, and cache have been cleared.", self)
        burn_message_label.setAlignment(Qt.AlignCenter)

        close_button = QDialogButtonBox(QDialogButtonBox.Ok)
        close_button.clicked.connect(burn_message_dialog.accept)

        layout.addWidget(burn_message_label)
        layout.addWidget(close_button)

        burn_message_dialog.setLayout(layout)
        burn_message_dialog.exec_()

app = QApplication(sys.argv)
browser = Browser()
sys.exit(app.exec_())
