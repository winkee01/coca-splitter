### Introduction
This script can split [COCA](https://www.wordfrequency.info/) vocabulary into small groups to be imported into
dictionary app (e.g. Eudic) for studying.

Please refer to [COCA 词频表使用](https://zhuanlan.zhihu.com/p/53261968) and [快速掌握 COCA 词汇表](https://zhuanlan.zhihu.com/p/56823867).

### Requirements
- **Python 2**

This script is orginally written in Python 2, so make sure you have Python 2 installed in your environment. Also, the script does not have any third-party library dependencies, so you don't need to install anything other than Python 2.

### Usage

```
python split.py coca20000.txt 15
```

##### Note:
The last number 15 is the group size, it means each group contains 15 words, you can change it to your need.

### Files

- **`coca20000.txt`** contains the origianl vocabulary list
- **`coca_refinded`** contains the final refined vocabulary list according to this article [快速掌握 COCA 词汇表](https://zhuanlan.zhihu.com/p/56823867)