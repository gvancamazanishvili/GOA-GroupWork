print("Welcome to our Bank!")



# ანამარია კაბულაშვილი

# სესხის გაცემა 
def loan_disbursement():
    print("სესხის განაცხადი\n")
    
    # პერსონალური ინფორმაციის შეტანა
    first_name = input("შეიყვანეთ თქვენი სახელი: ")
    last_name = input("შეიყვანეთ თქვენი გვარი: ")
    personal_id = input("შეიყვანეთ თქვენი პირადი ID: ")
    
    # სესხის ტიპები 
    print("აირჩიეთ სესხის ტიპი:")
    print("1. პირადი სესხი")
    print("2. ბიზნეს სესხი")
    print("3. იპოთეკური სესხი")
    loan_type_choice = input("Enter 1, 2, or 3: ")

    if loan_type_choice == "1":
        loan_type = "პირადი სესხი"
    elif loan_type_choice == "2":
        loan_type = "ბიზნეს სესხი"
    elif loan_type_choice == "3":
        loan_type = "იპოთეკური სესხი"
    else:
        loan_type = "უცნობი სესხის ტიპი"
        loan_type_choice = input("აირჩიეთ რომელიმე ზემოთ ჩამოთვლილი სესხის ტიპები: (1-3) ")

    
    # სესხის თანხის კითხვა
    amount = input("შეიყვანეთ სესხის ოდენობა: ")

    # წარმატების შეტყობინება
    print(f"\nწარმატებით დასრულდა {loan_type} სესხის აღება {amount} თანხით")


def process_payment():
    print(" სესხის გადახდა")
    
    # პირადი  ინფორმაცია
    first_name = input("შეიყვანეთ თქვენი სახელი: ")
    last_name = input("შეიყვანეთ თქვენი გვარი: ")
    personal_id = input("შეიყვანეთ თქვენი პირადი ID: ")
    
    # სესხის რაოდენობა და გადახდა 
    loan_amount = float(input("შეიყვანეთ თქვენი სესხის ოდენობა: "))
    payment = float(input("შეიყვანეთ თქვენი გადახდის ოდენობა: "))
    
    # შედეგი
    if payment >= loan_amount:
        print(f"\n{first_name}, თქვენი სესხი სრულად არის გადახდილი ")
        if payment > loan_amount:
            print(f"თქვენი ხურდა: {payment - loan_amount} USD")
    else:
        print(f"\n{first_name}, შენ ჯერ კიდევ ვალი გაქვს: {loan_amount - payment} ")






# გვანცა მაზანიშვილი


# ვალუტის გაცვლა
def currency_exchange():
    print("ვალუტის გაცვლა\n")
    

    # ვინახავთ იმ ინფორმაციებს {} ფრჩხილებში რითაც შემდეგ შეგვიძლია ჩავწვდეთ მას [] ფრჩხილებით
    exchange_rates = {
        "დოლარიდან ლარში": 2.68,
        "ევროდან ლარში": 2.91,
        "ფუნტიდან ლარში": 3.39,
        "ლარიდან დოლარში": 0.37,
        "ლარიდან ევროში": 0.34,
        "ლარიდან ფუნტში": 0.29
    }

    # ვარჩევინებთ მომხმარებელს რომელი ტიპის გაცვლა სურს
    print("აირჩიეთ გაცვლის ტიპი:")
    print("1. დოლარიდან ლარში")
    print("2. ევროდან ლარში") 
    print("3. ფუნტიდან ლარში")
    print("4. ლარიდან დოლარში")
    print("5. ლარიდან ევროში")
    print("6. ლარიდან ფუნტში")
    
    choice = input("აირჩიეთ ვარიანტი (1-6): ")
    amount = float(input("შეიყვანეთ გასაცვლელი თანხა: "))
    
    # იმისთვის რომ გამოვიანგარისოთ თუ რამდენი უნდა დავუბრუნოთ მომხმარებელს რაოდენობა ფულის უნდა გავამრავლოთ იმ ფულის გაცვლის ტიპთან რომელიც აირჩია რომელსაც ვაკავშირებთ []-ი ფრჩხილებით


    if choice == "1":
        result = amount * exchange_rates["დოლარიდან ლარში"]
        print(f"\n{amount} დოლარი $ = {result:.2f} ლარი ")
    elif choice == "2":
        result = amount * exchange_rates["ევროდან ლარში"]
        print(f"\n{amount} ევრო = {result:.2f} ლარი")
    elif choice == "3":
        result = amount * exchange_rates["ფუნტიდან ლარში"]
        print(f"\n{amount} ფუნტი = {result:.2f} ლარი")
    elif choice == "4":
        result = amount * exchange_rates["ლარიდან დოლარში"]
        print(f"\n{amount} ლარი = {result:.2f} დოლარი $")
    elif choice == "5":
        result = amount * exchange_rates["ლარიდან ევროში"]
        print(f"\n{amount} ლარი = {result:.2f} ევრო")
    elif choice == "6":
        result = amount * exchange_rates["ლარიდან ფუნტში"]
        print(f"\n{amount} ლარი = {result:.2f} ფუნტი")
    else:
        print("არასწორი არჩევანი!")
        choice = input("აირჩიეთ ვარიანტი (1-6): ")
        amount = float(input("შეიყვანეთ გასაცვლელი თანხა: "))

        
    


    # საკომისიოს გამოთვლა ანუ ბანკის მომსახურების საფასური ამ შემთხვევაში ეს არის მოწოდებული თანხის 2%
    commission = result * 0.02
    final_amount = result - commission
    print(f"კომისია (2%): {commission:.2f}")
    print(f"საბოლოო თანხა: {final_amount:.2f}")
    print("გაცვლა წარმატებით დასრულდა!")


