import requests
import os

def cut_string(input_str, head, tail):
    if isinstance(
        head,
        str) and isinstance(
            tail,
            str) and isinstance(
            input_str,
            str):
        start = input_str.find(head) + len(head)
        end = input_str.find(tail, start)

        rt_str = ""
        for index in range(start, end):
            rt_str += input_str[index]
        return rt_str
    else:
        raise TypeError("Inputs are not string!")


url_base="http://zyk.ajiao.com/dzkb/"

def get_name(content):
    cut1=cut_string(content,"trend","td_comm5")
    return cut_string(cut1,"n>","</s")

for i in range(100,500):
    url_base="http://zyk.ajiao.com/dzkb/"
    content=requests.get(url_base+str(i)+"_1.html").text
    print(str(i)+" > " + get_name(content))

