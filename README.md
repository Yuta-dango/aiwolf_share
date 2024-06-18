# 各ディレクトリの概要
.ipynbは実験段階で、完成し次第.pyに変更する予定です。

# 6/17時点での問題点
- 占い結果の開示の文が、ほとんどの場合DIVINEDではなくESTIMATEで書かれる。考えられる理由としては、DIVINEDにはTEAMが付属するが、白黒ではなく人狼などと直接言うことが多いため、類似度で見たときにESTIMATEのほうが近くなってしまうと考えられる。→新しくTEAMをROLEに変えた分も加えてやってみる
- 否定の～ない　のような言い回しは、有無で意味が反転するが、類似度で判別しづらく、時折間違えてしまう（つくべきではないNOTがつくなど）。そもそもNOT文が用意されてないのが原因（CO）とそうでないのがある
- 全体的にみて、"人狼"のようなワードが入ると、ESTIMATEに流されやすくなり、文章が短めになると、COに流されやすくなる。（本来のなってほしい分を増やして、そうじゃないほうは減らすことで対処）

～閾値によって解決される問題もあるかもなので今後要検討～


以下のコードは、SentenceとCommentというクラスを利用して、Commentオブジェクトを生成し、その内容をプロトコルリストに変換するものだ。まず、コードの各部分について詳しく説明する。

python
コードをコピーする
from main_classes import Sentence, Comment  # Sentence/Commentクラスのインポート

# Commentクラスのインスタンス生成
comment1 = Comment("Agent[02]を占ったら黒だったよ。Agent[01]を占ったら白だったよ。", "Agent[00]", me="Agent[03]") 

# コメントをプロトコルリストに変換
protocol_list = comment1.remark_to_protocol()

if __name__ == "__main__":
    # プロトコルリストの内容を出力
    for protocol in protocol_list:
        print(protocol.verb, protocol.agent, protocol.role, protocol.team)
    # comment1のフラグを出力
    print(comment1.flag)
Comment クラスのインスタンス生成
comment1 という名前で Comment クラスのインスタンスを生成する。このインスタンスには、以下の3つの引数が渡されている：

text - コメントの内容: "Agent[02]を占ったら黒だったよ。Agent[01]を占ったら白だったよ。"
speaker - コメントを発したエージェント: "Agent[00]"
me - 自分自身のエージェントID: "Agent[03]"
remark_to_protocol メソッドの呼び出し
comment1 オブジェクトの remark_to_protocol メソッドを呼び出し、コメントをプロトコル形式に変換する。このメソッドは、おそらくコメントの内容を解析し、特定のアクションや発言をプロトコルとして抽出する。

プロトコルリストの出力
protocol_list には、プロトコルオブジェクトのリストが格納される。このリスト内の各プロトコルについて、verb（動詞）、agent（エージェント）、role（役割）、team（チーム）を出力する。

flag の出力
最後に、comment1 オブジェクトの flag 属性を出力する。このフラグは、コメントの解析結果に基づく何らかのステータスを示していると考えられる。

実行結果の例
もし remark_to_protocol メソッドが以下のように解析する場合：

Agent[02]を占ったら黒だったよ。 は、「占った」(divine) という動詞で、Agent[00] が Agent[02] を対象にし、その結果「黒」(werewolf) だったという情報をプロトコルとして出力する。
Agent[01]を占ったら白だったよ。 も同様に解析され、「占った」という動詞で、Agent[00] が Agent[01] を対象にし、その結果「白」(villager) だったという情報をプロトコルとして出力する。
