from guizero import App, Text, TextBox, PushButton, Picture

un = 'Ford'
pw = 'MustangGT500'
app = App(title='Log In', bg=(255, 0, 0))
message = Text(app, text='Username', color=(0, 255, 0))


def check_user():
    if un_box.value == un and pw_box.value == pw:
        message = Text(app, text='Access Granted', color=(0, 255, 0))
        picture = Picture(app, image="Pictures\\Ford_MustangGT500.png")

    else:
        message = Text(app, text='Access Denied', color=(0, 255, 0))


un_box = TextBox(app)
message = Text(app, text='Password', color=(0, 255, 0))
pw_box = TextBox(app)
submit = PushButton(app, command=check_user)
app.display()
