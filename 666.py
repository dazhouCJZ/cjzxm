import openai

# 填你的秘钥
openai.api_key = "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"


# 提问代码
def chat_gpt(prompt):
    # 你的问题
    prompt = prompt

    # 调用 ChatGPT 接口
    model_engine = "text-davinci-003"
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    response = completion.choices[0].text
    print(response)

chat_gpt("你能帮我列出十种语言吗")