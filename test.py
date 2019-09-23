def pointer_count(start,pointer):
    if (ord(pointer)>ord(start)):
        return ord(pointer)-ord(start)
    elif (ord(pointer)<ord(start)):
        return 26-(ord(start)-ord(pointer))
    return 26
if __name__ == "__main__":

    s1 = 'X'
    s2 = 'D'
    s3 = 'H'
    r1 = 'W'
    r2 = 'F'
    r3 = 'R'
    r1_count = pointer_count(s1, r1)
    r2_count = pointer_count(s2, r2)
    r3_count = pointer_count(s3, r3)

    while(1):
        INPUT = input()  # 輸入第一個密碼
        r1_count -= 1
        if ((ord(s1) + 1) > 90):
            s1 = chr(65)
        else:
            s1 = chr(ord(s1) + 1)  # input後輪盤1轉動
        if (r2_count == 1):
            r2_count -= 1
            if (r2_count == 0):
                r2_count = 26
                r3_count -= 1
                if ((ord(s3) + 1) > 90):
                    s3 = chr(65)
                else:
                    s3 = chr(ord(s3) + 1)  # 轉盤2一圈後輪盤3轉動
            if ((ord(s2) + 1) > 90):
                s2 = chr(65)
            else:
                s2 = chr(ord(s2) + 1)  # 轉盤1一圈後輪盤2轉動
        if (r1_count == 0):
            r1_count = 26
            r2_count -= 1
            if (r2_count == 0):
                r2_count = 26
                r3_count -= 1
                if ((ord(s3) + 1) > 90):
                    s3 = chr(65)
                else:
                    s3 = chr(ord(s3) + 1)  # 轉盤2一圈後輪盤3轉動
            if ((ord(s2) + 1) > 90):
                s2 = chr(65)
            else:
                s2 = chr(ord(s2) + 1)  # 轉盤1一圈後輪盤2轉動

        # r1_count -= 1
        # if (r1_count == 0):
        #     s2 = chr(ord(s2)+1)
        #     r2_count -= 1
        # if (r2_count == 1):
        #     s2 = chr(ord(s2) + 1)
        #     r2_count = 25
        # # print(s2)
        #
        # if ((ord(s1)+1)>90):
        #     s1 = chr(65)
        # s1 = chr(ord(s1)+1) # input後輪盤1轉動



        print('s1: ',s1,'s2: ',s2,'s3: ',s3)
        print(r1_count,' ',r2_count,' ',r3_count)
