# introduction

knpの実行結果を保存しておき、解析時間を短します。

```
from dumpKNP import KNP
knp = KNP()

# このknp.parseにかかる時間が短くなります
knp_result = knp.parse(string)
```

何回かsample.pyを実行してみて、時間を確認してください
