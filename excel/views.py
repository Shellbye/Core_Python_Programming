# -*- coding:utf-8 -*-
__author__ = 'shellbye'
import xlrd
import xlsxwriter
# https://xlsxwriter.readthedocs.org/


def extract_info_from_excel(file_url):
    # 打开excel
    data = xlrd.open_workbook(file_url)
    table = data.sheet_by_index(0)
    for i in range(26):
        for j in range(2):
            print "i:" + str(i) + " j:" + str(j) + " =" + table.cell(j, i).value


def save_info_into_excel(file_url):
    # 获取数据数据
    workbook = xlsxwriter.Workbook(file_url)
    worksheet = workbook.add_worksheet()
    title = (u'序号', u'学号', u'性别')
    header_format = workbook.add_format({
        'bold': True,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': '#D7E4BC',
        'border': 1
    })
    worksheet.set_column('A:C', 16)  # set column from A to I width to 16
    worksheet.set_row(0, 20)  # set row height to 20 and some format
    worksheet.freeze_panes(1, 0)
    worksheet.write_row('A1', title, header_format)
    # row and column number start from 0
    # integer
    worksheet.write(1, 0, 1)
    # string
    worksheet.write(1, 1, "shellbye")
    # select
    worksheet.write(1, 2, "boy")
    worksheet.data_validation(
        1, 2, 1, 2,
        {
            'validate': 'list',
            'source': ["boy", "girl"]
        }
    )
    workbook.close()
    return True


if __name__ == "__main__":
    excel_file = "./stu_info.xls"
    new_excel_file = "new_stu_info.xlsx"
    # extract_info_from_excel(excel_file)
    save_info_into_excel(new_excel_file)