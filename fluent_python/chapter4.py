# -*- coding: utf-8 -*-
"""
An encoding is an algorithm that converts code points to byte sequences and vice-versa.

Converting from code points to bytes is encoding; from bytes to code points is decoding.

In python3, str represents Unicode text data, bytes represents binaray data.
http://www.ituring.com.cn/article/1116

How to display the binary data:
1. For bytes in the printable ASCII range, the ASCII character itself is used.
2. For bytes corresponding to tab, newline, carriage return and \, the escape sequences \t, \n, \r and \\ are used.abs
3. For every other type byte value, an hexadecimal escape sequence is usued, e.g. \X00 is the null byte.

The array object represents the sequence of basic values: characters, integers and floating point numbers.
"""

# Example 4-2.
cafe = bytes('cafe', encoding='utf-8')
print(cafe)
cafe = bytearray(cafe)
print(cafe)