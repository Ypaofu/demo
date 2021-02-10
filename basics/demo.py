have_gift = False

def send():
    print("发礼物了")
    global have_gift
    have_gift = True

def show():
    if have_gift == True:
        print("收到礼物了")
    else:
        print("没有礼物")

# if __name__ == '__main__':
#     send()
#     show()
