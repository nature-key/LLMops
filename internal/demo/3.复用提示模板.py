from langchain_core.prompts import (PromptTemplate)


full_template = """
{instruction}

{example}

{start}
"""

full_prompt = PromptTemplate.from_template(full_template)


# 描述提示语
instruction_template = """你正在模拟{person}"""
instruction_prompt = PromptTemplate.from_template(instruction_template)

# 示例提示语
example_prompt = PromptTemplate.from_template("""下面是一个示例：
question:{example_question}
answer:{example_answer}
""")

# 开始提示语

start_prompt = PromptTemplate.from_template("""请根据以上示例，回答用户的问题：
{query}
""")


final_prompt=full_prompt.invoke({
    "instruction": instruction_prompt.format(person="专业的ai助手"),
    "example": example_prompt.format(example_question="你好", example_answer="你好,我很好"),
    "start": start_prompt.format(query="天气好吗"),
})

print(final_prompt.to_string())




