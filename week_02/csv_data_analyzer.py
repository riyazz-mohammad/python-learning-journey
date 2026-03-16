import csv
from datetime import datetime

def create_sample_csv():
    sales_data = [
        ['Date', 'Product', 'Category', 'Quantity', 'Price', 'Revenue'],
        ['2026-03-01', 'Laptop', 'Electronics', '5', '50000', '250000'],
        ['2026-03-01', 'Mouse', 'Electronics', '20', '500', '10000'],
        ['2026-03-02', 'Keyboard', 'Electronics', '15', '1500', '22500'],
        ['2026-03-02', 'Chair', 'Furniture', '8', '5000', '40000'],
        ['2026-03-03', 'Desk', 'Furniture', '3', '15000', '45000'],
        ['2026-03-03', 'Monitor', 'Electronics', '10', '12000', '120000'],
        ['2026-03-04', 'Phone', 'Electronics', '25', '30000', '750000'],
        ['2026-03-04', 'Tablet', 'Electronics', '12', '20000', '240000'],
        ['2026-03-05', 'Headphones', 'Electronics', '30', '2000', '60000'],
        ['2026-03-05', 'Sofa', 'Furniture', '2', '25000', '50000']
    ]
       
    with open('sales_data.csv','w') as file:
              writer=csv.writer(file)
              writer.writerows(sales_data)
    print("Sample csv created:sales_data.csv")


def read_csv(filename):
       try:
              with open(filename,'r')as file:
                     reader=csv.DictReader(file)
                     data=list(reader)
              print(f"Loaded {len(data)} rows from {filename}")
              return data
       except FileNotFoundError:
              print(f"Error:file '{filename}' not found!")
              return []
def display_data(data):
       if not data:
              print("No data found!")
       header=list(data[0].keys())

       print("\n"+"="*60)
       header_format="".join([f"{h:<15}" for h in header])
       print(header_format)
       print("-"*80)

       for row in data:
              row_format=''.join([f"{row[h]:<15}" for h in header])
              print(row_format)
       print("="*80)

def calculate_statistics(data,column):
       if not data:
              print("No data found!")
              return
       try:
              values=[float(row[column]) for row in data]
              total=sum(values)
              average=total/len(values)
              minimum=min(values)
              maximum=max(values)

              print(f"\n STATISTICS FOR {column}")
              print("-"*40)
              print(f"Total:{total:.2f}")
              print(f"Average:{average:.2f}")
              print(f"Minimum:{minimum}")
              print(f"Maximum:{maximum}")
              print(f"Count:{len(values)}")
              print("-"*40)
       except(ValueError,KeyError) as e:
              print(f"Error: {e}")
              print("Make sure the column exists and contains numbers!")
def filter_data(data,column,operator,value):
       """
    Filter data based on condition
    
    NEW: List comprehension with conditions
    Operators: '>', '<', '>=', '<=', '==', '!='
    """
       try:
              filtered=[]
              for row in data:
                     row_value=float(row[column])
                     compare_value=float(value)

                     if operator == '>':
                            if row_value>compare_value:
                                   filtered.append(row)
                     elif operator == '<':
                            if row_value < compare_value:
                                   filtered.append(row)
                     elif operator == '>=':
                            if row_value >= compare_value:
                                   filtered.append(row)
                     elif operator == '<=':
                            if row_value <= compare_value:
                                   filtered.append(row)
                     elif operator == '==':
                            if row_value == compare_value:
                                   filtered.append(row)
                     elif operator == '!=':
                            if row_value != compare_value:
                                   filtered.append(row)
              print(f"Found {len(filtered)} rows where {column} {operator} {value}")
              return filtered
       except(ValueError,KeyError)as e:
              print(f"Error:{e}")
              return []
def sort_data(data,column,reverse=False):
       try:
              sorted_data=sorted(data,key=lambda row:float(row[column]),reverse=reverse)
              order="descending" if reverse else "ascending"
              print(f"\n Data sorted by '{column}' ({order})")
              return sorted_data
       except(ValueError,KeyError) as e:
              print(f"Error :{e}")
              return data
def group_by_category(data,category_column,value_cloumn):
       try:
              group={}
              for row in data:
                     category=row[category_column]
                     value=float(row[value_cloumn])
                     if category not in group:
                            group[category]=0
                     group[category]+=value
              print(f"GROUPED BY '{category_column}'")
              print("-"*40)
              for category,total in sorted(group.items(),key=lambda x:x[1],reverse=True):
                     print(f"{category:<20}{total:.2f}")
              print("-"*40)
       except (ValueError,KeyError) as e:
              print(f"Erroe:{e}")
