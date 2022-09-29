from pprint import pprint

a = { 'a' :  1}

b = {'x' :'y'}
pprint(a)
pprint(b)


c = {**a , **b}
pprint(c)

pprint({**a, **b, **{'foo':'bar'}, "a":None})

pprint({**a, "a": 2})