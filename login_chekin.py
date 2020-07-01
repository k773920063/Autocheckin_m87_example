import requests, re

#填写邮箱和密码，其他不需要动
e_mail = '@qq.com'
password = '000000'

def m87_check_in(ID, passwd):
    login_url = "https://m87is.best/auth/login"
    url_checkin = 'https://m87is.best/user/checkin'
    #post_header={
    #    'accept': 'application/json, text/javascript, */*; q=0.01',
    #    'accept-encoding': 'gzip, deflate, br',
    #    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    #    'content-length': '57',
    #    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    #    'origin': 'https://m87is.best',
    #    'referer': 'https://m87is.best/auth/login',
    #    'sec-ch-ua': '"\\Not\"A;Brand";v="99", "Chromium";v="84", "Microsoft Edge";v="84"',
    #    'sec-ch-ua-mobile': '?0',
    #    'sec-fetch-dest': 'empty',
    #    'sec-fetch-mode': 'cors',
    #    'sec-fetch-site': 'same-origin',
    #    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.68 Safari/537.36 Edg/84.0.522.28',
    #    'x-requested-with': 'XMLHttpRequest',
    #}
    post_data = {
        'email': ID,
        'passwd': passwd,
        'code': '',
    }
    session = requests.Session()

    cache = session.post(login_url,data=post_data)
    str = cache.text.encode('utf-8').decode('unicode-escape')
    str = re.sub("[A-Za-z0-9\!\%\[\]\,\。\{\}\"\:]", "", str)
    print(str)
    if str != '登录成功':
        print("脚本已结束,请重试")
        return
    cookie = session.cookies
    cache = session.post(url_checkin, cookies=cookie)
    str = cache.text.encode('utf-8').decode('unicode-escape')
    str = re.findall("尊贵.*?流量", str)
    if str:
        print(str[0])
    else:
        print("已签到")

if __name__ == "__main__":
    m87_check_in(e_mail, password)
