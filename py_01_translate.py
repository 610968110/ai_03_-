import requests
import json

from click._compat import raw_input


def main(input_word):
    if input_word is None or input_word == "":
        input_word = raw_input("请输入单词\n")
        if input_word is None or input_word == "":
            print("bye bye~")
            return
    print("查询中请稍后")
    data = {
        "query": input_word,
        "from": "zh",
        "to": "en",
        "token": "65de658061028973042e33bbd554dad5",
        "sign": "232427.485594"
    }
    headers = {
        "authority": "fanyi.baidu.com",
        "method": "POST",
        "path": "/basetrans",
        "scheme": "https",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "content-length": "96",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://fanyi.baidu.com",
        "x-requested-with": "XMLHttpRequest",
        "referer": "https://fanyi.baidu.com/translate?aldtype=16047&query=&" +
                   "keyfrom=baidu&smartresult=dict&lang=auto2zh",
        "user-agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T)"
                      + " AppleWebKit/537.36 (KHTML, like Gecko) "
                      + "Chrome/75.0.3770.100 Mobile Safari/537.36",
        "cookie": "BAIDUID=87F7E33E6EB32A79EF10304EB5DDF4B2:FG=1; BIDUPSID=87F7E33E6EB32A79EF10304EB5DDF4B2; PSTM=1560130903; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; MCITY=-131%3A; BDUSS=RwdU1sTjFCQkphNDZzaEcwNVRCQXVuUlA0S0tnUFhuUDZITTJWVGlaMHJrMkJkSUFBQUFBJCQAAAAAAAAAAAEAAADzoP0dbGJ4NjEwOTY4MTEwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACsGOV0rBjldT0; pgv_pvi=5414098944; cflag=13%3A3; locale=zh; from_lang_often=%5B%7B%22value%22%3A%22fra%22%2C%22text%22%3A%22%u6CD5%u8BED%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1564366396,1564711685,1565077365,1565153669; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1565153730; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1565153730; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1565153730; yjs_js_security_passport=7da2a3abe2b4f969106f9c10edaef0d17f115ff2_1565153737_js",
    }
    r = requests.post("https://fanyi.baidu.com/basetrans", data=data, headers=headers)
    # print(r)
    # print(r.content.decode())
    result = json.loads(r.content.decode())
    errno = result["errno"]
    if errno == 0:
        try:
            word = result["trans"][0]["dst"]
            print(word)
        except KeyError as e:
            print("KeyError %s" % e)
    else:
        print("err -> {}".format(errno))


if __name__ == "__main__":
    main("你好")
