# Result

Ran the texttest tool, everything is fine except this

```
---------- Differences in stdout ----------
24c24
< Conjured Mana Cake, 2, 5
---
> Conjured Mana Cake, 2, 4
36c36
< Conjured Mana Cake, 1, 4
---
> Conjured Mana Cake, 1, 2
48c48
< Conjured Mana Cake, 0, 3
---
> Conjured Mana Cake, 0, 0
60c60
< Conjured Mana Cake, -1, 1
---
> Conjured Mana Cake, -1, 0
```

The stddout in texttest does not follow the rule as explained in the requirements, my guess is that it's on purpose

