try:
    import sublime
except ImportError, e:
    raise e
import os
import json

AUTO_SAVE_SESSION = u'Settings/Auto Save Session.sublime_session'
SESSION = u'Settings/Session.sublime_session'


class Assistant():
    def __init__(self):
        self.st_path, _ = os.path.split(sublime.packages_path())
        self.get_session()

    def get_session(self):
        path = os.path.join(self.st_path, AUTO_SAVE_SESSION)
        if os.path.exists(path):
            with open(path) as f:
                session_data = f.read()
        elif os.path.exists(os.path.join(self.st_path, SESSION)):
            with open(os.path.join(self.st_path, SESSION)) as f:
                session_data = f.read()
        else:
            raise IOError('Session not found')

        js = json.JSONDecoder(strict=False)
        self.session = js.decode(session_data)

    def is_portable(self):
        _, _dir = os.path.split(self.st_path)
        return _dir == u'Data'

    def is_minimap_visible(self):
        return self.session['windows'][0]['show_minimap']

    def is_status_bar_visible(self):
        return self.session['windows'][0]['status_bar_visible']

    def is_side_bar_visible(self):
        return self.session['windows'][0]['side_bar_visible']
