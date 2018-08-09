from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from multiprocessing import Pool
import os,json,sys
import requests,time

base_url = "https://beeg.com/people/UmaJolie"
# base_url = "https://beeg.com/"

'''拿到单个播放链接'''
def get_video_url(base_url):
    # opts = FirefoxOptions()
    # opts.add_argument("--headless")
    # browser = webdriver.Firefox(firefox_options=opts)
    browser = webdriver.Chrome()
    browser.get(base_url)
    time.sleep(3)
    class_div = browser.find_elements_by_class_name("thumb-unit")
    video_url_list = []
    for div in class_div:
        href = div.find_element_by_tag_name("a").get_attribute('href')
        video_url_list.append(href)
    return video_url_list

'''获取到真实播放链接'''
def get_video_down(video_url_list):
    browser = webdriver.Chrome()
    for video_url in video_url_list:
        browser.get(video_url)
        time.sleep(2)
        class_div = browser.find_element_by_class_name("video-wrapper")
        video_play_url = class_div.find_element_by_class_name("video").get_attribute("src")
        print(video_play_url)
    return video_play_url

'''下载文件'''
def down_video(video_play_url):
    reque_obj = requests.get(video_play_url)
    name = video_play_url.split("/")[-1]
    print(name)
    with open('/usr/local/download/%s'%name, 'wb') as f:
        f.write(reque_obj.content)

'''主函数'''
def main():
    video_url_list = get_video_url(base_url)
    pool = Pool(4)
    for video_url in video_url_list:
        pool.apply_async(func=get_video_down, args=(video_url,),callback=down_video)
    pool.close()
    pool.join()


if __name__  == "__main__":
    # main()
    # get_video_url(base_url)
    down_video("https://video.beeg.com/data=pc_US_144.202.127.156_1533304847_xSbFhPgg/key=pAjkc7ifl6Qcq+8NKdzSVg%2Cend=1533139881/480p/2409387.mp4")