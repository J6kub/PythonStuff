from email.quoprimime import header_check

data = 'PS-SL-A287,LT-1,PRODUCT,25,EA,31250.00,USD,2,19,365,50,30,100,10,30,10,,Street Lighting,B,ONHAND,NEW,INDUSTRIAL;PS-SL-A288,LT-1,PRODUCT,20,EA,25000.00,USD,2,35,365,50,30,100,10,30,10,,Street Lighting,B,ONHAND,NEW,INDUSTRIAL;PS-SL-H309,LT-1,PRODUCT,3,EA,3750.00,USD,2,14,365,50,30,100,10,30,10,,Street Lighting,B,ONHAND,NEW,INDUSTRIAL;PS-SL-H310,LT-1,PRODUCT,35,EA,43750.00,USD,2,16,365,50,30,100,10,30,10,,Street Lighting,A,ONHAND,NEW,INDUSTRIAL;PS-SL-F342,LT-1,PRODUCT,43,EA,53750.00,USD,2,42,365,50,30,100,10,30,10,,Street Lighting,A,ONHAND,NEW,INDUSTRIAL;PS-SL-F343,LT-1,PRODUCT,49,EA,61250.00,USD,2,41,365,50,30,100,10,30,10,,Street Lighting,A,ONHAND,NEW,INDUSTRIAL'
dataHeader = 'product.partNumber,location.locationIdentifier,inventoryType,quantity,quantityUnits,value,valueCurrency,reservationOrders,daysOfSupply,shelfLife,reorderLevel,expectedLeadTime,quantityUpperThreshold,quantityLowerThreshold,daysOfSupplyUpperThreshold,daysOfSupplyLowerThreshold,expiringThreshold,plannerCode,velocityCode,inventoryParentType,class,segment'
a = data.split(";")
dataHeader = dataHeader.split(",")


class Table:
    '''
    Input an array with rows split by comma: Function splits it automatically
    Input an array with header elements.
    '''
    def createRow(self, rawRow, headerX):
        row = {}
        splitRow = rawRow.split(',')
        for i in range(len(headerX)):
            row[headerX[i]] = splitRow[i]
        return row

    def __init__(self, headish, rowData):
        rows = []
        self.headish = headish
        for x in rowData:
            rows.append(self.createRow(x,headish))
        self.rows = rows

    def printItemTypes(self):
        for x in self.headish:
            print(x)
    def getRow(self,n):
        return self.rows[n]


tabelka = Table(dataHeader,a)

for row in tabelka.rows:
    print(row['value'])

tabelka.printItemTypes()
print(tabelka.getRow(0)["segment"])
