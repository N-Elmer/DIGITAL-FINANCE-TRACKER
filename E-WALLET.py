import sys
import random
import sqlite3
from prettytable import ALL
from matplotlib import style
style.use ('fivethirtyeight')
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from prettytable import from_db_cursor

print("")
print("")

print("********************* ELECTRONIC WALLET *********************")
print("*************************************************************")

print("")
print("")

print("************************ MAIN MENU **************************")
print("*************************************************************")

print("")
print("")

print("********************* CHOOSE AN OPTION **********************")
print("*************************************************************")

print("")
print("")

conn = sqlite3.connect("ManageTransaction.db")
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS TransactionTable (Id INTEGER, Date TEXT, Income INTEGER, Remarks_1 TEXT, Expense INTEGER, Remarks_2 TEXT)")

x = PrettyTable(hrules = ALL)
x.add_column("MAIN MENU",["[1]: MANAGE TRANSACTION","[2]: VIEW ANALYTICS"])
x.align = "l"
print(x)
print("\nRESPONSE ? ")
MainMenu = str(input())

print("")
print("")

while MainMenu != "1" and MainMenu != "2":
    print("ERROR ENTER [1] OR [2]")
    MainMenu = str(input())

print("")
print("")

if MainMenu == "1":
    
    print("***************** MANAGE TRANSACTION MENU *******************")
    print("*************************************************************")
    
    print("")
    print("")
    
    print("******************** CHOOSE AN OPTION ***********************")
    print("*************************************************************")
    
    print("")
    print("")

    x = PrettyTable(hrules = ALL)
    x.add_column("TRANSACTION MENU",["[1]: ADD TRANSACTION","[2]: VIEW TRANSACTION HISTORY"])
    x.align = "l"
    print(x)
    print("\nRESPONSE ? ")
    TransactionMenu = str(input())

    print("")
    print("")

    while TransactionMenu != "1" and TransactionMenu != "2":
        print("ERROR ENTER [1] OR [2]")
        TransactionMenu = str(input())
    
    print("")
    print("")

    if TransactionMenu == "1":
        
        print("******************** ADD TRANSACTION ************************")
        print("*************************************************************")
        
        print("")
        print("")

        def data_entry():

            MinId = 1000
            # MinId means Minimum Transaction Id Value
            MaxID = 2000
            # MaxId means Maximum Transaction Id Value
            IdRange = [i for i in range(MinId, MaxID+1)]
            # IdRange is the range formed by the MaxId and MinId Values
            random.shuffle(IdRange)
            id = IdRange[0]
            print("TRANSACTION ID: \n",id)
            
            print("ENTER TRANSACTION DATE: ")
            date = str(input())
            
            while True:
                try:
                    print("ENTER INCOME AMOUNT: ")
                    income = int(input())
                    break
                except ValueError:
                    print("")
                    print("ERROR!!! INPUT AN INTEGER ONLY")
                    print("")
                    continue
            
            print("ENTER INCOME REMARKS: ")
            remarks_1 = str(input())
            
            while True:
                try:
                    print("ENTER EXPENSE AMOUNT: ")
                    expense = int(input())
                    break
                except ValueError:
                    print("")
                    print("ERROR!!! INPUT AN INTEGER ONLY")
                    print("")
                    continue
            
            print("ENTER EXPENSE REMARKS: ")
            remarks_2 = str(input())
            
            print("")
            print("")
            
            print("******************** DATA ENTERED SUCCESSFULLY **************")
            print("*************************************************************")
            
            print("")
            print("")
            
            c.execute("INSERT INTO TransactionTable (Id, Date, Income, Remarks_1, Expense, Remarks_2) VALUES(?, ?, ?, ?, ?, ?)", (id, date, income, remarks_1, expense, remarks_2))
            conn.commit()

        def syntax_control():
            
            x = PrettyTable(hrules = ALL)
            x.add_column("AUXILIARY MENU",["[1]: DISPLAY ANALYTICS","[2]: DISPLAY HISTORY","[3]: ENTER NEW DATA","[4]: EDIT DATA","[5]: DELETE DATA","[6]: SEARCH DATA","[E]: SAVE AND EXIT"])
            x.align = "l"
            print(x)
            print("\nRESPONSE ? ")
            TSMO = str(input())
            # TSMO means Transaction Sub Menu Option
            
            while TSMO != "1" and TSMO != "2" and TSMO != "3" and TSMO != "4" and TSMO != "5" and TSMO != "6" and TSMO != "E" and TSMO != "e":
                print("ERROR ENTER [1] OR [2] OR [3] OR [4] OR [5] OR [6] OR [E]")
                TSMO = str(input())
            
            print("")
            print("")
            
            if TSMO == "1":
                
                print("")
                print("")
                
                data_analytics()
                syntax_control()
            
            if TSMO == "2":
                
                print("")
                print("")
                
                display_data()
                syntax_control()
            
            print("")
            print("")
            
            if TSMO == "3":
                data_entry()
                syntax_control()
            
            if TSMO == "4":
                data_edit()
                syntax_control()
            
            if TSMO == "5":
                data_delete()
                syntax_control()
            
            if TSMO == "6":
                data_search()
                syntax_control()
            
            if TSMO == "E" or "e":
                
                print("**************** SAVED AND EXITED SUCCESSFULLY **************")
                print("*************************************************************")
                
                print("")
                print("")
                
                print("******************** SOFTWARE BY N.ELMER ********************")
                print("*************************************************************")
                
                sys.exit()
            
            print("")
            print("")

        def data_edit():
            
            while True:
                try:
                    print("ENTER THE RECORD ID YOU WISH TO EDIT: ")
                    target_id = int(input())
                    break
                except ValueError:
                    print("")
                    print("ERROR!!! INPUT AN INTEGER ONLY")
                    print("")
                    continue
            
            print("ENTER NEW TRANSACTION DATE: ")
            new_date = str(input())
            
            while True:
                try:
                    print("ENTER NEW INCOME AMOUNT: ")
                    new_income = int(input())
                    break
                except ValueError:
                    print("")
                    print("ERROR!!! INPUT AN INTEGER ONLY")
                    print("")
                    continue
            
            print("ENTER NEW INCOME REMARKS: ")
            new_remarks_1 = str(input())
            
            while True:
                try:
                    print("ENTER NEW EXPENSE AMOUNT: ")
                    new_expense = int(input())
                    break
                except ValueError:
                    print("")
                    print("ERROR!!! INPUT AN INTEGER ONLY")
                    print("")
                    continue
            
            print("ENTER NEW EXPENSE REMARKS: ")
            new_remarks_2 = str(input())
            
            print("")
            print("")
            
            print("******************** DATA UPDATED SUCCESSFULLY **************")
            print("*************************************************************")
            
            print("")
            print("")
            
            c.execute("UPDATE TransactionTable set Date = ?, Income = ?, Remarks_1 = ?, Expense = ?, Remarks_2 = ? WHERE Id = ?", (new_date, new_income, new_remarks_1, new_expense, new_remarks_2, target_id))
            conn.commit()

        def data_delete():
            
            while True:
                try:
                    print("ENTER THE RECORD ID YOU WISH TO DELETE: ")
                    target_id2 = int(input())
                    break
                except ValueError:
                    print("")
                    print("ERROR!!! INPUT AN INTEGER ONLY")
                    print("")
                    continue
            
            print("")
            print("")
            
            print("******************** DATA DELETED SUCCESSFULLY **************")
            print("*************************************************************")
            
            print("")
            print("")
            
            c.execute("DELETE FROM TransactionTable WHERE Id = ?", (target_id2,))
            conn.commit()

        def data_search():
            
            print("ENTER THE SEARCH QUERRY: ")
            search = str(input())
            
            c.execute("SELECT * FROM TransactionTable WHERE Id LIKE ? OR Date LIKE ? OR Income LIKE ? OR Remarks_1 LIKE ? OR Expense LIKE ? OR Remarks_2 LIKE ?", (search, search, search, search, search, search))
            x = from_db_cursor(c, hrules = ALL)
            x.align = "l"
            
            print("")
            print("")
            
            print("************************ SEARCH RESULT **********************")
            print("*************************************************************")
            
            print("")
            print("")
            
            print(x)
            
            print("")
            print("")
            
            conn.commit()

        def display_data():
            
            print("*************************************************************")
            print("*************************************************************")
            
            print("")
            print("")
            
            c.execute("SELECT * FROM TransactionTable")
            x = from_db_cursor(c, hrules = ALL)
            x.align = "l"
            print(x)
            
            print("")
            print("")
            
            print("*************************************************************")
            print("*************************************************************")
            
            print("")
            print("")
            
            balance_computation()
            
            print("")
            print("")
            
            print("*************************************************************")
            print("*************************************************************")
            
            print("")
            print("")
            
            syntax_control()

        def balance_computation():
            
            c.execute("SELECT SUM(Income) as TOTAL_INCOME, SUM(Expense) as TOTAL_EXPENDITURE FROM TransactionTable")
            a = from_db_cursor(c)
            
            c.execute("SELECT (SUM(Income) - SUM(Expense)) as BALANCE FROM TransactionTable")
            d = from_db_cursor(c)
            
            print(a)
            print(d)

        def data_analytics():
            
            c.execute("SELECT Date, Income, Expense FROM TransactionTable")
            data = c.fetchall()
            
            Date = []
            Income = []
            Expense = []
            
            for row in data:
                Date.append(row[0])
                Income.append(row[1])
                Expense.append(row[2])
            
            plt.plot(Date,Income,"-",label="Income")
            plt.plot(Date,Expense,"--",label="Expenditure")
            leg = plt.legend();
            plt.show()
            
            print("")
            print("")

        create_table()
        data_entry()
        syntax_control()
        data_edit()
        data_delete()
        data_search()
        display_data()
        balance_computation()
        data_analytics()

        if conn:
            c.close()
            conn.close()

    if TransactionMenu == "2":
        
        print("******************* VIEW TRANSACTION ************************")
        print("*************************************************************")
        
        print("")
        print("")

        def data_entry():
            
            MinId = 1000
            # MinId means Minimum Transaction Id Value
            MaxID = 2000
            # MaxId means Maximum Transaction Id Value
            IdRange = [i for i in range(MinId, MaxID+1)]
            # IdRange is the range formed by the MaxId and MinId Values
            random.shuffle(IdRange)
            id = IdRange[0]
            print("TRANSACTION ID: \n",id)
            
            print("ENTER TRANSACTION DATE: ")
            date = str(input())
            
            while True:
                try:
                    print("ENTER INCOME AMOUNT: ")
                    income = int(input())
                    break
                except ValueError:
                    print("")
                    print("ERROR!!! INPUT AN INTEGER ONLY")
                    print("")
                    continue
            
            print("ENTER INCOME REMARKS: ")
            remarks_1 = str(input())
            
            while True:
                try:
                    print("ENTER EXPENSE AMOUNT: ")
                    expense = int(input())
                    break
                except ValueError:
                    print("")
                    print("ERROR!!! INPUT AN INTEGER ONLY")
                    print("")
                    continue
            
            print("ENTER EXPENSE REMARKS: ")
            remarks_2 = str(input())
            
            print("")
            print("")
            
            print("***************** DATA ENTERED SUCCESSFULLY *****************")
            print("*************************************************************")
            
            print("")
            print("")
            
            c.execute("INSERT INTO TransactionTable (Id, Date, Income, Remarks_1, Expense, Remarks_2) VALUES(?, ?, ?, ?, ?, ?)", (id, date, income, remarks_1, expense, remarks_2))
            conn.commit()

        def syntax_control():
            
            x = PrettyTable(hrules = ALL)
            x.add_column("AUXILIARY MENU",["[1]: DISPLAY ANALYTICS","[2]: DISPLAY HISTORY","[3]: ENTER NEW DATA","[4]: EDIT DATA","[5]: DELETE DATA","[6]: SEARCH DATA","[E]: SAVE AND EXIT"])
            x.align = "l"
            print(x)
            print("\nRESPONSE ? ")
            TSMO = str(input())
            # TSMO means Transaction Sub Menu Option
            
            while TSMO != "1" and TSMO != "2" and TSMO != "3" and TSMO != "4" and TSMO != "5" and TSMO != "6" and TSMO != "E" and TSMO != "e":
                print("ERROR ENTER [1] OR [2] OR [3] OR [4] OR [5] OR [6] OR [E]")
                TSMO = str(input())
            
            print("")
            print("")
            
            if TSMO == "1":
                
                print("")
                print("")
                
                data_analytics()
                syntax_control()
            
            if TSMO == "2":
                
                print("")
                print("")
                
                display_data()
                syntax_control()
            
            print("")
            print("")
            
            if TSMO == "3":
                data_entry()
                syntax_control()
            
            if TSMO == "4":
                data_edit()
                syntax_control()
            
            if TSMO == "5":
                data_delete()
                syntax_control()
            
            if TSMO == "6":
                data_search()
                syntax_control()
            
            if TSMO == "E" or "e":
                
                print("**************** SAVED AND EXITED SUCCESSFULLY **************")
                print("*************************************************************")
                
                print("")
                print("")
                
                print("******************** SOFTWARE BY N.ELMER ********************")
                print("*************************************************************")
                
                sys.exit()
            
            print("")
            print("")

        def data_edit():
            
            while True:
                try:
                    print("ENTER THE RECORD ID YOU WISH TO EDIT: ")
                    target_id = int(input())
                    break
                except ValueError:
                    print("")
                    print("ERROR!!! INPUT AN INTEGER ONLY")
                    print("")
                    continue
            
            print("ENTER NEW TRANSACTION DATE: ")
            new_date = str(input())
            
            while True:
                try:
                    print("ENTER NEW INCOME AMOUNT: ")
                    new_income = int(input())
                    break
                except ValueError:
                    print("")
                    print("ERROR!!! INPUT AN INTEGER ONLY")
                    print("")
                    continue
            
            print("ENTER NEW INCOME REMARKS: ")
            new_remarks_1 = str(input())
            
            while True:
                try:
                    print("ENTER NEW EXPENSE AMOUNT: ")
                    new_expense = int(input())
                    break
                except ValueError:
                    print("")
                    print("ERROR!!! INPUT AN INTEGER ONLY")
                    print("")
                    continue
            
            print("ENTER NEW EXPENSE REMARKS: ")
            new_remarks_2 = str(input())
            
            print("")
            print("")
            
            print("***************** DATA UPDATED SUCCESSFULLY *****************")
            print("*************************************************************")
            
            print("")
            print("")
            
            c.execute("UPDATE TransactionTable set Date = ?, Income = ?, Remarks_1 = ?, Expense = ?, Remarks_2 = ? WHERE Id = ?", (new_date, new_income, new_remarks_1, new_expense, new_remarks_2, target_id))
            conn.commit()

        def data_delete():
            
            while True:
                try:
                    print("ENTER THE RECORD ID YOU WISH TO DELETE: ")
                    target_id2 = int(input())
                    break
                except ValueError:
                    print("")
                    print("ERROR!!! INPUT AN INTEGER ONLY")
                    print("")
                    continue
            
            print("")
            print("")
            
            print("******************** DATA DELETED SUCCESSFULLY **************")
            print("*************************************************************")
            
            print("")
            print("")
            
            c.execute("DELETE FROM TransactionTable WHERE Id = ?", (target_id2,))
            conn.commit()

        def data_search():
            
            print("ENTER THE SEARCH QUERRY: ")
            search = str(input())
            
            c.execute("SELECT * FROM TransactionTable WHERE Id LIKE ? OR Date LIKE ? OR Income LIKE ? OR Remarks_1 LIKE ? OR Expense LIKE ? OR Remarks_2 LIKE ?", (search, search, search, search, search, search))
            x = from_db_cursor(c, hrules = ALL)
            x.align = "l"
            
            print("")
            print("")
            
            print("************************ SEARCH RESULT **********************")
            print("*************************************************************")
            
            print("")
            print("")
            
            print(x)
            
            print("")
            print("")
            
            conn.commit()

        def display_data():
            
            print("*************************************************************")
            print("*************************************************************")
            
            print("")
            print("")
            
            c.execute("SELECT * FROM TransactionTable")
            x = from_db_cursor(c, hrules = ALL)
            x.align = "l"
            print(x)
            
            print("")
            print("")
            
            print("*************************************************************")
            print("*************************************************************")
            
            print("")
            print("")
            
            balance_computation()
            
            print("")
            print("")
            
            print("*************************************************************")
            print("*************************************************************")
            
            print("")
            print("")
            
            syntax_control()

        def balance_computation():
            
            c.execute("SELECT SUM(Income) as TOTAL_INCOME, SUM(Expense) as TOTAL_EXPENDITURE FROM TransactionTable")
            a = from_db_cursor(c)
            
            c.execute("SELECT (SUM(Income) - SUM(Expense)) as BALANCE FROM TransactionTable")
            d = from_db_cursor(c)
            
            print(a)
            print(d)

        def data_analytics():
            
            c.execute("SELECT Date, Income, Expense FROM TransactionTable")
            data = c.fetchall()
            
            Date = []
            Income = []
            Expense = []
            
            for row in data:
                Date.append(row[0])
                Income.append(row[1])
                Expense.append(row[2])
            
            plt.plot(Date,Income,"-",label="Income")
            plt.plot(Date,Expense,"--",label="Expenditure")
            leg = plt.legend();
            plt.show()
            
            print("")
            print("")

        create_table()
        display_data()
        balance_computation()
        syntax_control()
        data_edit()
        data_delete()
        data_entry()
        data_search()
        data_analytics()

        if conn:
            c.close()
            conn.close()

