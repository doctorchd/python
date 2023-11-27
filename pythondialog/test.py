#!/usr/bin/env python3

import locale
import time
from dialog import Dialog

# This is almost always a good thing to do at the beginning of your programs.
locale.setlocale(locale.LC_ALL, 'uk_UA.UTF-8')

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
            ("(14)", "buildlist()"),
            ("(15)", "radiolist()"),
            ("(16)", "treeview()"),
            ("(17)", "inputbox()"),
            ("(18)", "inputmenu()"),
            ("(19)", "passwordbox()"),
            ("(20)", "form()"),
            ("(21)", "mixedform()"),
            ("(22)", "passwordform()"),
            ("(23)", "dselect()"),
            ("(24)", "fselect()"),
            ("(25)", "calendar()"),
            ("(26)", "timebox()"),
            ("(27)", "rangebox()"),
            ("(28)", "yesno()"),
            ("(0)", "exit")
        ],
        help_button=True
    )

    # input(f'You pressed {button_names[code]} button')

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
            # input(f'You pressed {button_names[code]} button, tag: {tag}')
            # if code == d.OK:
            #     input(f'{tag} was chosen')

        elif tag == "(2)":
            # check msgbox()
            code = d.msgbox('This is a message box', title='Test message box')
            # input(f'You pressed {button_names[code]} button')

        elif tag == "(3)":
            # check infobox()
            code = d.infobox('This is an infobox', height =20, width=20, title='Test infobox')
            # input(f'You pressed {button_names[code]} button')

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
            # input(f'You pressed {button_names[code]} button, tag: {tag}')

        elif tag == "(5)":
            # check textbox()
            code = d.textbox('test.txt')
            # input(f'You pressed {button_names[code]} button')

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
            # input(f'You pressed {button_names[code]} button')

        elif tag == "(7)":
            # check editbox()
            code, text = d.editbox('test.txt')
            # input(f'You pressed {button_names[code]} button')

        elif tag == "(8)":
            # check progressbox()
            code = d.progressbox('/var/log/syslog')
            # input(f'You pressed {button_names[code]} button')

        elif tag == "(9)":
            # check programbox()
            code = d.programbox('/var/log/syslog')
            # input(f'You pressed {button_names[code]} button')

        elif tag == "(10)":
            # check tailbox()
            code = d.tailbox('/var/log/syslog')
            # input(f'You pressed {button_names[code]} button')

        elif tag == "(11)":
            # check pause()
            code = d.pause(
                'Pausing 20 sec',
                seconds=20
            )
            # input(f'You pressed {button_names[code]} button')

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

            # input(f'You pressed {button_names[code]} button')

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
                percent=0,
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
                percent=20,
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
                percent=40,
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
                percent=80,
                text='example'
            )

            # input(f'You pressed {button_names[code]} button')

        elif tag == "(14)":
            # check buildlist()
            code, tag = d.buildlist(
                "This is a buildlist",
                items=[
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
            # input(f'You pressed {button_names[code]} button, tag: {tag}')

        elif tag == "(15)":
            # check radiolist()
            code, tag = d.radiolist(
                "Choose some item",
                title="Test Radio List",
                choices=[
                    ("1", "choice 1", True, "Help1"),
                    ("2", "choice 2", False, "Help2"),
                    ("3", "choice 3", False, "Help3"),
                    ("4", "choice 4", False, "Help4"),
                ],
                help_button=True,
                item_help=True,
                help_tags=True
            )
            # input(f'You pressed {button_names[code]} button, tag: {tag}')
            # if code == d.OK:
            #     input(f'{tag} was chosen')

        elif tag == "(16)":
            # check treeview()
            code, tag = d.treeview(
                "Choose some item",
                title="Test Radio List",
                nodes=[
                    ("1", "choice 1", True, 1, "Help1"),
                    ("2", "choice 2", False, 2, "Help2"),
                    ("3", "choice 3", False, 3, "Help3"),
                    ("4", "choice 4", False, 2, "Help4"),
                ],
                help_button=True,
                item_help=True,
                help_tags=True
            )
            # input(f'You pressed {button_names[code]} button, tag: {tag}')
            # if code == d.OK:
            #     input(f'{tag} was chosen')

        elif tag == "(17)":
            # check inputbox()
            code, string = d.inputbox(
                "Enter something",
                title="Test Input Box",
                init='',
                help_button=True,
                item_help=True,
                help_tags=True
            )
            # input(f'You pressed {button_names[code]} button, string: {string}')

        elif tag == "(18)":
            # check inputmenu()
            exit_info, tag, new_item_text = d.inputmenu(
                "Enter something",
                title="Test Input Menu",
                choices=[
                    ("1", "choice 1", "Help1"),
                    ("2", "choice 2", "Help2"),
                    ("3", "choice 3", "Help3"),
                    ("4", "choice 4", "Help4")
                ],
                help_button=True,
                item_help=True,
                help_tags=True
            )
            # input(f'You got exit_info: {exit_info}, tag: {tag}, new_item_text: {new_item_text}')

        elif tag == "(19)":
            # check inputbox()
            code, password = d.passwordbox(
                "Enter password",
                title="Test Password Box",
                init='qwerty123',
                insecure=True,
                help_button=True,
                item_help=True,
                help_tags=True
            )
            # input(f'You pressed {button_names[code]} button, password: {password}')

        elif tag == "(20)":
            # check form()
            code, list = d.form(
                "Fill the Form",
                # height=20,
                # width=40,
                # form_height=8,
                title="Test Form",
                # help_button=True,
                # item_help=True,
                # help_tags=True,
                elements=[
                    ("label1", 1, 1, "item1", 1, 10, 10, 20),
                    ("label2", 2, 1, "item2", 2, 10, 10, 20),
                    ("label3", 3, 1, "item3", 3, 10, 10, 20),
                    ("label4", 4, 1, "item4", 4, 10, 10, 20),
                    ('label5', 5, 1, "item5", 5, 10, 10, 20)
                ]
            )
            # input(f'You pressed {button_names[code]} got list: {list}')

        elif tag == "(21)":
            # check mixedform()
            code, list = d.mixedform(
                "Fill the Form",
                title="Test Mixed Form",
                elements=[
                    ("label1", 1, 1, "item1", 1, 10, 10, 20, 0, ''),
                    ("label2", 2, 1, "item2", 2, 10, 10, 20, 0, ''),
                    ("label3", 3, 1, "item3", 3, 10, 10, 20, 0, ''),
                    ("label4", 4, 1, "item4", 4, 10, 10, 20, 1, '')
                ],
                help_button=True,
                item_help=True,
                help_tags=True,
                insecure=True
            )
            # input(f'You pressed {button_names[code]} got list: {list}')

        elif tag == "(22)":
            # check passwordform()
            code, list = d.passwordform(
                "Fill the Form",
                title="Test Password Form",
                elements=[
                    ("label1", 1, 1, "item1", 1, 10, 10, 20, 'aaa'),
                    ("label2", 2, 1, "item2", 2, 10, 10, 20, 'bbb'),
                    ("label3", 3, 1, "item3", 3, 10, 10, 20, 'ccc'),
                    ("label4", 4, 1, "item4", 4, 10, 10, 20, 'ddd')
                ],
                help_button=True,
                item_help=True,
                help_tags=True,
                insecure=True
            )
            # input(f'You pressed {button_names[code]} got list: {list}')

        elif tag == "(23)":
            # check dselect()
            code, path = d.dselect(
                "/",
                title="Directory Selector"
            )
            input(f'path: {path}')
            # input(f'You pressed {button_names[code]} got list: {list}')

        elif tag == "(24)":
            # check fselect()
            code, path = d.fselect(
                "/",
                title="Directory and File Selector"
            )
            input(f'path: {path}')
            # input(f'You pressed {button_names[code]} got list: {list}')

        elif tag == "(25)":
            # check calendar()
            code, date = d.calendar(
                "This is a calendar",
                day=-1, month=-1, year=-1,
                title="Calendar"
            )
            input(f'date: {date}')
            # input(f'You pressed {button_names[code]} got list: {list}')

        elif tag == "(26)":
            # check timebox()
            code, time = d.timebox(
                "This is a timebox",
                hour=-1, minute=-1, second=-1,
                title="Timebox"
            )
            input(f'time: {time}')
            # input(f'You pressed {button_names[code]} got list: {list}')

        elif tag == "(27)":
            # check rangebox()
            code, val = d.rangebox(
                "This is a rangebox",
                min=0, max=100, init=20,
                title="Rangebox"
            )
            input(f'val: {val}')
            # input(f'You pressed {button_names[code]} got list: {list}')

        elif tag == "(28)":
            # check yesno()
            code = d.yesno(
                "This is a Yes/No box",
                title="Yes/No box"
            )
            input(f'code: {code}')
            # input(f'You pressed {button_names[code]} got list: {list}')

    elif code == d.ESC:
        # print('ESC was pressed')
        pass

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
