class Editor(object):
    def __init__(self):
        self.text = ""
        self.history = []

    def save(self):
        mem = Memento()
        mem.text = self.text
        return mem

    def restore(self, mem):
        self.text = mem.text


class Memento(object):
    def __init__(self):
        self.text = ""


class SaveCommand(object):
    def __init__(self, editor):
        self.editor = editor
        self.history = []

    def execute(self):
        mem = self.editor.save()
        self.editor.history.append(mem)
        print(f"'{mem.text}' saved to history.")


class RestoreCommand(object):
    def __init__(self, editor):
        self.editor = editor

    def execute(self):
        last_mem = self.editor.history.pop()
        self.editor.restore(last_mem)
        print(f"'{last_mem.text}' restored")


def main():
    editor = Editor()
    save_command = SaveCommand(editor)
    restore_command = RestoreCommand(editor)

    editor.text += "Yesterday afternoon, "
    save_command.execute()
    editor.text += "I were in the park."
    restore_command.execute()
    editor.text += "I was in the park."
    save_command.execute()


if __name__ == "__main__":
    main()
