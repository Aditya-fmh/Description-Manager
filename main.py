import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QComboBox, QMessageBox, QTextEdit
import random

# Sample data - replace with your actual descriptions
descriptions = {
    'Lenovo': {
        'Type 1': ['Description 1 for Lenovo Type 1', 'Description 2 for Lenovo Type 1', 'Description 3 for Lenovo Type 1'],
        'Type 2': ['Description 1 for Lenovo Type 2', 'Description 2 for Lenovo Type 2', 'Description 3 for Lenovo Type 2']
    },
    'DELL': {
        'Type 1': ['Description 1 for DELL Type 1', 'Description 2 for DELL Type 1', 'Description 3 for DELL Type 1'],
        'Type 2': ['Description 1 for DELL Type 2', 'Description 2 for DELL Type 2', 'Description 3 for DELL Type 2']
    },
    'Toshiba': {
        'Type 1': ['Description 1 for Toshiba Type 1', 'Description 2 for Toshiba Type 1', 'Description 3 for Toshiba Type 1'],
        'Type 2': ['Description 1 for Toshiba Type 2', 'Description 2 for Toshiba Type 2', 'Description 3 for Toshiba Type 2']
    }
}

class MarketplaceApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Marketplace Description App')
        self.layout = QVBoxLayout()

        self.brand_combo = QComboBox()
        self.brand_combo.addItems(descriptions.keys())
        self.layout.addWidget(self.brand_combo)

        self.type_combo = QComboBox()
        self.layout.addWidget(self.type_combo)

        self.description_text = QTextEdit()
        self.layout.addWidget(self.description_text)

        self.copy_button = QPushButton('Copy Description')
        self.copy_button.clicked.connect(self.copy_description)
        self.layout.addWidget(self.copy_button)

        self.brand_combo.currentIndexChanged.connect(self.update_types)
        self.update_types()

        self.setLayout(self.layout)

    def update_types(self):
        brand = self.brand_combo.currentText()
        self.type_combo.clear()
        self.type_combo.addItems(descriptions[brand].keys())

    def copy_description(self):
        brand = self.brand_combo.currentText()
        laptop_type = self.type_combo.currentText()
        descriptions_list = descriptions[brand][laptop_type]
        description = random.choice(descriptions_list)
        self.description_text.setPlainText(description)
        QApplication.clipboard().setText(description)
        QMessageBox.information(self, 'Description Copied', 'Description copied to clipboard.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MarketplaceApp()
    window.show()
    sys.exit(app.exec_())