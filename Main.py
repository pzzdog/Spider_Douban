#!/user/bin/env python3
#-*- coding:utf-8 -*-

import re
import urllib.request


class Douban(object):
    """Class about douban"""

    def __init__(self):
        self.page_num=1
        self.cur_url='https://movie.douban.com/top250?start={page}&filter='
        self.datas=[]
        self.top_num=1
        print('Ready?GO!')

    def get_page(self,cur_page):
        url=self.cur_url
        try:
            my_page=urllib.request.urlopen(
                url.format(
                    page=(cur_page-1)*25
                )
            ).read().decode('utf-8')
            return my_page
        except urllib.request.URLError as e:
            if hasattr(e,"code"):
                print('Error code:%s'% e.code)
            elif hasattr(e,"reason"):
                print("Reason: %s"%e.code)

    def find_title(self,my_page,Lan):
        temp_data=[]
        move_items=re.findall(r'<span.*?class="title">(.*?)</span>',my_page)
        for index,item in enumerate(move_items):
            if item.find("&nbsp;/&nbsp;")==-Lan:
                temp_data.append("Top"+str(self.top_num)+" "+item.replace('&nbsp;/&nbsp;',''))
                self.top_num+=1
        self.datas.extend(temp_data)

    def start_spider(self,Lan):
        while self.page_num<=10:
            my_page=self.get_page(self.page_num)
            self.find_title(my_page,Lan)
            self.page_num+=1




def main():
    Lan='judgement'
    print("##########################\n"
          "豆瓣TOP250\n"
          "##########################")
    Spider=Douban()
    while Lan!=0 and Lan!=1:
        Lan=int(input("Chinese?(1:YES 0:NO)"))
        print('--------------------------')

    Spider.start_spider(Lan)
    for item in Spider.datas:
        print(item)
    print("#########################\n"
          "------------END----------\n"
          "###########################")

if __name__ == '__main__':
    main()
