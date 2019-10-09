import os


date_yyyy_mm_dd=''

class CONST():

    user_path = os.path.expanduser('~')
    user_name = os.path.split(user_path)[-1]
    SOURCE = 'ssource'
    DEST = 'destination'

    global date_yyyy_mm_dd

    dd = '03'
    mm = '03'
    yyyy = '2019'
    csv_reader = None

    @staticmethod
    def show(date):
        CONST.date_yyyy_mm_dd=date
        print(date_yyyy_mm_dd)
        print(CONST().input_file)

    src_file_path = ''
    dest_file_path = ''
    input_file = dest_file_path

    @staticmethod
    def DP_csv():
        DP_csv = CONST.user_path + '\\' + CONST.DEST+'\\' + CONST.date_yyyy_mm_dd + '\\Daily_performance.csv'
        return DP_csv

    @staticmethod
    def D1Gap_csv():
        D1Gap_csv = CONST.user_path + '\\' + CONST.DEST+'\\' + CONST.date_yyyy_mm_dd + '\\1DGAP.csv'
        return D1Gap_csv

    @staticmethod
    def D2Gap_csv():
        D2Gap_csv = CONST.user_path + '\\' + CONST.DEST + '\\' + CONST.date_yyyy_mm_dd + '\\2DGAP.csv'
        return D2Gap_csv

    @staticmethod
    def D3Gap_csv():
        D3Gap_csv = CONST.user_path + '\\' + CONST.DEST + '\\' + CONST.date_yyyy_mm_dd + '\\3DGAP.csv'
        return D3Gap_csv

    @staticmethod
    def D5Gap_csv():
        D5Gap_csv = CONST.user_path + '\\' + CONST.DEST + '\\' + CONST.date_yyyy_mm_dd + '\\5DGAP.csv'
        return D5Gap_csv

    @staticmethod
    def sorted_D1Gap_csv():
        sorted_D1Gap_csv = CONST.user_path + '\\' + CONST.DEST + '\\' + CONST.date_yyyy_mm_dd + '\\1Dsorted_GAP.csv'
        return sorted_D1Gap_csv

    @staticmethod
    def sorted_D2Gap_csv():
        sorted_D2Gap_csv = CONST.user_path + '\\' + CONST.DEST + '\\' + CONST.date_yyyy_mm_dd + '\\2Dsorted_GAP.csv'
        return sorted_D2Gap_csv

    @staticmethod
    def sorted_D3Gap_csv():
        sorted_D3Gap_csv = CONST.user_path + '\\' + CONST.DEST + '\\' + CONST.date_yyyy_mm_dd + '\\3Dsorted_GAP.csv'
        return sorted_D3Gap_csv

    @staticmethod
    def sorted_D5Gap_csv():
        sorted_D5Gap_csv = CONST.user_path + '\\' + CONST.DEST + '\\' + CONST.date_yyyy_mm_dd + '\\5Dsorted_GAP.csv'
        return sorted_D5Gap_csv

    @staticmethod
    def last_12_csv():
        last_12_csv = CONST.user_path + '\\' + CONST.DEST + '\\' + CONST.date_yyyy_mm_dd + '\\Last 12 months.csv'
        return last_12_csv

    @staticmethod
    def last_6_csv():
        last_6_csv = CONST.user_path + '\\' + CONST.DEST + '\\' + CONST.date_yyyy_mm_dd + '\\Last 6 months.csv'
        return last_6_csv

    @staticmethod
    def since_year_start_csv():
        since_year_start_csv = CONST.user_path + '\\' + CONST.DEST + '\\' + CONST.date_yyyy_mm_dd + '\\Since year Start.csv'
        return since_year_start_csv

    @staticmethod
    def inception_csv():
        inception_csv = CONST.user_path + '\\' + CONST.DEST + '\\' + CONST.date_yyyy_mm_dd + '\\Since Inception.csv'
        return inception_csv

    @staticmethod
    def available_csv():
        available_csv = CONST.user_path + '\\' + CONST.DEST + '\\' + CONST.date_yyyy_mm_dd + '\\Available_managers.csv'
        return available_csv

    @staticmethod
    def divested_csv():
        divested_csv = CONST.user_path + '\\' + CONST.DEST + '\\' + CONST.date_yyyy_mm_dd + '\\Diversed_managers.csv'
        return divested_csv

    @staticmethod
    def summary_csv():
        summary_csv = CONST.user_path + '\\' + CONST.DEST + '\\' + CONST.date_yyyy_mm_dd + '\\Summary.csv'
        return summary_csv
    @staticmethod
    def tierA_csv():
        tierA_csv = CONST.user_path + '\\' + CONST.DEST + '\\' + CONST.date_yyyy_mm_dd + '\\TierA.csv'
        return tierA_csv

    @staticmethod
    def tierB_csv():
        tierB_csv = CONST.user_path + '\\' + CONST.DEST + '\\' + CONST.date_yyyy_mm_dd + '\\TierB.csv'
        return tierB_csv

    @staticmethod
    def tierC_csv():
        tierC_csv = CONST.user_path + '\\' + CONST.DEST + '\\' + CONST.date_yyyy_mm_dd + '\\TierC.csv'
        return tierC_csv

    @staticmethod
    def tierD_csv():
        tierD_csv = CONST.user_path + '\\' + CONST.DEST + '\\' + CONST.date_yyyy_mm_dd + '\\TierD.csv'
        return tierD_csv


    VOLATILITY = ['last 12 months', 'last 6 months', 'since start of year', 'since inception']

    WORST_XDAYS = ['Worst 1D %', 'Worst 2D %', 'Worst 3D %', 'Worst 5D %']
    xdays = [1, 2, 3, 5]
    tierA = [2, 3, 3, 'N/A', 5, 5, 5, 5]
    tierB = [3, 4, 'N/A', 7, 7, 'N/A', 'N/A', 'N/A']
    tierC = ['N/A', 'N/A', 'N/A', 10, 'N/A', 'N/A', 10, 'N/A']


    # def changeTierAContraints(worst5D):
    #     tierA[3] = worst5D
    #
    #
    # def changeTierBContraints(worst3D, month12, month6, inception):
    #     tierB[2] = worst3D
    #     tierB[5] = month12
    #     tierB[6] = month6
    #     tierB[7] = inception
    #
    #
    # def changeTierCContraints(worst1D, worst2D, worst3D, inception, month12, since_start):
    #     tierC[0] = worst1D
    #     tierC[1] = worst2D
    #     tierC[2] = worst3D
    #     tierC[4] = inception
    #     tierC[5] = month12
    #     tierC[7] = since_start
