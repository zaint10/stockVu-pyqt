from PyQt5.QtWidgets import QMainWindow
from gui import Ui_vMainWindow
from stockvu import *
import pathlib,shutil
from CONST import *


class AppWindow(QMainWindow):

    ui=None
    DH=None   

    def __init__(self):
        super().__init__()
        self.ui = Ui_vMainWindow()
        self.ui.setupUi(self)
        DirectoyHandler().setDirName()

        self.show()

    @staticmethod
    def start(gui):
        finish=Analyzer().start()
        if finish:
            gui.updateStatus('Analysis complete',True)

    @staticmethod
    def startt(gui):
        finish = Analyzer().startt(gui)
        if finish:
            gui.updateStatus('Analysis complete',True)
    @staticmethod
    def generateT(arr_guideline,gui):
        finish,date=Analyzer().calculate_tiersX(arr_guideline,gui)
        if finish:
            gui.showMesssage('Tiers Have been generated. Refer the Destination Directory\\' +str(date)+'\\')





class DirectoyHandler():
    user_path = ''
    user_name = ''
    src_dir_path = ''
    dest_dir_path = ''

    def __init__(self):
        pass
    @classmethod
    def setDirName(cls):
        cls.user_path = CONST.user_path
        cls.user_name = CONST.user_name
        cls.src_dir_path = CONST.user_path + '\\' + CONST.SOURCE
        cls.dest_dir_path = CONST.user_path + '\\' + CONST.DEST
        print(cls.src_dir_path)
        print(cls.dest_dir_path)

    @staticmethod
    def fetch_file(gui):
        if gui.YYYMMDD == '':
            gui.updateStatus('Date Not Selected')
            return

        src_dir_path = DirectoyHandler().src_dir_path + '\\' + gui.YYYMMDD
        dest_dir_path = DirectoyHandler().dest_dir_path + '\\' + gui.YYYMMDD
        CONST.src_file_path = src_dir_path + '\\' + CONST.user_name + gui.YYYMMDD + '.csv'
        CONST.dest_file_path = dest_dir_path + '\\' + CONST.user_name + gui.DDMMYYYY + '.csv'

        pathlib.Path(src_dir_path).mkdir(parents=True, exist_ok=True)
        pathlib.Path(dest_dir_path).mkdir(parents=True, exist_ok=True)

        if not os.path.isfile(CONST.src_file_path):
            gui.updateStatus(DirectoyHandler.user_name + gui.YYYMMDD + '.csv' + ' doesn''t exists.')
        else:
            shutil.copyfile(CONST.src_file_path, CONST.dest_file_path)
            gui.updateStatus("Files Fetched. Ready to Analyze")

            CONST.input_file = CONST.dest_file_path
            CONST.date_yyyy_mm_dd=gui.YYYMMDD
            print('fffff')
            CONST.show(gui.YYYMMDD)

            gui.ready_to_analyze=True




