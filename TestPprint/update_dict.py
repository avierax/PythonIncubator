from pprint import pprint


def factory(**kwargs):
    my_dictionary = {'a': 'b', 'client': {'firstname': 'manolo'}}
    my_dictionary.update(kwargs)
    return my_dictionary


pprint(factory(foo='bar', client.lastname='sanchez'))
