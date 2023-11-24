#!/usr/bin/env python3

import locale
import time
from dialog import Dialog

# This is almost always a good thing to do at the beginning of your programs.
locale.setlocale(locale.LC_ALL, '')

# You may want to use 'autowidgetsize=True' here (requires pythondialog >= 3.1)
d = Dialog(dialog="dialog", autowidgetsize=True)

# Dialog.set_background_title() requires pythondialog 2.13 or later
d.set_background_title("Testing pythondialog")

button_names = {
    d.OK: "Ok",
    d.CANCEL: "Cancel",
    d.HELP: "Help",
    d.EXTRA: "Extra",
    d.ESC: "Esc"
}

while True:
    # Choose what to check
    code, tag = d.menu(
        "Choose what you want to check",
        title="Main Menu",
        choices=[
            ("(1)", "menu()"),
            ("(2)", "msgbox()"),
            ("(3)", "infobox()"),
            ("(4)", "checklist()"),
            ("(5)", "textbox()"),
            ("(6)", "scrollbox()"),
            ("(7)", "editbox()"),
            ("(8)", "progressbox()"),
            ("(9)", "programbox()"),
            ("(10)", "tailbox()"),
            ("(11)", "pause()"),
            ("(12)", "regular gauge"),
            ("(13)", "mixed gauge"),
            ("(0)", "exit")
        ],
        help_button=True
    )

    input(f'You pressed {button_names[code]} button')

    if code == d.OK:
        if tag == "(0)":
            break

        elif tag == "(1)":
            # check menu()
            code, tag = d.menu(
                "Choose some item",
                title="Test Menu",
                choices=[
                    ("1", "choice 1", "Help1"),
                    ("2", "choice 2", "Help2"),
                    ("3", "choice 3", "Help3"),
                    ("4", "choice 4", "Help4"),
                ],
                help_button=True,
                item_help=True,
                help_tags=True
            )
            input(f'You pressed {button_names[code]} button, tag: {tag}')
            # if code == d.OK:
            #     input(f'{tag} was chosen')

        elif tag == "(2)":
            # check msgbox()
            code = d.msgbox('This is a message box', title='Test message box')
            input(f'You pressed {button_names[code]} button')

        elif tag == "(3)":
            # check infobox()
            code = d.infobox('This is an infobox', height =20, width=20, title='Test infobox')
            input(f'You pressed {button_names[code]} button')

        elif tag == "(4)":
            # check checklist()
            code, tag = d.checklist(
                "This is a checklist",
                choices=[
                    ("choice 1", "tag 1", False, "help1"),
                    ("choice 2", "tag 2", True, "help2"),
                    ("choice 3", "tag 3", True, "help3"),
                    ("choice 4", "tag 4", False, "help4")
                ],
                help_button=True,
                item_help=True,
                help_tags=True,
                help_status=True
            )
            input(f'You pressed {button_names[code]} button, tag: {tag}')

        elif tag == "(5)":
            # check textbox()
            code = d.textbox('test.txt')
            input(f'You pressed {button_names[code]} button')

        elif tag == "(6)":
            # check scrollbox()
            code = d.scrollbox(
                """
                'test test test test test test test test test test '
                'test test test test test test test test test test '
                'test test test test test test test test test test '
                'test test test test test test test test test test '
                'test test test test test test test test test test '
                'test test test test test test test test test test '
                'test test test test test test test test test test '
                'test test test test test test test test test test '
                'test test test test test test test test test test '
                'test test test test test test test test test test '
                'test test test test test test test test test test '
                'test test test test test test test test test test '
                'test test test test test test test test test test '
                'test test test test test test test test test test '
                'test test test test test test test test test test '
                'test test test test test test test test test test '
                """
            )
            input(f'You pressed {button_names[code]} button')

        elif tag == "(7)":
            # check editbox()
            code, text = d.editbox('test.txt')
            input(f'You pressed {button_names[code]} button')

        elif tag == "(8)":
            # check progressbox()
            code = d.progressbox('/var/log/syslog')
            input(f'You pressed {button_names[code]} button')

        elif tag == "(9)":
            # check programbox()
            code = d.programbox('/var/log/syslog')
            input(f'You pressed {button_names[code]} button')

        elif tag == "(10)":
            # check tailbox()
            code = d.tailbox('/var/log/syslog')
            input(f'You pressed {button_names[code]} button')

        elif tag == "(11)":
            # check pause()
            code = d.pause(
                'Pausing 20 sec',
                seconds=20
            )
            input(f'You pressed {button_names[code]} button')

        elif tag == "(12)":
            # check regular gauge
            d.gauge_start(text='gauge start')
            time.sleep(2)
            d.gauge_update(10, text='step 1', update_text=True)
            time.sleep(2)
            d.gauge_update(20, text='step 2', update_text=True)
            time.sleep(2)
            d.gauge_update(30, text='step 3', update_text=True)
            time.sleep(2)
            d.gauge_update(40, text='step 4', update_text=True)
            time.sleep(2)
            d.gauge_update(50, text='step 5', update_text=True)
            time.sleep(2)
            d.gauge_update(60, text='step 6', update_text=True)
            time.sleep(2)
            d.gauge_update(70, text='step 7', update_text=True)
            time.sleep(2)
            d.gauge_update(80, text='step 8', update_text=True)
            time.sleep(2)
            d.gauge_update(90, text='step 9', update_text=True)
            time.sleep(2)
            d.gauge_update(100, text='completed', update_text=True)
            d.gauge_stop()

            input(f'You pressed {button_names[code]} button')

        elif tag == "(13)":
            # check mixed gauge
            d.mixedgauge(
                title='mixed gauge',
                elements=[
                    ('test1', '-0'),
                    ('test2', '-0'),
                    ('test3', '-0'),
                    ('test4', '-0')
                ],
                percent='0',
                text='example'
            )
            time.sleep(2)
            d.mixedgauge(
                title='mixed gauge',
                elements=[
                    ('test1', '-0'),
                    ('test2', '-30'),
                    ('test3', '-0'),
                    ('test4', '-100')
                ],
                percent='20',
                text='example'
            )
            time.sleep(2)
            d.mixedgauge(
                title='mixed gauge',
                elements=[
                    ('test1', '-100'),
                    ('test2', '-30'),
                    ('test3', '-0'),
                    ('test4', '-100')
                ],
                percent='40',
                text='example'
            )
            time.sleep(2)
            d.mixedgauge(
                title='mixed gauge',
                elements=[
                    ('test1', '-50'),
                    ('test2', '-30'),
                    ('test3', '0'),
                    ('test4', '-90')
                ],
                percent='80',
                text='example'
            )

            input(f'You pressed {button_names[code]} button')

    elif code == d.ESC:
        print('ESC was pressed')

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
