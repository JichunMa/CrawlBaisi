from lxml import etree

import BaiSiModel


# 使用 xpath 获取用户名，发布时间，内容，图片地址字段信息

def crawl(data):
    if data == '':
        return []
    model_list = []
    source = etree.HTML(data)
    li_list = source.xpath('//div[@class="j-r-list"]/ul/li')
    for li in li_list:
        user_name_list = li.xpath('div[@class="j-list-user"]/div[@class="u-txt"]/a/text()')
        user_name = ''
        if len(user_name_list) > 0:
            user_name = user_name_list[0]

        create_time_list = li.xpath('div[@class="j-list-user"]/div[@class="u-txt"]/span/text()')
        create_time = ''
        if len(create_time_list) > 0:
            create_time = create_time_list[0]
        content_list = li.xpath('div[@class="j-r-list-c"]/div[@class="j-r-list-c-desc"]/a/text()')
        content = ''
        if len(content_list) > 0:
            content = content_list[0]
            content = content.replace('\u200b', '')
            content = content.replace('\xa0', '')
        img_url_list = li.xpath('div[@class="j-r-list-c"]/div[@class="j-r-list-c-img"]/a/img/@data-original')
        img_url = ''
        if len(img_url_list) > 0:
            img_url = img_url_list[0]
        model = BaiSiModel.BaiSi(user_name, create_time, content, img_url)
        model_list.append(model)
    return model_list
