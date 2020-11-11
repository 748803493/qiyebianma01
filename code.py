import os, time, string, random, tkinter, qrcode
from pystrich.ean13 import EAN13Encoder
import tkinter.filedialog      # 文件对话框，其中tkinter模块为python的标准图形化界面接口
import tkinter.messagebox      # 消息对话框
from tkinter import *
from string import digits
root = tkinter.Tk()  # 建立根窗口
# 初始化数据
number = "1234567890"
letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
allis = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+"
i = 0
randstr = []
fourth = []
fifth = []
randfir = ""
randsec = ""
randthr = ""
str_one = ""
strone = ""
strtwo = ""
nextcard = ""
userput = ""
nres_letter = ""


def mainmenu():

    print("""\033[1;34m
    **********************************************************
                        企业编码生产系统
    **********************************************************
        1.生产6位数字防伪编码（213563型）
        2.生成9位系列产品数字防伪编码（879-33577型）
        3.生成25位混合产品序列号（R2R12-M7TY3-GH35O-DW2K8）
        4.生成含数据分析功能的防伪编码（1245M9569D3）
        5.智能批量生产带数据分析功能的防伪编码
        6.后续补加生成防伪码（5A64M5621A3）
        7.EAN-13条形码批量生成
        8.二维码批量输出
        9.企业粉丝防伪码抽签
        0.退出系统
    **********************************************************
                    说明：通过数字键选择菜单
    **********************************************************
    \033[0m""")


def input_validation(insel):
    if str.isdigit(insel):
        if insel == "0":
            print("\033[1;31;40m 注意：即将退出系统！！！\033[0m")
            return "0"
        else:
            return insel
    else:
        print("\033[1;31;40m 非法输入，请重新输入！！！\033[0m")
        return 0


def scode1(schoice):
    # 调用inputbox函数对输入数据进行非空、输入合法性判断
    incount = inputbox("\033[1;32m     请输入您要生成验证码的数量:\33[0m", 1, 0)
    while int(incount) == 0:  # 如果输入为字母或数字0,则要求重新输入
        incount = inputbox("\033[1;32m     请输入您要生成验证码的数量:\33[0m", 1, 0)
    randstr.clear()  # 清空保存批量注册码信息的变量randstr
    for j in range(int(incount)):  # 根据输入的验证码数量循环批量生成注册码
        randfir = ''  # 设置存储单条注册码的变量为空
        for i in range(6):  # 循环生成单条注册码
            randfir = randfir + random.choice(number)  # 产生数字随机因子　
        randfir = randfir + "\n"  # 在单条注册码后面添加转义换行字符“\n”，使验证码单条列显示　
        randstr.append(randfir)  # 将单条注册码添加到保存批量验证码的变量randstr　
    # 调用函数wfile()，实现生成的防伪码屏幕输出和文件输出
    wfile(randstr, "scode" + str(schoice) + ".txt", "", "已生成6位防伪码共计：", "codepath")


def scode2(schoice):
    ordstart = inputbox("\033[1;32m 请输入系列产品的数字起始号（3位）:\033[0m", 3, 3)
    # 如果输入非法，则要求重新输入
    while int(ordstart) == 0:
        ordstart = inputbox("\033[1;32m 请输入系列产品的数字起始号（3位）:\033[0m", 3, 3)
    ordcount = inputbox("\033[1;32m 请输入系列产品的数量:\033[0m", 1, 0)
    # 如果输入的产品序列号小于1或者大于9999，则要求重新输入
    while int(ordcount)<1 or int(ordcount)>9999:
        ordcount = inputbox("\033[1;32m 请输入系列产品的数量:\033[0m", 1, 0)
    incount = inputbox("\033[1;32m 请输入要生成的每个系列产品的防伪码数量:\033[0m", 1, 0)
    while int(incount) == 0:
        incount = inputbox("\033[1;32m 请输入要生成的每个系列产品的防伪码数量:\033[0m", 1, 0)
    randstr.clear()   # 清空保存批量防伪码信息的变量
    for m in range(int(ordcount)):   # 分类产品编号
        for j in range(int(incount)):  # 产品防伪码编号
            randfir =""
            for i in range(6):  # 生成一个不包含类别的产品防伪码
                randfir = randfir + random.choice(number)  # 每次生成一个随机因子
            # 将生产的单条防伪码添加到防伪码列表
            randstr.append(str(int(ordstart) + m) + randfir + "\n")
    # 调用wfile函数，实现生产的防伪码在屏幕输出和文件
    wfile(randstr, "scode" + str(schoice) + ".txt", "", "已经生成9位系列产品防伪码共计：", "codepath")


