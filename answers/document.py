from curtsies import Input, FSArray , CursorAwareWindow, fsarray
from curtsies.fmtfuncs import red, bold, green, on_blue, yellow
import textwrap


class Document:
    def __init__(self, text='', cursor=None):
        if cursor is None:
            cursor = len(text)
        self._lbuffer = text[:cursor]
        self._rbuffer = text[cursor:]

    def handle(self, key):
        if len(key) == 1:
            self.add(key)
        elif key == '<SPACE>':
            self.add(' ')
        elif key == '<BACKSPACE>':
            self.bksp()
        elif key == '<Ctrl-j>':
            self.add('\n')

    def add(self, key):
        self._lbuffer += key

    def bksp(self):
        self._lbuffer = self._lbuffer[:-1]

    @property
    def lines(self):
        # TODO: should be wrapped
        return str(self).split('\n')

    @property
    def cursor(self):
        return len(self._lbuffer.split('\n'))-1, len(self._lbuffer) - self._lbuffer.rfind('\n') - 1

    def __format__(self, fmt):
        return str(self)

    def __str__(self):
        return self._lbuffer+self._rbuffer

def prompt(msg):
    with CursorAwareWindow(extra_bytes_callback=lambda x:x, hide_cursor=False) as window:
        document = Document()
        with Input() as keys:
            for key in keys:
                if key == '<Ctrl-j>':
                    window.render_to_terminal([], (0,0))
                    return str(document)
                if key == '<Esc+Ctrl-J>':
                    key = '<Ctrl-j>'
                document.handle(key)
                window.render_to_terminal(fsarray(document.lines), document.cursor)
