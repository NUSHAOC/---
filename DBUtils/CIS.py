
import requests
import xlwt

site_name = {''}
book = xlwt.Workbook(encoding='utf-8')
sheet = book.add_sheet('站点经纬度信息', cell_overwrite_ok=True)

col_name = {'站点名字','经度','维度','线路'}
for i in range(4):
    sheet.write(0,1,col_name[i])

for i in range(len(site_name)):
    url = 'https://webapi.amap.com/search?query={}&region=昆明&output=json' \
          'key=1a55cd30c5124e47a4a7bbb0c9e87ee7' .format(site_name)

    site_text = requests.get(url).json()
    name = site_text['results'][0]['name']
    log = site_text['results'][0]['log']
    lat = site_text['results'][0]['lat']
    NUM = site_text['results'][0]['NUM']
    sheet.write(i+1,0,name)
    sheet.write(i + 1, 1, log)
    sheet.write(i + 1, 2, lat)
    sheet.write(i + 1, 3, NUM)

    print('%s爬取结束=========' % name)

book.save('站点.xlsx')



