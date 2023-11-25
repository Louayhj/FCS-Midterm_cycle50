import json
#function to close a tab option number 2 
# Function to close a tab (Option 2)
tabs = []

def closeTab(current_tab_index, index=None):
  while True:
    if index is None:
      index = current_tab_index
    try:#try to check the input if empty or wrong input 
      if index == "":
        index = len(tabs)  # Close the last opened tab
        index = int(index)
        index -= 1        
      if 0 <= index < len(tabs):
        closed_tab = tabs.pop(index)
        print("Tab closed: " + closed_tab["title"])
        if current_tab_index >= len(tabs):
         current_tab_index = len(tabs) - 1
        break
      else:
           print("Invalid tab index. Please try again.")
           index = input("Enter the index of the tab you want to close\n"
                                      "Leave it empty to close the last open tab: ")

    except ValueError:
      print("Invalid input. Please enter a valid integer index.")
      index = input("Enter the index of the tab to close (optional): ")

  return current_tab_index
 # Function to open a new tab (Option 1)
def newTab(title, url):
  new_tab = {"title": title, "url": url, "nested_tabs": []}
  tabs.append(new_tab)
  current_tab_index = len(tabs) - 1
  print("Tab opened: " + title)
  return current_tab_index
# Main menu function containing the options for the user to choose from
def mainMenu():
  current_tab_index = -1  # Dummy value for current tab
  choice = -99  # Dummy value
  while choice != 9:  # Taking options and ending the loop on option 9
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
     choice = int(input())
     if choice == 1:  # Opening a new tab with title and URL
       title = input("Enter the title of the website: ")
       url = input("Enter the URL: ")
       current_tab_index = newTab(title, url)
     elif choice == 2:  # Closing a tab
       index = input("Enter the index of the tab you want to close\n""Leave it empty to close the last open tab: ")                           
       current_tab_index = closeTab(current_tab_index, index)
     # elif choice == 3:
            
      # elif choice == 4:
            
      # elif choice == 5:
            
      # elif choice == 6:
         
      # elif choice == 7:
            
      # elif choice == 8:
            
     elif choice == 9:#closing the program 
            print("Thank you for using the Advanced Browser Tabs Simulation")
     else:#input less than 0 or greater than 9 
            print("Invalid input")

# Run the main menu
mainMenu()
