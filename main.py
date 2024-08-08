from main_classes import Sentence, Comment # Sentence/Commentクラス

comment1 = Comment("みんな、自分の役職を早く言うてくれへん？ここで黙っとったら、怪しまれるで。", talker="Agent[00]", me="Agent[03]") 
protocol_list = comment1.remark_to_protocol(ruizido_check=True, check_gpt=True)


for protocol in protocol_list:
    print(protocol.verb, protocol.agent, protocol.role, protocol.team)
print(comment1.flag)

