
import os
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
                createTable()
                break
            elif resp.lower() == "n" or resp.lower() == "no":
                quit()
            else:
                print("invalid response")

    # Connect to the database
    conn = sqlite3.connect('example.db')

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
    print(DatabaseName)


    # Connect to a database (creates a new one if it doesn't exist)
    conn = sqlite3.connect("Tables/" + DatabaseName + '.db')

    # Create a cursor object to execute SQL commands
    c = conn.cursor()

    # Create a table with columns 'id', 'name', and 'age'
    c.execute('''CREATE TABLE example_table
                (id INT PRIMARY KEY NOT NULL,
                name TEXT NOT NULL,
                age INT NOT NULL);''')

    # Save changes and close the connection
    conn.commit()
    conn.close()


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
