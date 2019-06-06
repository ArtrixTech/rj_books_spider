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


def download_pic(img_url, local_url):
    img_content = requests.get(img_url).content
    with open(local_url, "wb") as file:
        file.write(img_content)


def get_range(content):
    cut1 = cut_string(content, "td_comm5", "trend")
    cut2 = cut_string(cut1, ">页码：</span><span class=", "/span")
    cut3 = cut_string(cut2, ">", "<")
    return int(cut3)


url_base = "http://zyk.ajiao.com/dzkb/"
img_base = "http://res.ajiao.com/uploadfiles/Book/"
book_code = input("Input the book code:\n")
content = requests.get(url_base + book_code + "_1.html").text
page_count = get_range(content)
print("  > This book contains " + str(page_count) + " pages.")

save_dir = 'pics\\' + str(book_code) + "\\"
if not os.path.exists("pics"):
    os.mkdir("pics")
if not os.path.exists(save_dir):
    os.mkdir(save_dir)

for page_index in range(1, page_count + 1):
    img_url = img_base + book_code + "/" + str(page_index) + '.jpg'
    print("  > Downloding pic #" + str(page_index))

    download_pic(img_url, "pics\\" + str(book_code) + "\\" + str(page_index) + ".jpg")
