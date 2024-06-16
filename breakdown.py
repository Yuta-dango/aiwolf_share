from openai import OpenAI # type: ignore
import openai # type: ignore
import os

# APIキーを環境変数として設定
openai.api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI()

def get_list(talker, remark, model="gpt-3.5-turbo-0125", me='Agent[00]'):
    """
    sentense: 発話内容
    """

    system = f"""
    You are playing a werewolf game. Write the output appropriately

    # output
    - English
    - python tuple including two elements
    - The first element is a python list(elements: contents of the input rewritten into concise contents)
    - the second element is a python bool for indicator of request and inquiry. 
    
    # rule 
    - Remarks should be divided as finely as possible. Each element in the list should be less than 12 words (less than 8 words is better)
    - Use the following verbs actively: estimate, suspect, vote, divine, agree
    - Representing a person, use Agent[00], Agent[01], Agent[02], Agent[03], Agent[04], or I
    - Representing the job title, use werewolf, possessed, villager or seer
    - When referring to the result of divination, use "black" for werewolf or possessed, "white" for villager or seer
    - Ignore information that has nothing to do with werewolf game 
    - . is unnecessary
    - The second element must be 0 or 1. It works as a flag. If the speaker request or inquire something to {me}, the flag must be 1. If else, the flag is 0.
  
    # example
    Talker: Agent[00] 
    Remark: エージェント[03]がずいぶん口をつぐんでるな。なんなんだあいつは。あいつが人狼かもしれん。今夜はエージェント[03]に投票するつもりや。
    Here, your answer should be (["Agent[03] is quiet", "Agent[03] might be a werewolf", "I'm planning to vote for Agent[03] tonight"], 0)
    """

    user = f"Talker: {talker} Remark: {remark}"

# 1Mあたり80円/240円
# 入力が400、出力が100トークンの場合、発話1回あたり80/1000 + 240/10000 = 0.1円

    completion = client.chat.completions.create(
      model=model,
      messages=[
        {"role": "system", "content": system},
        {"role": "user", "content": user}
      ]
    )
    gpt_output = eval(completion.choices[0].message.content) # expeceted to be a tuple
    broken_list, frag = gpt_output[0], gpt_output[1]

    # tupleの中身がstrの場合、evalで変換
    if type(broken_list) == str:
        broken_list = eval(broken_list)
    if type(frag) == str:
        frag = eval(frag)
    
    return broken_list, frag


if __name__ == "__main__":
    talker = "Agent[03]"  
    remark = "Agent[02]を占ったら黒だったよ。Agent[01]を占ったら白だったよ。"
    with open("output.log", 'a') as f:
        print('入力: ', file=f)
        print(remark, file=f)
        print(get_list(talker, remark), file=f)
        print(file=f)



