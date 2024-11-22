import tkinter
import tkinter.font as tfont
import utils


def init():
    file = utils.get_file()
    data, cur_id = utils.load_data(file)
    if cur_id == len(data) - 1:
        print("Finished!")
        exit(0)
    return data, cur_id


def update_selected_text(event):
    selected_text = text_box.get(tkinter.SEL_FIRST, tkinter.SEL_LAST) if text_box.tag_ranges(tkinter.SEL) else ""
    cur_selection.config(text=selected_text)


def add_text():
    global selected_words, cur_selection, selected_box
    selected_words.append(cur_selection.cget("text"))
    selected_box.delete(1.0, tkinter.END)
    selected_box.insert(tkinter.END, utils.produce_shown_words(selected_words))


def clear_text():
    global selected_words, selected_box
    selected_words = []
    selected_box.delete(1.0, tkinter.END)


def next_sentence():
    global data, cur_id, selected_words, selected_box, cur_selection, text_box, id_box
    data[cur_id]['Private_Entities'] = selected_words
    data[-1]['cur_id'] = cur_id + 1
    utils.write_tmp_file(data)

    data, cur_id = init()
    cur_selection.config(text='No Content')
    selected_box.delete(1.0, tkinter.END)
    text_box.delete(1.0, tkinter.END)
    text_box.insert(tkinter.END, data[cur_id]['Input Text'])
    selected_words = []
    id_box.config(text=f'CUR:{cur_id} ALL:{len(data)-1}')


def is_ambigorous():
    global data, cur_id, selected_words, selected_box, cur_selection, text_box, id_box
    data[cur_id]['Private_Entities'] = ["???"]
    data[-1]['cur_id'] = cur_id + 1
    utils.write_tmp_file(data)

    data, cur_id = init()
    cur_selection.config(text='No Content')
    selected_box.delete(1.0, tkinter.END)
    text_box.delete(1.0, tkinter.END)
    text_box.insert(tkinter.END, data[cur_id]['Input Text'])
    selected_words = []
    id_box.config(text=f'CUR:{cur_id} ALL:{len(data)-1}')


if __name__ == '__main__':
    data, cur_id = init()
    top = tkinter.Tk()
    top.title('LabelLabor')
    top.geometry('1024x768')

    font = tfont.Font(family='times', size=20, slant='italic')

    text_box = tkinter.Text(top, font=font, height=10, width=60)
    text_box.place(relx=0.1, rely=0.02)
    text_box.insert(tkinter.END, data[cur_id]['Input Text'])

    instruction_box = tkinter.Label(top , text='Current Selection:', font=font)
    instruction_box.place(relx=0.35, rely=0.45)
    cur_selection = tkinter.Label(top, text='No Content', font=font)
    cur_selection.place(relx=0.35, rely=0.5)

    selected_words = []
    selected_box = tkinter.Text(top, font=font, height=10, width=10)
    selected_box.place(relx=0.1, rely=0.5)
    selected_box.insert(tkinter.END, utils.produce_shown_words(selected_words))

    id_box = tkinter.Label(top, text=f'CUR:{cur_id} ALL:{len(data)-1}', font=font)
    id_box.place(relx=0.4, rely=0.85)

    b_add = tkinter.Button(top, text='Add', command=add_text)
    b_add.place(relx=0.3, rely=0.7, relwidth=0.1, relheight=0.04)

    b_clear = tkinter.Button(top, text='Clear', command=clear_text)
    b_clear.place(relx=0.3, rely=0.75, relwidth=0.1, relheight=0.04)

    b_amb = tkinter.Button(top, text='Ambiguous', command=is_ambigorous)
    b_amb.place(relx=0.5, rely=0.7, relwidth=0.1, relheight=0.1)

    b_next = tkinter.Button(top, text='Next', command=next_sentence)
    b_next.place(relx=0.7, rely=0.7, relwidth=0.1, relheight=0.1)

    text_box.bind("<<Selection>>", update_selected_text)

    top.mainloop()
