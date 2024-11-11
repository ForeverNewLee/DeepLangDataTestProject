import traceback

def html_parse(words: str) -> tuple[str, str]:
    """
    解析HTML内容，提取<p>标签内的文本。

    Args:
        words (str): 待解析的HTML内容字符串。

    Returns:
        tuple[str, str]: 一个包含两个字符串的元组。第一个字符串是提取的文本内容，每行对应一个<p>标签内的文本；
                        第二个字符串是操作结果状态，成功为"SUCCESS"，失败为"FAILED"。

    Raises:
        不显式抛出异常，但内部处理中捕获到异常时会将错误信息包含在返回元组的第一个字符串中。

    """
    try:
        
        start_tag = "<p>"
        end_tag = "</p>"
        start_index = 0
        text_content = []

        while True:
            start_index = words.find(start_tag, start_index)
            if start_index == -1:
                break 
            end_index = words.find(end_tag, start_index + len(start_tag))
            if end_index == -1:
                break  # 如果没有找到</p>标签，结束循环
            # 提取<p>和</p>之间的文本
            text = words[start_index + len(start_tag):end_index].strip()
            if 'p>' not in text:
                idx = text.find('<', 0)
                text_content.append(text[:idx].strip() if idx != -1 else text)
            start_index = end_index + len(end_tag)
        return '\n'.join(str(num) for num in text_content), "SUCCESS"
    except Exception as e:
        return f"opus! some exception {e}\n{traceback.format_exc()}", "FAILED"


def test_html_parse_no_p_tag():
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
    expected_text = '333\n555'
    expected_status = "SUCCESS"
    actual_text, actual_status = html_parse(html_content)
    assert actual_text == expected_text
    assert actual_status == expected_status
    
if __name__ == "__main__":
    test_html_parse_no_p_tag()