# კომინალური გადასახადები

def utility_bills():
    print("კომუნალური გადასახადები\n")


    # მომხმარებელს ვაწვდით გადასახადების ჩამონათვალს
    print("1. ელექტრო ენერგია")
    print("2. წყალი")
    print("3. ინტერნეტი")
    print("4. გაზი")
    print("5. საკაბელო ტელევიზია")
    print("6. ტელეფონი")

    choice = input("აირჩიეთ ვარიანტი (1-6): ")

    if choice == "1":
        choice = "ელექტრო ენერგია"
    elif choice == "2":
        choice = "წყალი"
    elif choice == "3":
        choice = "ინტერნეტი"
    elif choice == "4":
        choice = "გაზი"
    elif choice == "5":
        choice = "საკაბელო ტელევიზია"
    elif choice == "6":
        choice = "ტელეფონი"
        number = input("შეიყვანეთ თქვენი ნომერი: ")

    first_name = input("შეიყვანე თქვენი  სახელი: ")
    last_name = input("შეიყვანეთ თქვენი გვარი: ")
    pay = float(input("შეიყვანეთ თქვენი თანხა: "))
    print("წარმატებით გადაიხადე თანხა")






# მატა ნემსიწვერიძე



def insurance_services():
    # ჩვენ ვაჩვენებთ მომხმარებელს სერვისების ჩამონათვალს
    print("სერვისების ტიპები:")
    print("1. სიცოცხლის დაზღვევა")
    print("2. უძრავი ქონების დაზღვევა")
    print("3. ავტომობილის დაზღვევა")
    print("4. სამედიცინო დაზღვევა")

    # მომხმარებლისგან სერვისის არჩევა
    choice = input("გთხოვთ, აირჩიოთ სერვისის ნომერი (1-4): ")

    if choice == '1':
        service_name = "სიცოცხლის დაზღვევა"
    elif choice == '2':
        service_name = "უძრავი ქონების დაზღვევა"
    elif choice == '3':
        service_name = "ავტომობილის დაზღვევა"
    elif choice == '4':
        service_name = "სამედიცინო დაზღვევა"
    else:
        print("არასწორი არჩევანი. სცადეთ თავიდან.")
        choice = input("გთხოვთ, აირჩიოთ სერვისის ნომერი (1-4): ")

    print(f"თქვენ აირჩიეთ: {service_name}")

    # პირადი მონაცემების შეგროვება
    first_name = input("შეიყვანეთ თქვენი სახელი: ")
    last_name = input("შეიყვანეთ თქვენი გვარი: ")
    personal_id = input("შეიყვანეთ თქვენი პირადი ნომერი: ")
    phone_number = input("შეიყვანეთ თქვენი ტელეფონის ნომერი: ")
    email = input("შეიყვანეთ თქვენი ელფოსტა: ")

    print("მიღებული ინფორმაცია")

