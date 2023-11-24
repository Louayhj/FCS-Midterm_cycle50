import json
#function to open a new tab option number 1 
def newTab(title,url):
   newTab={"title":title,"url":url}
   tab.update(newTab)
   current_tab_index = len(tab) - 1
   print("Tab opened: " + title)
   return tab, current_tab_index

  
#main menu function containing the options for the user to choose from 
def mainMenu():
  
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
      title = input("Enter the title of the website: ")
      url = input("Enter the URL: ")
      newTab(title,url)
    elif choice ==2:
      print("bye bye")
    else:
      print("ivalid input")
tab= {}
mainMenu()
