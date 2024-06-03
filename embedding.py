from openai import OpenAI # type: ignore
import openai # type: ignore
import os
import numpy as np
import pandas as pd

# APIキーを環境変数として設定
openai.api_key = os.environ["OPENAI_API_KEY"]

client = OpenAI()

def get_embedding(text, model="text-embedding-3-small"):
   result = client.embeddings.create(input = [text], model=model).data[0].embedding
   return np.array(result)

def cos_sim(a, b):
   return a@b / (np.linalg.norm(a) * np.linalg.norm(b))