import sys
from PyQt5.QtWidgets import  QApplication, QApplication, QMainWindow, QTextEdit, QStackedWidget, QGraphicsDropShadowEffect, QWidget, QLineEdit, QGridLayout, QVBoxLayout, QHBoxLayout, QPushButton, QFrame, QLabel, QSizePolicy
from PyQt5.QtGui import QIcon, QPainter, QMovie, QColor, QTextCharFormat, QFont, QPixmap, QTextBlockFormat
from PyQt5.QtCore import Qt, QSize, QTimer
from PyQt5 import QtCore
from .Manager import *
import subprocess
import textwrap

User_Name, User_Assistant_name, User_ApiKey, User_Email, User_Mobile = Read_data_from_database()
database_setup_if_none_is_history(User_Name, User_Assistant_name)
chatlog_setup_if_none_is_history(User_Name, User_Assistant_name)
database_manager()
show_chat_log_on_gui()
old_chat_message = ""

def SetValue(Data):
    with open("Backend//Mic.status", "w", encoding='utf-8') as file:
        file.write(Data)

def ButtonClickerOn():
    SetValue("False")

def ButtonClickerOff():
    SetValue("True")

def TextToSpeech(text):
    if text==None:
        return
    
    chunk_size = 1000
    chunks = textwrap.wrap(text, width=chunk_size)
    for chunk in chunks:
        command = ['say', chunk]
        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
        
class ChatSection(QWidget):

    def __init__(self):
        super(ChatSection, self).__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(-10, 40, 40, 100)
        layout.setSpacing(-100)
        self.chat_text_edit = QTextEdit()
        self.chat_text_edit.setReadOnly(True)
        self.chat_text_edit.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.chat_text_edit.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.chat_text_edit.setFrameStyle(QFrame.NoFrame)
        layout.addWidget(self.chat_text_edit)
        self.setStyleSheet("background-color: black;")
        layout.setSizeConstraint(QVBoxLayout.SetDefaultConstraint)
        layout.setStretch(1, 1)
        self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.chat_text_edit.setFocusPolicy(Qt.WheelFocus)
        text_color = QColor(Qt.blue)
        text_color_text = QTextCharFormat()
        text_color_text.setForeground(text_color)
        self.chat_text_edit.setCurrentCharFormat(text_color_text)
        self.gif_label = QLabel()
        self.gif_label.setStyleSheet("border: none;")
        movie = QMovie('Frontend//gif.gif')
        max_gif_size_W = 480
        max_gif_size_H = 270
        movie.setScaledSize(QSize(max_gif_size_W, max_gif_size_H))
        self.gif_label.setAlignment(Qt.AlignRight | Qt.AlignBottom)
        self.gif_label.setMovie(movie)
        movie.start()
        self.label = QLabel("Listening...")
        self.label.setStyleSheet("color: white; font-size:16px ; margin-right:191px;  border: none; margin-top: -30px;")
        self.label.setAlignment(Qt.AlignRight)
        layout.addWidget(self.label)
        layout.setSpacing(-10)
        layout.addWidget(self.gif_label)
        font = QFont()
        font.setPointSize(13)
        self.chat_text_edit.setFont(font)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.loadMessages)
        self.timer.timeout.connect(self.SpeechRecogText)
        self.timer.start(5)
        self.chat_text_edit.viewport().installEventFilter(self)

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.MouseButtonPress:
            return True
        return super().eventFilter(obj, event)

    def loadMessages(self):
        global old_chat_message
        with open("Backend//Response.data", "r", encoding='utf-8') as file:
            messages = file.read()

            if None==messages:
                pass

            elif len(messages)<=1:
                pass

            elif str(old_chat_message)==str(messages):
                pass

            else:
                self.addMessage(message=messages,color='White')
                old_chat_message = messages

    def SpeechRecogText(self):
        with open("Backend//Status.data", "r", encoding='utf-8') as file:
            messages = file.read()
            self.label.setText(messages)

    def addMessage(self, message, color):
        cursor = self.chat_text_edit.textCursor()
        format = QTextCharFormat()
        formatm = QTextBlockFormat()
        formatm.setTopMargin(10)
        formatm.setLeftMargin(10)
        format.setForeground(QColor(color))
        cursor.setCharFormat(format)
        cursor.setBlockFormat(formatm)
        cursor.insertText(message + "\n")
        self.chat_text_edit.setTextCursor(cursor)

