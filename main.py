from main_classes import Sentence, Comment # Sentence/Commentクラス

comment1 = Comment("""Agent[03]が言う通り、Agent[02]は占い師ではなく村人です。Agent[01]も占い師ではなく、村人として協力していくべきです。混乱を招くことは避けましょう。""", talker="Agent[00]", me="Agent[03]") 
protocol_list = comment1.remark_to_protocol(ruizido_check=True, check_gpt=True)


for protocol in protocol_list:
    print(protocol.verb, protocol.agent, protocol.role, protocol.team)
print(comment1.flag)
print(comment1.talker)

