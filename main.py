from logger import *
from Functions import *
import os

Manager_Menu = ["1. Add New Customer", "2. Edit Customer Information", "3. Add New Employee", "4. Edit Employee Information", 
"5. Add New Item to Inventory", "6. Add Raw Materials to Inventory", "7. Raw Material Purchase Invoices Reporting", 
"8. Sell Products", "9. Sales Invoices Reporting", "10. Add New Menu Item", "11. Edit a Menu Item", "12. Delete a Menu Item", "13. Exit"]

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    for i in Manager_Menu:
        print(i)

    try:
        user_selection = int(input("Enter the desired option: "))

        match user_selection:
            case 1:
                product_name = input("bla bla bla: ")
                Add_New_Customer()
            case 2:
                product_name = input("bla bla bla: ")
                Edit_Customer_Information()
            case 3:
                product_name = input("bla bla bla: ")
                Add_New_Employee()
            case 4:
                product_name = input("bla bla bla: ")
                Edit_Employee_Information()
            case 5:
                product_name = input("bla bla bla: ")
                Add_New_Item_to_Inventory()
            case 6:
                product_name = input("bla bla bla: ")
                Add_Raw_Materials_to_Inventory()
            case 7:
                product_name = input("bla bla bla: ")
                Raw_Material_Purchase_Invoices_Reporting()
            case 8:    
                product_name = input("bla bla bla: ")
                Sell_Products()
            case 9:    
                product_name = input("bla bla bla: ")
                Sales_Invoices_Reporting()
            case 10:
                product_name = input("bla bla bla: ")
                Add_New_Menu_Item()
            case 11:    
                product_name = input("bla bla bla: ")
                Edit_a_Menu_Item()
            case 12:
                product_name = input("bla bla bla: ")
                Delete_a_Menu_Item()
            case 13:    
                break
            
    except ValueError:
        print("Invalid input")
        temp = input("press any key to continue: ")

##########################################################################################################################
# todo: write a function for any task
"""
Manager_Menu:

1. Add New Customer
2. Edit Customer Information

3. Add New Employee
4. Edit Employee Information

5. Add New Item to Inventory

6. Add Raw Materials to Inventory --->  First, get the raw material purchase invoice information and save it in its own file (Raw Material Purchase Invoices), 
                                        then add the material to the inventory file.
7. Raw Material Purchase Invoices Reporting

8. Sell Product --->    First, issue the sales invoice and save it in its own file (sales_invoices), 
                        then deduct the raw materials required for that item from the inventory file (inventory).
                        Then, display the invoice for printing.
9. Sales Invoices Reporting

10. Add New Menu Item
11. Edit a Menu Item
12. Delete a Menu Item
13. Exit

#   فقط از فاکتور ها گزارش میگیریم, از بقیه فایل ها گزارش نمیگیریم
#   (بجر بعضی آیتم های منو که دیگه سرو نمیشن) هیچ اطلاعاتی رو حذف نمیکنیم
#   بعد از هر کاری که کردیم در لاگ زخیره میکنیم     
#   OK همه شو نوشتم و مطمعنم که همیناست و دیگه چیزی اضافه نمیشه و کم هم نمیشه
"""

