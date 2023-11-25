import json
#function to close a tab option number 2 
# Function to close a tab (Option 2)
tabs = []
def closeTab(current_tab_index, index=None):
  while True:
      if index is None:
          index = current_tab_index

      try:#added the try and except and the while loop to prevent user from entering an index that is not available 
          index = int(index)  # Convert the input index to an integer
          index -= 1  # Adjust for 1-based index input

          if 0 <= index < len(tabs):
              closed_tab = tabs.pop(index)
              print("Tab closed: " + closed_tab["title"])
              if current_tab_index >= len(tabs):
                  current_tab_index = len(tabs) - 1
              break  # Break out of the loop if the operation is successful
          else:
              print("Invalid tab index. Please try again.")
              index = input("Enter the index of the tab you want to close  \n leave it empty to close the last open tab : ")

      except ValueError:
          print("Invalid input. Please enter a valid integer index.")
          index = input("Enter the index of the tab to close (optional): ")

  return current_tab_index



#function to open a new tab option number 1
def newTab(title, url):
    new_tab = {"title": title, "url": url, "nested_tabs": []}
    tabs.append(new_tab)
    current_tab_index = len(tabs) - 1
    print("Tab opened: " + title)
    return current_tab_index


#main menu function containing the options for the user to choose from
def mainMenu():
    current_tab_index = -1 #dummy value for current tab 
    choice = -99  # dummy value

    while choice != 9: # taking options and ending the loop on option 9
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
      if choice == 1:#opening a new tab with title and url 
            title = input("Enter the title of the website: ")
            url = input("Enter the URL: ")
            current_tab_index = newTab(title, url)
              
      elif choice == 2:#closing a tab 
            index = input("Enter the index of the tab you want to close leave it empty to close the last open tab : ")
            current_tab_index = closeTab(current_tab_index, index)
     # elif choice == 3:
            
      # elif choice == 4:
            
      # elif choice == 5:
            
      # elif choice == 6:
         
      # elif choice == 7:
            
      # elif choice == 8:
            
      elif choice == 9:#closin the program 
            print("Thank you for using the Advanced Browser Tabs Simulation")
      else:#input less than 0 or greater than 9 
            print("Invalid input")

# Run the main menu
mainMenu()
