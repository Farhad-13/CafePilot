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

while True:
    for i in Manager_Menu:
        print(i)

    user_selection = int(input("Enter the desired option: "))
    if user_selection == 1:
        product_name = input("bla bla bla: ")
    elif user_selection == 2:
        product_name = input("Ebla bla bla: ")
    else:
        break
