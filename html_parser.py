html_content = '''
<a>
   111
   <b>222</b>
   <p>
      333
      <c>444</c>
   </p>
   <p>555</p>
</a>
'''

def get_text(words):
    start_tag = "<p>"
    end_tag = "</p>"
    start_index = 0
    text_content = []

    while True:
        start_index = html_content.find(start_tag, start_index)
        if start_index == -1:
            break 
        end_index = html_content.find(end_tag, start_index + len(start_tag))
        if end_index == -1:
            break  # 如果没有找到</p>标签，结束循环
        # 提取<p>和</p>之间的文本
        text = html_content[start_index + len(start_tag):end_index].strip()
        if 'p>' not in text:
            idx = text.find('<', 0)
            text_content.append(text[:idx].strip() if idx != -1 else text)
        start_index = end_index + len(end_tag)
    return text_content

if __name__ == "__main__":
    texts = get_text(html_content)
    for text in texts:
        print(text)
