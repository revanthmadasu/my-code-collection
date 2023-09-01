def str_to_int(res):
    int_list1=[]
    for u in res:
        int_list1.append(int(u))
    return(int_list1)
given_input=input().split(" ")
main_res=[]
for i in given_input:
    c=""
    for j in i:
        if j.isdigit():
            c=c+j
        elif c:
            main_res=main_res+[c]
            c = ""
    if c:
        main_res=main_res+[c]
res=[]
for ele in main_res:
    if ele.strip():
        res.append(ele)
wanted_list=str_to_int(res)
main_len=len(wanted_list)
print(sum(wanted_list))
print((sum(wanted_list))/main_len)