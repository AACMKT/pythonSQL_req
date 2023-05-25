import PySimpleGUI as sg
import re
from sql_req import *


layout1 = [[sg.Button('CONNECT TO BASE', size=(23, 1), key='-specify_base-')],
           [sg.Button('Exit', size=(23, 1), key='-Exit_gen-')]]
layout2 = [[sg.Text('', size=(28, 1), justification='center', key='BASE_HINTS')],
           [sg.Text('base name', size=(8, 1)),
            sg.InputText(size=(23, 5), key='base_row1', border_width=2, enable_events=True)],
           [sg.Text('username', size=(8, 1)),
            sg.InputText(size=(23, 5), key='base_row2', border_width=2, enable_events=True)],
           [sg.Text('password', size=(8, 1)),
            sg.InputText(size=(15, 5), key='base_row3', border_width=2, enable_events=True),
            sg.Button('', key='-hide_show_password-', visible=False, size=(5, 1))],
           [sg.Text(' ', size=(23, 1), justification='center')],
           [sg.Button('Exit', size=(10, 1), key='-Exit_conn-'),
            sg.Button('Connect', size=(10, 1), disabled=True, enable_events=True, key='-connect-')]]
layout3 = [[sg.Text('              MAIN MENU', size=(23, 1))], [sg.Button('Create', size=(23, 1))],
           [sg.Button('Edit', size=(23, 1))], [sg.Button('Read', size=(23, 1))],
           [sg.Text(' ', size=(23, 1), justification='center')], [sg.Button('Exit', size=(23, 1))]]
layout4 = [[sg.Text(size=(23, 1), text_color='black', key='-TEXT-')], [sg.Button('Create tables', size=(23, 1))],
           [sg.Button('Back', size=(23, 1))]]
layout5 = [[sg.Text('Tables editing interface', size=(23, 1))],
           [sg.Checkbox("Insert data", key='c1', enable_events=True),
            sg.Checkbox("Edit data", size=(7, 1), key='c2', enable_events=True),
            sg.Button('Clear all', key='-clear-', size=(14, 1), visible=False)],
           [sg.Text(size=(22, 1), text_color='black', key='-HINTS-'),
            sg.Button('Delete record', key='-cut_cl_rec-', size=(14, 1), visible=False)],
           [sg.Text(key='-t1-'), sg.InputText(key='row1', border_width=2, visible=False, enable_events=True,
                                              use_readonly_for_disable=True, disabled_readonly_background_color='Grey'),
            sg.Button('Find', key='-find1-', visible=False,  size=(19, 1)),
            sg.Button('Confirm changes', key='-edit1-', visible=False,  size=(19, 1))],
           [sg.Text(key='-t2-'), sg.InputText(size=(30, 5), key='row2', border_width=2, visible=False,
                                              enable_events=True)],
           [sg.Text(key='-t3-'), sg.InputText(size=(30, 5), key='row3', border_width=2, visible=False,
                                              enable_events=True, disabled_readonly_background_color='Grey')],
           [sg.Text(key='-t4-'), sg.InputText(size=(30, 5), key='row4', border_width=2, visible=False,
                                              enable_events=True, disabled_readonly_background_color='Grey')],
           [sg.Text(key='-t5-', text_color='black')],
           [sg.Text(key='-t6-'), sg.InputText(size=(26, 5),
                                              key='row5', border_width=2, visible=False, enable_events=True),
            sg.Button('EDIT PHONE NUMBERS RECORDS',
                      key='-to_phones_menu-', size=(36, 1), visible=False, enable_events=True)],
           [sg.Text('')],
           [sg.Button('Confirm', key='-confirm-', visible=False, enable_events=True), sg.Button('Back'), sg.Exit(),
            sg.Button('Show the full list of clients', key='-records-', visible=False, enable_events=True)]]
layout6 = [[sg.Text('Read')], [sg.Button('Back')]]
layout7 = [[sg.Text('Clients phone numbers editing interface', size=(30, 1))],
           [sg.Button('Edit', size=(8, 1), key='-edit_phones-'),
            sg.Button('Add', size=(8, 1), key='-add_phones-'),
            sg.Button('Delete', size=(8, 1),  key='-delete_phones-')]]
