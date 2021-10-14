
def translate(seq):
    """
    translates M2000 sequences to human readable sequences.py

    Arguemnts:
      - seq: string containin g M2000 sequences

    Returns:
      - new_seq: human-readable strings

    Examples:

    >>> translate("...")
    'AAA'

    >>> translate("*!")
    'TG'
    """
    seq = seq.replace('.', 'A')
    seq = seq.replace('-', 'C')
    seq = seq.replace('*', 'T')
    seq = seq.replace('!', 'G')
    return seq


import doctest
doctest.testmod()
