#Given the array orders, which represents the orders that customers have done 
#in a restaurant. More specifically orders[i]=[customerNamei,tableNumberi,
# foodItemi] where customerNamei is the name of the customer, tableNumberi 
# is the table customer sit at, and foodItemi is the item customer orders.

#Return the restaurant's “display table”. The “display table” is a table whose 
# row entries denote how many of each food item each table ordered. The first column 
# is the table number and the remaining columns correspond to each food item in alphabetical 
# order. The first row should be a header whose first column is “Table”, followed by the 
# names of the food items. Note that the customer names are not part of the table. 
# Additionally, the rows should be sorted in numerically increasing order.

orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
# Output: [["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],["3","0","2","1","0"],["5","0","1","0","1"],["10","1","0","0","0"]] 
# Explanation:
# The displaying table looks like:
# Table,Beef Burrito,Ceviche,Fried Chicken,Water
# 3    ,0           ,2      ,1            ,0
# 5    ,0           ,1      ,0            ,1
# 10   ,1           ,0      ,0            ,0
# For the table 3: David orders "Ceviche" and "Fried Chicken", and Rous orders "Ceviche".
# For the table 5: Carla orders "Water" and "Ceviche".
# For the table 10: Corina orders "Beef Burrito". 

def display_table(orders):
    tableNums = []
    tablesToRemember = []
    food = ["Table"]
    for index in range(len(orders)):
        item = orders[index][2]
        table = orders[index][1]
        if table in tableNums:
            for tab in tablesToRemember:
                if tab[0] == table:
                    for count in range(len(tab)):
                        if count == index:
                            tab[count] = 1
        else:
            tableNums.append(table)
            thisTable = [table]
            for count in range(len(orders)):
                if count == index:
                    thisTable.append(1)
                else:
                    thisTable.append(0)

            tablesToRemember.append(thisTable)
                

        food.append(item)

    return [food] + tablesToRemember

print(display_table(orders))