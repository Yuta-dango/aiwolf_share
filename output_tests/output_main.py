from openai import OpenAI
import openai
import os

from output_module import first_translate

# APIキーを環境変数として設定
openai.api_key = os.environ["OPENAI_API_KEY"]

#入力のプロトコル文
protocol = "REQUEST ANY (COMINGOUT ANY ANY)"
first = first_translate(protocol)
if first == None:
  first = "SKIP"


#出力
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "system", 
      "content": "あなたは、人狼ゲームの参加者の、ドラえもんです。人狼ゲーム中で、発言したい内容が英語の一文で与えられるので、その趣旨を保ったまま、できる限り流ちょうな日本語で話を膨らませながら発言してください。最低でも3文は話すこと。"\
        "ただし、例外が存在するのでその場合は以下のように出力すること。"\
        "contentが「SKIP」または「OVER」の場合、出力はそのまま、SKIPおよびOVERを返してください。"
    },
    
    {
      "role": "user", 
      "content": first
    }
  ]
)

print(completion.choices[0].message.content)