if MainMenu == "2":
    
    print("*********************** VIEW ANALYTICS **********************")
    print("*************************************************************")
    
    print("")
    print("")

    def data_entry():
        
        MinId = 1000
        # MinId means Minimum Transaction Id Value
        MaxID = 2000
        # MaxId means Maximum Transaction Id Value
        IdRange = [i for i in range(MinId, MaxID+1)]
        # IdRange is the range formed by the MaxId and MinId Values
        random.shuffle(IdRange)
        id = IdRange[0]
        print("TRANSACTION ID: \n",id)
        
        print("ENTER TRANSACTION DATE: ")
        date = str(input())
        
        while True:
            try:
                print("ENTER INCOME AMOUNT: ")
                income = int(input())
                break
            except ValueError:
                print("")
                print("ERROR!!! INPUT AN INTEGER ONLY")
                print("")
                continue
        
        print("ENTER INCOME REMARKS: ")
        remarks_1 = str(input())
        
        while True:
            try:
                print("ENTER EXPENSE AMOUNT: ")
                expense = int(input())
                break
            except ValueError:
                print("")
                print("ERROR!!! INPUT AN INTEGER ONLY")
                print("")
                continue
        
        print("ENTER EXPENSE REMARKS: ")
        remarks_2 = str(input())
        
        print("")
        print("")
        
        print("******************** DATA ENTERED SUCCESSFULLY **************")
        print("*************************************************************")
        
        print("")
        print("")
        
        c.execute("INSERT INTO TransactionTable (Id, Date, Income, Remarks_1, Expense, Remarks_2) VALUES(?, ?, ?, ?, ?, ?)", (id, date, income, remarks_1, expense, remarks_2))
        conn.commit()

    def syntax_control():
        
        x = PrettyTable(hrules = ALL)
        x.add_column("AUXILIARY MENU",["[1]: DISPLAY ANALYTICS","[2]: DISPLAY HISTORY","[3]: ENTER NEW DATA","[4]: EDIT DATA","[5]: DELETE DATA","[6]: SEARCH DATA","[E]: SAVE AND EXIT"])
        x.align = "l"
        print(x)
        print("\nRESPONSE ? ")
        TSMO = str(input())
        # TSMO means Transaction Sub Menu Option
        
        while TSMO != "1" and TSMO != "2" and TSMO != "3" and TSMO != "4" and TSMO != "5" and TSMO != "6" and TSMO != "E" and TSMO != "e":
            print("ERROR ENTER [1] OR [2] OR [3] OR [4] OR [5] OR [6] OR [E]")
            TSMO = str(input())
        
        print("")
        print("")
        
        if TSMO == "1":
            
            print("")
            print("")
            
            data_analytics()
            syntax_control()
        
        if TSMO == "2":
            
            print("")
            print("")
            
            display_data()
            syntax_control()
        
        print("")
        print("")
        
        if TSMO == "3":
            data_entry()
            syntax_control()
        
        if TSMO == "4":
            data_edit()
            syntax_control()
        
        if TSMO == "5":
            data_delete()
            syntax_control()
        
        if TSMO == "6":
            data_search()
            syntax_control()
        
        if TSMO == "E" or "e":
            
            print("**************** SAVED AND EXITED SUCCESSFULLY **************")
            print("*************************************************************")
            
            print("")
            print("")
            
            print("******************** SOFTWARE BY N.ELMER ********************")
            print("*************************************************************")
            
            sys.exit()
        
        print("")
        print("")

    def data_edit():
        
        while True:
            try:
                print("ENTER THE RECORD ID YOU WISH TO EDIT: ")
                target_id = int(input())
                break
            except ValueError:
                print("")
                print("ERROR!!! INPUT AN INTEGER ONLY")
                print("")
                continue
        
        print("ENTER NEW TRANSACTION DATE: ")
        new_date = str(input())
        
        while True:
            try:
                print("ENTER NEW INCOME AMOUNT: ")
                new_income = int(input())
                break
            except ValueError:
                print("")
                print("ERROR!!! INPUT AN INTEGER ONLY")
                print("")
                continue
        
        print("ENTER NEW INCOME REMARKS: ")
        new_remarks_1 = str(input())
        
        while True:
            try:
                print("ENTER NEW EXPENSE AMOUNT: ")
                new_expense = int(input())
                break
            except ValueError:
                print("")
                print("ERROR!!! INPUT AN INTEGER ONLY")
                print("")
                continue
        
        print("ENTER NEW EXPENSE REMARKS: ")
        new_remarks_2 = str(input())
        
        print("")
        print("")
        
        print("******************** DATA UPDATED SUCCESSFULLY **************")
        print("*************************************************************")
        
        print("")
        print("")
        
        c.execute("UPDATE TransactionTable set Date = ?, Income = ?, Remarks_1 = ?, Expense = ?, Remarks_2 = ? WHERE Id = ?", (new_date, new_income, new_remarks_1, new_expense, new_remarks_2, target_id))
        conn.commit()

    def data_delete():
        
        while True:
            try:
                print("ENTER THE RECORD ID YOU WISH TO DELETE: ")
                target_id2 = int(input())
                break
            except ValueError:
                print("")
                print("ERROR!!! INPUT AN INTEGER ONLY")
                print("")
                continue
        
        print("")
        print("")
        
        print("******************** DATA DELETED SUCCESSFULLY **************")
        print("*************************************************************")
        
        print("")
        print("")
        
        c.execute("DELETE FROM TransactionTable WHERE Id = ?", (target_id2,))
        conn.commit()

    def data_search():
        print("ENTER THE SEARCH QUERRY: ")
        search = str(input())
        
        c.execute("SELECT * FROM TransactionTable WHERE Id LIKE ? OR Date LIKE ? OR Income LIKE ? OR Remarks_1 LIKE ? OR Expense LIKE ? OR Remarks_2 LIKE ?", (search, search, search, search, search, search))
        x = from_db_cursor(c, hrules = ALL)
        x.align = "l"
        
        print("")
        print("")
        
        print("************************ SEARCH RESULT **********************")
        print("*************************************************************")
        
        print("")
        print("")
        
        print(x)
        print("")
        print("")
        
        conn.commit()

    def display_data():
        
        print("*************************************************************")
        print("*************************************************************")
        
        print("")
        print("")
        
        c.execute("SELECT * FROM TransactionTable")
        x = from_db_cursor(c, hrules = ALL)
        x.align = "l"
        print(x)
        
        print("")
        print("")
        
        print("*************************************************************")
        print("*************************************************************")
        
        print("")
        print("")
        
        balance_computation()
        
        print("")
        print("")
        
        print("*************************************************************")
        print("*************************************************************")
        
        print("")
        print("")
        
        syntax_control()

    def balance_computation():
        
        c.execute("SELECT SUM(Income) as TOTAL_INCOME, SUM(Expense) as TOTAL_EXPENDITURE FROM TransactionTable")
        a = from_db_cursor(c)
        
        c.execute("SELECT (SUM(Income) - SUM(Expense)) as BALANCE FROM TransactionTable")
        d = from_db_cursor(c)
        
        print(a)
        print(d)

    def data_analytics():
        
        c.execute("SELECT Date, Income, Expense FROM TransactionTable")
        data = c.fetchall()
        
        Date = []
        Income = []
        Expense = []
        
        for row in data:
            Date.append(row[0])
            Income.append(row[1])
            Expense.append(row[2])
        
        plt.plot(Date,Income,"-",label="Income")
        plt.plot(Date,Expense,"--",label="Expenditure")
        leg = plt.legend();
        plt.show()
        
        print("")
        print("")

    data_analytics()
    syntax_control()
    create_table()
    data_edit()
    data_delete()
    data_search()
    data_entry()
    display_data()
    balance_computation()

    if conn:
        c.close()
        conn.close()