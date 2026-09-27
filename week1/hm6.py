products={}
while True:
    menu=input("Please select one of the options\nadd\nsell\nsearch\nsave\nshow\nreport\nexit\n  ")
    if menu=="add":
        new_pro=input("enter name product:  ")
        qut_pro=int(input("enter quntity producy:  "))
        if new_pro in products:
            products[new_pro]+=qut_pro
        else:
            products[new_pro]=qut_pro
    if menu=="sell":
        name_pro=input("enter name product: ")
        qut_sel=int(input("enter quntity sell:  "))
        if name_pro in products and products[name_pro]>=qut_sel:
            products[name_pro]-=qut_sel
            if products[name_pro]==0:
                del products[name_pro]
        else:
            print("Insufficient stock")
    if menu=="search":
        name_ser=input("enter name product:  ")
        print(f"quntity {name_ser} is -->{products[name_ser]}")
    if menu=="show":
        for i,j in products.items():
            print(f" {i}--->{j}")
    if menu=="save":
        with open("pro.txt","w") as f:
            for i,j in products.items():
                f.write(f"{i} - {j}")
    if menu=="report":
        print(f"quntity all products: {len(products)} number")
        print(f"stock all :{sum(products.values())}")
        max_product = max(products, key=products.get)
        print(max_product,products[max_product])
        min_product = min(products, key=products.get)
        print(min_product,products[min_product])
    if menu=="exit":
        break



    