from . import TextFilter

class RemoveWhitespaceLinesTextFilter(TextFilter):
    def __init__(self, data=None):
        super().__init__(data)

    def filter(self, data=None, **kwargs):
        super().filter(data, kwargs=kwargs)
        line_set = set()
        self._text = '\n'.join(line_set.update(self._text.split('\n')))