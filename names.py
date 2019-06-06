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


url_base = "http://zyk.ajiao.com/dzkb/"


def get_name(content):
    cut1 = cut_string(content, "trend", "td_comm5")
    return cut_string(cut1, "n>", "</s")


def get_version(content):
    cut1 = cut_string(content, "td_comm5", "trend")
    cut2 = cut_string(cut1, "教育版本", "/p")
    cut3 = cut_string(cut2, "blue\">", "<")
    return cut3


for i in range(270, 300):
    try:
        url_base = "http://zyk.ajiao.com/dzkb/"
        content = requests.get(url_base + str(i) + "_1.html").text
        print(str(i) + " > " + get_version(content) + ": " + get_name(content))
        import time

        # time.sleep(5)

    except:
        pass
