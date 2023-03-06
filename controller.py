import view
import phone_book


pb = phone_book.PhoneBook()


def start():
    while True:
        user_choice = view.menu()
        match user_choice:
            case 1:
                pb.open_file()
            case 2:
                pb.save_file()
            case 3:
                book = pb.get()
                view.show_contact(book)
            case 4:
                add_contact = view.new_contact()
                pb.new_contact(add_contact)
            case 5:
                word = view.input_request('искомое слово')
                result = pb.search(word)
                view.show_contact(result)
            case 6:
                new_value = view.change_contact(pb.get())
                pb.change(*new_value)
            case 7:
                index = view.select_to_delete()
                view.show_contact(pb.get())
                contact = view.select_to_delete()
                name = pb.get_name(contact)
                if view.ask_user('удалить', name):
                    pb.delete(index)
            case 8:
                view.goodbye()
                break