layout8 = [[sg.Text('Clients phone numbers editing interface', size=(40, 1))],
           [sg.Text(key='-p_i_HINTS-', text_color='black'),
            sg.Button('NEW SEARCH', key='-alter_phones_new_search-', size=(14, 1), visible=False)],
           [sg.Text(visible=False, key='-p_i_client_info-')],
           [sg.Text(key='-p1-'), sg.InputText(size=(20, 5), key='phones_row0', border_width=2, visible=False,
                                              enable_events=True),
            sg.Button('Find', key='-find2-', visible=False,  size=(8, 1)), sg.Text(key='-p_i_cl_info1-')],
           [sg.Text(key='-p_i_cl_info2-')], [sg.Text(key='-p_i_cl_info3-')],
           [sg.Text(key='-p2-', text_color='black', justification='center')],
           [sg.Text(key='-phone_n1-', size=(6, 1)),
            sg.InputText(size=(30, 5), key='phones_row1', border_width=2, visible=False, enable_events=True,
                         use_readonly_for_disable=True, disabled_readonly_background_color='Grey'),
            sg.Button('', key='-alter_phone1-', size=(8, 1), visible=False, enable_events=True),
            sg.Text(key='-alter_phone_status1-')],
           [sg.Text(key='-phone_n2-', size=(6, 1)),
            sg.InputText(size=(30, 5), key='phones_row2', border_width=2, visible=False, enable_events=True,
                         use_readonly_for_disable=True, disabled_readonly_background_color='Grey'),
            sg.Button('', key='-alter_phone2-', size=(8, 1), visible=False, enable_events=True),
            sg.Text(key='-alter_phone_status2-')],
           [sg.Text(key='-phone_n3-', size=(6, 1)),
            sg.InputText(size=(30, 5), key='phones_row3', border_width=2, visible=False, enable_events=True,
                         use_readonly_for_disable=True, disabled_readonly_background_color='Grey'),
            sg.Button('', key='-alter_phone3-', size=(8, 1), visible=False, enable_events=True),
            sg.Text(key='-alter_phone_status3-')],
           [sg.Text(key='-phone_n4-', size=(6, 1)),
            sg.InputText(size=(30, 5), key='phones_row4', border_width=2, visible=False, enable_events=True,
                         use_readonly_for_disable=True, disabled_readonly_background_color='Grey'),
            sg.Button('', key='-alter_phone4-', size=(8, 1), visible=False, enable_events=True),
            sg.Text(key='-alter_phone_status4-')],
           [sg.Text(key='-phone_n5-', size=(6, 1)),
            sg.InputText(size=(30, 5), key='phones_row5', border_width=2, visible=False, enable_events=True,
                         use_readonly_for_disable=True, disabled_readonly_background_color='Grey'),
            sg.Button('', key='-alter_phone5-', size=(8, 1), visible=False, enable_events=True),
            sg.Text(key='-alter_phone_status5-')],
           [sg.Button('Back'), sg.Exit()]]

layout = [[sg.Column(layout1, key='-General-'),
           sg.Column(layout2, visible=False, key='-Enter_database-'),
           sg.Column(layout3, visible=False, key='-Menu-'),
           sg.Column(layout4, visible=False, key='-Create-'),
           sg.Column(layout5, visible=False, key='-Edit-'),
           sg.Column(layout6, visible=False, key='-Read-'),
           sg.Column(layout7, visible=False, key='-phones_menu-'),
           sg.Column(layout8, visible=False, key='-phones_interface-')]]

window = sg.Window('DB interface', layout)


layout = 1
base = ''
name = ''
password = ''
pr_event = ''
get_pass_inp = 0
conn_det_count = 0
emp_row = 0
k = 'Menu'
edit_add = None
filler_edit = 0
client_id = 0
phone_id = 0
phones_event = 0
alter_phones_option = ''
al_ph_opt_switch_control = 0
prev = []
last_input_add = []
[last_input_add.append(f'row{i}') for i in range(1, 4)]
p_edit_counter = [0, 0, 0, 0, 0, 0]
alter_phones_buttons = []
[alter_phones_buttons.append(f'-alter_phone{i}-') for i in range(1, 6)]
row = ''
client_info_title = ['FIRST NAME:', 'LAST NAME: ', 'MAIL:            ']