def generate_report(data,filename='report.txt'):
       if not data:
              print("No data to report!")
              return
       try:
              with open(filename,'w',encoding='utf-8') as file:
                     file.write("="*60+"\n")
                     file.write("DATA ANALYSIS REPORT\n")
                     file.write(f"   Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                     file.write("="*60 + "\n\n")
                     file.write(f"Total Records:{len(data)}\n")
                     revenues=[float(row['Revenue'])for row in data]
                     file.write("REVENUE ANALYSIS:\n")
                     file.write("-"*40 + "\n")
                     file.write(f"Total Revenue:   ${sum(revenues):,.2f}\n")
                     file.write(f"Average Revenue: ${sum(revenues)/len(revenues):,.2f}\n")
                     file.write(f"Highest Sale:    ${max(revenues):,.2f}\n")
                     file.write(f"Lowest Sale:     ${min(revenues):,.2f}\n\n")
                     categories={}
                     for row in data:
                            cat=row['Category']
                            rev=float(row['Revenue'])
                            categories.get(cat,0)+rev
                     file.write("CATEGORY BREAKDOWN:\n")
                     file.write("-"*40+"\n")
                     for cat,total in sorted(categories.items(),key=lambda x:x[1],reverse=True):
                            percentage=(total/sum(revenues))*100
                            file.write(f"{cat:<20}${total:>12,.2f}({percentage:>5.1f})%\n")
              print(f"Report generated sucessfully!:{filename}")
       except Exception as e:
              print(f"Error generating report:{e}")

def find_top_items(data,column,n=5):
      try:
            sorted_data=sorted(data,key=lambda row:float(row[column]),reverse=True)
            top_n=sorted_data[:n]
            print(f"\n🏆 TOP {n} BY '{column}'")
            print("-" * 60)
            display_data(top_n)
        
      except Exception as e:
              print(f"❌ Error: {e}")
def compare_columns(data,col1,col2):
      try:
            values1=[float(row[col1]) for row in data]
            values2=[float(row[col2]) for row in data]
            print(f"\n📊 COMPARISON: {col1} vs {col2}")
            print("=" * 60)
            print(f"{'Metric':<20} {col1:>15} {col2:>15}")
            print("-" * 60)
            print(f"{'Total':<20} {sum(values1):>15,.2f} {sum(values2):>15,.2f}")
            print(f"{'Average':<20} {sum(values1)/len(values1):>15,.2f} {sum(values2)/len(values2):>15,.2f}")
            print(f"{'Maximum':<20} {max(values1):>15,.2f} {max(values2):>15,.2f}")
            print(f"{'Minimum':<20} {min(values1):>15,.2f} {min(values2):>15,.2f}")
            print("=" * 60)
        
      except Exception as e:
        print(f"❌ Error: {e}")

def display_menu():
    """Display main menu"""
    print("\n" + "=" * 60)
    print("📊 CSV DATA ANALYZER")
    print("=" * 60)
    print("1. Create Sample CSV")
    print("2. Load CSV File")
    print("3. Display Data")
    print("4. Calculate Statistics")
    print("5. Filter Data")
    print("6. Sort Data")
    print("7. Group by Category")
    print("8. Generate Report")
    print("9. Find top N items")
    print("10. Compare columns")
    print("11. Exit")
    print("=" * 60)


def main():
    """Main program loop"""
    print("\n🎉 Welcome to CSV Data Analyzer!")
    
    data = []
    
    while True:
        display_menu()
        
        try:
            choice = int(input("\nEnter choice (1-9): "))
            
            if choice == 1:
                create_sample_csv()
                
            elif choice == 2:
                filename = input("Enter CSV filename: ")
                data = read_csv(filename)
                
            elif choice == 3:
                if not data:
                    print("❌ Load CSV first!")
                    continue
                display_data(data)
                
            elif choice == 4:
                if not data:
                    print("❌ Load CSV first!")
                    continue
                column = input("Enter column name: ")
                calculate_statistics(data, column)
                
            elif choice == 5:
                if not data:
                    print("❌ Load CSV first!")
                    continue
                column = input("Enter column name: ")
                operator = input("Enter operator (>, <, >=, <=, ==, !=): ")
                value = input("Enter value: ")
                filtered = filter_data(data, column, operator, value)
                if filtered:
                    display_data(filtered)
                    
            elif choice == 6:
                if not data:
                    print("❌ Load CSV first!")
                    continue
                column = input("Enter column to sort by: ")
                order = input("Descending? (yes/no): ").lower()
                data = sort_data(data, column, reverse=(order == 'yes'))
                display_data(data)
                
            elif choice == 7:
                if not data:
                    print("❌ Load CSV first!")
                    continue
                category_col = input("Enter category column: ")
                value_col = input("Enter value column to sum: ")
                group_by_category(data, category_col, value_col)
                
            elif choice == 8:
                if not data:
                    print("❌ Load CSV first!")
                    continue
                generate_report(data)
            elif choice == 9:
               if not data:
                    print("❌ Load CSV first!")
                    continue
               column = input("Enter column name: ")
               N = int(input("Enter value: "))
               find_top_items(data,column,N)

            elif choice == 10:
                  if not data:
                        print("Load CSV first!")
                        continue
                  column1=input("Enter the column name(1): ")
                  column2=input("Enter the column name(2): ")
                  compare_columns(data,column1,column2)
        
        
    
                
            elif choice == 11:
                print("\n👋 Goodbye!")
                break
                
            else:
                print("❌ Invalid choice! Choose 1-9")
                
        except ValueError:
            print("❌ Invalid input! Enter a number")


if __name__ == "__main__":
    main()
              



  
  
     
       
       




       
            
    