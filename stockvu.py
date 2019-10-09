import numpy as np, statistics, math,itertools
from datetime import datetime, timedelta
from CONST import *
import csv

UI = None
tierAPass,tierBPass,tierCPass,_tierD=(list(),)*4
stocks_pass=set()
ERROR=False


class Analyzer:
    global UI
    global ERROR
    tierAPass=list()
    tierBPass=list()
    tierCPass=list()
    _tierD=list()
    stocks_pass=set()
    csv_reader = ''
    header = []
    stock_names = []
    count = 0
    ROWS = 0
    COLS = 0

    def startt(self, UII):
        print('seeing:')
        self.ERROR=False
        self.tierAPass = list()
        self.tierBPass = list()
        self.tierCPass = list()
        self._tierD = list()
        self.stocks_pass = set()
        print(CONST.date_yyyy_mm_dd)
        self.UI = UII
        for _ in range(0, 1):
            self.dailyPerformance()
            self.XDayGap()
            self.volatility()

        return True

    def dailyPerformance(self):
        print('Calculating Daily Performance')
        with open(CONST.input_file, mode='r') as csv_file:

            self.csv_reader = csv.reader(csv_file, delimiter=",")
            self.header = [name for name in next(self.csv_reader)]
            header_length = len(self.header)
            data_daily_perf = []
            line = 0
            prev_row = []

            for row in self.csv_reader:
                self.count = self.count + 1
                temp = []
                if line == 0:

                    for index in range(0, header_length, 2):
                        if row[index] != '':
                            temp.append(row[index])
                            daily_performance = 0
                            temp.append(daily_performance)

                    line += 1
                else:

                    for index in range(0, header_length, 2):
                        if row[index] != '':
                            temp.append(row[index])

                            todays_price = float(row[index + 1])
                            if prev_row[index] == '':
                                daily_performance = 0
                            else:
                                yesterdays_price = float(prev_row[index + 1])
                                daily_performance = (todays_price / yesterdays_price) - 1
                            temp.append(daily_performance)
                        else:
                            temp.append(row[index])
                            daily_performance = ''
                            temp.append(daily_performance)

                data_daily_perf.append(temp)
                prev_row = row

        csv_file.close()

        self.write_file('w', CONST.DP_csv(), data_daily_perf)

    def calculate_1DGAP(self, array):
        temp = []
        gap = []
        for row in range(0, self.ROWS, 1):
            for col in range(1, self.COLS, 2):

                temp.append(array[row][col - 1])
                if array[row][col - 1] != '':
                    if row == 0:
                        temp.append(0)

                    elif row != 0 and array[row - 1][col - 1] != '':

                        today = float(array[row][col])
                        yesterday = float(array[row - 1][col])

                        cal = self.calculate_xDayGap(today, yesterday)
                        temp.append(cal)
                    else:
                        temp.append('')
                else:
                    temp.append('')

            gap.append(temp)
            temp = []

        del temp

        self.write_file(mode='w', file_csv=CONST.D1Gap_csv(), data=gap)
        return gap

    def calculate_2DGAP(self, array):
        temp = []
        gap = []

        for row in range(0, self.ROWS, 1):
            for col in range(1, self.COLS, 2):
                temp.append(array[row][col - 1])
                if array[row][col - 1] != '':
                    if row == 0 or row == 1:
                        temp.append(0)

                    elif row > 1 and array[row - 2][col - 1] != '':
                        today = float(array[row][col])

                        yesterday = float(array[row - 2][col])
                        cal = self.calculate_xDayGap(today, yesterday)
                        temp.append(cal)
                    else:
                        temp.append('')
                else:
                    temp.append('')

            gap.append(temp)
            temp = []

        del temp
        self.write_file(mode='w', file_csv=CONST.D2Gap_csv(), data=gap)
        return gap

    def calculate_3DGAP(self, array):
        temp = []
        gap = []

        for row in range(0, self.ROWS, 1):
            for col in range(1, self.COLS, 2):
                temp.append(array[row][col - 1])
                if array[row][col - 1] != '':
                    if row == 0 or row == 1 or row == 2:
                        temp.append(0)

                    elif row > 3 and array[row - 3][col - 1] != '':
                        today = float(array[row][col])

                        yesterday = float(array[row - 3][col])
                        cal = self.calculate_xDayGap(today, yesterday)
                        temp.append(cal)
                    else:
                        temp.append('')
                else:
                    temp.append('')

            gap.append(temp)
            temp = []

        del temp
        self.write_file(mode='w', file_csv=CONST.D3Gap_csv(), data=gap)
        return gap

    def calculate_5DGAP(self, array):
        temp = []
        gap = []

        for row in range(0, self.ROWS, 1):
            for col in range(1, self.COLS, 2):
                temp.append(array[row][col - 1])
                if array[row][col - 1] != '':
                    if row == 0 or row == 1 or row == 2 or row == 3 or row == 4:
                        temp.append(0)

                    elif row > 5 and array[row - 5][col - 1] != '':
                        today = float(array[row][col])

                        yesterday = float(array[row - 5][col])
                        cal = self.calculate_xDayGap(today, yesterday)
                        temp.append(cal)
                    else:
                        temp.append('')
                else:
                    temp.append('')

            gap.append(temp)
            temp = []

        del temp
        self.write_file(mode='w', file_csv=CONST.D5Gap_csv(), data=gap)
        return gap

    def XDayGAP_Sorted(self, output, file_name):
        sorted_gap_data = []
        last_row = ''
        for col in range(1, self.COLS, 2):
            new_temp = []
            to_ignore = []
            for row in range(0, self.ROWS, 1):
                x = []
                if output[row][col] != '':

                    elem = float(output[row][col])
                    x.append(output[row][col - 1])
                    x.append(elem)
                    new_temp.append(x)
                else:
                    if last_row != '':
                        last_row = (row - 1)
                    x.append('')
                    x.append('')
                    to_ignore.append(x)

            new_temp.sort(key=lambda p: p[1])
            new_temp.extend(to_ignore)

            if col < 3:
                sorted_gap_data.extend(new_temp)

            else:

                k = []
                for (prev, new) in zip(range(0, len(sorted_gap_data)), range(0, len(new_temp))):
                    k.append(sorted_gap_data[prev] + new_temp[new])

                sorted_gap_data = [row for row in k]

        self.write_file(mode='w', file_csv=file_name, data=sorted_gap_data)

    def XDayGap(self):
        print('Calculating XDay Gap')
        with open(CONST.input_file, mode='r') as csv_file:
            self.csv_reader = csv.reader(csv_file, delimiter=",")
            self.header = [name for name in next(self.csv_reader)]
            print(self.header)

            new_temp = []
            for row in self.csv_reader:
                new_temp.append(row)

            array = np.array(new_temp)
            del new_temp
            self.show_MetaData(array)

            for day in CONST.xdays:
                if day == 1:

                    output = self.calculate_1DGAP(array)
                    self.XDayGAP_Sorted(output, CONST.sorted_D1Gap_csv())
                elif day == 2:
                    output = self.calculate_2DGAP(array)
                    self.XDayGAP_Sorted(output, CONST.sorted_D2Gap_csv())
                elif day == 3:
                    output = self.calculate_3DGAP(array)
                    self.XDayGAP_Sorted(output, CONST.sorted_D3Gap_csv())
                elif day == 5:
                    output = self.calculate_5DGAP(array)
                    self.XDayGAP_Sorted(output, CONST.sorted_D5Gap_csv())

        csv_file.close()

    @staticmethod
    def calculate_xDayGap(x, y):
        if y != 0:
            return float((x / y) - 1)
        return 0

    def volatility(self):
        # ----------------------------------------------------------

        print('Date Format ' + CONST.date_yyyy_mm_dd)

        date = datetime.strptime(CONST.date_yyyy_mm_dd, '%Y%m%d')
        last_12_month = date - timedelta(days=364.25)
        last_6_month = date - timedelta(days=180.125)
        since_year_start = str(0) + str(date.day - date.day + 1) + '/' + str(0) + str(
            date.month - date.month + 1) + '/' + str(
            date.year)

        curr_date = date.strftime('%d/%m/%Y')
        last_12_month = last_12_month.strftime('%d/%m/%Y')
        last_6_month = last_6_month.strftime('%d/%m/%Y')
        print(
            'Cuurent ' + curr_date + '\nLast 12 months ' + last_12_month + '\nlast 6 months ' + last_6_month + '\nsince_year_start ' + since_year_start)

        # --------------------Opening and Reading Daily Perfomance file----------------------
        with open(CONST.DP_csv(), mode='r') as file:
            csv_reader = csv.reader(file, delimiter=",")
            self.header = [name for name in next(csv_reader)]
            self.stock_name = [name for name in self.header if name != 'Date' and name != '']

            temp = []

            for row in csv_reader:
                temp.append(row)

            array = np.array(temp)
            print('rows' + str(len(array)))
            print('cols' + str(len(array[5])))
            print(array[5][45])

            if not self.show_MetaData(array):
                print('LOG=> stockvu' + 'return False from show_MetaData(arg) inside def @ volatility()')

            del temp

            VOL_FILES_CSV = [CONST.last_12_csv(), CONST.last_6_csv(), CONST.since_year_start_csv(),
                             CONST.inception_csv()]
            for vol, vol_file in zip(range(0, len(CONST.VOLATILITY)), range(0, len(VOL_FILES_CSV))):

                if CONST.VOLATILITY[vol] == 'last 12 months':
                    volt_data = self.calculate_volatilities(self.ROWS, self.COLS, last_12_month, curr_date, array)
                    self.write_file('w', VOL_FILES_CSV[vol_file], volt_data, ['Stock', CONST.VOLATILITY[vol]], True)

                elif CONST.VOLATILITY[vol] == 'last 6 months':
                    print('----------------------------------')
                    volt_data = self.calculate_volatilities(self.ROWS, self.COLS, last_6_month, curr_date, array)
                    self.write_file('w', VOL_FILES_CSV[vol_file], volt_data, ['Stock', CONST.VOLATILITY[vol]], True)
                elif CONST.VOLATILITY[vol] == 'since start of year':
                    print('----------------------------------')
                    volt_data = self.calculate_volatilities(self.ROWS, self.COLS, since_year_start, curr_date,
                                                            array)
                    self.write_file('w', VOL_FILES_CSV[vol_file], volt_data, ['Stock', CONST.VOLATILITY[vol]], True)

                elif CONST.VOLATILITY[vol] == 'since inception':
                    print('----------------------------------')
                    volt_data = self.calculate_volatilities(self.ROWS, self.COLS, 'since_inception', curr_date,
                                                            array)
                    self.write_file('w', VOL_FILES_CSV[vol_file], volt_data, ['Stock', CONST.VOLATILITY[vol]], True)

            self.managers(curr_date, array)
        file.close()

    def calculate_volatilities(self, ROWS, COLS, period, curr_date, array):
        print('----------------------------------------')
        print(period)
        volt = []
        if period == 'since_inception':
            return self.calculate_vol_inception(ROWS, COLS, curr_date, array)
        for col in range(1, COLS, 2):
            temp, data, flag = [], [], False

            for row in range(0, ROWS, 1):

                try:

                    if array[row][col - 1] == str(period):
                        print(
                            'Found on doc @ [' + str(row + 2) + '][' + str(col + 1) + ']: ' + str(array[row][col - 1]))
                        for last in range(row, ROWS, 1):
                            if array[last][col - 1] != curr_date and array[last][col - 1] != '':
                                temp.append(array[last][col])
                            elif array[last][col - 1] == curr_date and array[last][col - 1] != '':
                                temp = [float(t) for t in temp]
                                cal = 0.0
                                try:
                                    cal = float(statistics.stdev(temp) * math.sqrt(252))

                                    print(type(cal))
                                except Exception as e:
                                    print(e)
                                print(cal)
                                data.append(self.header[col])
                                data.append(cal)
                                flag = True
                                break
                            else:
                                data.append(self.header[col])
                                data.append('N/A')
                                flag = True
                                break

                    elif row == ROWS - 1:
                        if array[row-1][col] == '':
                            data.append(self.header[col])
                            data.append('N/A')
                            volt.append(data)
                            break

                        else:
                            data.append(self.header[col])
                            data.append('N/A')
                            volt.append(data)
                            break

                    if flag:
                        volt.append(data)
                        break
                except Exception as e:
                    print(str(e))

        return volt

    def calculate_vol_inception(self, ROWS, COLS, curr_date, array):
        volt = []

        for col in range(1, COLS, 2):
            temp, last_row = [], ''
            for row in range(0, ROWS, 1):
                if array[row][col] != '':
                    if row == self.ROWS - 1:
                        if array[row][col - 1] == curr_date:

                            print(col)
                            _1col = array[:row, col]
                            _1col = [float(price) for price in _1col]

                            cal = (statistics.stdev(_1col) * math.sqrt(252))

                            temp.append(self.header[col])
                            temp.append(cal)
                            break
                        else:
                            temp.append(self.header[col])
                            temp.append('N/A')
                            break
                else:
                    if last_row == '':
                        last_row = row - 1

                    if array[last_row][col - 1] == curr_date:

                        _1col = array[:last_row, col]
                        _1col = [float(price) for price in _1col]

                        cal = (statistics.stdev(_1col) * math.sqrt(252))
                        temp.append(self.header[col])
                        temp.append(cal)
                        break
                    else:
                        temp.append(self.header[col])
                        temp.append('N/A')
                        break

            volt.append(temp)

        return volt

    def managers(self, curr_date, array):

        available, diversed = [], []

        for col in range(1, self.COLS, 2):
            last_row = ''
            for row in range(0, self.ROWS, 1):

                if array[row][col - 1] != '':
                    if row == self.ROWS - 1:
                        if array[row][col - 1] == curr_date:

                            available.append(self.header[col])
                            break
                        else:

                            diversed.append(self.header[col])
                            break
                elif array[row][col - 1] == '':
                    if row == 51:
                        print('ZAINNNN')
                        print(array[row - 1][col - 1])
                    if last_row == '':
                        last_row = row - 1

                    if array[last_row][col - 1] == curr_date:
                        available.append(self.header[col])

                        break
                    else:
                        diversed.append(self.header[col])

                        break

        print(np.shape(diversed))
        print(diversed)

        for _ in range(0, 2):
            if _ == 0:
                self.write_file('w', CONST.available_csv(), available, ['Stock'], True, True)
            elif _ == 1:
                self.write_file('w', CONST.divested_csv(), diversed, ['Stock'], True, True)

    def calculate_tiersX(self, arr_guidelines,ui):
        self.UI=ui
        self.ERROR=False
        self.array = self.extract_data()

        self.header = ['Stocks'] + CONST.WORST_XDAYS + CONST.VOLATILITY
        self.write_file('w', CONST.summary_csv(), self.array, self.header, True)
        print(type(self.array[0][1]))
        self.array = np.array(self.array)
        self.show_MetaData(self.array)

        for row in range(0, self.ROWS):
            self.cheking_constraints(self.array[row], arr_guidelines,row)

        for tier in stocks_pass:
            if tier=='a':
                print(self.tierAPass)
                self.write_file2_0('w', CONST.tierA_csv(), self.tierAPass, ['Stocks'])
            elif tier=='b':
                self.write_file2_0('w', CONST.tierB_csv(), self.tierBPass, ['Stocks'])
            elif tier=='c':
                self.write_file2_0('w', CONST.tierC_csv(), self.tierCPass, ['Stocks'])
            elif tier=='d':

                self.write_file2_0('w', CONST.tierD_csv(), self._tierD, ['Stocks'])


        if not self.ERROR:
            return True, CONST.date_yyyy_mm_dd
        elif self.ERROR:
            return False, CONST.date_yyyy_mm_dd

    def cheking_constraints(self, data, arr_guideline,line):

        print('----------Checking Contraints-------------- STOCK ',data[0])
        print('My Guide=>   ',arr_guideline)
        arr_guideline=list(map(lambda x: list(map(lambda y:y/100,x)),arr_guideline))

        print('My Guideline now ',arr_guideline)
        worst1d = float(data[1])
        worst2D = float(data[2])
        worst3D = float(data[3])
        worst5D = float(data[4])
        last_12_months = 0.0
        last_6_months = 0.0
        since_start = 0.0
        since_inception = 0.0
        if 'N/A' not in data[5]:
            last_12_months = float(data[5])
        else:
            last_12_months=0.0
        if 'N/A' not in data[6]:
            last_6_months = float(data[6])
        else:
            last_6_months=0.0
        if 'N/A' not in data[7]:
            since_start = float(data[7])
        else:
            since_start=0.0
        if 'N/A' not in data[8]:
            since_inception = float(data[8])
        else:
            since_inception=0.0

        TOTAL_TIER=3
        global PASS

        for tier,guide in itertools.zip_longest(range(0,TOTAL_TIER),range(0,len(arr_guideline))):
            print('Calcualating ',tier+1,' and applying guide ',arr_guideline[guide])
            if self.classif_tiers(arr_guideline[guide],worst1d,worst2D,worst3D,worst5D,last_12_months,last_6_months,since_start,since_inception):
                print(data[0],'  PASS')
                PASS=True
            else:
                print(data[0], '  NOT PASS')
                PASS=False
            print('Line is ',line)
            if tier==0 and PASS:
                stocks_pass.add('a')
                self.tierAPass = self.tierAPass +[data[0]]

                break
            if tier==1 and PASS:
                stocks_pass.add('d')
                self.tierBPass=self.tierBPass+[data[0]]
                break
            if tier==2 and PASS:
                stocks_pass.add('c')
                self.tierCPass=self.tierCPass+[data[0]]

                break
            if tier==2 and not PASS:
                stocks_pass.add('d')
                self._tierD=self._tierD+[data[0]]

                break





    @staticmethod
    def classif_tiers(guide,worst1d,worst2D,worst3D,worst5D,last_12_months,last_6_months,since_start,since_inception):
        if worst1d < guide[0]and worst2D < guide[1] and worst3D < guide[
            2] and worst5D < guide[3] and last_12_months < guide[4] and last_6_months < \
                guide[5] and since_start < guide[6] and since_inception < guide[7]:
            return True
        else:
            return False

    def extract_data(self):
        data_array, self.array = ([],) * 2
        SORTED_CSV = [CONST.sorted_D1Gap_csv(), CONST.sorted_D2Gap_csv(), CONST.sorted_D3Gap_csv(),
                      CONST.sorted_D5Gap_csv()]
        VOL_FILES_CSV = [CONST.last_12_csv(), CONST.last_6_csv(), CONST.since_year_start_csv(), CONST.inception_csv()]

        sort_arr=list()
        stock_name = []
        for file in SORTED_CSV:
            temp = []

            with open(file, mode='r') as csv_file:
                self.csv_reader = csv.reader(csv_file, dialect='excel', delimiter=',')
                stock_name = [name for name in next(self.csv_reader) if name!='Date' ]
                for row in self.csv_reader:

                    temp=[row[i] for i in range(1,len(row),2)]
                    break

            print(stock_name)
            sort_arr.append(temp)

            csv_file.close()
        print('Sort_Array ' + str(np.shape(sort_arr)))
        print(sort_arr[0])
        vol_arr = list()
        for file in VOL_FILES_CSV:
            temp = list()
            with open(file, mode='r') as csv_file:
                self.csv_reader = csv.reader(csv_file, dialect='excel', delimiter=',')
                self.header = [name for name in next(self.csv_reader)]
                for rowNum, row in enumerate(self.csv_reader):
                    for colNum, col in enumerate(row):
                        if colNum == 1:
                            temp=temp+[col]



            vol_arr.append(temp)
            csv_file.close()

        print('Vol_Array ' + str(np.shape(vol_arr)))
        print(vol_arr[0])


        cols = np.size(sort_arr,1)
        for col in range(0, cols, 1):
            temp = []
            merge_arr = list()

            for gap in range(0,len(sort_arr)):
                elem = sort_arr[gap][col]
                if 'N/A' not in elem and elem.isdigit():
                    elem = float(elem)
                temp=temp+[elem]

            for vol in (range(0,len(vol_arr))):


                elem = vol_arr[vol][col]
                if 'N/A' not in elem and elem.isdigit():
                    elem = float(elem)
                temp=temp+[elem]
                merge_arr=[stock_name[col]] + temp

            self.array.append(merge_arr)
            del temp

        print('Done Extracting Data Mergence of Sorted GAPS & VOLATILITY')
        return self.array
    @staticmethod
    def overwrite(file):
        with open(file, mode='w') as _file:
            writer = csv.writer(_file, delimiter=',', quoting=csv.QUOTE_NONE, lineterminator='\r', dialect='excel')
            writer.writerow('\n')
            _file.close()
            print('Flie is cleared')


    def write_file2_0(self,mode,file_csv,data,header):

        print('Writing .... ',file_csv)
        try:
            with open(file_csv,mode=mode) as file:
                writer=csv.writer(file,delimiter=',',quoting=csv.QUOTE_NONE,lineterminator='\r',dialect='excel')
                writer.writerow(header)
                for r in data:
                    r=[r]
                    writer.writerow(r)
        except:
            self.ERROR = True
            self.UI.showError(msg='Please close all *.csv files befor proceeding',title='Error writing the file')


    def write_file(self, mode, file_csv, data, change_header=None, tweak=False, tweak2=False):

        print('Writing...' + file_csv)
        if change_header is None:
            change_header = []

        try:
            with open(file_csv, mode=mode) as file:

                writer = csv.writer(file, delimiter=',',
                                    quoting=csv.QUOTE_NONE, lineterminator='\r', dialect='excel')

                if not tweak:
                    writer.writerow(self.header)
                else:
                    writer.writerow(change_header)
                if tweak2:
                    writer = csv.writer(file, delimiter='\t',
                                        quoting=csv.QUOTE_NONE, lineterminator='\r', dialect='excel')
                    for d in data:
                        writer.writerow(d)
                    writer.writerow('\n')
                else:
                    writer.writerows(data)
        except:
            self.ERROR = True
            self.UI.showError(msg='Please close all *.csv files befor proceeding',title='Error writing the file')


    def show_MetaData(self, array):
        try:
            rows = len(array)
            cols = len(array[0])
            self.ROWS = rows
            self.COLS = cols
            print('Total Rows: ' + str(rows)+'  '+'Tot COLS ' + str(cols))
            print('Columns are')
            print(self.header)
            print('Total Stocks to work on ' + str(int(cols / 2)))
            print('How row look like: ')
            print(array[0])
            print(array[0][4])

            print('Dim of array  '+str(np.shape(array)))

            print('Type of first 2 colns ',type(array[:, 0:2]))

            print('-----------------End of Metadata----------------------------------')
            return True
        except Exception as e:
            print(e)
            self.ERROR = True
            self.UI.showError(
                'Either File Format is not correct or some first 20 starting stocks [Date , Name] are empty','File Exception')
            return False


if __name__ == '__main__':
    a = Analyzer()
    # a.start()
    # a.XDayGap()

    # a.dailyPerformance()
    # a.volatility()
    # a.calculate_tiersX()
