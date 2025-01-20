def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def book_word_count(books):
    word_count = 0
    words = books.split()
    for word in words:
        word_count += 1
    return (word_count)

def letter_count(books):
    dict_letter = {}
    letters = list(books.lower())
    for letter in letters:
        if letter not in dict_letter:
            dict_letter[letter] = 1
        else:
            dict_letter[letter] = dict_letter[letter] + 1
    return dict_letter
'''
def book_report(letter_count):
    dict_isAlpha = {}
    sorted_list = []
    #print(letter_count)
    for key, value in letter_count.items(): 
        if key.isalpha():
            dict_isAlpha[key] = value
'''
def sort_on(letter_count):
    report_list = []
    for key,value in letter_count.items():
        list_update = {}
        if key.isalpha():
            list_update[key] = value
        else:
            continue
        report_list.append(list_update)
    book_report = sorted(report_list, key=lambda d: list(d.values())[0], reverse=True)
    print(book_report)


sort_on(letter_count(main()))
