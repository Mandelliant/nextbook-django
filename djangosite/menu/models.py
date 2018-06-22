from django.db import models

# Create your models here.

class Book(models.Model):
    number = models.IntegerField
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=500)

    def random(self):
        random_book = random.choice
        return random_book


    # Placeholder for new book model.
    def new_book(self):
        fields = [nbt, author]

        with open(self.csvfile, 'a', newline='') as library:

            writer = csv.writer(library, delimiter=',')

            line_number = Book.book_line(self)

            writer.writerow([line_number] + fields)

            newbook = '{} by {}'.format(nbt, author)

            return "Added {}".format(newbook)