# 生成25位混合产品序列号的函数，参数schoice设置输出的文件名称
def scode3(schoice):
    # 输入要生成的防伪码数量
    incount = inputbox("\033[1;32m 请输入要生成的25位混合产品序列号数量：\033[0m", 1, 0)
    while int(incount) == 0: # 如果输入非法，则重新输入
        incount = inputbox("\033[1;32m 请输入要生成的25位混合产品序列号数量：\033[0m", 1, 0)
    randstr.clear()   # 清空保存批量防伪码信息的变量
    for j in range(int(incount)):   # 按输入的数量生成防伪码
        strone = ""   # 保存生成的单条防伪码，不带横向，循环时清空
        for i in range(25):
            # 每次随机生成一个因子，也就是每次产生单条防伪码的一位
            strone = strone +random.choice(letter)
        # 将生产的防伪码每隔5位添加横向
        strtwo = strone[:5] + "-" + strone[5:10] + "-" + strone[10:15] + "-" + strone[15:20] + "-" + strone[20:25] + "\n"
        randstr.append(strtwo)   # 添加防伪码到防伪码列表
    #  调用函数wfile(),实现生产的防伪码在屏幕输出和文件输出
    wfile(randstr, "scode" + str(schoice) + ".txt", "", "已生成25位混合防伪序列码共计：", "codepath")


# 生成含数据分析功能防伪码函数，参数schoice设置输出的文件格式
def scode4(schoice):
    intype = inputbox("\033[1;32m  请输入数据分析编号（3位字母） :\033[0m", 2, 3)
    # 验证输入是否是三个字母，所以要判断是否是字母和输入长度是否为3
    while not str.isalpha(intype) or len(intype) != 3:
        intype = inputbox("\033[1;32m  请输入数据分析编号（3位字母） :\033[0m", 2, 3)
    incount = inputbox("\033[1;32m  输入要生成的带数据分析功能的防伪码数量：\033[0m", 1, 0)
    # 验证输入是否大于零的整数，方法是判断输入转换为整数值时是否大于0
    while int(incount) == 0:  # 如果转换为整数时，需要重新输入
        incount = inputbox("\033[1;32m  输入要生成的带数据分析功能的防伪码数量：\033[0m", 1, 0)
    ffcode(incount, intype, "", schoice)  # 调用ffcode()函数生成防伪码


def scode5(schoice):
    default_dir = r"codeauto.mri"   # 设置默认打开的文件名
    # 打开文件选择对话框，指定打开的文件名称为“codeauto.aut”，扩展名为“.mri”，记事本可以打开和编辑
    file_path = tkinter.filedialog.askopenfilename(filetypes=[("Text file", "*.mri")], title=u"请选择智能批处理文件：", initialdir=(os.path.expanduser(default_dir)))
    codelist = openfile(file_path)  # 读取从文件选择对话框中选取的文件
    # 以换行符为分割符读取的信息内容转换为列表
    codelist = codelist.split("\n")
    print(codelist)
    for item in codelist:   # 读取的信息循环生产防伪码
        codea = item.split(",")[0]   # 信息用“，”分隔，逗号前面的信息存储防伪码标准信息
        codeb = item.split(",")[1]  # 信息用“，”分隔，逗号后面的信息存储防伪码标生产的数量
        ffcode(codeb, codea, "no", schoice)   # 调用ffcode函数批量生产同一标识信息的防伪码


