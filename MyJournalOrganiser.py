from LinkedList import*
from journal import*
import pickle


def check_input_int(message):
    while True:
        try:
            user_input = int(input(message))

        except ValueError:
            print("\n***Invalid chioce. Check if you entered integer***")
            continue
        else:
            return user_input


def main():

    menu = 0

    while menu != 3:

        print("\n___________MENU__________")
        print("1: Read My Journal")
        print("2: Start / Edit My Journal")
        print("3: Exit")
        menu = check_input_int("\nChoose one of them: ")

        if menu == 1:
            journal = None
            sub_menu = 0
            while sub_menu != 4:
                print("_________MENU________")
                print("1: Load a journal")
                print("2: Go to next page")
                print("3: go to previous page")
                print("4: Close the journal")
                sub_menu = check_input_int("\nChoose one of them: ")
                if sub_menu == 1:
                    filename = input("\nEnter a file's name: ")
                    try:
                        with open(filename, "rb") as dataFile:
                            journal = pickle.load(dataFile)
                            journal.currNd = journal.list.head
                            print('\n---------PAGE--------')
                            print(journal.currNd)
                            print()
                    except:
                        print("\nError: Object file does not exist!\n")

                if sub_menu == 2:
                    journal.get_next()
                if sub_menu == 3:
                    journal.get_prev()

        if menu == 2:
            journal = None
            sub_menu = 0
            while sub_menu != 7:
                print("\n____________MENE___________")
                print("1: Make a new jornal")
                print("2: Add new page")
                print("3: add page at start")
                print("4: add in after a page number")
                print("5: Edit a page")
                print("6: Store new/update journal")
                print("7: Exit")
                sub_menu = check_input_int("\nChoose one of them: ")

                if sub_menu == 1:
                    journal_name = input("\nEnter your new journal's name: ")
                    journal = Journal(journal_name)

                if sub_menu == 2:
                    if (journal != None):
                        content = input("\nEnter your journal entry: \n")
                        journal.add_page_last(content)
                        print(journal)
                    else:
                        raise Exception('No joutnal name')

                if sub_menu == 3:
                    if (journal != None):
                        content = input("\nEnter your journal entry: \n")
                        journal.add_page_front(content)
                        print(journal)
                    else:
                        raise Exception('No joutnal name')

                if sub_menu == 4:
                    if (journal != None):
                        content = input("\nEnter your journal entry: \n")
                        pageNum = check_input_int(
                            "\nAfter which page do you want to save?: ")
                        journal.add_page_middle(content, pageNum)
                        print(journal)
                    else:
                        raise Exception('No joutnal name')

                if sub_menu == 5:
                    pageNum = check_input_int(
                        "\nWhich page do you want to edit?: ")
                    content = input("\nEnter your Journal entry: ")
                    journal.edit_page(pageNum, content)
                    print(journal)

                if sub_menu == 6:
                    print("\nSaving Object to File...")
                    try:
                        with open(journal.name+".dat", "wb") as dataFile:
                            pickle.dump(journal, dataFile)
                    except:
                        print("\nError: problem pickling object!")


if __name__ == "__main__":
    main()
