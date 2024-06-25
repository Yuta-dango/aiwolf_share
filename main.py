from main_classes import Sentence, Comment # Sentence/Commentクラス

comment1 = Comment("占ってみたらAgent[02]は人狼だったよ。Agent[01]は人間だったよ。", talker="Agent[00]", me="Agent[03]") 
protocol_list = comment1.remark_to_protocol()

if __name__ == "__main__":
    for protocol in protocol_list:
        print(protocol.verb, protocol.agent, protocol.role, protocol.team)
    print(comment1.flag)
    print(comment1.talker)


