items=[
    {"id":1,"name":"suagr","price":40,"avl_qty":10},
    {"id":2,"name":"milk","price":28,"avl_qty":40},
    {"id":3,"name":"teapowder","price":230,"avl_qty":100},
    {"id":4,"name":"potato","price":230,"avl_qty":100},
    {"id":5,"name":"tomatto","price":120,"avl_qty":5},
    {"id":6,"name":"carrot","price":80,"avl_qty":0},
    {"id":7,"name":"oreo","price":45,"avl_qty":0},
    {"id":8,"name":"hideandseek","price":50,"avl_qty":50}
]

# for i in items:
#     if i.get("price")<50:
#         print(i.get("name"))

# for i in items:
#     if i.get("name"):
#         print(i.get("name"))

# for i in items:
#     if i.get("avl_qty")>0:
#         print(i.get("name"))

# for i in items:
#     if i.get("price")<=50  and i.get("price")>=20:
#         print(i.get("name"))


# print(len(items),"products") 


costly_product=max(items,key=lambda i:i.get("price"))
print(costly_product)