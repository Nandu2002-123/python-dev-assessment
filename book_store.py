

from datetime import datetime

class Book:
    def __init__(self, title: str, author: str, publication_year: int, summary: str):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.summary = summary

    def get_age(self) -> int:
        """Calculates the age of the book based on the current year."""
        current_year = datetime.now().year  # Evaluates to 2026
        return current_year - self.publication_year

    def display_details(self):
        """Prints all attributes of the book cleanly."""
        print(f"Title:   {self.title}")
        print(f"Author:  {self.author}")
        print(f"Age:     {self.get_age()} years old (Published: {self.publication_year})")
        print(f"Summary: {self.summary}")
        print("-" * 50)


# Information of the 3 Book Objects

if __name__ == "__main__":
    # Book 1 Details
    book1 = Book(
        title="Harry Potter and the Philosopher's Stone",
        author="J.K. Rowling",
        publication_year=1997,
        summary="An orphaned boy discovers he is a wizard and attends a magical boarding school, where he uncovers dark secrets about his past."
    )

    # Book 2 Details
    book2 = Book(
        title="The Alchemist",
        author="Paulo Coelho",
        publication_year=1988,
        summary="An Andalusian shepherd boy journeys to Egypt in search of worldly treasure, discovering spiritual wisdom along the way."
    )

    # Book 3 Details
    book3 = Book(
        title="A Man Called Ove",
        author="Fredrik Backman",
        publication_year=2012,
        summary="An isolated, grumpy widower whose strict routines are disrupted by an boisterous young family moving in next door."
    )

    # Displaying details for all books
    print("--- 2.2. Object-Oriented Programming Fundamentals ---\n")
    book1.display_details()
    book2.display_details()
    book3.display_details()