def deposit():
# ანგარიშის ტიპის არჩევა
    print("აირჩიეთ ანგარიშის ტიპი")
    print("1. მიმდინარე ანგარიში")
    print("2. შემნახველი ანგარიში")
    print("3. ყოველდღიური დეპოზიტი")
    account_choice = input("შეიყვანეთ ნომერი (1-3): ")

    # არჩევანის მიხედვით ანგარიშის ტიპის განსაზღვრა

    if account_choice == '1':
        account_type = "მიმდინარე ანგარიში"
    elif account_choice == '2':
        account_type = "შემნახველი ანგარიში"
    elif account_choice == '3':
        account_type = "ყოველდღიური დეპოზიტი"
    else:
        print("არასწორი არჩევანი")
    
    # ვადის არჩევა
    print("აირჩიეთ ვადა")
    print("1. 1-12 თვე (მოკლევადიანი)")
    print("2. 1-3 წელი (საშუალოვადიანი)")
    print("3. მეტი წელი (გრძელვადიანი)")
    term_choice = input("შეიყვანეთ ნომერი (1-3): ")

    # ვადის განსაზღვრა არჩევანის მიხედვით
    if term_choice == '1':
        term = "1-12 თვე"
    elif term_choice == '2':
        term = "1-3 წელი"
    elif term_choice == '3':
        term = "მეტი წელი"
    else:
        print("არასწორი არჩევანი")  # შეცდომა თუ არასწორი ნომერი შეიყვანა
        return
    
    # პირადი მონაცემების შეყვანა
    print("შეიყვანეთ პირადი ინფორმაცია")
    first_name = input("სახელი: ")
    last_name = input("გვარი: ")
    personal_id = input("პირადი ნომერი: ")
    phone = input("ტელეფონის ნომერი: ")
    email = input("ელფოსტა: ")


    # მონაცემების გამოტანა
    print("თქვენი მოთხოვნა:")
    print("ანგარიშის ტიპი:", account_type)
    print("სახელი:", first_name)
    print("გვარი:", last_name)
    print("პირადი ნომერი:", personal_id)
    print("ტელეფონი:", phone)
    print("ელფოსტა:", email)







# გვანცა მაზანიშვილი

# ბანკის სისტემა
def bank_system():
    print("გთხოვთ აირჩიოთ სერვისის ნომერი:")
    
    # ბანკის სერვისის ტიპები
    print("1. სესხების გაცემა")
    print("2. გადახდების დამუშავება")
    print("3. ვალუტის გაცვლა")
    print("4. კომუნალური გადასახადები")
    print("5. სადაზღვევო სერვისები")
    print("6. დეპოზიტების მიღება")

    type_service = input("\nაირჩიე მომსახურების ტიპი (1-6): ")


    if type_service == "1":
        print("თქვენ აირჩიეთ სესხის აღება")
        loan_disbursement()  # ვაკავშირებთ დაწერის ფუნქციებს მთავარი ფუნქციის ჩონჩხთან
    elif type_service == "2":
        print("თქვენ აირჩიეთ გადახდების დამუშავება")
        process_payment()    
    elif type_service == "3":
        print("თქვენ აირჩიეთ ვალუტის გაცვლა")
        currency_exchange()
    elif type_service == "4":
        print("თქვენ აირჩიეთ კომისიური სერვისები")
        utility_bills()
    elif type_service == "5":
        print("თქვენ აირჩიეთ სადაზღვეო სერვისები")
        insurance_services()
    elif type_service == "6":
        print("თქვენ აირჩიეთ დეპოზიტების მიღება")
        deposit()

    else:
        print("თქვენი შემოტანილი ნომრის შესაბამისი სერვისი არ გვაქვს სცადეთ ხელახლა")
        type_service = input("\nაირჩიე მომსახურების ტიპი (1-6): ")


# ვუშვებთ მთავარ ფუნქციას
bank_system()
