import csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from lxml import etree  #解析html

# 定义url
urls = ['https://www.zhipin.com/', 'https://www.zhipin.com/web/geek/job?query={}&page={}']

proxies = '116.242.31.64:80'

prefix = 'https://www.zhipin.com'

# 浏览器设置
options = webdriver.FirefoxOptions()   # 初始化

options.add_argument('-headless')  # 无界面
options.add_argument('--disable-gpu')  # 禁用gpu
options.add_argument('excludeSwitches')  # 规避检测风险

service = Service('./geckodriver.exe')   # 浏览器的驱动

# 模拟人类进行浏览器操作

web = webdriver.Firefox(service=service, options=options)  # 实例化一个浏览器对象
web.get(urls[0])  # 让浏览器发起一个指定url请求

sleep(5)

search_tag = web.find_element(By.CSS_SELECTOR, value='.ipt-search')  # 定位搜索框的值
search_tag.send_keys("北京") # 输入搜索内容
btn = web.find_element(By.CSS_SELECTOR, value='.btn-search')  # 定位搜索按钮的值
btn.click()  # 点击搜索按钮


# 自定义
# city_tag = web.find_element(By.CSS_SELECTOR,'')
# city_tag.click()

sleep(15)

f = open("boss直聘.csv", "w", encoding="utf-8_sig", newline="")
csv.writer(f).writerow(["职位", "位置", "薪资", "联系人", "经验要求", "公司名", "公司类型",  "福利", "详情"])


def parse():
    jobList = []  # 存放获取到的信息

    page_text = web.page_source  # 提取信息

    tree = etree.HTML(page_text) # 将从互联网上获取的数据加载到tree对象中

    job = tree.xpath('//div[@class="search-job-result"]/ul/li')

    for i in job:

        job_name = i.xpath(".//span[@class='job-name']/text()")[0] # 职位

        jobArea = i.xpath(".//span[@class='job-area']/text()")[0] # 位置

        linkman_list = i.xpath(".//div[@class='info-public']//text()") # 联系人
        linkman = "·".join(linkman_list)

        detail_url = prefix + i.xpath(".//h3[@class='company-name']/a/@href")[0] # 详情页url

        salary = i.xpath(".//span[@class='salary']/text()")[0] # 薪资

        job_label_list = i.xpath(".//ul[@class='tag-list']//text()")  # 经验要求
        job_labels = " ".join(job_label_list)

        company = i.xpath(".//h3[@class='company-name']/a/text()")[0]  # 公司名

        companyScale_list = i.xpath(".//div[@class='company-info']/ul//text()")  # 公司类型
        companyScale = " ".join(companyScale_list)

        try:
            job_desc = i.xpath(".//div[@class='info-desc']/text()")[0]  #公司福利
        except:
            job_desc = " "

        # 将数据写入csv
        csv.writer(f).writerow(
            [job_name, jobArea, salary, linkman, job_labels, company, companyScale,  job_desc, detail_url])

        jobList.append({
            "jobName": job_name,
            "jobArea": jobArea,
            "salary": salary,
            "linkman": linkman,
            "jobLabels": job_labels,
            "company": company,
            "companyScale": companyScale,
            "job_desc": job_desc,
            "detailUrl": detail_url,
        })

    return {"jobList": jobList}


if __name__ == '__main__':

    print(f"正在开始爬取")
    print(f"第1页")
    jobList = parse() # 访问第一页
    query = "北京"

    # 继续访问
    for i in range(2, 11):
        print(f"第{i}页")
        url = urls[1].format(query, i)  # 拼接url
        web.get(url)  # 访问
        sleep(15)
        jobList = parse()

    web.quit()  # 关闭浏览器


