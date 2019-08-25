try:
    from selenium import webdriver
except ImportError as e:
    import os

    os.system('pip install selenium')
    from selenium import webdriver
import time


def run():
    # web = webdriver.Chrome()  # 实例化一个浏览器
    web = webdriver.PhantomJS()  # 实例化一个浏览器
    web.set_window_size(1920, 1080)
    # web.maximize_window()
    web.get("http://www.baidu.com")  # 发送请求
    # web.switch_to.frame("id")
    web.find_element_by_id("kw").send_keys("python")
    web.find_element_by_id('su').click()
    # time.sleep(1)
    web.save_screenshot("./img.png")
    # print(web.page_source)  # 网页源码,element,可以用xPath解析
    # web.quit()


if __name__ == '__main__':
    run()
