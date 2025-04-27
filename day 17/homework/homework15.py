def title_case(title):
    return ' '.join([title.split()[0].lower()] + [word.capitalize() for word in title.split()[1:]])
