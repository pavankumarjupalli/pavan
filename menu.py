import os

def main():

    while True:

        # Menu

        print("Menu:")

        print("1. Create a File")

        print("2. Rename a File")

        print("3. Open and Read a File")

        print("4. Exit Program")

 

        choice = input("Enter your choice: ")

 

        if choice == "1":

            # Create a File

            create_file()

        elif choice == "2":

            # Rename a File

            rename_file()

        elif choice == "3":

            # Open and Read a File

            open_and_read_file()

        elif choice == "4":

            # Exit Program

            break

        else:

            print("Invalid choice. Please select a valid option.")

 

# File Handling

 

 

def create_file():

    file_name = input("Enter the name of the file to create: ")

   

    # Check if the file already exists

    if os.path.exists(file_name):

        print("File already exists. Please choose a different name.")

        return

   

    # Get content from the user

    file_content = input("Enter the content for the file: ")

   

    # Create the file and write the content to it

    with open(file_name, 'w') as file:

        file.write(file_content)

   

    print(f"File '{file_name}' created successfully.")

 

 

 

def rename_file():

    old_file_name = input("Enter the current name of the file: ")

   

    # Check if the file exists

    if not os.path.exists(old_file_name):

        print("File not found. Please enter a valid file name.")

        return

   

    new_file_name = input("Enter the new name for the file: ")

   

    try:

        os.rename(old_file_name, new_file_name)

        print(f"File '{old_file_name}' renamed to '{new_file_name}' successfully.")

    except Exception as e:

        print(f"An error occurred while renaming the file: {e}")

 

 

def open_and_read_file():

    file_name = input("Enter the name of the file to open: ")

   

    # Check if the file exists

    if not os.path.exists(file_name):

        print("File not found. Please enter a valid file name.")

        return

   

    try:

        # Open and read the file

        with open(file_name, 'r') as file:

            content = file.read()

        print(f"Content of '{file_name}':\n{content}")

    except Exception as e:

        print(f"An error occurred while opening or reading the file: {e}")

 

 

if __name__ == "__main__":

    main()
