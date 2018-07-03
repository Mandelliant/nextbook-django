from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

def suggestion(request):
    #return HttpResponse("Get a reading suggestion: Yes or no?")
    #books = Book.objects.order_by('?').first()
    #Book.objects.random
    #books is the QuerySet variable, basically sets the variable books to be a random Book object from the model

    books = Book.randoms.all()[0]

    return render(request, 'nextbook/index.html', {'books': books})












'''
def what_book(self):
        with open(self.csvfile, 'rt') as f:
            reader = csv.DictReader(f)
            rows = [row for row in reader if row['status'] == 'to read'.lower()]
            book_choice = random.choice(rows)
            suggestion = {k: book_choice[k] for k in book_choice.keys() & {'title', 'author'}}

            return '{title} by {author}'.format(**suggestion)

    def book_line(self):

        with open(self.csvfile, 'r', newline='') as library:

            line_number = len(library.readlines())

            new_book_id = int(line_number)

            return new_book_id
'''
