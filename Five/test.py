
import execjs

def get_m_value():
    with open(r'D:\Code\JSReverse\Five\newTest.js', encoding='utf-8', mode='r') as f:
        JsData = f.read()
    m = execjs.compile(JsData).call("get_data_value")
    print(m)
    print("1617431182868")

if __name__ == '__main__':
    get_m_value()