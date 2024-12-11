"""
Author:  Owen Widup
Date written: 11/29/2024
Assignment: Module #5 Assignment: #1 
Short Desc: The applicatio calculates the number of various types of items
(ex. Shirts, pants, etc.) that the clothing store has as well as the price of the individual types of clothing
and the overall price of the whole stock. Along with that, at any time, they can increase or
decrease the stock as they buy/sell more. 
"""
#imports GUI commands
from breezypythongui import EasyFrame

#Setting GUI Properties
class WidupOwenFinalProject(EasyFrame):
    def __init__(self, title= "Clothing Store Manager"):
        EasyFrame.__init__(self)
        self.title = self.addLabel(text= "Clothing Store Manager", 
                                   row= 0, column= 0)
        #Misc Labels
        self.addLabel(text= "Stock", row= 2, column= 0)
        self.addLabel(text= "Price", row= 3, column= 0)
        #Shirt Stock
        self.addLabel(text= "Total Shirt Stock: ", row= 1, column= 1)
        self.shirtStock = self.addIntegerField(value= 0, row= 2, column= 1)
        self.shirtTotal = self.addIntegerField(value= 0, row= 3, column= 1, state= "readonly")
        self.addLabel(text= "Price Per Shirt: $20", row= 4, column= 1)
        self.shirtUpdate = self.addButton(text= "Update", row= 5, column= 1, command= self.shirtPrices)
        #Pants Stock
        self.addLabel(text= "Total Pants Stock: ", row= 1, column= 2)
        self.pantsStock = self.addIntegerField(value= 0, row= 2, column= 2)
        self.pantsTotal = self.addIntegerField(value= 0, row= 3, column= 2, state= "readonly")
        self.addLabel(text= "Price Per Pants Pair: $25", row= 4, column= 2)
        self.pantsUpdate = self.addButton(text= "Update", row= 5, column= 2, command= self.pantsPrices)
        #Jacket Stock
        self.addLabel(text= "Total Jacket Stock: ", row= 1, column= 3)
        self.jacketStock = self.addIntegerField(value= 0, row= 2, column= 3)
        self.jacketTotal = self.addIntegerField(value= 0, row= 3, column= 3, state= "readonly")
        self.addLabel(text= "Price Per Jacket: $35", row= 4, column= 3)
        self.jacketUpdate = self.addButton(text= "Update", row= 5, column= 3, command= self.jacketPrices)
        #Dress Stock
        self.addLabel(text= "Total Dress Stock: ", row= 1, column= 4)
        self.dressStock = self.addIntegerField(value= 0, row= 2, column= 4)
        self.dressTotal = self.addIntegerField(value= 0, row= 3, column= 4, state= "readonly")
        self.addLabel(text= "Price Per Dress: $45", row= 4, column= 4)
        self.dressUpdate = self.addButton(text= "Update", row= 5, column= 4, command= self.dressPrices)
        #Skirt Stock
        self.addLabel(text= "Total Skirt Stock: ", row= 1, column= 5)
        self.skirtStock = self.addIntegerField(value= 0, row= 2, column= 5)
        self.skirtTotal = self.addIntegerField(value= 0, row= 3, column= 5, state= "readonly")
        self.addLabel(text= "Price Per Skirt: $30", row= 4, column= 5)
        self.skirtUpdate = self.addButton(text= "Update", row= 5, column= 5, command= self.skirtPrices)
        #Sock Stock
        self.addLabel(text= "Total Sock Stock: ", row= 1, column= 6)
        self.sockStock = self.addIntegerField(value= 0, row= 2, column= 6)
        self.sockTotal = self.addIntegerField(value= 0, row= 3, column= 6, state= "readonly")
        self.sockUpdate = self.addButton(text= "Update", row= 5, column= 6, command= self.sockPrices)
        self.addLabel(text= "Price Per Sock Pair: $5", row= 4, column= 6)

    #Calculate Shirt Price
    def shirtPrices(self):
        updatedShirt = self.shirtStock.getNumber() * 20
        self.shirtTotal.setNumber(updatedShirt)
    #Calculate Pants Price
    def pantsPrices(self):
        updatedPants = self.pantsStock.getNumber() * 25
        self.pantsTotal.setNumber(updatedPants)
    #Calculate Jacket Price
    def jacketPrices(self):
        updatedJacket = self.jacketStock.getNumber() * 35
        self.jacketTotal.setNumber(updatedJacket)
    #Calculate Dress Price
    def dressPrices(self):
        updatedDress = self.dressStock.getNumber() * 45
        self.dressTotal.setNumber(updatedDress)
    #Calculate Skirt Price
    def skirtPrices(self):
        updatedSkirt = self.skirtStock.getNumber() * 30
        self.skirtTotal.setNumber(updatedSkirt)
    #Calculate Sock Price
    def sockPrices(self):
        updatedSock = self.sockStock.getNumber() * 5
        self.sockTotal.setNumber(updatedSock)


#Executing the main window     
def main():
    WidupOwenFinalProject().mainloop()

if __name__ == "__main__":
    main()