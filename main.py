import requests


url = "http://old.pep.com.cn/gzhx/gzhxjs/0pl/kb/dzkb/bx1/201009/t20100916_%page_index%.htm"
page_range = (899898, 900011)


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
    print("[download]" + img_url)
    img_content = requests.get(img_url).content
    with open(local_url, "wb") as file:
        file.write(img_content)


for page_index in range(page_range[0], page_range[1]):

    cleared_url = url.replace("%page_index%", str(page_index))
    page_content = requests.get(cleared_url).text

    img_url = cut_string(page_content, "align=center><IMG", " OLDSRC")
    if "建议您使用" in img_url:
        img_url = cut_string(page_content, "align=\"center\"><IMG", " OLDSRC")

    if "src=./"in img_url or "src=\"./"in img_url:

        if "\"" in img_url:
            img_extend = cut_string(img_url, "src=\"./", ".jpg") + ".jpg"
        else:
            img_extend = cut_string(img_url, "src=./", ".jpg") + ".jpg"

        img_url = "http://old.pep.com.cn/gzhx/gzhxjs/0pl/kb/dzkb/bx1/201009/" + img_extend
        download_pic(img_url, "pics\\" + str(page_index) + ".jpg")
