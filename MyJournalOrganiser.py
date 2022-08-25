from LinkedList import*
from journal import*
import pickle


def main():

    menu = 0

    while menu != 3:
        print("\n___________MENU__________")
        print("1: Read My Journal")
        print("2: Start / Edit My Journal")
        print("3: Exit")
        menu = int(input("\nChoose one of them: "))

        if menu == 1:
            try:
                with open('linkedlist.dat', "rb") as dataFile:
                    LinkedList = pickle.load(dataFile)
                    print(LinkedList)
            except:
                print("\nError: Object file does not exist!\n")

        if menu == 2:
            sub_menu = 0
            while sub_menu != 5:
                print("\n____________MENE___________")
                print("1: Make a new jornal")
                print("2: Add new page")
                print("3: Edit a page")
                print("4: Store new/update journal")
                print("5: Exit")
                sub_menu = int(input("\nchoose one of them: "))

                if sub_menu == 1:
                    journal_name = input("\nEnter your new journal's name: ")
                    journal = Journal(journal_name)

                if sub_menu == 2:
                    option = 0
                    while option != 4:
                        print("\n____________menu___________")
                        print("1: add page at the end")
                        print("2: add page at start")
                        print("3: add page in the middle")
                        print("4: Exit")
                        option = int(input("\nchoose one of them: "))

                        if option == 1:
                            content = input("\nEnter your journal: \n")
                            journal.add_page_last(content)
                            print(journal)

                        if option == 2:
                            content = input("\nEnter your journal: \n")
                            journal.add_page_front(content)
                            print(journal)

                        if option == 3:
                            content = input("\nEnter your journal: \n")
                            pageNum = int(input(
                                "\nAfter which page do you want to save?: "))
                            journal.add_page_middle(content, pageNum)
                            print(journal)

                if sub_menu == 3:
                    pageNum = int(input("\nWhich page do you want to edit?: "))
                    content = input("\nEnter your Journal: ")
                    journal.pickData(pageNum, content)

                if sub_menu == 4:
                    print("\nSaving Object to File...")
                    try:
                        with open('linkedlist.dat', "wb") as dataFile:
                            pickle.dump(journal, dataFile)
                    except:
                        print("\nError: problem pickling object!")


if __name__ == "__main__":
    main()
