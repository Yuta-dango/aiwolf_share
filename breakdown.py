from openai import OpenAI # type: ignore
import openai # type: ignore
import os

# APIキーを環境変数として設定
openai.api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI()

def get_list(talker, sentense):
    """
    sentense: 発話内容
    """

    system = """
    You are playing a werewolf game. Write the output appropriately

    # output
    - English
    - python tupple including two elements
    - The first element is a python list(elements: contents of the input rewritten into concise contents)
    - the second element is a python bool for indicator of request and inquiry. 
    
    # rule 
    - each element in the list should be less than 12 words
    - Representing a person, use Agent[00], Agent[01], Agent[02], Agent[03], Agent[04], or I.
    - Representing the job title, use villager, werewolf, possessed, or seer
    - Ignore information that has nothing to do with werewolf game 
    - . is unnecessary
    - Indicate the subject matter.
    - The second element must be 0 or 1. It works as a flag. If the speaker request or inquire something to Agent[00], the flag must be 1. If else, the flag is 0.

    # example
    Speaker: Agent[00] 
    Input: エージェント[03]がずいぶん口をつぐんでるな。なんなんだあいつは。あいつが人狼かもしれん。今夜はエージェント[03]に投票するつもりや。
    Here, your answer should be (["Agent[03] is quiet", "Agent[03] might be a werewolf", "Agent[00] is planning to vote for Agent[03] tonight"], 0)
    """

    user = f"Speaker: {talker} Input: {sentense}"

# 1Mあたり80円/240円
# 入力が400、出力が100トークンの場合、発話1回あたり80/1000 + 240/10000 = 0.1円

    model = "gpt-3.5-turbo-0125" # gpt-3.5-turbo-0125
    completion = client.chat.completions.create(
      model=model,
      messages=[
        {"role": "system", "content": system},
        {"role": "user", "content": user}
      ]
    )
    return completion.choices[0].message.content


    if __name__ == "__main__":
        talker = "Agent[00]"
        sentence = "Agent[00]を占ったら黒だったよ。Agent[01]を占ったら白だったよ。"
        with open("output.log", 'a') as f:
          print('入力: ', file=f)
          print(user2, file=f)
          print(f'{model}: ', file=f)
          print(breakdown.get_list(talker, sentence), file=f)
          print(file=f)


