from abc import ABC, abstractmethod


class Resource(ABC):
    def __init__(self, resource_number, title, subject, rental_price, copies):
        self.resource_number = resource_number
        self.title = title
        self.subject = subject
        self.rental_price = rental_price
        self.copies = copies

    def is_available(self):
        return self.copies > 0

    def lend(self):
        if self.copies > 0:
            self.copies -= 1
            return True
        return False

    def return_resource(self):
        self.copies += 1

    @abstractmethod
    def display(self):
        pass


class Book(Resource):
    VALID_FORMATS = ["Hardcover", "Paperback"]
    VALID_SUBJECTS = ["Science", "History", "Literature"]

    def __init__(
        self,
        isbn,
        title,
        book_format,
        subject,
        rental_price,
        copies
    ):
        super().__init__(
            isbn,
            title,
            subject,
            rental_price,
            copies
        )
        self.format = book_format

    def display(self):
        status = "Available" if self.is_available() else "Unavailable"

        print(
            f"ISBN: {self.resource_number} | "
            f"Title: {self.title} | "
            f"Format: {self.format} | "
            f"Subject: {self.subject} | "
            f"Price/Day: {self.rental_price:.2f} | "
            f"Copies: {self.copies} | "
            f"Status: {status}"
        )


class Magazine(Resource):
    VALID_SUBJECTS = ["Science", "Technology", "Sports"]

    def __init__(
        self,
        magazine_number,
        title,
        print_type,
        subject,
        rental_price,
        copies
    ):
        super().__init__(
            magazine_number,
            title,
            subject,
            rental_price,
            copies
        )
        self.print_type = print_type

    def display(self):
        status = "Available" if self.is_available() else "Unavailable"

        print(
            f"Magazine No: {self.resource_number} | "
            f"Title: {self.title} | "
            f"Print: {self.print_type} | "
            f"Subject: {self.subject} | "
            f"Price/Day: {self.rental_price:.2f} | "
            f"Copies: {self.copies} | "
            f"Status: {status}"
        )


class EducationalDVD(Resource):
    VALID_SUBJECTS = ["Astronomy", "Math", "Technology"]

    def __init__(
        self,
        dvd_number,
        title,
        subject,
        rental_price,
        copies
    ):
        super().__init__(
            dvd_number,
            title,
            subject,
            rental_price,
            copies
        )

    def display(self):
        status = "Available" if self.is_available() else "Unavailable"

        print(
            f"DVD No: {self.resource_number} | "
            f"Title: {self.title} | "
            f"Subject: {self.subject} | "
            f"Price/Day: {self.rental_price:.2f} | "
            f"Copies: {self.copies} | "
            f"Status: {status}"
        )


class LectureCD(Resource):
    VALID_SUBJECTS = ["Music", "Math", "Foreign Languages"]

    def __init__(
        self,
        cd_number,
        title,
        subject,
        rental_price,
        copies
    ):
        super().__init__(
            cd_number,
            title,
            subject,
            rental_price,
            copies
        )

    def display(self):
        status = "Available" if self.is_available() else "Unavailable"

        print(
            f"CD No: {self.resource_number} | "
            f"Title: {self.title} | "
            f"Subject: {self.subject} | "
            f"Price/Day: {self.rental_price:.2f} | "
            f"Copies: {self.copies} | "
            f"Status: {status}"
        )