from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QTextBrowser, QCheckBox, QHBoxLayout, QVBoxLayout

from Modules.lineEdit import LineEdit


class MainTab(QWidget):

    def __init__(self, parent=None):
        super().__init__()

        # Starts the program (Youtube-dl)
        self.start_btn = QPushButton('Download')
        # stops the program
        self.stop_btn = QPushButton('Abort')
        # Closes window (also stops the program)
        self.close_btn = QPushButton('Close')

        # Label and lineedit creation. Line edit for acception youtube links as well as paramters.
        self.label = QLabel("Url: ")
        self.lineedit = LineEdit()

        # TextEdit creation, for showing status messages, and the youtube-dl output.
        self.textbrowser = QTextBrowser()

        self.textbrowser.setAcceptRichText(True)
        self.textbrowser.setOpenExternalLinks(True)
        self.textbrowser.setContextMenuPolicy(Qt.NoContextMenu)

        # Adds welcome message on startup.
        self.textbrowser.append('Welcome!\n\nAdd video url, or load from text file.')
        # self.edit.append('<a href="URL">Showtext</a>') Learning purposes.

        # Start making checkbutton for selecting downloading from text file mode.
        self.checkbox = QCheckBox('Download from text file.')

        ## Layout tab 1.

        # Contains, start, abort, close buttons, and a stretch to make buttons stay on the correct side on rezise.
        self.QH = QHBoxLayout()

        self.QH.addStretch(1)
        self.QH.addWidget(self.start_btn)
        self.QH.addWidget(self.stop_btn)
        self.QH.addWidget(self.close_btn)

        # Horizontal layout 2, contains label and LineEdit. LineEdit stretches horizontally by default.
        self.QH2 = QHBoxLayout()

        self.QH2.addWidget(self.label)
        self.QH2.addWidget(self.lineedit)

        # Creates vertical box for tab1.
        self.QV = QVBoxLayout()

        # Adds horizontal layouts, textbrowser and checkbox to create tab1.
        self.QV.addLayout(self.QH2)
        self.QV.addWidget(self.checkbox)
        self.QV.addWidget(self.textbrowser, 1)
        self.QV.addLayout(self.QH)

        self.setLayout(self.QV)