keywords = ["ESTIMATE", "COMINGOUT", "DIVINATION", "GUARD", "VOTE", "ATTACK", "DIVINED", "IDENTIFIED", "GUARDED", "VOTED", "ATTACKED", 
           "AND", "OR", "NOT", "XOR",  ]
verbs = ["ESTIMATE", "COMINGOUT", "DIVINATION", "GUARD", "VOTE", "ATTACK", "DIVINED", "IDENTIFIED", "GUARDED", "VOTED", "ATTACKED"]

def keyword_check(protocol) :
    #OVERとSKIPを確認
    if protocol == "OVER" :
        return "OVER"
    elif protocol == "SKIP" :
        return "SKIP"
    
    #REQUEST文/INQUIRE文か判別
    elif protocol.split()[0] == "REQUEST" :
        return "REQUEST"
    
    elif protocol.split()[0] == "INQUIRE" :
        return "INQUIRE"
    
    #動詞・文構造を確定させる
    else :
        a = None
        for i in keywords:
            if i in [protocol.split()[0], protocol.split()[1]]:
                a = i
            else:
                pass
        return a
    

def first_translate(protocol):    #プロトコル文を最初の短い文章に翻訳する関数
    
    keyword = keyword_check(protocol)
    
    if keyword == "OVER" or keyword == "SKIP":
        return keyword
    
    elif keyword in verbs:  #一般動詞の場合
        if protocol.split()[0] == keyword: #主語なし
            if keyword == "ESTIMATE":
                return f"I think {protocol.split()[1]} is the {protocol.split()[2]}."
            elif keyword == "COMINGOUT":
                return f"I am the {protocol.split()[2]}."                       #comingoutを他人に対して使うことは想定していない
            elif keyword == "DIVINATION":
                return f"I will divine {protocol.split()[1]} tonight. "
            elif keyword == "GUARD":
                return f"I'm going to guard {protocol.split()[1]} from werewolf."
            elif keyword == "VOTE":
                return f"I'm going to vote {protocol.split()[1]} today."
            elif keyword == "ATTACK":
                return f"I will kill {protocol.split()[1]} tonight."
            elif keyword == "DIVINED":
                return f"I divined {protocol.split()[1]} last night and he was the {protocol.split()[2]}."
            elif keyword == "IDENTIFIED" :
                return f"I identified {protocol.split()[1]} as a medium last night and he was the {protocol.split()[2]}."
            elif keyword == "GUARDED":
                return f"I guaded {protocol.split()[1]} from werewolf last night."
            elif keyword == "VOTED":
                return f"I voted {protocol.split()[1]} yesterday."
            elif keyword == "ATTACKED":
                return f"I attacked {protocol.split()[1]} last night."
            else :
                return None
        
        elif protocol.split()[1] == keyword :
            if keyword == "ESTIMATE":
                return f"I think {protocol.split()[2]} is the {protocol.split()[3]}."
            elif keyword == "COMINGOUT":
                return f"I am the {protocol.split()[3]}."
            elif keyword == "DIVINATION":
                return f"I will divine {protocol.split()[2]} tonight. "
            elif keyword == "GUARD":
                return f"I'm going to guard {protocol.split()[2]} from werewolf."
            elif keyword == "VOTE":
                return f"I'm going to vote {protocol.split()[2]} today."
            elif keyword == "ATTACK":
                return f"I will kill {protocol.split()[2]} tonight."
            elif keyword == "DIVINED":
                return f"I divined {protocol.split()[2]} last night and he was the {protocol.split()[3]}."
            elif keyword == "IDENTIFIED" :
                return f"I identified {protocol.split()[2]} last night and he was the {protocol.split()[3]}."
            elif keyword == "GUARDED":
                return f"I guaded {protocol.split()[2]} from werewolf last night."
            elif keyword == "VOTED":
                return f"I voted {protocol.split()[2]} yesterday."
            elif keyword == "ATTACKED":
                return f"I attacked {protocol.split()[2]} last night."
            else :
                return None
            
    elif keyword == "REQUEST":
        if protocol.split()[2] == "(DIVINATION":
            return f"I want {protocol.split()[1]} to divine {protocol.split()[3]}."
        elif protocol.split()[2] == "(GUARD":
            return f"I want {protocol.split()[1]} to guard {protocol.split()[3]} tonight."
        elif protocol.split()[2] == "(VOTE":
            return f"I want {protocol.split()[1]} to vote {protocol.split()[3]} tonight."
        elif protocol.split()[2] == "(ATTACK":
            return f"I want {protocol.split()[1]} to assault {protocol.split()[3]} tonight."
        elif protocol.split()[2] == "(ESTIMATE":
            return f"I want {protocol.split()[1]} to consider that {protocol.split()[3]} is the {protocol.split()[4]}."
        elif protocol.split()[2] == "(COMINGOUT" and not protocol.split()[4] == "ANY)" :
            return f"I want {protocol.split()[1]} to coming out to be {protocol.split()[3]}."
        elif protocol.split()[2] == "(COMINGOUT" and protocol.split()[4] == "ANY)" :
            return f"I want {protocol.split()[1]} to coming out your job now."
        else: 
            return None
    
    elif keyword == "INQUIRE":
        return f"Hey {protocol.split()[1]}, I'm curious about {protocol.split()[2:]}."
    
    else: #ANDなどの演算子はだるいので一旦保留
        return None
    
