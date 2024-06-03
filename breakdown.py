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
    - Python list (elements: contents of the input rewritten into concise contents)

    # rule 
    - each element should be less than 12 words
    - Representing a person, use Agent[00], Agent[01], Agent[02], Agent[03],or Agent[04]
    - Representing the job title, use villager, werewolf, possessed, or seer
    - Ignore information that has nothing to do with werewolf game 
    - . is unnecessary
    - Indicate the subject matter.

    # example
    Speaker: Agent[00] 
    Input: エージェント[03]がずいぶん口をつぐんでるな。なんなんだあいつは。あいつが人狼かもしれん。今夜はエージェント[03]に投票するつもりや。
    Here, your answer should be ["Agent[03] is quiet", "Agent[03] might be a werewolf", "Agent[00] is planning to vote for Agent[03] tonight"]
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


