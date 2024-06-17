import breakdown # remarkを要素に分割/flag
import embedding # 文章をembedding
from embedding import get_embedding, cos_sim # embeddingの取得/cos類似度
from csv_to_df import prepare_dataframe

# dataframeの設定
df = prepare_dataframe("embedded_all.csv")

class Sentence:
    def __init__(self, verb, agent, role, team):
        self.verb = verb
        self.agent = agent
        self.role = role
        self.team = team


class Comment:
    def __init__(self, remark, talker):
        self.remark = remark
        self.talker = talker
        self.flag = None 
        
    def remark_to_protocol(self):
        """
        大元のメソッド. Commentのインスタンスに対して呼び出すと、remarkがプロトコルに変換され、flagが立つ
        """
        vectorlist = self.remark_to_vectors(self.talker, self.remark)
        return self.vectors_to_protocols(vectorlist)

    def remark_to_vectors(self, talker, remark):
        """
        gptの処理を呼び出して、remarkを要素に分割し、各要素をembeddingしたリストを返す
        flagも設定する
        """
        return_from_gpt = breakdown.get_list(talker, remark)
        sentences = return_from_gpt[0]
        self.flag = return_from_gpt[1]

        # 各要素をembeddingしたリスト
        return [get_embedding(sentence) for sentence in sentences]
    
    def ruizido(self, vector):
        """
        入力文の要素の一つをembedしたベクトルと、データフレームのembedded列のベクトルとの類似度を計算し、最も類似度が高い文のindexを返す
        """
        similarity_list = [] #一旦、類似度だけを格納しておくためのリスト
        for i in df["embedded"]:
            similarity_list.append(cos_sim(i, vector))
            
        index = similarity_list.index(max(similarity_list))
        max_sim = max(similarity_list)
        
        
        #最大の類似度と、その文のindexを返す
        return (max_sim, index)

    #最終的なリストの作成
    #from send import Sentence

    def vectors_to_protocols(self, vectorlist): #vectorlistはto_vectors(talker, comment)の返り値
        protocol_list = []
        for i in vectorlist:
            verb = df.loc[self.ruizido(i)[1], "Verb"]
            agent = df.loc[self.ruizido(i)[1], "Agent"]
            role = df.loc[self.ruizido(i)[1], "Role"]
            team = df.loc[self.ruizido(i)[1], "Team"]
            
            
            
            sentence = Sentence(verb, agent, role, team)
            protocol_list.append(sentence)
        
        return protocol_list
        