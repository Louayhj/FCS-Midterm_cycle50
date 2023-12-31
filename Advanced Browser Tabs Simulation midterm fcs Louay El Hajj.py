#Louay El Hajj 
#FCS Cycle-50
#Midterm 

#lbraries imported for json and web scraping 
#URL used for web scraping code snippet help : https://www.geeksforgeeks.org/python-web-scraping-beautiful-soup/

import json # json library 
from bs4 import BeautifulSoup  # for web scraping 
import requests  # to perform html requests 
import re # regular expression library
tabs = [] #initiating empty tab

#function to import tabs from file option 8
def importTabs(filePath): #Time Complexity: big O(n), where n is the number of elements in the fil
  try:#used try and except to prevent error such as data types and file not found
      with open(filePath, 'r') as file:  #(openning file in read mode )used with open to close the file automatically
          loaded_tabs = json.load(file)  #loading the files
          tabs.extend(loaded_tabs)
      print("Tabs loaded from:", filePath)
  except FileNotFoundError:
      print("File not found. Please enter a valid file path.")
  except json.JSONDecodeError:
      print("Error decoding JSON. Please ensure the file contains valid JSON data.")
  except Exception as e: #https://docs.python.org/3/tutorial/errors.html
      print("An error occurred:", str(e))

#function to save tabs to json files option 7 
def saveTabs(tabs,filePath):#Time Complexity: big O(n), where n is the number of elements in the tabs list.
  #used the with open function instead the open so the file will automatically close at the end 
  with open(filePath, 'w') as file:#opening a file in write mode ('w')
    json.dump(tabs, file, indent=4)#indent is the number of spaces to make it more readable 
    print("Tabs saved in:", filePath)#output of the success of saving in right path

#function to sort all tabs (option6)
#using selection sort 
def sortTabs(tabs):
    n = len(tabs)
    for border in range(n - 1):#Time Complexity:  big O(n^2), where n is the number of elements in the tabs list
        min_index = border # contain the index of the minimum element
        for i in range(border + 1, n):# to find the index of the minimum element
           if tabs[i]["title"] < tabs[min_index]["title"]:
                min_index = i
             # Swap the two elements
        tabs[border], tabs[min_index] = tabs[min_index], tabs[border]
    print("Tabs sorted based on titles.")

# Function to open a nested tab (Option 5)
def openNestedTab(current_tab_index): #Time Complexity:big O(1)
    index = int(input("Enter the index of the parent tab: "))
    if 0 <= index < len(tabs):#checking if the input is in range 
        title = input("Enter the title of the website: ")
        url = input("Enter the URL: ")
        new_tab = {"title": title, "url": url, "nested_tabs": []}#Append the new tab to the list of nested tabs
        tabs[index]["nested_tabs"].append(new_tab)
        print("Nested tab opened: " + title)
    else:
        print("Invalid parent tab index.")
    return current_tab_index

# Function to display all tabs (Option 4)
def displayAllTabs():# Time Complexity: big O(n), where n is the number of elements in the tabs list
    for i, tab in enumerate(tabs):
        print("{}. {}".format(i + 1, tab["title"]))
        if tab["nested_tabs"]:
            displayNestedTabs(tab["nested_tabs"], i + 1)

# Function to display nested tabs related to option 4
#Time Complexity: bigO(n), where n is the number of elements in the nested_tabs list
def displayNestedTabs(nested_tabs, parent_index):#https://www.w3schools.com/python/ref_string_format.asp
    for j, nested_tab in enumerate(nested_tabs):
        print("   {}.{}. {}".format(parent_index, j + 1, nested_tab["title"]))
        if nested_tab["nested_tabs"]:
            displayNestedTabs(nested_tab["nested_tabs"], parent_index)

