from library import Library
from resources import (
    Book,
    Magazine,
    EducationalDVD,
    LectureCD
)


# ==========================================
# Helper Functions
# ==========================================

def get_positive_integer(message):

    while True:

        try:
            value = int(input(message))

            if value < 0:
                print("Please enter a positive number.")
            else:
                return value

        except ValueError:
            print("Please enter a valid number.")


def get_positive_float(message):

    while True:

        try:
            value = float(input(message))

            if value < 0:
                print("Please enter a positive number.")

            else:
                return value

        except ValueError:
            print("Please enter a valid price.")


def choose_book_format():

    while True:

        print("\nAvailable Formats:")
        print("1. Hardcover")
        print("2. Paperback")

        choice = input("Choose format: ")

        if choice == "1":
            return "Hardcover"

        elif choice == "2":
            return "Paperback"

        else:
            print("Invalid choice.")


def choose_book_subject():

    while True:

        print("\nAvailable Book Subjects:")
        print("1. Science")
        print("2. History")
        print("3. Literature")

        choice = input("Choose subject: ")

        subjects = {
            "1": "Science",
            "2": "History",
            "3": "Literature"
        }

        if choice in subjects:
            return subjects[choice]

        print("Invalid choice.")


def choose_magazine_subject():

    while True:

        print("\nAvailable Magazine Subjects:")
        print("1. Science")
        print("2. Technology")
        print("3. Sports")

        choice = input("Choose subject: ")

        subjects = {
            "1": "Science",
            "2": "Technology",
            "3": "Sports"
        }

        if choice in subjects:
            return subjects[choice]

        print("Invalid choice.")


def choose_dvd_subject():

    while True:

        print("\nAvailable DVD Subjects:")
        print("1. Astronomy")
        print("2. Math")
        print("3. Technology")

        choice = input("Choose subject: ")

        subjects = {
            "1": "Astronomy",
            "2": "Math",
            "3": "Technology"
        }

        if choice in subjects:
            return subjects[choice]

        print("Invalid choice.")


def choose_cd_subject():

    while True:

        print("\nAvailable CD Subjects:")
        print("1. Music")
        print("2. Math")
        print("3. Foreign Languages")

        choice = input("Choose subject: ")

        subjects = {
            "1": "Music",
            "2": "Math",
            "3": "Foreign Languages"
        }

        if choice in subjects:
            return subjects[choice]

        print("Invalid choice.")


def choose_print_type():

    while True:

        print("\nPrint Type:")
        print("1. Color")
        print("2. Black & White")

        choice = input("Choose print type: ")

        if choice == "1":
            return "Color"

        elif choice == "2":
            return "Black & White"

        else:
            print("Invalid choice.")


# ==========================================
# Add Resource
# ==========================================

def add_resource(library):

    print("\n========== ADD RESOURCE ==========")

    print("1. Book")
    print("2. Magazine")
    print("3. Educational DVD")
    print("4. Lecture CD")

    choice = input("Choose resource type: ")

    if choice == "1":

        isbn = input("Enter ISBN: ")
        title = input("Enter title: ")

        book_format = choose_book_format()
        subject = choose_book_subject()

        rental_price = get_positive_float(
            "Enter rental price per day: "
        )

        copies = get_positive_integer(
            "Enter number of copies: "
        )

        book = Book(
            isbn,
            title,
            book_format,
            subject,
            rental_price,
            copies
        )

        library.add_resource(book)

    elif choice == "2":

        number = input("Enter magazine number: ")
        title = input("Enter title: ")

        print_type = choose_print_type()
        subject = choose_magazine_subject()

        rental_price = get_positive_float(
            "Enter rental price per day: "
        )

        copies = get_positive_integer(
            "Enter number of copies: "
        )

        magazine = Magazine(
            number,
            title,
            print_type,
            subject,
            rental_price,
            copies
        )

        library.add_resource(magazine)

    elif choice == "3":

        number = input("Enter DVD number: ")
        title = input("Enter title: ")

        subject = choose_dvd_subject()

        rental_price = get_positive_float(
            "Enter rental price per day: "
        )

        copies = get_positive_integer(
            "Enter number of copies: "
        )

        dvd = EducationalDVD(
            number,
            title,
            subject,
            rental_price,
            copies
        )

        library.add_resource(dvd)

    elif choice == "4":

        number = input("Enter CD number: ")
        title = input("Enter title: ")

        subject = choose_cd_subject()

        rental_price = get_positive_float(
            "Enter rental price per day: "
        )

        copies = get_positive_integer(
            "Enter number of copies: "
        )

        cd = LectureCD(
            number,
            title,
            subject,
            rental_price,
            copies
        )

        library.add_resource(cd)

    else:
        print("Invalid resource type.")


# ==========================================
# Remove Resource
# ==========================================

def remove_resource(library):

    print("\n========== REMOVE RESOURCE ==========")

    number = input(
        "Enter resource number / ISBN: "
    )

    library.remove_resource(number)


