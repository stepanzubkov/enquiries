__author__ = 'Peter Holloway'
from enquiries.yesno import confirm
from enquiries.choices import choose
from enquiries.document import prompt as freetext

__all__ = ['confirm', 'choose', 'freetext']

del yesno, choices, document
