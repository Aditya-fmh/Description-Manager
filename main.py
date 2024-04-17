import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QComboBox, QMessageBox, QTextEdit
import random

# Sample data - replace with your actual descriptions
descriptions = {
    'Lenovo': {
        'L450': ['Laptop Lenovo L450 3 Jutaan mulus no minus ada Garansi\n\nCore i5-5300U (Gen 5)\nRAM 4 GB DDR3\nSSD 128 GB\nLCD 14"\n\nBisa COD Sekitaran Garut\nUntuk luar kota Rekber via Tokped dan Shopee\nBisa kredit lewat akulaku dan shopee paylater\n\nKontak: 088221957963 (Adit)', 'Dijual laptop seken Lenovo L450 kondisi mulus no minus, siap jajap sekitaran garut.\nGaransi 1 bulan, aplikasi lengkap siap pakai. Bisa rekber lewat tokped dan shopee.\nBisa kredit lewat akulaku dan spaylater.\n\nMinat inbox atau WA 088221957963 (Aditya)', '#WTS\n#Jual\n\nLaptop seken Lenovo ThinkPad L450 \n\nSpek:\nIntel Core i5 Gen 5\nRAM 4 GB\nSSD 128 GB\nLayar 14 inci\nWindows 10\n\nKelengkapan:\nGaransi\nMouse\nAplikasi\nDus\nCharger\n\nMenerima COD untuk sekitaran Garut\nUntuk luar garut bisa rekber lewat tokopedia dan shopee.\n\nMinat inbox atau hub WA di 088221957963 (Adit)\n\nBisa juga kredit lewat akulaku dan shopee'],
        'L460': ['#WTS\n#ForSale\n\nLaptop Lenovo ThinkPad L460 Seken\n\nSpek:\nIntel Core i5 Gen 6\nRAM 8 GB DDR3\nSSD 256 GB\nLayar 14"\n\nGaransi laptop 1 bulan, aplikasi lengkap siap pakai\nMenerima COD sekitaran Garut, untuk luar Garut bisa rekber via Tokopedia dan Shopee\nMenerima kredit via Akulaku dan SPaylater\n\nMinat inbox atau WA 088221957963 (Adit)', 'Dijual laptop Lenovo L460 seken ex-kantor 3 jutaan mulusn no minus, ada garansi. Laptop fullset + dus dan mouse\nBisa COD sekitaran garut, untuk luar garut bisa rekber lewat shopee dan tokopedia.\nUntuk yang mau kredit bisa lewat aplikasi akulaku dan shopee paylater.\n\nInfo lebih lanjut hubungi 088221957963 (Aditya)', 'Bismillah\n\nJual laptop lenovo bekas kantoran tipe ThinkPad L460 masih mulus no minus.\n\nSpesifikasi: Intel Core i5 Gen 6, RAM 8, SSD 256, LCD 14"\n\nSudah pakai windows 10, aplikasi lengkap siap pakai\nMenerima COD untuk sekitaran garut\nRekber? Tokopedia dan Shopee\nKredit? Akulaku dan Spaylater\n\nMinat hub WA 088221957963 (Adit)'],
        'L490 8 GB': ['#JUAL\n#WTS\nCp 088221957963 (Adit)\n\nLaptop Lenovo L490 second kantoran, kondisi barang mulus\n\nSpesifikasi\nIntel Core i5 Gen 8\nRAM 8GB DDR4\nSSD 256GB M.2 NVME\nLCD 14"\nWindows 11 Pro 23H2\nAplikasi standar lengkap siap pakai\n\nKelengkapan:\nLaptop\nCharger\nDus\nMouse\nGaransi service 1 bulan\nGaransi software 3 bulan', 'Description 2 for Lenovo Type 2', 'Description 3 for Lenovo Type 2'],
        'L490 16 GB': ['Description 1 for Lenovo Type 2', 'Description 2 for Lenovo Type 2', 'Description 3 for Lenovo Type 2'],
        'T420': ['Description 1 for Lenovo Type 2', 'Description 2 for Lenovo Type 2', 'Description 3 for Lenovo Type 2'],
        'T450': ['Description 1 for Lenovo Type 2', 'Description 2 for Lenovo Type 2', 'Description 3 for Lenovo Type 2'],
        'T460s 8 GB': ['#WTS\n#laptop\n\nLenovo ThinkPad T460s\nLaptop seken ex-kantoran, bodi masih mulus no minus dan bergaransi.\n\nSpesifikasi:\nIntel Core i5 Gen 6\nRAM 8 GB/16 GB\nSSD 256 GB\nLCD 14"\nWindows 10/11\n\nKelengkapan:\nLaptop\nDus\nMouse\nKartu Garansi\n\nMinat hub WA 088221957963 (Aditya)', 'Description 2 for Lenovo Type 2', 'Description 3 for Lenovo Type 2'],
        'T460s 16 GB': ['#WTS\n#laptop\n\nLenovo ThinkPad T460s\nLaptop seken ex-kantoran, bodi masih mulus no minus dan bergaransi.\n\nSpesifikasi:\nIntel Core i5 Gen 6\nRAM 8 GB/16 GB\nSSD 256 GB\nLCD 14"\nWindows 10/11\n\nKelengkapan:\nLaptop\nDus\nMouse\nKartu Garansi\n\nMinat hub WA 088221957963 (Aditya)', 'Description 2 for Lenovo Type 2', 'Description 3 for Lenovo Type 2'],
        'T470': ['Description 1 for Lenovo Type 2', 'Description 2 for Lenovo Type 2', 'Description 3 for Lenovo Type 2'],
        'T470s 8 GB': ['Jual Laptop seken Lenovo T470s Slim no minus bergaransi\nSpek Intel Core i7 Gen 7\nRAM 8 GB, SSD 256 GB\nBodi slim 14 inci. Windows 10\n\nLok Garut kota\nkontak: 088221957963 (Adit)', 'Description 2 for Lenovo Type 2', 'Description 3 for Lenovo Type 2'],
        'T470s 12 GB': ['Description 1 for Lenovo Type 2', 'Description 2 for Lenovo Type 2', 'Description 3 for Lenovo Type 2'],
        'T470s 20 GB': ['Description 1 for Lenovo Type 2', 'Description 2 for Lenovo Type 2', 'Description 3 for Lenovo Type 2'],
        'X240 HDD': ['Description 1 for Lenovo Type 2', 'Description 2 for Lenovo Type 2', 'Description 3 for Lenovo Type 2'],
        'X240 SSD': ['Description 1 for Lenovo Type 2', 'Description 2 for Lenovo Type 2', 'Description 3 for Lenovo Type 2'],
        'X250 RAM 4 GB HDD 500': ['Description 1 for Lenovo Type 2', 'Description 2 for Lenovo Type 2', 'Description 3 for Lenovo Type 2'],
        'X250 RAM 8 GB HDD 500': ['#WTS\nCP: 088221957963 (Adiya)\nLok Garut\n\nLenovo X250 seken Ex-Kantor Bergaransi\nSpesifikasi:\nIntel Core i5 Gen 5\nRAM 8 GB\nHDD 500 GB\nLCD 12,5 inci\nWindows 10\n\nKelengkapan:\n- Unit laptop\n- Charger\n- Mouse\n- Garansi', 'Description 2 for Lenovo Type 2', 'Description 3 for Lenovo Type 2'],
        'X250 RAM 8 GB SSD 256': ['Description 1 for Lenovo Type 2', 'Description 2 for Lenovo Type 2', 'Description 3 for Lenovo Type 2'],
        'X250 RAM 8 GB SSD 512': ['Description 1 for Lenovo Type 2', 'Description 2 for Lenovo Type 2', 'Description 3 for Lenovo Type 2'],
        'X280': ['Gaduh Laptop Lenovo X280 seken no minus, hoyong di cash. Kondisi + spesifikasi sesuai gambar. Tiasa COD sekitaran garut.\n\nMinat inbox atau WA 088221957963 (Adiya)', 'Description 2 for Lenovo Type 2', 'Description 3 for Lenovo Type 2']
    },
    'DELL': {
        '5490': ['Description 1 for DELL Type 1', 'Description 2 for DELL Type 1', 'Description 3 for DELL Type 1'],
        'E7470': ['Description 1 for DELL Type 2', 'Description 2 for DELL Type 2', 'Description 3 for DELL Type 2']
    },
    'Toshiba': {
        'B553': ['LAPTOP TOSHIBA B553 2 JUTAAN COCOK UNTUK KANTOR, KASIR, KULIAH, ADMIN\n\nCore i5 Gen 3\nRAM 4\nHDD 500\n\nGaransi 1 bulan\nSiap COD sekitaran garut, luar garut rekber tokped/shopee\nMenerima kredit via Akulaku dan Spaylater\nCp: 088221957963', 'Description 2 for Toshiba Type 1', 'Description 3 for Toshiba Type 1'],
        'R73': ['Description 1 for Toshiba Type 2', 'Description 2 for Toshiba Type 2', 'Description 3 for Toshiba Type 2'],
        'R734': ['WTS LAPTOP TOSHIBA R734 MASIH MULUS PEMAKAIAN KANTORAN. SPEK CORE I5 RAM 4GB SSD 128GB SUDAH WINDOWS 10 COCOK UNTUK KEPERLUAN RINGAN ATAU BUAT YANG MAU/MASIH BELAJAR LAPTOP.\n\nCP: 088221957963 (ADITYA)', 'Description 2 for Lenovo Type 2', 'Description 3 for Lenovo Type 2']
    },
    'General': {
        'General': ['JUAL LAPTOP SEKEN MURAH BERGARANSI HARGA MULAI DARI 1,9JT-AN, TERSEDIA UNTUK BERBAGAI MACAM KEBUTUHAN SEPERTI SEKOLAH, KULIAH, KERJA, DESAIN, GAMING.\n\nBISA COD SEKITARAN GARUT DAN REKBER TOKPED/SHOPEE UNTUK LUAR GARUT.\n\nBISA JUGA KREDIT LEWAT AKULAKU DAN SHOPEE PAYLATER. MINAT WA ATAU HUB 088321957963 (ADIT)', 'Sedia Laptop dan Komputer seken kantoran, kondisi rata2 80-90%. Pc fullset/batangan. Laptop fullset. Semua ada garansi service selama 1 bulan dan software selama 2 bulan.\n\nTersedia merk:\n> Lenovo\n> DELL\n> Toshiba\n> Acer\n\nMetode pembayaran fleksibel:\n- Cash\n- Transfer\n- Rekber tokped/shopee\n- Kredit akulaku/spaylater\nMinat hub WA 088221957963 (ADIT)', 'Ready Laptop seken ex-kantor mulus no minus dan bergaransi. Tersedia untuk berbagai kebutuhan mulai dari sekolah, kuliah, kerja dan gaming ringan.\n\nTersedia berbagai merk mulai dari:\n- DELL\n- Lenovo\n- Toshiba\n\nKelengkapan Laptop:\n- Laptop\n- Charger\n- Dus\n- Kartu Garansi\n\nPembayaran bisa melalui:\n- Cash\n- Transfer\n- Kredit (Akulaku dan Spaylater)\n- Rekber (Tokopedia dan Shopee)\n- COD (Khusus daerah sekitar garut)\n\nMinat hubungi WA 088221957963 (Aditya)','MENJUAL LAPTOP SEKEN MURAH BERGARANSI UNTUK BERBAGAI KEBUTUHAN, MULAI DARI KERJA, GAMING, EDITING, KASIR, ADMIN DAN LAINNYA.  HARGA MULAI DARI 1,5JT - 6JT\n\nMENERIMA COD UNTUK SEKITARAN GARUT. UNTUK LUAR GARUT BISA REKBER VIA TOKOPEDIA DAN SHOPEE.\n\nBISA KREDIT LEWAT AKULAKU DAN SHOPEE. MINAT HUB WA 088221957963 (ADITYA)']
    }
}

class MarketplaceApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Æ')
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
