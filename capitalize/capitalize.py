def capitalize(input_text):
    if isinstance(input_text, int):
        return 'it is a number!'

    if not input_text:
        return ''
    head, *tail = input_text
    rest_chars = ''.join(tail)
    return f'{head.upper()}{rest_chars}'