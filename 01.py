"""
收银系统
"""
import datetime
import random


class CommodityInfo():
    def __init__(self, cid=0, name="", price=0, count=0):
        self.cid = cid
        self.name = name
        self.price = price
        self.count = count


cinfo = [CommodityInfo(cid=1001, name="华为手机", price=5000, count=random.randint(1,2)),
         CommodityInfo(cid=1002, name="小米手机", price=2999, count=random.randint(1,2)),
         CommodityInfo(cid=1003, name="苹果手机", price=7999, count=random.randint(1,2)),
         CommodityInfo(cid=1004, name="一加手机", price=4999, count=random.randint(1,2))]
def cashier():
    # 建立商品字典
    commodity_dict = {}
    for item in cinfo:
        commodity_dict[item.price]=item.count
    print(commodity_dict)
    amount = 0
    for price, count in commodity_dict.items():
        amount += price * count
    data ="     XXX自助超市     "
    with open("receipt", 'w') as f:
        f.write(data+'\n')
        f.write("编号 "+"名称　   "+"单价  "+"数量　\n")
        for item in cinfo:
            f.write(str(item.cid)+item.name+": "+str(item.price)+"  "+str(item.count)+'\n')
        f.write(f"总计:{amount}元\n")
        f.write( f"{datetime.datetime.today():%Y‐%m‐%d %H:%M:%S}")
cashier()
