def capitalize(input_text):
    if not input_text:
        return ''
    return input_text.capitalize()
    head, *tail = input_text
    rest_chars = ''.join(tail)
    return f'{head.upper()}{rest_chars}'