class InitialScreen(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        desktop = QApplication.desktop()
        screen_width = desktop.screenGeometry().width()
        screen_height = desktop.screenGeometry().height()
        content_layout = QVBoxLayout()
        content_layout.setContentsMargins(0, 0, 0, 0)
        gif_label = QLabel()
        movie = QMovie("Frontend//gif.gif")
        gif_label.setMovie(movie)
        max_gif_size_H = int(screen_width / 16 * 9)
        movie.setScaledSize(QSize(screen_width, max_gif_size_H))
        gif_label.setAlignment(Qt.AlignCenter)
        movie.start()
        gif_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.icon_label = QLabel()
        pixmap = QPixmap("Frontend//voice_icon.png")
        new_pixmap = pixmap.scaled(60, 60)
        self.icon_label.setPixmap(new_pixmap)
        self.icon_label.setFixedSize(150,150)
        self.icon_label.setAlignment(Qt.AlignCenter)
        self.toggled = True
        self.toggle_icon()
        self.icon_label.mousePressEvent = self.toggle_icon
        self.label = QLabel("Listening...")
        self.label.setStyleSheet("color: white; font-size:16px ; margin-bottom:0;")
        content_layout.addWidget(gif_label, alignment=Qt.AlignCenter)
        content_layout.addWidget(self.label, alignment=Qt.AlignCenter)
        content_layout.addWidget(self.icon_label, alignment=Qt.AlignCenter)
        content_layout.setContentsMargins(0, 0, 0, 150)
        self.setLayout(content_layout)
        self.setFixedHeight(screen_height)
        self.setFixedWidth(screen_width)
        self.setStyleSheet("background-color: black;") 
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.SpeechRecogText)
        self.timer.start(5)

    def SpeechRecogText(self):
        with open("Backend//Status.data", "r", encoding='utf-8') as file:
            messages = file.read()
            self.label.setText(messages)
        
    def load_icon(self, path, width=60, height=60):
        pixmap = QPixmap(path)
        new_pixmap = pixmap.scaled(width, height)  # Resize the pixmap
        self.icon_label.setPixmap(new_pixmap)

    def toggle_icon(self, event=None):
        if self.toggled:
            self.load_icon("Frontend//voice_icon.png", 60, 60)
            ButtonClickerOn()

        else:
            self.load_icon("Frontend//rec_icon.png", 60, 60)
            ButtonClickerOff()

        self.toggled = not self.toggled
    
