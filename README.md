### Introduction
This script can split [COCA](https://www.wordfrequency.info/) vocabulary into small groups to be imported into a
dictionary app (e.g. Eudic) for studying.

Please refer to [COCA 词频表使用](https://zhuanlan.zhihu.com/p/53261968) and [快速掌握 COCA 词汇表](https://zhuanlan.zhihu.com/p/56823867).

### Requirements
- **Python 3**

Please make sure you have **Python 3** installed in your environment. For me, it's `/usr/bin/python3`.

### Usage

```
python split.py coca20000.txt 15
```
by default, the **Output file** is `coca20000_batch_import.txt`.

##### Note:
The last number 15 is the group size, it means each group contains 15 words, you can change it to fit your need.

### Files

- **`coca20000.txt`** contains the origianl vocabulary list
- **`coca_refined.txt`** contains the final refined vocabulary list according to this article [快速掌握 COCA 词汇表](https://zhuanlan.zhihu.com/p/56823867)
