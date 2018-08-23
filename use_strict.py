import sublime
import sublime_plugin

class InsertUseStrictCommand(sublime_plugin.TextCommand):
    def settings(self, key=None):
        settings = sublime.load_settings('UseStrict.sublime-settings')
        if not key:
            return settings
        return settings.get(key)

    def run(self, edit):
        quote_symbol = self.settings('quote_symbol')
        semicolon = ';' if self.settings('semicolon') else ''
        insert_position = 0
        insert_text = quote_symbol + 'use strict' + quote_symbol + semicolon + '\n'

        first_line = self.view.substr(self.view.line(0))

        if first_line.startswith("#!"):
            insert_position = self.view.text_point(1, 0)
            insert_text = '\n' + insert_text
        else:
            insert_text = insert_text + '\n'

        self.view.insert(edit, insert_position, insert_text)