# ==========================================
# View Available Resources
# ==========================================

def view_available_resources(library):

    print("\n========== RESOURCE TYPE ==========")

    print("1. All")
    print("2. Books")
    print("3. Magazines")
    print("4. Educational DVDs")
    print("5. Lecture CDs")

    choice = input("Choose type: ")

    if choice == "1":
        library.view_available()

    elif choice == "2":
        library.view_available(Book)

    elif choice == "3":
        library.view_available(Magazine)

    elif choice == "4":
        library.view_available(EducationalDVD)

    elif choice == "5":
        library.view_available(LectureCD)

    else:
        print("Invalid choice.")


# ==========================================
# View Unavailable Resources
# ==========================================

def view_unavailable_resources(library):

    print("\n========== RESOURCE TYPE ==========")

    print("1. All")
    print("2. Books")
    print("3. Magazines")
    print("4. Educational DVDs")
    print("5. Lecture CDs")

    choice = input("Choose type: ")

    if choice == "1":
        library.view_unavailable()

    elif choice == "2":
        library.view_unavailable(Book)

    elif choice == "3":
        library.view_unavailable(Magazine)

    elif choice == "4":
        library.view_unavailable(EducationalDVD)

    elif choice == "5":
        library.view_unavailable(LectureCD)

    else:
        print("Invalid choice.")


# ==========================================
# Search By Subject
# ==========================================

def search_by_subject(library):

    print("\n========== SEARCH BY SUBJECT ==========")

    subject = input(
        "Enter subject: "
    )

    library.search_by_subject(subject)


# ==========================================
# Lend Resource
# ==========================================

def lend_resource(library):

    print("\n========== LEND RESOURCE ==========")

    number = input(
        "Enter resource number / ISBN: "
    )

    library.lend_resource(number)


# ==========================================
# Return Resource
# ==========================================

def return_resource(library):

    print("\n========== RETURN RESOURCE ==========")

    number = input(
        "Enter resource number / ISBN: "
    )

    library.return_resource(number)


# ==========================================
# Main Menu
# ==========================================

def display_menu():

    print("\n")
    print("=" * 45)
    print("       UNIVERSITY LIBRARY SYSTEM")
    print("=" * 45)

    print("1. Add New Resource")
    print("2. Remove Resource")
    print("3. View Available Resources")
    print("4. View Unavailable Resources")
    print("5. Search Resources by Subject")
    print("6. Lend Resource")
    print("7. Return Resource")
    print("8. View All Resources")
    print("9. Exit")

    print("=" * 45)


# ==========================================
# Sample Data
# ==========================================

def load_sample_data(library):

    library.add_resource(
        Book(
            "ISBN1234",
            "The Solar System",
            "Hardcover",
            "Science",
            15.00,
            5
        )
    )

    library.add_resource(
        Book(
            "ISBN9876",
            "Types of Animal Species",
            "Paperback",
            "Science",
            10.00,
            8
        )
    )

    library.add_resource(
        Book(
            "ISBN1290",
            "Second World War",
            "Hardcover",
            "History",
            12.50,
            1
        )
    )

    library.add_resource(
        Magazine(
            "01",
            "History of Cricket",
            "Color",
            "Sports",
            5.00,
            7
        )
    )

    library.add_resource(
        Magazine(
            "02",
            "Evolution of the Computer",
            "Black & White",
            "Technology",
            3.00,
            21
        )
    )

    library.add_resource(
        EducationalDVD(
            "10",
            "Birth of the Solar System",
            "Astronomy",
            2.50,
            10
        )
    )

    library.add_resource(
        EducationalDVD(
            "11",
            "Pythagoras Theorem",
            "Math",
            1.00,
            50
        )
    )

    library.add_resource(
        LectureCD(
            "21",
            "Basics of Western Music",
            "Music",
            1.50,
            11
        )
    )

    library.add_resource(
        LectureCD(
            "22",
            "Japanese Language",
            "Foreign Languages",
            2.00,
            3
        )
    )


# ==========================================
# Application
# ==========================================

def main():

    library = Library()

    # Load the resources given in the question
    load_sample_data(library)

    while True:

        display_menu()

        choice = input(
            "Enter your choice: "
        )

        if choice == "1":
            add_resource(library)

        elif choice == "2":
            remove_resource(library)

        elif choice == "3":
            view_available_resources(library)

        elif choice == "4":
            view_unavailable_resources(library)

        elif choice == "5":
            search_by_subject(library)

        elif choice == "6":
            lend_resource(library)

        elif choice == "7":
            return_resource(library)

        elif choice == "8":
            library.view_all()

        elif choice == "9":
            print(
                "\nThank you for using "
                "the University Library System."
            )
            break

        else:
            print(
                "\nInvalid choice. "
                "Please select 1-9."
            )


if __name__ == "__main__":
    main()