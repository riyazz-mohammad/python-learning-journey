
from datetime import datetime

transactions=[]
categories={
    'income':['Salary','Freelance','Business','Investment','Others'],
    'expenses':['Food','Shopping','Entertainment','Healthcare','Education','Bills','Transport','Others']
}
budget_limit={}

def display_header():

    print(f"{'='*50}")
    print("\n Personal Finance Manager")
    print(f"{'='*50}")

def get_current_date():
    return datetime.now().strftime("%Y-%m-%d")

def get_current_month():
    return datetime.now().strftime("%Y-%m")

# Transaction Functions:

def add_transaction(trans_type):
    display_header()
    print(f"Add:{trans_type.upper()}")
    #Get Amount
    while True:
        try:
            amount=float(input("Amount:$"))
            if amount<=0:
                print("Amount should be Postive!")
                continue
            break
        except ValueError:
            print("Invalid amount!")

    #Showing categories:
    print("\n Categories:")
    for i,cat in enumerate(categories[trans_type],1):
        print(f"{i}.{cat}")

    #Get categories:
    while True:
        try: 
          chioce=int(input("Enter the choice(numbers):"))
          if 1<=chioce<=len(categories[trans_type]):
               category=categories[trans_type][chioce-1]
               break
          else:
              print("Inavlid Choice!")
        except ValueError:
            print("Invalid Input!")

    decription=input("Enter Description:")

    transactions={
        "id":len(transactions)+1,
        'date':get_current_date,
        'type':trans_type,
        'category':category,
        'amount':amount,
        'decription':decription
                }
    transactions.append(transactions)
    print(f"\n{trans_type.title()} of $:{amount} added successfully!")

    # Budget warning for expenses
    #code required..


def view_all_transactions():
    if not transactions:
        print("\n No transactions record!")
        return
    display_header()
    print(f"All Transations (Total:{len(transactions)})")
    print(f"{'-'*80}")
    print(f"\n{'ID':<5}{'Date':<12}{'Type':<10}{'Category':<15}{'Amount':<20}'Description'")
    print('-'*80)
    for trans in transactions:
        trans_sym='+'if trans['category']=='income' else '-'
        print(f"{trans['id']:.5}{trans['date']:<12}{trans['type']:<10}{trans['category']:<15}{trans_sym}${trans['amount']:<20}{trans['description']}")
print("-"*80)


def calculate_balance():
    total_income=sum(t['amount']for t in transactions if t['category']=='income')
    total_expenses=sum(t['amount']for t in transactions if t['category']=='expenses')
    balance=total_income-total_expenses

    print(f"\n===FINANCIAL SUMMARY===")
    print("\n -"*50)
    print(f"Total Income:${total_income:.2f}")
    print(f"Total Expenses:${total_expenses}:.2f")
    print("-"*40)

    if balance>0:
        print(f"Current Balance :${balance:.2f}")
    else:
        print(f" Current Balance:${balance} Defficit!")

    if total_income>0:
        saving_rate=(balance/total_income)*100
        print(f"Saving Rate:${saving_rate:.1f}%")
    return balance

def category_breakdown():
    if not transactions:
        print("\nNo Transaction record!")
        return
    display_header()
    print("\nCATEGORY-WISE BREAKDOWN")
    print("\n=Income=")
    income_by_cat={}
    for tran in transactions:
        if tran['type']=='income':
            cat=tran['category']
            income_by_cat[cat]=tran.get(cat,0)+tran['amount']

    if income_by_cat:
        for cat,amount in sorted(income_by_cat.items(),key=lambda x:x[1],reverse=True):
            print(f"{cat:<20}${amount:.2f}")
        print(f"{'Total':<20}${sum(income_by_cat.values()):,.2f}")
    else:
        print("No Income records!")

    print("\n=Expenses=")
    expenses_by_cat={}
    for tran in transactions:
        if tran['type']=='expenses':
            cat=tran['category']
            expenses_by_cat[cat]=tran.get(cat,0)+tran['amount']
    if expenses_by_cat:
        total_expenses=sum(expenses_by_cat.values())
        for cat,amount in sorted(expenses_by_cat.items(),key=lambda x:x[1],reverse=True):
            percentage=(amount/total_expenses)*100
            print(f"{cat:<20}${amount:.2f}({percentage:.1f}%)")
        print(f"{'Total':<20}${sum(expenses_by_cat.values()):,.2f}")
    else:
        print("No Expenses record")

def monthly_summary():
    current_month=get_current_month()
    monthly_transaction=[t for t in transactions if t['date'].startwith(current_month)]

    if not monthly_transaction:
        print(f"No transaction record for {current_month}")
        return
    display_header()
    print(f"\nMONTHLY SUMMARY - {current_month}")
    print('-'*40)
    month_income=sum(t['amount'] for t in monthly_transaction if t['type']=='income')
    month_expenses=sum(t['amount']for t in monthly_transaction if t['type']=='expenses')
    month_balance=month_income-month_expenses
    print(f"Month Income:${month_income:,.2f}")
    print(f"Month Expenses:${month_expenses:,.2f}")
    print(f"Month Balnce:${month_balance:,.2f}")
    print(f"Transactions: {len(monthly_transaction)}")
    if month_expenses>0:
        print("\n Top Spending Categories:")
        cat_expenses={}
        for tran in monthly_transaction:
            if tran['type']=='expenses':
                cat=tran['category']
                cat_expenses[cat]=tran.get(cat,0)+tran['amount']

        for cat,amount in sorted(cat_expenses.items(),key=lambda x:x[1],reverse=True)[:3]:
            percentage=(amount/month_expenses)*100
            print(f"{cat}:${amount:.2f}({percentage:.1f}%)")




    
        
    





    



        

        
      
        
       

        

    

 
        
