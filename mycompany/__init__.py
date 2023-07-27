from urllib.parse import quote
import requests  # 发送网络请求的模块
import prettytable as pt  # 格式化输出表格 as pt

# 1. 向 目标网站 发送网络请求
# 请求方式: get post delete...
# 加一些伪装 伪装就已经准备好了
# 快捷替换小技巧
# 1. 选中要替换的内容
# 2. Ctrl + r
# 3. 在第一个框框里面输入(.*?): (.*) 第二个框里面输入 '$1': '$2'
# 4. 点击 Replace All替换


searchKey = input('请输入你要下载的歌曲或歌手名:')
searchKey = quote(searchKey)
headers = {
    'Cookie': '_ga=GA1.2.1829952759.1632831324; BusinessId={"std_plat":404,"std_dev":"b24a2c89-d830-47f5-ee62-3eaa2cbcd9e8","std_imei":"b24a2c89-d830-47f5-ee62-3eaa2cbcd9e8"}; _gid=GA1.2.1213855107.1635853703; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1635230576,1635230784,1635345246,1635853703; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1635853703; kw_token=SK7FZCBITOJ',
    'csrf': 'SK7FZCBITOJ',
    'Host': 'www.kuwo.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
}
# 字符串的格式化
url = f'http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={searchKey}&pn=1&rn=30'
response = requests.get(url=url, headers=headers)
# <Response [403]>: 爬虫程序 被抓到了
# 200: 发送请求成功了 没被抓到
# 2. 获取数据
# 通过 .text拿到的是字符串
# 通过 .json()拿到的 python语言当中的字典
json_data = response.json()
# 3. 提取数据 (歌曲名称 歌手名称 专辑名称)
#       字典取值
# 列表
data_list = json_data['data']['list']
# 新建了一个表格
tb = pt.PrettyTable()
# 写一行表头
tb.field_names = ['序号', '歌名', '歌手', '专辑']
count = 0   # 定义了一个序号
info_list = []
for data in data_list:
    # 字典 alt + 鼠标左键
    rid = data['rid']  # 歌曲id
    name = data['name']  # 歌曲名称
    artist = data['artist']  # 歌手名称
    album = data['album']  # 专辑名称
    tb.add_row([count, name, artist, album])    # 表格数据写入
    info_list.append([rid, name, artist])      # 下载歌曲要用的信息
    count += 1
print(tb)

# 死循环
while True:
    input_index = eval(input("请输入与你要下载歌曲的序号(-1退出):"))
    if input_index == -1:
        break
    download_info = info_list[input_index]
    # 以前 酷我音乐的链接, 把以前的接口里面要传入的参数 给添加到这个接口里面了
    # br=320kmp3控制音乐音质的一个参数 高品质音乐
    url_1 = f'http://www.kuwo.cn/api/v1/www/music/playUrl?mid={download_info[0]}&type=convert_url3&br=320kmp3'
    # 发送网络请求
    response_1 = requests.get(url_1, headers=headers).json()
    # 解析数据
    music_url = response_1['data']['url']
    # 发送请求
    music_data = requests.get(music_url).content
    with open(f'download/{download_info[1]}-{download_info[2]}.mp3', mode='wb') as f:
        f.write(music_data)
    print(f'{download_info[1]}, 下载完成!')
