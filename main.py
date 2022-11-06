class ProgressBar:
    def __init__(self, total):
        self.total = total
        self.current = 0
        self.prev_len = 0

    def next(self, string):
        self._clear()

        self.current += 1
        assert self.current <= self.total, 'Incorrect total task count'

        current_string = '[{}/{}] {}'.format(self.current, self.total, string)
        self.prev_len = len(current_string)
        print(current_string, end='', flush=True)

    def _clear(self):
        import sys

        if self.current == 0:
            return

        if sys.__stdout__.isatty():
            print('\r', end='')
            print(' ' * self.prev_len, end='')
            print('\r', end='')
        else:
            print('')
