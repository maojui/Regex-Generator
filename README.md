# Regex-Generator

Usage : 

```
python3 project.py
```

# parser.py

先找出最長的 Common String 作為基底

剩下的切割後給 maker 製造 regex

# maker.py 

提供 parser 可以處理一列東西

如 `['kkab', 'zznew', 'tw']`

化簡成 `.{2,5}`, `\w{2,5}`, `(kkab|zznew|tw)`, ... 依基因而定

# utils.py

放會用到的 Common string 和 Longest common subsequence 演算法 

# corpse.py 

Code 屍體