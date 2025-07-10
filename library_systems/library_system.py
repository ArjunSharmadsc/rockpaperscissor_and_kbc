class Library:
    total_books_across_libraries = 0

    def __init__(self, name, romantic, horror, thriller):
        self.name = name
        self.romantic = romantic
        self.horror = horror
        self.thriller = thriller
        self.book_count = self.no_of_books()  # This also updates the class total

    def no_of_books(self):
        count = len(self.romantic) + len(self.horror) + len(self.thriller)
        Library.total_books_across_libraries += count
        return count

    @classmethod
    def total_across_all(cls):
        return cls.total_books_across_libraries



library1 = Library(
name="Radhika's library",
romantic=["Pride and Prejudice", "Outlander (Outlander, #1)", "Jane Eyre", "Sense and Sensibility"],
horror=["The Haunting of Hill House", "The Memoirs of a Ghost", "Strangers and Pilgrims", "The White People and Other Weird Stories", "Our Share of Night: A Novel."],
thriller=["Why Mystery Books Are So Satisfying", "The Woman in White", "Crime and Punishment.", "The Leavenworth Case"]
)

library2 = Library(
    name="Arjun's library",
    romantic=["Pride and Prejudice", "The Notebook", "Outlander", "Me Before You", "The Fault in Our Stars"],
    horror=["The Shining", "It", "Dracula", "The Haunting of Hill House", "Pet Sematary"],
    thriller=["Gone Girl", "The Girl with the Dragon Tattoo", "The Da Vinci Code", "The Silent Patient", "The Woman in the Window"]
)


print(f"There is one library named {library1.name} with {library1.book_count} books \n where the romantic books are {len(library1.romantic)}, the horror books are {len(library1.horror)}, and thriller books are {len(library1.thriller)}")
print(f"There is another library named {library2.name} with {library2.book_count} books\n where the romantic books are {len(library2.romantic)}, the horror books are {len(library2.horror)}, and thriller books are {len(library2.thriller)}")
print(f"\n Total number of books across all libraries are: {Library.total_across_all()}")