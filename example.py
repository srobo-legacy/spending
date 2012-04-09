#!/usr/bin/env python
import spending
from decimal import Decimal as D

bud = spending.load_budget_with_spending( "./" )

for b in bud.walk():
    spent = D()
    for t in b.transactions:
        spent += t.cost
    print b.name, b.cost, spent
