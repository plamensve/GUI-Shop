from tkinter import Button
from tkinter import Entry

from buying_page import display_products
from canvas import root, frame
from helpers import clean_screen, get_password_hash
from json import dump, loads


def get_users_data():
    info_data = []
    with open('db/users_information.txt', 'r') as users_file:
        for line in users_file:
            info_data.append(loads(line))
    return info_data


def render_entry():
    register_button = Button(
        root,
        text='Register',
        bg='green',
        fg='white',
        bd=0,
        width=10,
        height=1,
        font='sans',
        command=register,
    )

    login_button = Button(
        root,
        text='Log In',
        bg='blue',
        fg='white',
        bd=0,
        width=10,
        height=1,
        font='sans',
        command=login,
    )

    frame.create_window(330, 320, window=register_button)
    frame.create_window(330, 280, window=login_button)


def register():
    clean_screen()

    frame.create_text(350, 100, text='REGISTRATION FORM', font=("Comic Sans MS", 12), fill='white')

    frame.create_text(170, 150, text='First name: ', font=("Comic Sans MS", 12), fill='white')
    frame.create_text(170, 200, text='Last name: ', font=("Comic Sans MS", 12), fill='white')
    frame.create_text(170, 250, text='Username: ', font=("Comic Sans MS", 12), fill='white')
    frame.create_text(170, 300, text='Password: ', font=("Comic Sans MS", 12), fill='white')

    frame.create_window(370, 150, width=300, height=20, window=first_name_box)
    frame.create_window(370, 200, width=300, height=20, window=last_name_box)
    frame.create_window(370, 250, width=300, height=20, window=username_box)
    frame.create_window(370, 300, width=300, height=20, window=password_box,)

    submit_button = Button(
        root,
        text='Submit',
        bg='green',
        fg='white',
        bd=0,
        font=('Comic Sans MS', 12),
        command=registration
    )

    frame.create_window(370, 360, width=300, height=40, window=submit_button,)


def registration():
    info_dict = {
        'First name': first_name_box.get(),
        'Last name': last_name_box.get(),
        'Username': username_box.get(),
        'Password': password_box.get(),
    }

    if check_registration(info_dict):
        with open("db/users_information.txt", 'a') as users_file:
            info_dict['Password'] = get_password_hash(info_dict['Password'])
            dump(info_dict, users_file)
            users_file.write('\n')
            successful_registration()


def successful_registration():
    clean_screen()
    frame.create_text(
        370,
        270,
        text=f'Your registration is successful',
        fill='green'
    )

    back_to_login = Button(
        root,
        text='Return to home menu',
        bg='green',
        fg='white',
        bd=0,
        font=('Comic Sans MS', 12),
        command=back_to_entry
    )

    frame.create_window(370, 230, width=300, height=40, window=back_to_login, )


def back_to_entry():
    clean_screen()
    render_entry()


def check_registration(info_dict):
    frame.delete('error')

    for key, value in info_dict.items():
        if not value.strip():
            frame.create_text(
                370,
                395,
                text=f'{key} cannot be empty!',
                fill='red',
                tags='error',
            )

            return False

    users_data = get_users_data()

    for user in users_data:
        if user['Username'] == info_dict['Username']:
            frame.create_text(
                370,
                395,
                text=f'Username is already taken!',
                fill='red',
                tags='error'
            )
            return False

    return True


def login():
    clean_screen()

    frame.create_text(190, 250, text='Username:', fill='white')
    frame.create_text(190, 300, text='Password:', fill='white')
    frame.create_window(370, 250, width=300, height=20, window=username_box)
    frame.create_window(370, 300, width=300, height=20, window=password_box,)
    frame.create_window(370, 360, width=300, height=40, window=login_button,)


def check_login():
    users_data = get_users_data()
    user_username = username_box.get()
    user_password = get_password_hash(password_box.get())

    for user in users_data:
        current_user_username = user['Username']
        current_user_password = user['Password']

        if current_user_username == user_username and current_user_password == user_password:
            return True

    return False


def logging():
    if check_login():
        clean_screen()
        display_products()
    else:
        frame.create_text(
            370,
            400,
            text='Invalid Username or Password',
            fill='red',
            tags='error',
         )


def change_login_button_status(event):
    info = [
        username_box.get(),
        password_box.get(),
    ]

    for el in info:
        if not el.strip():
            login_button['state'] = 'disabled'
            break
    else:
        login_button['state'] = 'normal'


first_name_box = Entry(root, bd=0, font=("Comic Sans MS", 12, 'bold'), )
last_name_box = Entry(root, bd=0, font=("Comic Sans MS", 12, 'bold'), )
username_box = Entry(root, bd=0, font=("Comic Sans MS", 12, 'bold'), )
password_box = Entry(root, bd=0, font=("Comic Sans MS", 12, 'bold'), show='*')

login_button = Button(
        root,
        text='Log In',
        bg='green',
        fg='white',
        bd=0,
        font=('Comic Sans MS', 12),
        command=logging
    )
login_button['state'] = 'disabled'
root.bind('<KeyRelease>', change_login_button_status)