def edit_input_text_states():
    window['row2'].update(disabled=False)
    window['row3'].update(disabled=False)
    window['row4'].update(disabled=False)
    window['-find1-'].update(visible=False)
    window['-edit1-'].update(visible=True)


def fill_phone_edit_interface(database, username, passwrd):
    window['phones_row0'].update('', visible=False)
    window['-p1-'].update('', visible=False)
    window['-find2-'].update(visible=False)
    if alter_phones_option != '-add_phones-':
        if len(get_phones(database, username, passwrd, client_id)) > 0:
            window['-p2-'].update('-- Below are the client\'s phone numbers available for editing --',
                                  visible=True)
            for i in range(len(get_phones(database, username, passwrd, client_id))):
                window[f'-phone_n{i + 1}-'].update(f'phone {i + 1}')
                window[f'-phone_n{i + 1}-'].update(visible=True)
                window[f'phones_row{i + 1}'].\
                    update(get_phones(base, name, password, client_id)[i][2], visible=True, disabled=True)
                if alter_phones_option == '-edit_phones-':
                    window[f'-alter_phone{i + 1}-'].update('Edit!', visible=True)
                if alter_phones_option == '-delete_phones-':
                    window[f'-alter_phone{i + 1}-'].update('Delete', visible=True)
        else:
            window['-p2-']. \
                update('--       No saved phone numbers of this client were found      --', visible=True)
    elif alter_phones_option == '-add_phones-':
        window['-p2-'].update('--        Write a new phone number in the textbox below         --',
                              visible=True)
        window['-phone_n1-'].update('')
        window['phones_row1'].update('', visible=True, disabled=False)
        window['-alter_phone1-'].update('Add', visible=True)


