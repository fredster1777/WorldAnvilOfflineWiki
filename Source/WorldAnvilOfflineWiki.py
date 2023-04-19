
import os
import stat
import time
import sqlite3
import requests
from selenium import webdriver
from urllib.parse import urlparse


def detectTables():
    folder_path = 'Tables'

    # Check if the folder exists
    if not os.path.exists(folder_path):
        # Create the folder if it doesn't exist
        os.makedirs(folder_path)

    files = os.listdir(folder_path)

    db_files = [file for file in files if file.endswith(".db")]

    if not db_files:
        print("No Wiki's documented")
        while True:
            resp = input("Would you like to create a new Wiki? [y/n]")
            if resp.lower() == "y" or resp.lower() == "yes":
                selectedTable = createTable()
                break
            elif resp.lower() == "n" or resp.lower() == "no":
                quit()
            else:
                print("invalid response")
    else:
        while True:
            print("Please select a Wiki\n")
            displayTableChoices(db_files)
            resp = input("\nOr select 'New' to create a new Wiki\n")
            if resp.lower() == "new":
                selectedTable = createTable()
            elif resp in db_files:
                selectedTable = resp
                break
            else:
                print("\nInvalid Response\n")


    print("You selected " + selectedTable)
    quit()

    '''
    TODO Impliment a method of using selenium to load up each individual page

    # Connect to the database
    conn = sqlite3.connect(selectedTable)

    # Create a cursor object to execute SQL commands
    c = conn.cursor()

    # Check if the table exists
    table_exists = False
    try:
        c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='example_table'")
        result = c.fetchone()
        if result:
            table_exists = True
    except sqlite3.Error as e:
        print(e)

    # Close the connection
    conn.close()

    if table_exists:
        print("The table exists.")
    else:
        print("The table does not exist.")

    '''


def createTable():
    while True:
        resp = input("Please input the URL of the wiki you would like to create:\n")
        try:
            result = urlparse(resp)
            if all([result.scheme, result.netloc]):
                print("The URL is valid.")
                try:
                    response = requests.get(resp)
                    if response.status_code == 200:
                        print("The link is valid.")
                        break
                    else:
                        print("The link is not valid.")
                except requests.exceptions.RequestException:
                    print("The link is not valid.")
            else:
                print("The URL is not valid.")
        except ValueError:
            print("The URL is not valid.")

    DatabaseName = resp.split("/")[-1]


    # Connect to a database (creates a new one if it doesn't exist)
    conn = sqlite3.connect("Tables/" + DatabaseName + '.db')

    # Create a cursor object to execute SQL commands
    c = conn.cursor()

    #TODO create a table that is reflective of the data i want to capture. Currently Title, link, parent, children, text1, text2
    # Create a table with columns 'id', 'name', and 'age'
    c.execute('''CREATE TABLE example_table
                (id INT PRIMARY KEY NOT NULL,
                name TEXT NOT NULL,
                age INT NOT NULL);''')

    # Save changes and close the connection
    conn.commit()
    conn.close()
    return DatabaseName 

def displayTableChoices(db_files):
    for item in db_files:
        item_path = os.path.join("Tables", item)
        item_stat = os.stat(item_path)
        item_mtime = item_stat.st_mtime
        item_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(item_mtime))
        print(f"{item_time} {item}")


def click_link_by_category(url, category_list):
    # Start the browser and navigate to the url
    driver = webdriver.Chrome()
    driver.get(url)
    
    # Find the link with the specified category and click on it
    for category in category_list:
        link = driver.find_element_by_xpath("//a[contains(@href, '{}')]".format(category))
        link.click()
    
    # Close the browser
    driver.quit()


def main():
    detectTables()
    createTable()

    
    quit()








if __name__ == "__main__":
    while True:
        main()
