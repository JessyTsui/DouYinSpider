import xlrd

def read_excel_data(path):
    filename = path
    data = xlrd.open_workbook(filename)
    table = data.sheet_by_name('Sheet1')
    row_num = table.nrows  # 行数
    # col_num = table.ncols  # 列数
    datas = []
    tab = table.row_values(0)
    for i in range(1, row_num):
        xx = table.row_values(i)
        row_dict = dict(zip(tab, xx))
        datas.append(row_dict)
    return datas


