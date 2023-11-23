#function to open a new tab option number 1 
def newTab(title,url):
  
#main menu function containing the options for the user to choose from 
def mainMenu(items):
  tab={}
  choice=-99 # dummy value
  while choice !=9:
    print("Welcome to the Advanced Browser Tabs Simulation")
    print("Enter")
    print("1. Open Tab")
    print("2. Close Tab")
    print("3. Switch Tab")
    print("4. Display All Tabs")
    print("5. Open Nested Tab")
    print("6. Sort All Tabs")
    print("7. Save Tabs")
    print("8. Import Tabs")
    print("9. Exit")

    choice=int(input())

    if choice==1:
      newTab(title,url)
    elif choice ==2:
      
    elif choice ==3:
      
    elif choice ==4:
      
    elif choice ==5:
      
    elif choice ==6:
      
    elif choice ==7:
      
    elif choice ==8:
      
    elif choice ==9:
      
    else:
      print("ivalid input")