def scode6(schoice):
    default_dir = r"D:\企业编码\code\codepath\abcscode5.txt"   # 设置默认打开的文件名称
    # 按默认的文件名称打开文件选择对话框，用于打开已经存在的防伪码文件
    file_path = tkinter.filedialog.askopenfilename(title=u"请选择生成的防伪码文件", initialdir=(os.path.expanduser(default_dir)))
    codelist = openfile(file_path)   # 读取从文件选择对话框中的文件
    # 以换行符为分界符将读取的信息内容转换为列表
    codelist = codelist.split("\n")
    codelist.remove("")  # 删除列表中的空行
    strset = codelist[0]  # 读取一行数据，一遍获取原验证码的字母标志信息
    # 用maketrans()方法创建删除数字的字符映射转换表
    remove_digits = strset.maketrans("", "", digits)
    # 根据字符映射转换表删除该条码中的数字，获取字母标志信息
    res_letter = strset.translate(remove_digits)
    nres_letter = list(res_letter)   # 把信息列表变量nres_letter存储
    strpro = nres_letter[0]          # 从列表中取得第一个字母，即区域分析码
    strtype = nres_letter[1]         # 从列表中取得第二个字母，即色彩分析码
    strclass = nres_letter[2]        # 从列表中取得第三个字母，即版次分析码
    # 去除信息中的括号和引号
    nres_letter = strpro.replace(''''', '').replace(''''', '') + strtype.replace(
        ''''', '').replace(''''', '') + strclass.replace(''''', '').replace(''''', '')
    card = set(codelist)   # 将原有的防伪码放到集合变量card中去
    # 利用tkinter的messagebox提示用户之前生产的防伪码数量
    tkinter.messagebox.showinfo("提示", "之前的防伪码共计：" +  str(len(card)))
    root.withdraw()   # 关闭提示窗口
    incount = inputbox("请输入补充防伪码的数量：", 1, 0)
    # 最大值按输入生成数量的2倍生成新防伪码
    # 防止新生产防伪码与原有防伪码重复造成新生产的防伪码数量不够
    for j in range(int(incount)*2):
        randfir = random.sample(number, 3)  # 随机生成3位不重复的数字
        randsec = sorted(randfir)           # 对产生的数字进行排序
        addcount = len(card)                # 记录集合中防伪码的总数量
        strone = ""                         # 清空集合中存储防伪码的变量
        for i in range(9):                  # 生成9位的数字防伪码
            strone = strone + random.choice(number)
        # 将三个数字按randsec变量中存储的位置值添加到数字防伪码中，并放到sim变量中
        sim = str(strone[0:int(randsec[0])]) + strpro + str(
            strone[int(randsec[0]):int(randsec[1])]) + strtype+ str(
            strone[int(randsec[1]):int(randsec[2])]) + strclass + str(strone[int(randsec[2]):9]) + "\n"
        card.add(sim)   # 添加新生产的防伪码到集合
        # 如果添加到集合，证明生成的防伪码与原有的防伪码没有产生重复
        if len(card) > addcount:
            randstr.append(sim)            # 添加新生产的防伪码到新的防伪码列表
            addcount = len(card)           # 记录新生产防伪码集合的防伪码数量
        if len(randstr) >= int(incount):   # 如果新生产的防伪码数量达到输入的防伪码数量
            print(len(randstr))            # 输出已经生成防伪码的数量
            break                          # 退出循环
    # 调用wfile函数，将生产的防伪码屏幕输出和文件输出
    wfile(randstr, nres_letter + "ncode" + str(choice) + ".txt", nres_letter, "生成后补防伪码数量为：", "codeadd")


# EAN-13条形码批量生成
def scode7(schoice):
    mainid = inputbox("\033[1;32m  请输入EAN13的国家代码（3位）：\033[0m", 1, 0)
    while int(mainid) <1 or len(mainid) != 3:     # 验证输入是否为3位数字
        mainid = inputbox("\033[1;32m  请输入EAN13的国家代码（3位）：\033[0m", 1, 0)

    compid = inputbox("\033[1;32m  请输入企业代码（4位）：\033[0m", 1, 0)
    while int(compid ) < 1 or len(compid ) != 4:  # 验证输入是否为4位数字
        compid = inputbox("\033[1;32m  请输入企业代码（4位）：\033[0m", 1, 0)

    incount = inputbox("\033[1;32m  请输入要生成的条形码数量：\033[0m", 1, 0)
    while int(incount) == 0:
        incount = inputbox("\033[1;32m  请输入要生成的条形码数量：\033[0m", 1, 0)

    mkdir("barcode")      # 判断保存条形码的文件夹是否存在，不存在，则创建该文件夹
    for j in range(int(incount)):     # 批量生产条形码
        strone = ""             # 清空存储单条条形码的变量
        for i in range(5):      # 生成条形码的五位企业商品代码（数字）
            strone = strone + str(random.choice(number))
        barcode = mainid + compid + strone    # 将国家代码、企业代码 、企业商品代码进行组合
        # 计算条形码的效验码
        evensum = int(barcode[1]) + int(barcode[3])+ int(barcode[5]) + int(barcode[7]) + int(barcode[9]) + int(barcode[11])
        oddsum = int(barcode[0]) + int(barcode[2]) + int(barcode[4]) + int(barcode[6]) + int(barcode[8]) + int(barcode[10])
        checkbit = (evensum*3 + oddsum) % 10
        checkbit = int((10-checkbit)%10)
        barcode = barcode + str(checkbit)             # 组合成完整的EAN13条形码
        encode = EAN13Encoder(barcode)                # 调用EAN13Encoder函数生成条形码
        encode.save("barcode\\" + barcode + ".png")   # 保存条形码信息图片到文件夹


