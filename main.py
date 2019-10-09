# To install related packages used in entire programm. Opencommand prompt
# 1. pip3 install PyQt5
# 2. pip3 install PyQt5-tools
# 3. pip3 install pyeventbus
# 4. pip3 install pandas
# 5. pip3 install datetime

from PyQt5.QtWidgets import QApplication  # Python Related Package
import sys  # Python Related Package
import handler as hd  # Application Related Package

if __name__ == '__main__':
    qapp = QApplication(sys.argv)
    app = hd.AppWindow()
    app.show()
    sys.exit(qapp.exec_())