while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Quit') or 'Exit' in event:
        if len(password) > 0:
            psycopg2.connect(database=base, user=name, password=password).close()
            break
        else:
            break

    if event == '-specify_base-':
        window['-General-'].update(visible=False)
        window['-Enter_database-'].update(visible=True)
        try:
            with open('db_con.txt', 'r', encoding='utf-8') as log:
                info = log.read().split('\n')
                base = info[0]
                name = info[1]
                password = info[2]
            window['BASE_HINTS'].update('Ready for establishing connection')
            window['-connect-'].update(disabled=False)
        except FileNotFoundError:
            base = ''
            name = ''
            password = ''
            window['BASE_HINTS'].update('Provide connection details')
            window['-connect-'].update(disabled=True)
            window['-hide_show_password-'].update(visible=False)
        window['base_row1'].update(base, visible=True)
        window['base_row2'].update(name, visible=True)
        if len(str(password)) > 0:
            hidden_pass = '*'*len(str(password))
            window['base_row3'].update(hidden_pass, visible=True, disabled=True)
            window['-hide_show_password-'].update('SHOW', visible=True)
        else:
            window['base_row3'].update(password, visible=True)

    if event == '-hide_show_password-':
        if window[event].get_text() == 'SHOW':
            window['base_row3'].update(password, visible=True, disabled=False)
            window['-hide_show_password-'].update('HIDE', visible=True)
        elif window[event].get_text() == 'HIDE':
            hidden_pass = '*' * len(str(password))
            window['base_row3'].update(hidden_pass, visible=True, disabled=True)
            window['-hide_show_password-'].update('SHOW', visible=True)

    if event == 'base_row3' and window['-hide_show_password-'].get_text() == 'HIDE' and get_pass_inp == 0:
        get_pass_inp = 1
        print('Check 1')

    if event == 'base_row3' and get_pass_inp == 1:
        window['-hide_show_password-'].update('HIDE', visible=False)
        get_pass_inp = 0
        print('Check 2')

        for row in [base, name, password]:
            if len(row) == 0:
                emp_row += 1

    if event in ['base_row1', 'base_row2', 'base_row3']:
        if event != pr_event and conn_det_count < emp_row:
            conn_det_count += 1
        pr_event = event

    if window['-Enter_database-'].visible is True and conn_det_count == emp_row:
        window['-connect-'].update(disabled=False)
        conn_det_count = 0

    if event == '-connect-':
        hidden_pass = '*' * len(str(password))

        try:
            with open('db_con.txt', 'w', encoding='utf-8') as log:
                log.write(values['base_row1'] + '\n')
                log.write(values['base_row2'] + '\n')
                if values['base_row3'] != hidden_pass and values['base_row3'] != '':
                    log.write(values['base_row3'])
                    password = values['base_row3']

                else:
                    log.write(password)

        except Exception:
            window['BASE_HINTS'].update('Failed to connect. Check your input.')

        with open('db_con.txt', 'r', encoding='utf-8') as log:
            info = log.read().split('\n')
            base = info[0]
            name = info[1]
            password = info[2]

        try:
            conn = psycopg2.connect(database=base, user=name, password=password)
            cur = conn.cursor()
            conn.close()
            window['-Enter_database-'].update(visible=False)
            window['-Menu-'].update(visible=True)
            window['BASE_HINTS'].update('Ready for establishing connection')
        except Exception:
            window['BASE_HINTS'].update('Failed to connect. Check your input.')

    if event == 'Create':
        window['-Menu-'].update(visible=False)
        window['-Create-'].update(visible=True)
        k = 'Create'

    if event == 'Edit':
        window['-Menu-'].update(visible=False)
        window['-Edit-'].update(visible=True)
        k = 'Edit'

    if event == 'Read':
        # window['-Menu-'].update(visible=False)
        # window['-Read-'].update(visible=True)
        k = 'Read'

    if 'Back' in event:
        if window['-phones_interface-'].visible is True:
            window['-phones_interface-'].update(visible=False)
            window['-Edit-'].update(visible=True)
            k = 'Edit'
            phones_event = 1
        else:
            window[f'-{k}-'].update(visible=False)
            window['-Menu-'].update(visible=True)

    if event == 'Create tables':
        create_tables(base, name, password)
        window['-TEXT-'].update("CREATED! (IF NOT EXISTED)")

    if k == 'Edit' and event == 'c1':
        edit_add = 'c1'
        window['c2'].update(False)
        window['c1'].update(True)
        window['-HINTS-'].update("Fill in all input fields")
        window['-t1-'].update('FIRST NAME')
        window['-t2-'].update('LAST NAME ')
        window['-t3-'].update('MAIL            ')
        window['-t4-'].update('')
        window['-t5-'].update('Insert phone number (not obligatory)')
        window['-t6-'].update('PHONE NUMBER')
        window['row1'].set_size(size=(30, 1))
        window['row4'].update(visible=False)
        window['row5'].update(visible=True)
        window['-to_phones_menu-'].update(visible=False)
        window['-find1-'].update(visible=False)
        window['-edit1-'].update(visible=False)
        window['-clear-'].update(visible=False)
        window['-cut_cl_rec-'].update(visible=False)

        for i in range(1, 6):
            window[f'row{i}'].update('', disabled=False)
        for i in range(1, 4):
            window[f'row{i}'].update(visible=True)

    if event in last_input_add and event not in prev and edit_add == 'c1' and filler_edit < 3:
        prev.append(event)
        filler_edit += 1

    if k == 'Edit' and edit_add == 'c1' and filler_edit == 3 and \
            (len(values['row1']) > 0 and len(values['row2']) > 0 and len(values['row3']) > 0):
        window['-confirm-'].update(visible=True)
    else:
        window['-confirm-'].update(visible=False)

    if k == 'Edit' and event == '-confirm-':
        window['-HINTS-'].update("Fill in all input fields")
        try:
            if len(values['row5']) == 0 or\
                    (len(values['row5']) > 1 and re.search(r'^[+0-9]*\Z', str(values['row5'])) is not None):
                insert_data(base, name, password, values['row1'], values['row2'], values['row3'])
                window['-HINTS-'].update('SUCCESS')
            try:
                if len(values['row5']) > 1 and re.search(r'^[+0-9]*\Z', str(values['row5'])) is not None:
                    insert_phone(base, name, password, values['row1'], values['row3'], values['row5'])
                else:
                    if len(values['row5']) > 1 and re.search(r'^[+0-9]*\Z', str(values['row5'])) is None:
                        raise Exception('Incorrect phone num. format!')
            except Exception:
                window['-HINTS-'].update("CORRECT phone num. input")
        except Exception:
            window['-HINTS-'].update("Incorrect input or already exists")

    if k == 'Edit' and event == 'c2':
        edit_add = 'c2'
        window['c1'].update(False)
        window['c2'].update(True)
        window['-HINTS-'].update("Please fill id and/or mail")
        window['-t1-'].update('client_ID       ')
        window['-t2-'].update('MAIL            ')
        window['-t3-'].update('FIRST NAME')
        window['-t4-'].update('LAST NAME ')
        window['-t5-'].update('')
        window['-t6-'].update('')
        window['row1'].set_size(size=(6, 1))
        window['row5'].update('')
        window['row5'].update(visible=False)
        window['-to_phones_menu-'].update(visible=True)
        window['-records-'].update(visible=True)
        window['-find1-'].update(visible=False)
        window['-edit1-'].update(visible=False)
        window['-clear-'].update(visible=False)
        window['-cut_cl_rec-'].update(visible=False)

        for i in range(1, 5):
            window[f'row{i}'].update('', visible=True)

        for i in range(3, 5):
            window[f'row{i}'].update(disabled=True)

    if k == 'Edit' and edit_add == 'c2' and window['-edit1-'].visible is False\
            and (values['row1'] != '' or values['row2'] != ''):
        window['-find1-'].update(visible=True)
        if event == '-find1-' and values['row2'] != '':
            try:
                client_id = get_by_mail(base, name, password, values['row2'], 0)
                window['row1'].update(get_by_mail(base, name, password, values['row2'], 0))
                window['row3'].update(get_by_mail(base, name, password, values['row2'], 1))
                window['row4'].update(get_by_mail(base, name, password, values['row2'], 2))
                window['row1'].update(disabled=True)
                window['-clear-'].update(visible=True)
                window['-cut_cl_rec-'].update(visible=True)
                edit_input_text_states()
                window['-HINTS-'].update("SUCCESS")
            except Exception:
                window['-HINTS-'].update("Such record doesn't exists")

        if event == '-find1-' and values['row1'] != '':
            try:
                client_id = values['row1']
                window['row2'].update(get_by_id(base, name, password, values['row1'], 3))
                window['row3'].update(get_by_id(base, name, password, values['row1'], 1))
                window['row4'].update(get_by_id(base, name, password, values['row1'], 2))
                window['row1'].update(disabled=True)
                window['-clear-'].update(visible=True)
                window['-cut_cl_rec-'].update(visible=True)
                edit_input_text_states()
                window['-HINTS-'].update("SUCCESS")
            except Exception:
                window['-HINTS-'].update("Such record doesn't exists")

    if event == '-edit1-' and values['row1'] != '' and values['row2'] != '' \
            and values['row3'] != '' and values['row4'] != '':
        try:
            edit_client_data(base, name, password, values['row1'], values['row2'], values['row3'], values['row4'])
            window['-HINTS-'].update("SUCCESS")
        except Exception:
            window['-HINTS-'].update("CORRECT your input: wrong data format")

    if event == '-clear-':
        window['-find1-'].update(visible=False)
        for i in range(1, 5):
            window[f'row{i}'].update('')
        window['row1'].update(disabled=False)
        window['-edit1-'].update(visible=False)
        window['-clear-'].update(visible=False)
        window['-cut_cl_rec-'].update(visible=False)
        window['-HINTS-'].update("Please fill id and/or mail")

    if event == '-cut_cl_rec-':
        window['-find1-'].update(visible=False)
        delete_client(base, name, password, client_id)
        for i in range(1, 5):
            window[f'row{i}'].update('')
        window['row1'].update(disabled=False)
        window['-edit1-'].update(visible=False)
        window['-clear-'].update(visible=False)
        window['-cut_cl_rec-'].update(visible=False)
        window['-HINTS-'].update("Please fill id and/or mail")
        sg.popup(f'Record is deleted, \nincluding phones numbers')

    if event == '-to_phones_menu-':
        window['-Edit-'].update(visible=False)
        window['-phones_menu-'].update(visible=True)
        if phones_event == 0:
            for i in range(1, 6):
                window[f'-phone_n{i}-'].update('')
            for i in range(1, 4):
                window[f'-p_i_cl_info{i}-'].update(visible=False)
        k = 'phones_menu'

    if window['-phones_menu-'].visible is True and phones_event == 1 and event != alter_phones_option:
        al_ph_opt_switch_control = 1
    else:
        al_ph_opt_switch_control = 0

    if event in ('-edit_phones-', '-delete_phones-', '-add_phones-'):
        alter_phones_option = event

    if k == 'phones_menu' and (event == '-edit_phones-' or event == '-delete_phones-' or event == '-add_phones-'):
        if al_ph_opt_switch_control == 0:
            window['-phones_menu-'].update(visible=False)
            window['-phones_interface-'].update(visible=True)
            # window['-p_i_HINTS-'].update(visible=False)
            # window['-alter_phones_new_search-'].update(visible=False)
            if phones_event == 0:
                window['-p_i_HINTS-'].update('Insert client ID, MAIL or PHONE NUMBER', visible=True)
                window['phones_row0'].update(visible=True)
                window['phones_row1'].update(visible=False)
            elif window['-p_i_cl_info2-'].visible is True:
                window['-p_i_HINTS-'].update('-- Record is found --                               ', visible=True)
                window['-alter_phones_new_search-'].update(visible=True)

        else:
            window['phones_row0'].update(visible=True)
            window['phones_row1'].update(visible=False)
            window['-phones_menu-'].update(visible=False)
            window['-phones_interface-'].update(visible=True)
            window['-p_i_HINTS-'].update('Insert client ID, MAIL or PHONE NUMBER', visible=True)
            window['-find2-'].update(visible=False)
            window['-p1-'].update('', visible=False)
            window['-p2-'].update('', visible=False)
            window['-alter_phones_new_search-'].update(visible=False)
            for i in range(1, 6):
                window[f'-phone_n{i}-'].update(visible=False)
                window[f'phones_row{i}'].update(visible=False)
                window[f'-alter_phone{i}-'].update('', visible=False)
            for i in range(1, 4):
                window[f'-p_i_cl_info{i}-'].update('', visible=False)

        k = 'phones_interface'

    if k == 'phones_interface' and len(values['phones_row0']) > 0 \
            and window['phones_row0'].visible is True and window['phones_row1'].visible is False:
        window['-find2-'].update(visible=True)

    if k == 'phones_interface' and event == '-find2-':
        window['-p_i_HINTS-'].update('-- Record is found --                               ', visible=True)
        window['-find2-'].update(visible=False)
        window['-alter_phones_new_search-'].update(visible=True)

        if re.search(r'^[+0-9]*\Z', str(values['phones_row0'])) is not None:
            try:
                client_id = get_by_id_phone(base, name, password, values['phones_row0'], 0)
                for i in range(1, 4):
                    window[f'-p_i_cl_info{i}-']\
                        .update(f'{client_info_title[i-1]}'
                                f' {get_by_id_phone(base, name, password, values["phones_row0"], i)}')
                    window[f'-p_i_cl_info{i}-'].update(visible=True)
                fill_phone_edit_interface(base, name, password)
            except Exception:
                window['-p_i_HINTS-'].update(' -- CORRECT your input: nothing was found -- ', visible=True)
                window['-alter_phones_new_search-'].update(visible=False)

        else:
            try:
                client_id = get_by_mail_phone(base, name, password, values['phones_row0'], 0)
                for i in range(1, 4):
                    window[f'-p_i_cl_info{i}-']\
                        .update(f'{client_info_title[i-1]}'
                                f' {get_by_mail_phone(base, name, password, values["phones_row0"], i)}')
                    window[f'-p_i_cl_info{i}-'].update(visible=True)
                fill_phone_edit_interface(base, name, password)
            except Exception:
                window['-p_i_HINTS-'].update(' -- CORRECT your input: nothing was found -- ', visible=True)
                window['-alter_phones_new_search-'].update(visible=False)

    for i in range(1, 6):
        if k == 'phones_interface' and event == f'-alter_phone{i}-'\
                and window[f'-alter_phone{i}-'].get_text() == 'Edit!':
            phone_id = get_requested_phone(base, name, password, values[f'phones_row{i}'])
            window[f'-alter_phone{i}-'].update('Confirm', visible=True, disabled=True)
            window[f'phones_row{i}'].update(disabled=False)

        if event == f'phones_row{i}':
            p_edit_counter[i] += 1
            window[f'-alter_phone{i}-'].update(disabled=False)

    if event in alter_phones_buttons and window[event].get_text() == 'Confirm'\
            and p_edit_counter[int(str(event)[-2])] > 0:
        row = str(event)[-2]
        if re.search(r'^[+0-9]*\Z', values[f'phones_row{row}']) is not None:
            edit_phone_num(base, name, password, phone_id, values[f'phones_row{row}'])
            window[f'-alter_phone{row}-'].update('', visible=False)
            window[f'-phone_n{row}-'].update('DONE  ')
            window[f'phones_row{row}'].update(disabled=True)
            window['-p2-'].update('-- Below are the client\'s phone numbers available for editing --')
        else:
            window['-p2-'].update('--       WRONG DATA OR RECORD EXISTS. TRY AGAIN       --')
            window[f'phones_row{row}'].update(disabled=False)

    if event in alter_phones_buttons and window[event].get_text() == 'Delete':
        row = str(event)[-2]
        window[f'-phone_n{row}-'].update('DONE  ')
        delete_phone(base, name, password, values[f'phones_row{row}'])
        window[f'phones_row{row}'].update('')

    if event in alter_phones_buttons and window[event].get_text() == 'Add':
        row = str(event)[-2]
        if re.search(r'^[+0-9]*\Z', values[f'phones_row{row}']) is not None:
            window[f'phones_row{row}'].update(disabled=False)
            try:
                window[f'-phone_n{row}-'].update('DONE  ')
                add_phone(base, name, password, client_id, values[f'phones_row{row}'])
                window['-p2-'].update('------------------ Phone number is added ------------------')
                window['-alter_phone1-'].update(visible=False)
                window[f'phones_row{row}'].update(disabled=True)
            except Exception:
                window['-p2-'].update('--       WRONG DATA OR RECORD EXISTS. TRY AGAIN       --')
        else:
            window['-p2-'].update('--       WRONG DATA OR RECORD EXISTS. TRY AGAIN       --')
            window[f'phones_row{row}'].update('', disabled=False)

    if window['-find2-'].visible is True:
        p_edit_counter = [0, 0, 0, 0, 0, 0]

    if event == '-alter_phones_new_search-':
        phones_event = 0
        for i in range(1, 4):
            window[f'-p_i_cl_info{i}-'].update('', visible=True)
        window['phones_row0'].update(visible=True)
        window['phones_row0'].update('')
        window['-p_i_HINTS-'].update('Insert client ID, MAIL or PHONE NUMBER', visible=True)
        window['-p2-'].update('', visible=False)
        for i in range(1, 6):
            window[f'-alter_phone{i}-'].update('', visible=False, disabled=False)
            window[f'phones_row{i}'].update('')
            window[f'-phone_n{i}-'].update('', visible=False)
            window[f'phones_row{i}'].update('', visible=False, disabled=False)
            window['-alter_phones_new_search-'].update(visible=False)

    if event == '-records-':
        sg.popup_scrolled(*get_records(base, name, password),
                          title='id | first_name | last_name | mail | phones ', size=(50, 10))

    if k == 'Read':
        sg.popup_scrolled(*get_clients(base, name, password), title='data', size=(40, 10))
