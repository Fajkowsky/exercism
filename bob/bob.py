import sys

answers = {
    'question': 'Sure.',
    'yelling': 'Whoa, chill out!',
    'empty': 'Fine. Be that way!',
    'else': 'Whatever.'
}


def hey(what):
    what = what.strip()
    if sys.version_info <= (3, 0, 0):
        what = what.decode('utf-8')
    if what.isupper():
        return answers['yelling']
    elif what.endswith('?'):
        return answers['question']
    elif not what:
        return answers['empty']

    return answers['else']
