from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from multiprocessing import Pool
import os,json,sys
import requests

'''拿到单个播放链接'''
def get_video_url(base_url):
    opts = FirefoxOptions()
    opts.add_argument("--headless")
    browser = webdriver.Firefox(firefox_options=opts)
    browser.get('http://www.baidu.com')
    print(browser.get_cookies())
    video_url_dict = {}


    return video_url_dict

'''获取到真实播放链接'''
def get_video_down(video_url):
    video_play_url = 1

    return video_play_url

'''下载文件'''
def down_video(video_play_url):
    reque_obj = requests.get(video_play_url[1])
    with open('/usr/local/download/%s'%video_play_url[0], 'wb') as f:
        f.write(reque_obj.content)

'''主函数'''
def main():
    base_url = sys.argv[1]
    video_url_dict = get_video_url(base_url)
    pool = Pool()
    for video_url in video_url_dict:
        pool.apply_async(func=get_video_down, args=(video_url, video_url_dict[video_url]),callback=down_video)
    pool.close()
    pool.join()


if __name__  == "__main__":
    main()