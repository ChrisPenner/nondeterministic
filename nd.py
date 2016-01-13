class ND:
    def __init__(self, *args, **kwargs):
        self._store = list(*args)

    def __getattr__(self, name):
        print 'Running', name
        return ND([x.__getattribute__(name) for x in self._store])

    def __call__(self, *args, **kwargs):
        return ND([x(*args, **kwargs) for x in self._store])

    def __str__(self):
        s = ', '.join(str(e) for e in self._store)
        return "ND([{}])".format(s)
    
    def __repr__(self):
        s = ', '.join(str(e) for e in self._store)
        return "ND([{}])".format(s)

    def __coerce__(self, other):
        # This is used for integer math
        # print self, other
        return ND(coerce(x, other)[0] for x in self._store), other

    def __bool__(self):
        return any(self._store)
    __nonzero__=__bool__

    def filter(self, f):
        return ND(filter(f, self._store))

    def do(self, f):
        return ND(map(f, self._store))

    def cond(self, *conds):
        def mapper():
            for x in self._store:
                for cond in conds:
                    pred, f = cond
                    if pred(x):
                        yield f(x)
                        break
                else:
                    yield x
        return ND(cond_mapper())

    def do_if(self, cond, true_function, else_function=None):
        def mapper():
            for x in self._store:
                if cond(x):
                    yield true_function(x)
                else:
                    if else_function:
                        yield else_function(x)
                    else:
                        yield x
        return ND(mapper())




# nd = ND([15,2])
# print nd * 5

x = ND(xrange(1,30))
# x *= 20
# x -= 12
# x.do_if(lambda x: x % 2 == 0, lambda x: x/2)
# print x
y = True

while x.filter(lambda x: x % 2 == 0):
    x = x.do_if(lambda x: x % 2 == 0, lambda x: x / 2)

# print x

# nd = ND(['test', 'other'])
# print nd  == 'test'
# print nd._store

# nd = ND([[2, 1, 3],[4, 20, 5]])
# nd.append(15)
# nd.sort()
# print nd
# print sorted(nd)[0]

# nd = ND([ 15, 20, 25 ])

# print str(nd)
# print str(nd) + 'test'

# nd = [ 5 * x for x in nd]
# print sorted(nd)[0]


# nd = ND([1, 5, 10])
# nd /= 10.0
# print nd
# nd * 20
