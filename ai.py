# from openai import OpenAI


# def openAi(text1,text2):
#     client = OpenAI(api_key="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")

#     query = f"""Compare the two text provided below. Then provide feedback on the similarity for plagariasm.
#                 Text1 : {text1}
#                 Text2 : {text2}
#     """
#     response = client.chat.completions.create(
#         model="gpt-4-0613",
#         # response_format={ "type": "json_object" },
#         messages=[
#             {"role": "system", "content": f"you are a helpful assistant"},
#             {"role": "user", "content": f"{query}"}
#         ]
# return (response.choices[0].message.content)
#     )
#     # print(response.choices[0].message.content)

from openai import OpenAI

def openAi(text1, text2,text3,text4,text5):
    client = OpenAI(api_key="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")

    query = f"""Compare the two text provided below. Then provide feedback on the similarity for plagiarism.
                Text1 : {text1}
                Text2 : {text2}
                Text3 : {text3}
                Text4 : {text4}
                Text5 : {text5}
    """
    response = client.chat.completions.create(
        model="gpt-4-0613",
        messages=[
            {"role": "system", "content": "you are a helpful assistant"},
            {"role": "user", "content": f"{query}"}
        ]
    )
    return response.choices[0].message.content
