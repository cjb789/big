from socket import *
import datetime
c=socket()
ADDR=(("127.0.0.1",7777))
c.connect(ADDR)
class CommodityInfo():
    def __init__(self, cid="", name="", price=0.0, count=0,a=0):
        self.cid = cid
        self.name = name
        self.price = price
        self.count = count
        self.a=a
    # 输入商品编号
    def input_id(self):
      while True:
        cid=input("请输入商品编号:")
        try:
            int(cid)
        except:
            print("商品id不对,再次输入!")
            continue
        return cid
    # 输入商品数量
    def input_count(self):
        while True:
            try:
                self.count = int(input("请输入商品数量:"))
            except:
                print("输入不对,再次输入!")
                continue
            return self.count
def cash():
    # 建立商品字典
    commodity_dict = {}
    for item in list01:
        commodity_dict[item.price]=item.count
    # print(commodity_dict)
    amount = 0
    for price, count in commodity_dict.items():
        amount += price * count
    pay=float(input(f"总合计{amount}人民币,请您支付:"))
    zhaohui=pay-amount
    print(f"找给您{zhaohui}人民币")
    data ="     XXX自助超市     "
    with open("receipt", 'w') as f:
        f.write(data+'\n')
        f.write("编号 "+"名称　   "+"单价  "+"数量　\n")
        for item in list01:
            f.write(str(item.cid)+item.name+": "+str(item.price)+"  "+str(item.count)+'\n')
        f.write(f"总计:{amount}元\n")
        f.write( f"{datetime.datetime.today():%Y‐%m‐%d %H:%M:%S}")
ci=CommodityInfo()
list01=[]
def main():
    jian = 1
    all = ""
    while True:
        cid=ci.input_id()
        c.send(cid.encode())
        id_info=c.recv(1024)
        c.send("我需要商品名称".encode())
        name_info=c.recv(1024)
        c.send("我需要商品价格".encode())
        price_info=(c.recv(1024)).decode()
        c.send(b"all")
        info=c.recv(1024)
        count_info=ci.input_count()
        all+=f"商品{jian} "+info.decode()+f"数量:{count_info}\n"
        print(all)
        list01.append(CommodityInfo(cid=id_info.decode(),name=name_info.decode(),price=float(price_info),count=count_info))
        # 是否继续添加商品
        info = input("是否继续添加商品 yes or no:")
        if info == "yes":
            jian+=1
            c.send(b"goin")
            continue
        else:
            c.send(b"##")
            print(list01)
            c.close()
            break
    cash()
if __name__ == '__main__':
    main()