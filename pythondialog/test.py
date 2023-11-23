#!/usr/bin/env python3

import locale
from dialog import Dialog

# This is almost always a good thing to do at the beginning of your programs.
locale.setlocale(locale.LC_ALL, '')

# You may want to use 'autowidgetsize=True' here (requires pythondialog >= 3.1)
d = Dialog(dialog="dialog", autowidgetsize=True)

# Dialog.set_background_title() requires pythondialog 2.13 or later
d.set_background_title("Testing pythondialog")

while True:
    # Choose what to check
    code, tag = d.menu(
        "Choose what you want to check",
        title="Main Menu",
        choices=[
            ("(1)", "menu()"),
            ("(0)", "exit")
        ]
    )
    if code == d.OK:
        if tag == "(0)":
            break
        elif tag == "(1)":
            # check menu()
            code, tag = d.menu(
                "Choose some item",
                title="Test Menu",
                choices=[
                    ("1", "choice 1"),
                    ("2", "choice 2"),
                    ("3", "choice 3"),
                    ("4", "choice 4"),
                ]
            )
            if code == d.OK:
                input(f'{tag} was choosen')
    else:
        break


# # In pythondialog 3.x, you can compare the return code to d.OK, Dialog.OK or
# if d.yesno("Are you REALLY sure you want to see this?") == d.OK:
#     d.msgbox("You have been warned...")
#
#     # We could put non-empty items here (not only the tag for each entry)
#     code, tags = d.checklist("What sandwich toppings do you like?",
#                              choices=[("Catsup", "",             False),
#                                       ("Mustard", "",            False),
#                                       ("Pesto", "",              False),
#                                       ("Mayonnaise", "",         True),
#                                       ("Horse radish","",        True),
#                                       ("Sun-dried tomatoes", "", True)],
#                              title="Do you prefer ham or spam?",
#                              backtitle="And now, for something "
#                                        "completely different...")
#
#     if code == d.OK:
#         # 'tags' now contains a list of the toppings chosen by the user
#         print(f'tags: {tags}')
#
# else:
#     code, tag = d.menu("OK, then you have two options:",
#                        title="title text",
#                        backtitle="backtitle text",
#                        choices=[("(1)", "Leave this fascinating example"),
#                                 ("(2)", "Leave this fascinating example")])
#     if code == d.OK:
#         # 'tag' is now either "(1)" or "(2)"
#         print(f'tag: {tag}')
