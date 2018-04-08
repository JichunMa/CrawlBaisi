import crawlInfo
import saveTools
import downloadPicTools
import networkTools

if __name__ == '__main__':
    data = ''
    # with open('budejie.html', 'r')as f:
    #     data = f.rea
    baisi_url = 'http://www.budejie.com/pic/'
    data = networkTools.request_via_network(baisi_url)
    model_list = crawlInfo.crawl(data)
    for model in model_list:
        model.display()
        # 下载图片
        downloadPicTools.download('./imgs/', model.img_url)
    # 保存到本地
    saveTools.output('baisi.xlsx', model_list)
