import sublime
import sublime_plugin

class AppendUseStrictCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        insert_position = 0
        insert_text = '\'use strict\'\n'

        first_line = self.view.substr(self.view.line(0))

        if first_line.startswith("#!"):
            insert_position = self.view.text_point(1, 0)
            insert_text = '\n' + insert_text
        else:
            insert_text = insert_text + '\n'

        self.view.insert(edit, insert_position, insert_text)
