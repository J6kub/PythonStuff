#Jakub B, no rights reserved
def is_floatable(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
assert is_floatable(10) == True
assert is_floatable(10.23) == True
assert is_floatable("10.34") == True
assert is_floatable("13") == True
assert is_floatable("pepe") == False
assert is_floatable(".") == False

class TableCsv:
    '''
    Input an array with rows split by comma: Function splits it automatically
    Input an array with header elements.
    '''
    def createRow(self, rawRow):
        '''Creates rows'''
        row = {}
        splitRowRaw = rawRow.split(self.splitterType)
        splitRow = []
        for elm in splitRowRaw:
            if is_floatable(elm):
                splitRow.append(float(elm))
            else:
                splitRow.append(elm)
        for i in range(len(self.headish)):
            row[self.headish[i]] = splitRow[i]
        return row

    def __init__(self, csvFile, splitterType):
        self.file = open(csvFile,'r',encoding='utf-8').read()
        rows = []
        self.splitterType = splitterType
        self.splitted = self.file.splitlines()
        self.headish = self.splitted[0].split(self.splitterType)
        for x in range(1, len(self.splitted)):
            rows.append(self.createRow(self.splitted[x]))
        self.rows = rows

    def printItemTypes(self):
        for x in self.headish:
            print(x)
    def getItemTypes(self):
        res = []
        for x in self.headish:
            res.append(x)
        return res
    def getRow(self,n):
        '''Returns Row'''
        return self.rows[n]
    def getRowsByValue(self, htag, value):
        '''Returns Array of rows with the desired values'''
        rows = []
        for x in self.rows:
            if x[htag] == value:
                rows.append(x)
        return rows
    def getColumnList(self, column):
        res = []
        for row in self.rows:
            res.append(row[column])
        return res
    def printRows(self):
        for x in self.rows:
            print(x)
