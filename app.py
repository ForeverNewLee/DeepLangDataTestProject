import gradio as gr
import traceback


def hello_world_fn(username: str) -> tuple[str, str]:
    try:
        return f"HELLO WORLD\n{username.upper()}", "SUCCESS"
    except Exception as e:
        return f"opus! some exception {e}\n{traceback.format_exc()}", "FAILED"


def parser_fn(html):
    result = []
    html_len = len(html)
    i = 0
    while i < html_len:
        if html[i:i+3] == "<p>":
            i+=3
            text = ""
            while i < html_len and html[i:i+4] !="</p>":
                if html[i]=="<":
                    while i<html_len and html[i] != ">":
                        i+=1
                    i+=1
                else:
                    text +=html[i]
                    i += 1
            result.append(text.strip())
            i += 4
        else:
            i += 1
    return "\n".join(result)


def main() -> None:
    with gr.Blocks(title="DeepLang Data test project") as demo:
        with gr.Tab("hello world 0"):
            raw_input = gr.Textbox(lines=1, placeholder="输入你的名字(英文)", label="")
            pack_output = gr.Textbox(label="输出")
            status_output = gr.Textbox(label="状态信息")

            btn = gr.Button("开始转换")
            btn.click(
                fn=hello_world_fn,
                inputs=raw_input,
                outputs=[pack_output, status_output],
            )

        with gr.Tab("hello world 1"):
            raw_input = gr.Textbox(lines=1, placeholder="输入你的名字(英文)", label="")
            pack_output = gr.Textbox(label="输出")
            status_output = gr.Textbox(label="状态信息")

            btn = gr.Button("开始转换")
            btn.click(
                fn=hello_world_fn,
                inputs=raw_input,
                outputs=[pack_output, status_output],
            )

        with gr.Tab("htme parser"):
            raw_input = gr.Textbox(label="")
            pack_output = gr.Textbox(label="输出")


            btn = gr.Button("开始转换")
            btn.click(
                fn=parser_fn,
                inputs=raw_input,
                outputs=[pack_output],
            )

    demo.queue(default_concurrency_limit=100).launch(
        inline=False,
        debug=False,
        server_name="127.0.0.1",
        server_port=8081,
        show_error=True,
    )


if __name__ == "__main__":
    main()
