# 入力
S=input()

# 答え
ans=0
# 初期値
i=0
# i<(Sの文字数)である間
while i<len(S):
    # S[i]~S[i+1]=「00」ならば
    if S[i:i+2]=="00":
        # 答えにプラス1
        ans+=1
        # 2つ進める
        i+=2
    # そうでなければ
    else:
        # 答えにプラス1
        ans+=1
        # 一つ進める
        i+=1

# 答えの出力
print(ans)