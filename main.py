import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QComboBox, QMessageBox, QTextEdit
import random

# Sample data - replace with your actual descriptions
descriptions = {
    'Lenovo': {
        'L450': ['Laptop Lenovo L450 3 Jutaan mulus no minus ada Garansi\n\nCore i5-5300U (Gen 5)\nRAM 4 GB DDR3\nSSD 128 GB\nLCD 14"\n\nBisa COD Sekitaran Garut\nUntuk luar kota Rekber via Tokped dan Shopee\nBisa kredit lewat akulaku dan shopee paylater\n\nKontak: 088221957963 (Adit)', 'Dijual laptop seken Lenovo L450 kondisi mulus no minus, siap jajap sekitaran garut.\nGaransi 1 bulan, aplikasi lengkap siap pakai. Bisa rekber lewat tokped dan shopee.\nBisa kredit lewat akulaku dan spaylater.\n\nMinat inbox atau WA 088221957963 (Aditya)', '#WTS\n#Jual\n\nLaptop seken Lenovo ThinkPad L450 \n\nSpek:\nIntel Core i5 Gen 5\nRAM 4 GB\nSSD 128 GB\nLayar 14 inci\nWindows 10\n\nKelengkapan:\nGaransi\nMouse\nAplikasi\nDus\nCharger\n\nMenerima COD untuk sekitaran Garut\nUntuk luar garut bisa rekber lewat tokopedia dan shopee.\n\nMinat inbox atau hub WA di 088221957963 (Adit)\n\nBisa juga kredit lewat akulaku dan shopee'],
        'L460': ['#WTS\n#ForSale\n\nLaptop Lenovo ThinkPad L460 Seken\n\nSpek:\nIntel Core i5 Gen 6\nRAM 8 GB DDR3\nSSD 256 GB\nLayar 14"\n\nGaransi laptop 1 bulan, aplikasi lengkap siap pakai\nMenerima COD sekitaran Garut, untuk luar Garut bisa rekber via Tokopedia dan Shopee\nMenerima kredit via Akulaku dan SPaylater\n\nMinat inbox atau WA 088221957963 (Adit)', 'Description 2 for Lenovo Type 2', 'Description 3 for Lenovo Type 2'],
        'L490 8 GB': ['Description 1 for Lenovo Type 2', 'Description 2 for Lenovo Type 2', 'Description 3 for Lenovo Type 2'],
        'L490 16 GB': ['Description 1 for Lenovo Type 2', 'Description 2 for Lenovo Type 2', 'Description 3 for Lenovo Type 2'],
        'T420': ['Description 1 for Lenovo Type 2', 'Description 2 for Lenovo Type 2', 'Description 3 for Lenovo Type 2'],
        'T450': ['Description 1 for Lenovo Type 2', 'Description 2 for Lenovo Type 2', 'Description 3 for Lenovo Type 2'],
        'T460s 8 GB': ['Description 1 for Lenovo Type 2', 'Description 2 for Lenovo Type 2', 'Description 3 for Lenovo Type 2'],
        'T460s 16 GB': ['Description 1 for Lenovo Type 2', 'Description 2 for Lenovo Type 2', 'Description 3 for Lenovo Type 2'],
        'T470': ['Description 1 for Lenovo Type 2', 'Description 2 for Lenovo Type 2', 'Description 3 for Lenovo Type 2'],
        'T470s 8 GB': ['Description 1 for Lenovo Type 2', 'Description 2 for Lenovo Type 2', 'Description 3 for Lenovo Type 2'],
        'T470s 12 GB': ['Description 1 for Lenovo Type 2', 'Description 2 for Lenovo Type 2', 'Description 3 for Lenovo Type 2'],
        'T470s 20 GB': ['Description 1 for Lenovo Type 2', 'Description 2 for Lenovo Type 2', 'Description 3 for Lenovo Type 2'],
        'X240 HDD': ['Description 1 for Lenovo Type 2', 'Description 2 for Lenovo Type 2', 'Description 3 for Lenovo Type 2'],
        'X240 SSD': ['Description 1 for Lenovo Type 2', 'Description 2 for Lenovo Type 2', 'Description 3 for Lenovo Type 2'],
        'X250 RAM 4 GB HDD 500': ['Description 1 for Lenovo Type 2', 'Description 2 for Lenovo Type 2', 'Description 3 for Lenovo Type 2'],
        'X250 RAM 8 GB HDD 500': ['Description 1 for Lenovo Type 2', 'Description 2 for Lenovo Type 2', 'Description 3 for Lenovo Type 2'],
        'X250 RAM 8 GB SSD 256': ['Description 1 for Lenovo Type 2', 'Description 2 for Lenovo Type 2', 'Description 3 for Lenovo Type 2'],
        'X250 RAM 8 GB SSD 512': ['Description 1 for Lenovo Type 2', 'Description 2 for Lenovo Type 2', 'Description 3 for Lenovo Type 2'],
        'X280': ['Description 1 for Lenovo Type 2', 'Description 2 for Lenovo Type 2', 'Description 3 for Lenovo Type 2']
    },
    'DELL': {
        '5490': ['Description 1 for DELL Type 1', 'Description 2 for DELL Type 1', 'Description 3 for DELL Type 1'],
        'E7470': ['Description 1 for DELL Type 2', 'Description 2 for DELL Type 2', 'Description 3 for DELL Type 2']
    },
    'Toshiba': {
        'B553': ['Description 1 for Toshiba Type 1', 'Description 2 for Toshiba Type 1', 'Description 3 for Toshiba Type 1'],
        'R73': ['Description 1 for Toshiba Type 2', 'Description 2 for Toshiba Type 2', 'Description 3 for Toshiba Type 2'],
        'R734': ['Description 1 for Lenovo Type 2', 'Description 2 for Lenovo Type 2', 'Description 3 for Lenovo Type 2']
    },
    'General': {
        'General': ['Description 1 for Toshiba Type 1', 'Description 2 for Toshiba Type 1', 'Description 3 for Toshiba Type 1']
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
