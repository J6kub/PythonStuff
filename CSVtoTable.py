class TableCsv:
    '''
    Input an array with rows split by comma: Function splits it automatically
    Input an array with header elements.
    '''
    def createRow(self, rawRow):
        '''Creates rows'''
        row = {}
        splitRow = rawRow.split(',')
        for i in range(len(self.headish)):
            row[self.headish[i]] = splitRow[i]
        return row

    def __init__(self, csvFile):
        self.file = open(csvFile,'r').read()
        rows = []
        self.splitted = self.file.splitlines()
        self.headish = self.splitted[0].split(",")
        for x in range(1, len(self.splitted)):
            rows.append(self.createRow(self.splitted[x]))
        self.rows = rows

    def printItemTypes(self):
        for x in self.headish:
            print(x)
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


tt = TableCsv('country_full.csv')

tt.printItemTypes()

def printAllFromRegion(reg):
    alls = tt.getRowsByValue("region", reg)
    for x in alls:
        print(x["name"])
    print('done')

printAllFromRegion("Asia")
