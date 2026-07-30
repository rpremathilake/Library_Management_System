from resources import Book, Magazine, EducationalDVD, LectureCD


class Library:

    def __init__(self):
        self.resources = []

    # --------------------------------
    # Add Resource
    # --------------------------------

    def add_resource(self, resource):
        if self.find_resource(resource.resource_number):
            print("\nResource with this number already exists.")
            return False

        self.resources.append(resource)
        print("\nResource added successfully.")
        return True

    # --------------------------------
    # Remove Resource
    # --------------------------------

    def remove_resource(self, resource_number):
        resource = self.find_resource(resource_number)

        if resource is None:
            print("\nResource not found.")
            return False

        self.resources.remove(resource)

        print("\nResource removed successfully.")
        return True

    # --------------------------------
    # Find Resource
    # --------------------------------

    def find_resource(self, resource_number):
        for resource in self.resources:
            if resource.resource_number.lower() == resource_number.lower():
                return resource

        return None

    # --------------------------------
    # View Available Resources
    # --------------------------------

    def view_available(self, resource_type=None):

        print("\n========== AVAILABLE RESOURCES ==========")

        found = False

        for resource in self.resources:

            if resource.is_available():

                if resource_type is None or isinstance(
                    resource, resource_type
                ):
                    resource.display()
                    found = True

        if not found:
            print("No available resources found.")

    # --------------------------------
    # View Unavailable Resources
    # --------------------------------

    def view_unavailable(self, resource_type=None):

        print("\n========== UNAVAILABLE RESOURCES ==========")

        found = False

        for resource in self.resources:

            if not resource.is_available():

                if resource_type is None or isinstance(
                    resource, resource_type
                ):
                    resource.display()
                    found = True

        if not found:
            print("No unavailable resources found.")

    # --------------------------------
    # View Resources By Type
    # --------------------------------

    def view_by_type(self, resource_type):

        print("\n========== RESOURCES ==========")

        found = False

        for resource in self.resources:

            if isinstance(resource, resource_type):
                resource.display()
                found = True

        if not found:
            print("No resources found.")

    # --------------------------------
    # Search By Subject
    # --------------------------------

    def search_by_subject(self, subject):

        print(
            f"\n========== RESOURCES FOR SUBJECT: "
            f"{subject} =========="
        )

        found = False

        for resource in self.resources:

            if resource.subject.lower() == subject.lower():
                resource.display()
                found = True

        if not found:
            print("No resources found for this subject.")

    # --------------------------------
    # Lend Resource
    # --------------------------------

    def lend_resource(self, resource_number):

        resource = self.find_resource(resource_number)

        if resource is None:
            print("\nResource not found.")
            return

        if resource.lend():
            print(
                f"\nResource '{resource.title}' "
                f"has been lent successfully."
            )

            print(
                f"Remaining copies: {resource.copies}"
            )

        else:
            print(
                "\nThis resource is currently unavailable."
            )

    # --------------------------------
    # Return Resource
    # --------------------------------

    def return_resource(self, resource_number):

        resource = self.find_resource(resource_number)

        if resource is None:
            print("\nResource not found.")
            return

        resource.return_resource()

        print(
            f"\nResource '{resource.title}' "
            f"has been returned successfully."
        )

        print(
            f"Available copies: {resource.copies}"
        )

    # --------------------------------
    # View All Resources
    # --------------------------------

    def view_all(self):

        print("\n========== ALL RESOURCES ==========")

        if not self.resources:
            print("No resources available.")
            return

        for resource in self.resources:
            resource.display()