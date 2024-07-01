from main_classes import Sentence, Comment # Sentence/Commentクラス

comment1 = Comment("Agent1はみんなに黒だと言われている。その疑いを晴らすために、今夜は彼のことを占うよ", talker="Agent[00]", me="Agent[03]") 
protocol_list = comment1.remark_to_protocol(ruizido_check=True, check_gpt=True)


for protocol in protocol_list:
    print(protocol.verb, protocol.agent, protocol.role, protocol.team)
print(comment1.flag)

