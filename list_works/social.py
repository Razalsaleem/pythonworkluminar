all_users=["sachin","dhoni","kohli","rohith","sanju","padikkal"]

sanju_followings=["padikkal","sachin"]

st1=set(all_users)
st2=set(sanju_followings)
diff_set=st1.difference(st2)

sanju_list=list(diff_set)

sanju_pos=diff_set.index("sanju")

diff_set.pop(sanju_pos)

print(diff_set)