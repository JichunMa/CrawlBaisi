import xlwt


# 保存结果到xlsx
def output(filename, list_data):
    if len(list_data) == 0:
        return
    data_0 = list_data[0]
    book = xlwt.Workbook()
    sh = book.add_sheet('sheet1')
    data_dict = data_0.__dict__
    data_key_list = list(data_dict.keys())
    # 写标题
    index = 0
    for key in data_key_list:
        sh.write(0, index, key)
        index = index + 1
    # 写内容
    column_index = 1
    for item in list_data:
        for i in range(len(data_key_list)):
            data_dict = item.__dict__
            sh.write(column_index, i, data_dict[data_key_list[i]])
        column_index = column_index + 1
    book.save(filename)
