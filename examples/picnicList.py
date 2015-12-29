guests = {'Alice': {'apples': 5, 'bananas': 10, 'peaches': 5},
          'Joe': {'buns': 10, 'hot dogs': 10, 'bananas': 5},
          'Zack': {'cookies': 20, 'soda': 2, 'buns': 2}}

def totalBrought(item):
    total = 0
    for k,v in guests.items():
        total += v.get(item, 0)
    return total

print 'apples: %d' % (totalBrought('apples'))
print 'buns: %d' % (totalBrought('buns'))
print 'cookies: %d' % (totalBrought('cookies'))
print 'bananas: %d' % (totalBrought('bananas'))
print 'soy milk: %d' % (totalBrought('soy milk'))