# Function to switch tabs (Option 3)
#URL used for web scraping code snippet help : https://www.geeksforgeeks.org/python-web-scraping-beautiful-soup/
# please use https:// format to test the scraping 
def switch_tabs(current_tab_index, index=None):#Time Complexity:big O(1)
  global tabs #used global variable to detect the last opened tab 
  if not tabs:
      print("No tabs available.")
      return current_tab_index
  if index == "":
      index = len(tabs)  # Switch to the last opened tab
  else:
      try: # using try and except to prevent wrong value errors y the user 
          index = int(index)
          if not 1 <= index <= len(tabs):
              print("Invalid tab index. Please try again.")
              return current_tab_index
      except ValueError:
          print("Invalid input. Please enter a valid integer index.")
          return current_tab_index
  url = tabs[index - 1]["url"]  # Adjust for 1-based index
  response = requests.get(url)
  print("Switched to tab {}: {}".format(index, tabs[index - 1]["title"]))
  print(response.text)  # Print the response text
  return index

#function to close a tab option number 2 
def closeTab(current_tab_index, index=None):#Time Complexity: bigO(n), where n is the number of elements in the tabs list
  while True:
      if index is None:
          index = current_tab_index
      try: #using try and except to prevent user value errors
          if index == "":
              index = len(tabs)  # Close the last opened tab
          index = int(index)  # Convert index to integer

          if 0 <= index < len(tabs):
              closed_tab = tabs.pop(index - 1)  # https://railsware.com/blog/indexing-and-slicing-for-lists-tuples-strings-sequential-types
              print("Tab closed: " + closed_tab["title"])

              # Adjusting the current_tab_index if needed
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

 #function for url validation related to opening a new tab (option 1)
#url used for help https://www.slingacademy.com/article/python-ways-to-check-if-a-string-is-a-valid-url/
def isValidUrl(url):#Time Complexity:big O(1)
  url_pattern = re.compile(r'https?://\S+')
  return bool(re.match(url_pattern, url))
 
 # Function to open a new tab (Option 1)
 #added a new function to prevent user error by accepting only valid url format
def newTab(title, url):#Time Complexity:big O(1)
  while not isValidUrl(url):#validating the url with the isValidUrl function
    print("Invalid URL format. Please enter a valid URL (starting with http:// or https://).")
    url = input("Enter the URL: ")
  new_tab = {"title": title, "url": url, "nested_tabs": []}
  tabs.append(new_tab) #adding the new tab to the list 
  current_tab_index = len(tabs) - 1
  print("Tab opened: " + title)
  return current_tab_index

# Main menu function containing the options for the user to choose from
def mainMenu():
  current_tab_index = -1  # Dummy value for current tab
  choice = -99  # Dummy value
  while choice != 9:  # displaying options and ending the loop on option 9
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
     choice = int(input()) #taking user input 
     if choice == 1:  # Opening a new tab with title and URL
       title = input("Enter the title of the website: ")
       url = input("Enter the URL: ")
       current_tab_index = newTab(title, url)
     elif choice == 2:  # Closing a tab
       index = input("Enter the index of the tab you want to close\n""Leave it empty to close the last open tab: ")                           
       current_tab_index = closeTab(current_tab_index, index)
     elif choice == 3: # switching tabs
       index = input("Enter the index of the tab you want to switch to: (use valid urls http:// or https://)  ")
       current_tab_index = switch_tabs(current_tab_index, index)
     elif choice == 4: # displaying all tabs 
       displayAllTabs()
     elif choice == 5: #openning nested tabs
       current_tab_index = openNestedTab(current_tab_index)
     elif choice == 6:# sorting tabs 
        sortTabs(tabs)
     elif choice == 7: #saving tabs     
        filePath=input("Enter the path of the file to save the tabs to: ")
        saveTabs(tabs,filePath)
     elif choice == 8: #importing tabs
       filePath = input("Enter the path of the file to load tabs from: ")
       importTabs(filePath)
     elif choice == 9:#closin the program 
            print("Thank you for using the Advanced Browser Tabs Simulation")
     else:#input less than 0 or greater than 9 
            print("Invalid input ,try again please ")

# Run the main menu
mainMenu()
