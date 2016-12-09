#! /usr/bin/env python

import sys
import itertools

if __name__ == '__main__':

    word_list_dict = dict()
    # 读取big_wordlist.txt文件，通过argv第一个参数传递
    for word in open(sys.argv[1], "r"):
        # 去换行符
        word = word.strip("\n")
        # 添加单词长度为关键字
        obj = word_list_dict.setdefault(len(word), {})
        # 创建一个key,是单词所有字符排序的字符串
        obj.setdefault("".join(sorted(word)), set()).add(word)

    while True:
        # 读取输入字符串
        input_str = input()
        if input_str == "":
            break
        input_list = input_str.split(" ")
        word_len = int(input_list[1])
        # 退出
        if word_len == 0:
            break
        letter = input_list[0]

        # 通过长度word_len，查找单词是否由letter_key构成
        res = set()
        if word_len in word_list_dict:
            if word_len > 8:
                for key in word_list_dict[word_len].keys():
                    al_count = [0]*26
                    flag = True
                    for l in letter:
                        al_count[ord(l)-ord('a')] += 1
                    for k in key:
                        al_count[ord(k)-ord('a')] -= 1
                        if al_count[ord(k)-ord('a')] < 0:
                            flag = False
                            break
                    if flag:
                        res.update(word_list_dict[word_len][key])
            else:
                for val in itertools.combinations(sorted(letter), word_len):
                    letter_key = "".join(list(val))
                    if letter_key in word_list_dict[word_len]:
                        res.update(word_list_dict[word_len][letter_key])

        if res:
            for r in sorted(list(res)):
                print(r)
        print(".")
