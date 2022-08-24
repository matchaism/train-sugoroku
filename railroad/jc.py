# 中央線
JC_rapid = ["東京", "神田", "御茶ノ水", "四ツ谷", "新宿", "中野", "高円寺", "阿佐ヶ谷", "荻窪", "西荻窪"]
JC_commuterrapid = ["東京", "神田", "御茶ノ水", "四ツ谷", "新宿", "中野", "荻窪"]
JC_specialrapid = ["東京", "神田", "御茶ノ水", "四ツ谷", "新宿", "中野"]
JC_commuterspecialrapid = ["東京", "神田", "御茶ノ水", "四ツ谷", "新宿"]


def JC_rapid_res(crr, b, i):
    idx_crr = JC_rapid.index(crr)

    if b == "中央線快速 下り方面":
        return JC_rapid[min(idx_crr + i, len(JC_rapid)-1)]
    elif b == "東京":
        return JC_rapid[max(idx_crr - i, 0)]

    return crr

def JC_commuterrapid_res(crr, b, i):
    idx_crr = JC_commuterrapid.index(crr)

    if b == "中央線快速 下り方面":
        return JC_commuterrapid[min(idx_crr + i, len(JC_commuterrapid)-1)]
    elif b == "東京":
        return JC_commuterrapid[max(idx_crr - i, 0)]

    return crr

def JC_specialrapid_res(crr, b, i):
    idx_crr = JC_specialrapid.index(crr)

    if b == "中央線快速 下り方面":
        return JC_specialrapid[min(idx_crr + i, len(JC_specialrapid)-1)]
    elif b == "東京":
        return JC_specialrapid[max(idx_crr - i, 0)]

    return crr

def JC_commuterspecialrapid_res(crr, b, i):
    idx_crr = JC_commuterspecialrapid.index(crr)

    if b == "中央線快速 下り方面":
        return JC_commuterspecialrapid[min(idx_crr + i, len(JC_commuterspecialrapid)-1)]
    elif b == "東京":
        return JC_commuterspecialrapid[max(idx_crr - i, 0)]

    return crr