def scode8(schoice):
    # 输入要生成的二维码数量
    incount = inputbox("\033[1;32m   请输入要生成的12位数字二维码数量：\033[0m", 1, 0)
    while int(incount) == 0:
        incount = inputbox("\033[1;32m   请输入要生成的12位数字二维码数量：\033[0m", 1, 0)
    mkdir("qrcode")
    for j in range(int(incount)):
        strone = ''    # 清空存储单条二维码的变量
        for i in range(12):   # 生成单条二维码数字
            strone = strone + str(random.choice(number))
        encoder = qrcode.make(strone)   # 生成二维码
        encoder.save("qrcode\\" + strone + ".png")   # 保存二维码图片到文件
        print(strone)


def scode9(schoice):
    default_dir = r"lottery.ini"    # 默认打开文件项目路径下的“lottery.ini”
    # 选择包含用户抽奖信息票号的文件，扩展名为“.ini”
    file_path = tkinter.filedialog.askopenfilename(filetypes=[("Ini file", "*.ini")],
                title=u"请选择包含抽奖号码的文件：", initialdir=(os.path.expanduser(default_dir)))
    codelist = openfile(file_path)   # 调用openfile()函数读取刚打开的抽奖文件
    codelist = codelist.split("\n")  # 通过换行符吧抽签信息分割为抽奖列表
    # 要求用户输入中（抽）奖数量
    incount = inputbox("\033[1;32m   请输入要生成的抽签数量：\033[0m", 1, 0)
    # 非法输入，要求重新输入
    while int(incount) == 0 or len(codelist) < int(incount):
        incount = inputbox("\033[1;32m   请输入要生成的抽签数量：\033[0m", 1, 0)
    strone = random.sample(codelist, int(incount))  # 根据输入的中奖数进行抽奖
    for i in range(int(incount)):
        # 将抽奖列表中的中括号去掉
        wdata = str(strone[i].replace('[', '')).replace(']', '')
        # 将抽奖列表中的引号去掉
        wdata = wdata.replace(''''', '').replace(''''', '')
        # 输出中奖信息
        print(wdata)


def inputbox(showstr, showorder, length):
    instr = input(showstr)   # showstr为提示用户输入文字
    if len(instr) != 0:
        # 3种验证方式，1(数字，不限位数)，2(字母)3(数字且有位数要求)
        if showorder == 1:   # 数字，不限位数,大于0的整数
           if str.isdigit(instr):  # 验证是否为数字
               if instr == 0:
                   print("\033[1;31;40m 非法输入，请重新输入！！！\033[0m")
                   return 0
               else:
                   return instr
           else:
               print("\033[1;31;40m 非法输入，请重新输入！！！\033[0m")
               return 0
        if showorder == 2:    # 验证方式2，要求字母格式且是指定字母
           if str.isalpha(instr):   # 判断输入是否为字母
               if len(instr) != length:    #  判断输入位数
                   print("\033[1;31;40m必须输入"+ str(length)+"个字母，请重新输入！！！\033[0m")
                   return 0
               else:
                   return instr
           else:
               print("\033[1;31;40m 非法输入，请重新输入！！！\033[0m")
               return 0
        if showorder ==3:   # 要求数字格式且对输入位数有要求
           if str.isdigit(instr):   # 判断输入是否为数字
               if len(instr) != length:    #  判断输入位数
                   print("\033[1;31;40m必须输入"+ str(length)+"个数字，请重新输入！！！\033[0m")
                   return 0
               else:
                   return instr
           else:
               print("\033[1;31;40m 非法输入，请重新输入！！！\033[0m")
               return 0
    else:
        print("\033[1;31;40m 非法输入，请重新输入！！！\033[0m")
        return 0


def openfile(filename):      # 读取文件内容函数
    f = open(filename)
    fllist = f.read()
    f.close()
    return fllist


def mkdir(path):     # 创建文件夹函数
    isexists = os.path.exists(path)
    if not isexists:
        os.mkdir(path)       # 文件件不存在时创建文件夹