class MessageScreen(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        desktop = QApplication.desktop()
        screen_width = desktop.screenGeometry().width()
        screen_height = desktop.screenGeometry().height()
        layout = QVBoxLayout()
        label = QLabel("")
        layout.addWidget(label)
        chat_section = ChatSection()
        layout.addWidget(chat_section)
        self.setLayout(layout)
        self.setStyleSheet("background-color: black;")
        self.setFixedHeight(screen_height)
        self.setFixedWidth(screen_width)

class SettingScreen(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        layout = QGridLayout(self)
        layout.setContentsMargins(50, 50, 50, 50)
        layout.setHorizontalSpacing(10)  
        labels = ["Your Name: ", "Your AI Assistant Name: ", "Your OpenAI API Key: ", "Your Email: ", "Your Contact Number: "]
        self.inputs = []

        for row, label_text in enumerate(labels):
            label = QLabel(label_text)
            label.setStyleSheet("color: white; font-size: 16px;")
            input_field = QLineEdit()
            input_field.setStyleSheet("color: white; height: 30px; font-size: 15px; background-color: black; border: 1px solid white; border-radius: 5px; padding: 5px;")
            shadow = QGraphicsDropShadowEffect()
            shadow.setColor(QColor(255, 255, 255, 50))
            shadow.setBlurRadius(20)
            input_field.setGraphicsEffect(shadow)
            layout.addWidget(label, row, 0)
            layout.addWidget(input_field, row, 1)
            empty_label = QLabel("")
            layout.addWidget(empty_label, row, 2)
            empty_label2 = QLabel("")
            layout.addWidget(empty_label2, row, 3)
            self.inputs.append(input_field)

        submit_button = QPushButton("Submit")
        submit_button.setStyleSheet("""
        QPushButton {
            background-color: black;
            color: white;
            font-size: 18px;
            height: 40px;
            text-align: center;
            border: 2px solid white;
            border-radius: 10px;
        }
        QPushButton:hover {
            background-color: gray;
        }""")
        submit_button.clicked.connect(self.submitForm)
        submit_button.setFixedWidth(100)
        button_layout = QHBoxLayout()
        button_layout.addStretch(1)
        button_layout.addWidget(submit_button)
        button_layout.addStretch(1)
        layout.addLayout(button_layout, len(labels), 1)
        
    def submitForm(self):
        user_name_value = self.inputs[0].text()
        assistant_name_value = self.inputs[1].text()
        api_key_value = self.inputs[2].text()
        email_value = self.inputs[3].text()
        contact_number_value = self.inputs[4].text()
        database_updater_after_saving_the_data_from_gui(user_name_value, assistant_name_value)
        chat_log_updater_after_saving_the_data_from_gui(user_name_value, assistant_name_value)
        Update_data_of_database(user_name_value, assistant_name_value, api_key_value, email_value, contact_number_value)
        TextToSpeech("Please Restart The Program")

class CustomTopBar(QWidget):
    
    def __init__(self, parent, stacked_widget):
        super().__init__(parent)
        self.initUI()
        self.current_screen = None  # Track the current screen
        self.stacked_widget = stacked_widget

    def initUI(self):
        self.setFixedHeight(50)  # Set the height of the custom title bar
        layout = QHBoxLayout(self)
        layout.setAlignment(Qt.AlignRight)
        home_button = QPushButton()
        home_icon = QIcon('Frontend//home_icon.png')  # Replace with your profile icon image file
        home_button.setIcon(home_icon)
        home_button.setText("  Home")  # Add text next to the icon
        home_button.setStyleSheet("height:40px; line-height:40px ; background-color:white ; color: black")
        message_button = QPushButton()
        message_icon = QIcon('Frontend//message_icon.png')  # Replace with your profile icon image file
        message_button.setIcon(message_icon)
        message_button.setText("  Chat")  # Add text next to the icon
        message_button.setStyleSheet("height:40px; line-height:40px; background-color:white ; color: black")
        setting_button = QPushButton()
        setting_icon = QIcon('Frontend//setting_icon.png')  # Replace with your profile icon image file
        setting_button.setIcon(setting_icon)
        setting_button.setText("  Settings")  # Add text next to the icon
        setting_button.setStyleSheet("height:40px; line-height:40px; background-color:white ; color: black")
        minimize_button = QPushButton()
        minimize_icon = QIcon('Frontend//minimize.png')  # Replace with your minimize icon image file
        minimize_button.setIcon(minimize_icon)
        minimize_button.setStyleSheet("background-color:white")
        minimize_button.clicked.connect(self.minimizeWindow)
        self.maximize_button = QPushButton()
        self.maximize_icon = QIcon('Frontend//maximize_icon.png')
        self.restore_icon = QIcon('Frontend//minimize_icon.png')
        self.maximize_button.setIcon(self.maximize_icon)
        self.maximize_button.setFlat(True)
        self.maximize_button.setStyleSheet("background-color:white")
        self.maximize_button.clicked.connect(self.maximizeWindow)
        close_button = QPushButton()
        close_icon = QIcon('Frontend//close_icon.png')  # Replace with your close icon image file
        close_button.setIcon(close_icon)
        close_button.setStyleSheet("background-color:white")
        close_button.clicked.connect(self.closeWindow)
        line_frame = QFrame()
        line_frame.setFixedHeight(1)  # Set the height of the bottom line
        line_frame.setFrameShape(QFrame.HLine)
        line_frame.setFrameShadow(QFrame.Sunken)
        line_frame.setStyleSheet("border-color: black;")  # Set line color
        title_label = QLabel(f" {str(User_Assistant_name).capitalize()} AI")  # Replace with your desired title text
        title_label.setStyleSheet("color: black; font-size: 18px;; background-color:white")  # Customize the title label's style
        home_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        message_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        setting_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))
        layout.addWidget(title_label)
        layout.addStretch(1)
        layout.addWidget(home_button)
        layout.addWidget(message_button)
        layout.addWidget(setting_button)
        layout.addStretch(1)
        layout.addWidget(minimize_button)
        layout.addWidget(self.maximize_button)  # Add the maximize button
        layout.addWidget(close_button)
        layout.addWidget(line_frame)
        self.draggable = True
        self.offset = None

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), Qt.white)  # Set the background color to white
        super().paintEvent(event)

    def minimizeWindow(self):
        self.parent().showMinimized()

    def maximizeWindow(self):
        if self.parent().isMaximized():
            self.parent().showNormal()
            self.maximize_button.setIcon(self.maximize_icon)  # Set the maximize icon
        else:
            self.parent().showMaximized()
            self.maximize_button.setIcon(self.restore_icon)

    def closeWindow(self):
        self.parent().close()

    def mousePressEvent(self, event):
        if self.draggable:
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if self.draggable and self.offset:
            new_pos = event.globalPos() - self.offset
            self.parent().move(new_pos)

    def showMessageScreen(self):
        if self.current_screen is not None:
            self.current_screen.hide()  # Hide the current screen

        message_screen = MessageScreen(self)
        layout = self.parent().layout()
        if layout is not None:
            layout.addWidget(message_screen)
        self.current_screen = message_screen

    def showSettingScreen(self):
        if self.current_screen is not None:
            self.current_screen.hide()  # Hide the current screen

        setting_screen = SettingScreen(self)
        layout = self.parent().layout()
        if layout is not None:
            layout.addWidget(setting_screen)
        self.current_screen = setting_screen

    def showInitialScreen(self):
        if self.current_screen is not None:
            self.current_screen.hide()  # Hide the current screen

        initial_screen = InitialScreen(self)
        layout = self.parent().layout()
        if layout is not None:
            layout.addWidget(initial_screen)
        self.current_screen = initial_screen

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.initUI()
        
    def initUI(self):
        desktop = QApplication.desktop()
        screen_width = desktop.screenGeometry().width()
        screen_height = desktop.screenGeometry().height()
        stacked_widget = QStackedWidget(self)
        initial_screen = InitialScreen()
        message_screen = MessageScreen()
        setting_screen = SettingScreen()
        stacked_widget.addWidget(initial_screen)
        stacked_widget.addWidget(message_screen)
        stacked_widget.addWidget(setting_screen)
        self.setGeometry(0, 0, screen_width, screen_height)
        self.setStyleSheet("background-color: black;")
        top_bar = CustomTopBar(self, stacked_widget)
        self.setMenuWidget(top_bar)
        self.setCentralWidget(stacked_widget)

def GraphicalUserInterface():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    GraphicalUserInterface()