# 实现屏幕输出和文件输出编码信息函数，# sstr参数为输出防伪码数据, sfile为输出的文件名称
# typeis设置输出完成后是否通过信息框提示, smsg为信息提示框的提示文字，datapath 保存防伪码的文件夹
def wfile(sstr, sfile, typeis, smsg,datapath):
    mkdir(datapath)  # 调用该函数创建文件夹
    datafile = datapath + "\\" + sfile  # 设置保存防伪码的文件（包含路径）
    file = open(datafile, 'w')  # 打开保存防伪码的文件，如果文件不存在，则创建该文件
    wrlist = sstr  # 将防伪码信息赋值给wrlist
    pdata = ""  # 清空变量pdata，pdata存储屏幕输出的防伪码信息
    wdata = ""  # 清空变量 wdata ， wdata 存储保存到文本文件的防伪码信息
    for i in range(len(wrlist)):  # 按条循环读取防伪码数据
        wdata = str(wrlist[i].replace('[', '')).replace(']', '')  # 去掉字符的中括号
        wdata = wdata.replace(''''','').replace(''''', '')  # 去掉字符的引号
        file.write(str(wdata))  # 写入保存防伪码的文件
        pdata = pdata + wdata  # 将单条防伪码存储到pdata 变量
    file.close()  # 关闭文件
    print("\033[1;31m" + pdata + "\033[0m")  # 屏幕输出生成的防伪码信息
    if typeis != "no":  # 是否显示“输出完成”的信息提示框。如果typeis的值为“no”,不现显示
        # 显示“输出完成”的信息提示框。显示信息包含方位信息码的保存路径
        tkinter.messagebox.showinfo("提示", smsg + str(len(randstr)) + "\n 防伪码文件存放位置：" + datafile)
        root.withdraw()  # 关闭辅助窗口


# 生成含有数据分析功能的防伪编码函数，参数scount为要生成的防伪码数量，typestr为数据分析字符
# 参数ismessage在输出完成时是否显示提示信息，为“no” 时不显示；参数schoice为设置输出的文件名称
def ffcode(scount, typestr, ismessage, schoice):
    randstr.clear()    # 清空保存批量防伪码信息的变量
    # 按数量生成含有数据分析功能的防伪编码
    for j in range(int(scount)):
        strpro = typestr[0].upper()  # 取得3个字母的第1个字母并转为大写，区域分析码
        strtype = typestr[1].upper()  # 取得3个字母的第2个字母并转为大写，颜色分析码
        strclass = typestr[2].upper()  # 取得3个字母的第3个字母并转为大写，版本分析码
        randfir = random.sample(number, 3)   # 随机抽取防伪码中的3个位置，不分先后
        randsec = sorted(randfir)    # 对抽取的位置进行排序并赋值给randsec变量
        letterone = ""  # 清空存储单条防伪码的变量
        for i in range(9):   # 生成9位数字防伪码
            letterone = letterone + random.choice(number)
        # 将三个字母按randsec变量中存储的位置值添加到数字防伪码中，并保存到sim变量中
        sim = str(letterone[0:int(randsec[0])]) + strpro + str(
            letterone[int(randsec[0]):int(randsec[1])]) + strtype + str(
            letterone[int(randsec[1]):int(randsec[2])]) + strclass + str(
            letterone[int(randsec[2]):9]) + "\n"
        randstr.append(sim)   # 将组合生产的新防伪码添加到randstr变量中
        # 调用wfile函数，实现生成的防伪码屏幕输出和文件输出
        wfile(randstr, typestr + "scode" + str(schoice) + ".txt", ismessage, "生成含义数据分析功能的防伪码共计：", "codepath")


# 通过循环控制用户对程序功能的选择
while i < 9:
    # 调入程序主界面菜单
    mainmenu()
    # 键盘输入需要操作的选项
    choice = input("\033[1;32m     请输入您要操作的菜单选项:\33[0m")
    if len(choice) != 0:  # 输入如果不为空
        choice = input_validation(choice)  # 验证输入是否为数字
        if choice == "1":
           scode1( str(choice))      # 如果输入大于零的整数，调用scode1()函数生成注册码
        # 选择菜单2,调用scode2()函数生成9位系列产品数字防伪编码
        if choice == "2":
            scode2(choice)
        # 选择菜单3,调用scode3()函数生成25位混合产品序列号
        if choice == "3":
            scode3(choice)
        # 选择菜单4,调用scode4()函数生成含数据分析功能的防伪编码
        if choice == "4":
            scode4(choice)
        # 选择菜单5,调用scode5()函数智能批量生成带数据分析功能的防伪码
        if choice == "5":
            scode5(choice)
        # 选择菜单６,调用scode6()函数后续补加生成防伪码
        if choice == "6":
            scode6(choice)
        # 选择菜单7,调用scode7()函数批量生成条形码
        if choice == "7":
          scode7( choice)
        # 选择菜单8,调用scode8()函数批量生成二维码
        if choice == "8":
            scode8(choice)
        # 选择菜单9,调用scode9()函数生成企业粉丝抽奖程序
        if choice == "9":
            scode9(choice)
        # 选择菜单0,退出系统
        if choice == "0":
            i = 0
            print("正在退出系统!!")
            break
    else:
        print("\033[1;31;40m    输入非法，请重新输入！！\033[0m")
        time.sleep(2)

