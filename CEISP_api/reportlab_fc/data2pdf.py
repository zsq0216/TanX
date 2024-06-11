from reportlab.platypus import SimpleDocTemplate, Paragraph , PageBreak,Table, Image, BaseDocTemplate
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import Drawing
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.graphics.charts.barcharts import VerticalBarChart  # 图表类
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.charts.legends import Legend  # 图例类
from reportlab.graphics.shapes import Circle
from reportlab.graphics.charts.textlabels import Label
import calendar
import random
import os
import json

#唯一核心函数
def data2pdf(data):
    #data处理
    monthstr = str(data['show_data']['year'])+'年'+str(data['show_data']['month'])+'月'
    lastday = calendar.monthrange(data['show_data']['year'],data['show_data']['month'])[1]
    name_ = data['Enterprise_Name']
    data_ = data['show_data']
    historydata = data['history_data']
    historynum = data['history_num']
    
    #页面基础设置
    kai = 'simkai'
    sun = 'simsun'
    hei = 'simhei'
    ddjbt = 'ddjbt'
    pdfmetrics.registerFont(TTFont(kai,'simkai.ttf'))
    pdfmetrics.registerFont(TTFont(sun,'simsun.ttc'))
    pdfmetrics.registerFont(TTFont(hei,'simhei.ttf'))
    pdfmetrics.registerFont(TTFont(ddjbt,'ddjbt.ttf'))
    PAGE_HEIGHT = A4[1]
    PAGE_WIDTH = A4[0]
    def myFirstPage(canvas, doc):
        canvas.saveState()
        canvas.drawImage("./reportlab_fc/ytz.png", 0, 0, 52* cm, 40 * cm)
        canvas.setFillColor(colors.black)
        # 绘制居中标题文本
        left_ = 60
        up_ = 120
        canvas.setFont(ddjbt, 50)
        canvas.drawString(left_, PAGE_HEIGHT - up_, name_[:-6])
        canvas.setFont(ddjbt, 70)
        canvas.drawString(left_, PAGE_HEIGHT - up_ - 80, "碳排放")
        canvas.drawString(left_, PAGE_HEIGHT - up_ - 160, "核算报告")
        canvas.setFont(ddjbt, 50)
        canvas.drawString(left_, PAGE_HEIGHT - up_ - 230, monthstr)
        canvas.drawImage("./reportlab_fc/logo_n.png", 480, 20, 3* cm, 2.015 * cm,mask='auto')
        canvas.restoreState()

    def myLaterPage(canvas, doc):
        canvas.saveState()
        if doc.page == 5:
            canvas.drawImage("./reportlab_fc/end.png", 0, 0, PAGE_WIDTH, PAGE_HEIGHT)
            canvas.setFont(ddjbt, 15)
            canvas.drawString(40, PAGE_HEIGHT - 70, '免责及报告说明部分')
            canvas.drawImage("./reportlab_fc/logo_w.png", 450, PAGE_HEIGHT - 70 , 2.5* cm, 0.9766 * cm,mask='auto')
            canvas.setFont(sun, 15)
            hloc = 500
            r = 500
            canvas.drawRightString(r, hloc, "碳析（TanX）平台")
            canvas.drawImage("./reportlab_fc/tanx.png", r-112, hloc - 32 , 4* cm, 0.9472 * cm,mask='auto')
            canvas.drawRightString(r, hloc-50, "碳析，让地球不再叹息")
            canvas.drawRightString(r, hloc-75, "联系我们：tanxplatform@163.com")
        else:
            canvas.drawImage("./reportlab_fc/page.png", 0, 0, 21* cm, 29.7 * cm)
            canvas.setFont(hei, 10)
            canvas.drawString(40, PAGE_HEIGHT - 40, name_+monthstr+'碳排放核算报告')
            canvas.drawString(PAGE_WIDTH - 40, 20, "{}".format(doc.page))
            canvas.drawImage("./reportlab_fc/logo_w.png", 470, 790, 2.5* cm, 0.9766* cm,mask='auto')
        canvas.restoreState()
    
    #画图函数定义
    class Graphs:
        # 绘制小标题
        @staticmethod
        def draw_little_title(title: str):
            # 获取所有样式表
            style = getSampleStyleSheet()
            # 拿到标题样式
            ct = style['Normal']
            # 单独设置样式相关属性
            ct.fontName = 'simsun'  # 字体名
            ct.fontSize = 15  # 字体大小
            ct.textColor = colors.black  # 字体颜色
            #ct.firstLineIndent = 10
            ct.leading = 20
            # 创建标题对应的段落，并且返回
            return Paragraph(title, ct)
        
        @staticmethod
        def draw_content_title(title: str):
            # 获取所有样式表
            style = getSampleStyleSheet()
            # 拿到标题样式
            ct = style['Normal']
            # 单独设置样式相关属性
            ct.fontName = 'simsun'  # 字体名
            ct.fontSize = 12  # 字体大小
            ct.textColor = colors.blue  # 字体颜色
            #ct.firstLineIndent = 10
            ct.leading = 25
            ct.alignment = 1 
            # 创建标题对应的段落，并且返回
            return Paragraph(title, ct)

        # 绘制普通段落内容
        @staticmethod
        def draw_text(text: str,text_color = colors.grey,alignment = 0):
            # 获取所有样式表
            style = getSampleStyleSheet()
            # 获取普通样式
            ct = style['Normal']
            ct.textColor=text_color
            ct.fontName = sun
            ct.fontSize = 12
            ct.wordWrap = 'CJK'     # 设置自动换行
            ct.alignment = alignment     # 左对齐
            ct.firstLineIndent = 24     # 第一行开头空格
            ct.leading = 15
            return Paragraph(text, ct)
            
        @staticmethod
        def draw_item(text: str):
            # 获取所有样式表
            style = getSampleStyleSheet()
            # 获取普通样式
            text = '•'+ text
            ct = style['Normal']
            ct.textColor=colors.black
            ct.fontName = sun
            ct.fontSize = 12
            ct.wordWrap = 'CJK'     # 设置自动换行
            ct.alignment = 0        # 左对齐
            ct.firstLineIndent = 30     # 第一行开头空格
            ct.leading = 15
            return Paragraph(text, ct)
        
        @staticmethod
        def draw_empty(text = '&nbsp;&nbsp;'):
            # 获取所有样式表
            style = getSampleStyleSheet()
            # 获取普通样式
            ct = style['Normal']
            ct.textColor=colors.grey
            ct.fontName = sun
            ct.fontSize = 12
            ct.wordWrap = 'CJK'     # 设置自动换行
            ct.alignment = 0        # 左对齐
            ct.firstLineIndent = 24     # 第一行开头空格
            ct.leading = 5
            return Paragraph(text, ct)

        # 绘制表格
        @staticmethod
        def draw_table(*args,col_width,otherstytle = []):
            style = [
                ('FONTNAME', (0, 0), (-1, -1), 'simsun'),  # 字体
                ('FONTSIZE', (0, 0), (-1, 0), 12),  # 第一行的字体大小
                ('FONTSIZE', (0, 1), (-1, -1), 10),  # 第二行到最后一行的字体大小
                ('BACKGROUND', (0, 0), (-1, 0), '#d5dae6'),  # 设置第一行背景颜色
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # 第一行水平居中
                ('ALIGN', (0, 1), (-1, -1), 'LEFT'),  # 第二行到最后一行左右左对齐
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # 所有表格上下居中对齐
                ('TEXTCOLOR', (0, 0), (-1, -1), colors.darkslategray),  # 设置表格内文字颜色
                ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),  # 设置表格框线为grey色，线宽为0.5
                # ('SPAN', (0, 1), (0, 2)),  # 合并第一列二三行
                # ('SPAN', (0, 3), (0, 4)),  # 合并第一列三四行
                # ('SPAN', (0, 5), (0, 6)),  # 合并第一列五六行
                # ('SPAN', (0, 7), (0, 8)),  # 合并第一列五六行
            ]
            style = style + otherstytle
            table = Table(args, colWidths=col_width, style=style)
            return table
        
        # 创建图表
        @staticmethod
        def draw_bar(bar_data: list, ax: list, items: list):
            drawing = Drawing(500, 225)
            bc = VerticalBarChart()
            bc.x = 45       # 整个图表的x坐标
            bc.y = 45      # 整个图表的y坐标
            bc.height = 170     # 图表的高度
            bc.width = 400      # 图表的宽度
            bc.data = bar_data
            bc.strokeColor = colors.black       # 顶部和右边轴线的颜色
            #bc.fillColor = colors.blakc
            bc.valueAxis.valueMin = 0   # 设置y坐标的最小值
            bc.valueAxis.valueMax = int(max([sum(xx) for xx in list(zip(*bar_data))])/100)*110   # 设置y坐标的最大值
            bc.valueAxis.valueStep = int(bc.valueAxis.valueMax/10)  # 设置y坐标的步长
            bc.categoryAxis.labels.dx = 2
            bc.categoryAxis.labels.dy = -8
            bc.categoryAxis.labels.angle = 20
            bc.categoryAxis.labels.fontName = 'simsun'
            bc.categoryAxis.style = 'stacked'
            bc.categoryAxis.categoryNames = ax
            for i in range(len(items)):
                bc.bars[i].fillColor = list(zip(*items))[0][i]

            # 图示
            leg = Legend()
            leg.fontName = 'simsun'
            leg.alignment = 'right'
            leg.boxAnchor = 'ne'
            leg.x = 530         # 图例的x坐标
            leg.y = 170
            leg.dxTextSpace = 10
            leg.columnMaximum = 3
            leg.colorNamePairs = items
            drawing.add(leg)
            drawing.add(bc)
            return drawing

        # 绘制图片
        @staticmethod
        def draw_img(path,w,h):
            img = Image(path)       # 读取指定路径下的图片
            img.drawWidth = w*cm        # 设置图片的宽度
            img.drawHeight = h*cm       # 设置图片的高度
            return img

    def draw_pie(pie_data: list, pie_labels: list,colors_: list,x,y):
        xsort = list(zip(pie_data,pie_labels))
        xsort.sort(key=lambda m:m[0],reverse=True)
        pie_data,pie_labels = zip(*xsort)
        sum_ = sum(pie_data)
        rate_ = [format(100*i/sum_,'.1f')+'%' for i in pie_data]
        pc = Pie()
        pc.x = x
        pc.y = y
        pc.width = 100
        pc.height = 100
        pc.data = pie_data
        pc.labels = rate_
        #pc.slices.fontName=sun
        pc.slices.fontSize=10
        pc.slices.strokeWidth = 0
        pc.slices.fontColor = colors.green
        #pc.direction = 'clockwise'
        #pc.slices[3].popout = 5
        #pc.slices[3].strokeWidth = 1
        #pc.slices[3].strokeDashArray = [1, 1]
        #pc.slices[3].labelRadius = 1.75
        #pc.slices[3].fontColor = colors.red
        leg = Legend()
        leg.fontName = 'simsun'
        leg.alignment = 'right'
        leg.boxAnchor = 'ne'
        leg.x = x + pc.width + 100       # 图例的x坐标
        leg.y = y + pc.height -30
        leg.dxTextSpace = 10
        leg.columnMaximum = 3
        leg.colorNamePairs = list(zip(colors_,pie_labels))
        for i in range(len(colors_)):
            pc.slices[i].fillColor = colors_[i]
            pc.slices[i].strokeColor = colors.white
            pc.slices[i].popout = 3*i
            pc.slices[i].labelRadius = 1.25-0.1*i
        return [pc,leg]

    # mainpart
    y_m = str(data_['year']*100+data_['month'])
    randomstr = ''.join(random.sample('1234567890qwertyuiopasdfghjklzxcvbnm',30))
    usermonthstr = str((int(data['username'])*1000000 + data_['year']*100 + data_['month'])*5)
    #with open("info.json", "r") as f:      #(test.py use this line!!!!!!!!!)
    with open("./reportlab_fc/info.json", "r") as f:
        old_data = json.load(f)
        old_data.update({usermonthstr:randomstr})
    with open("./reportlab_fc/info.json", "w") as f:
        json.dump(old_data, f)
    fileloc = './reportlab_fc/reportfiles/'+usermonthstr+randomstr
    os.makedirs(fileloc)
    doc = SimpleDocTemplate(fileloc+'/'+y_m+'report.pdf', pagesize=A4,leftMargin=40,rightMargin=40,topMargin=45,bottomMargin=10)
    # 初始化内容
    story =[]
    # 将段落添加到内容中
    story.append(PageBreak())
    story.append(Graphs.draw_img('./reportlab_fc/gybbg.png',21,2.4177))
    story.append(Graphs.draw_little_title('报告边界：'))
    text = '本报告的报告边界为<font color="red">'+name_+'</font>组织边界内运营控制源产生的直接（范围一）温室气体排放、来自输入能源的间接（范围二）温室气体排放以及发生在价值链中的其他间接（范围三）实质性温室气体排放，此外，本报告还包含公司碳减排绩效。'
    story.append(Graphs.draw_text(text))
    text = '根据各类别排放的预计占比大小、给公司带来的气候风险以及开展相减排行动的可行性作为实质性的主要评估标准，本报告核算所涉的温室气体排放类别及对应的具体排放源信息如表1所示。'
    story.append(Graphs.draw_text(text))
    story.append(Graphs.draw_empty())
    story.append(Graphs.draw_content_title('表1：核算的温室气体排放类别及对应排放源'))
    sheet = [
            ('温室气体排放类别', '主要排放源', '活动数据来源'),
            ('范围1：直接温室气体排放', '煤，焦炭、天然气的固定燃烧','工厂燃料消耗清单'),
            ('范围1：直接温室气体排放', '汽油、柴油的移动燃烧', '工厂自有车辆加油登记表'),
            ('范围2：来自输入能源的间接温室气体排放', '外购电力', '电力采购发票'),
            ('范围2：来自输入能源的间接温室气体排放', '外购热力', '热力，蒸汽采购发票'),
            ('范围3：价值链上的间接温室气体排放', '员工差旅', '差旅系统、行程单等'),
            ('范围3：价值链上的间接温室气体排放', '员工通勤', '员工通勤调查问卷'),
            ('减排绩效', '购买绿色电力', 'I-Rec证书、绿电交易凭证等'),
            ('减排绩效', '其他减排', '其他证明材料')
        ]
    story.append(Graphs.draw_table(*sheet,col_width=[200,140,140]))
    story.append(Graphs.draw_empty())
    text = '本报告所涉及数据的时间范围是从<font color="red">'+monthstr+'1日</font>'+'到<font color="red">'+monthstr+str(lastday)+'日</font>'
    story.append(Graphs.draw_text(text))
    story.append(Graphs.draw_empty())
    story.append(Graphs.draw_little_title('核算标准：'))
    text = '根据ISO 14064-1:2018 中要求，并结合数据的实际可得性和获取成本，本报告依据'+name_+'所提供的活动数据和相关证明材料，采用排放因子法对'+name_+'的温室气体排放进行量化。'
    story.append(Graphs.draw_text(text))
    text = '综合考量排放因子来源的明确性和公信力、针对排放量化方法和活动数据的适用性以及时效性，选择尽可能精确、可靠、及时的排放因子进行核算。排放因子的来源及参考依据主要包括：'
    story.append(Graphs.draw_text(text))
    story.append(Graphs.draw_empty())
    story.append(Graphs.draw_item('《IPCC 2006 年国家温室气体清单指南》'))
    story.append(Graphs.draw_item('《温室气体核算体系：企业核算与报告标准（2011）》'))
    story.append(Graphs.draw_item('《温室气体核算体系：产品寿命周期核算和报告标准（2011）》'))
    story.append(Graphs.draw_item('《国民经济行业分类》'))
    story.append(Graphs.draw_item('《企业温室气体排放报告核查指南》'))
    story.append(Graphs.draw_item('《工业其他行业企业温室气体排放核算方法与报告指南（试行）（2015）》'))
    story.append(Graphs.draw_item('《温室气体自愿减排项目审定与核证指南》'))
    story.append(Graphs.draw_item('《关于做好2023-2025年发电行业企业温室气体排放报告管理有关工作的通知（2023）》'))
    story.append(PageBreak())


    story.append(Graphs.draw_img('./reportlab_fc/wsqthsjg.png',21,2.4320))
    story.append(Graphs.draw_little_title('排放详情：'))
    text =  '<font color="red">'+name_+'</font>从<font color="red">'+monthstr+'1日</font>'+'至<font color="red">'+monthstr+str(lastday)+'日</font>的温室气体排放情况如表2所示。'
    story.append(Graphs.draw_text(text))
    story.append(Graphs.draw_empty())
    story.append(Graphs.draw_content_title('表2：公司'+monthstr+'温室气体排放量'))
    sheet = [
            ('温室气体排放类别', '单位', monthstr+'排放量'),
            ('范围1：直接温室气体排放', '吨二氧化碳当量',format(data_['emission1'],',.3f')),
            ('范围2：来自输入能源的间接温室气体排放', '吨二氧化碳当量', format(data_['emission2'],',.3f')),
            ('范围3：价值链上的间接温室气体排放', '吨二氧化碳当量', format(data_['emission3'],',.3f')),
            ('范围1+范围2 温室气体排放', '吨二氧化碳当量',format(data_['emission1']+data_['emission2'],',.3f')),
            ('间接（范围2+范围3）温室气体排放', '吨二氧化碳当量', format(data_['emission2']+data_['emission3'],',.3f')),
            ('范围1+范围2+范围3 温室气体排放', '吨二氧化碳当量', format(data_['emission_all'],',.3f')),
        ]
    story.append(Graphs.draw_table(*sheet,col_width=[200,100,110],otherstytle=[('ALIGN', (-1, 1), (-1, -1), 'RIGHT')]))
    text = '按照温室气体排放源划分的具体排放占比如图1所示：'
    story.append(Graphs.draw_text(text))
    story.append(Graphs.draw_empty())
    story.append(Graphs.draw_content_title('图1：按照温室气体排放源划分的排放占比'))
    Dr = Drawing(PAGE_WIDTH,300)
    p1=draw_pie([data_['emission1'],data_['emission2'],data_['emission3']],['Scope1','Scope2','Scope3'],colors_=[colors.HexColor(0x080CE2),colors.HexColor(0x31ADFB),colors.HexColor(0x31FBFB)],x=50,y=150)
    p2=draw_pie([data_['fixburn'],data_['movingburn']],['固定燃烧','移动燃烧'],colors_=[colors.HexColor(0x080CE2),colors.HexColor(0x31ADFB)],x=PAGE_WIDTH/2-20,y=150)
    p3=draw_pie([data_['electricity'],data_['heating']],['购买电力','购买热力'],colors_=[colors.HexColor(0x080CE2),colors.HexColor(0x31ADFB)],x=50,y=0)
    p4=draw_pie([data_['commuting'],data_['travel']],['员工通勤','员工差旅'],colors_=[colors.HexColor(0x080CE2),colors.HexColor(0x31ADFB)],x=PAGE_WIDTH/2-20,y=0)
    for p in [p1[0],p1[1],p2[0],p2[1],p3[0],p3[1],p4[0],p4[1]]:
        Dr.add(p)
    for xy in [(100,50),(100,200),(PAGE_WIDTH/2+30,50),(PAGE_WIDTH/2+30,200)]:
        circle = Circle(xy[0], xy[1], 38)
        circle.fillColor = colors.white
        circle.strokeColor = colors.transparent
        Dr.add(circle)
    for xy_lab in [(130,130,'Scope1'),(130,290,'总排放'),(PAGE_WIDTH/2+60,130,'Scope3'),(PAGE_WIDTH/2+60,290,'Scope1')]:
        lab = Label()
        lab.setOrigin(xy_lab[0],xy_lab[1])
        lab.boxAnchor = 'ne'
        lab.fontName = 'simsun'
        lab.fillColor = colors.white
        lab.boxFillColor = colors.green
        lab.setText(xy_lab[2])
        lab.textAnchor = 'middle'
        lab.width = 50
        lab.fontSize = 12
        lab.height = 15
        Dr.add(lab)
    story.append(Dr)
    es = data_['emission_all']/data_['output']
    text = monthstr+'，'+name_+'的温室气体排放强度为：<b><font color="red">'+format(es,'.2f')+'吨二氧化碳/万元</font></b>'
    story.append(Graphs.draw_empty())
    story.append(Graphs.draw_empty())
    story.append(Graphs.draw_text(text,text_color=colors.black))


    story.append(PageBreak())


    story.append(Graphs.draw_img('./reportlab_fc/tjpjz.png',21,2.4294))
    story.append(Graphs.draw_little_title('排放趋势：'))
    if historynum >= 2:
        text = '依据'+name_+'所提供的活动数据和相关证明材料，综合公司前'+str(historynum)+'月份的气体排放数据，得到公司的碳排放趋势如下。'
        story.append(Graphs.draw_empty())
        story.append(Graphs.draw_text(text))
        emission1 = []
        emission2 = []
        emission3 = []
        output_all = 0
        ax_data = []
        historydata.reverse()
        historydata.append(data_)
        for h_data in historydata:
            emission1.append(h_data['emission1'])
            emission2.append(h_data['emission2'])
            emission3.append(h_data['emission3'])
            output_all = output_all + h_data['output']
            ax_data.append(str(h_data['year'])+'年'+str(h_data['month'])+'月')
        b_data = [tuple(emission1),tuple(emission2),tuple(emission3)]
        leg_items = [(colors.HexColor(0x080CE2),'Scope1'),(colors.HexColor(0x31ADFB),'Scope2'),(colors.HexColor(0x31FBFB),'Scope3')] 
        story.append(Graphs.draw_bar(b_data, ax_data, leg_items))
        h_e_sum = sum(emission1)+sum(emission2)+sum(emission3)
        h_es = h_e_sum / output_all
        h_e_average = h_e_sum / historynum
        if h_e_average >= data_['emission_all']:
            changerate = (1 - data_['emission_all'] / h_e_average) * 100
            e_str = '下降'+format(changerate,'.2f')+'%'
        else:
            changerate = (data_['emission_all'] / h_e_average -1) * 100
            e_str = '增长'+format(changerate,'.2f')+'%'
        if h_es >= es:
            changerate = (1 - es / h_es) * 100
            es_str = '下降'+format(changerate,'.2f')+'%'
        else:
            changerate = (es / h_es -1) * 100
            es_str = '增长'+format(changerate,'.2f')+'%'
        
        text = name_ + '前'+str(historynum)+'个月的月平均碳排放总量为'+format(h_e_average,'.2f')+'吨二氧化碳当量，本月排放量为'+format(data_['emission_all'],'.2f')+'吨二氧化碳当量，<font color="red">环比'+e_str+'</font>，同时，公司前'+str(historynum)+'个月的平均碳排放强度为'+format(h_es,'.2f')+'吨二氧化碳/万元，本月的碳排放强度为'+format(es,'.2f')+'吨二氧化碳/万元，<font color="red">环比'+es_str+'</font>。'
        story.append(Graphs.draw_text(text))
        Dr = Drawing(PAGE_WIDTH,100)
        for i in range(3):
            monthdata = historydata[-3+i]
            p1=draw_pie([monthdata['offset'],(monthdata['electricity']-monthdata['offset'])],['绿色电力','普通购电'],colors_=[colors.HexColor(0x0EF86F),colors.grey],x=50+125*i,y=0)
            Dr.add(p1[0])
            circle = Circle(100+125*i, 50, 38)
            circle.fillColor = colors.white
            circle.strokeColor = colors.transparent
            Dr.add(circle)
            lab = Label()
            lab.setOrigin(130+125*i,-5)
            lab.boxAnchor = 'ne'
            lab.fontName = 'simsun'
            lab.fillColor = colors.white
            lab.boxFillColor = colors.green
            lab.setText(str(monthdata['year'])+'月'+str(monthdata['month'])+'月')
            lab.textAnchor = 'middle'
            lab.width = 65
            lab.fontSize = 12
            lab.height = 15
            Dr.add(lab)
        #只需要最后一个图例
        Dr.add(p1[1])
        story.append(Graphs.draw_empty())
        story.append(Graphs.draw_little_title('碳中和：'))
        story.append(Graphs.draw_empty())
        text = '依据'+name_+'所提供的绿证等相关证明材料，公司的碳中和绩效如下。'
        story.append(Graphs.draw_text(text))
        story.append(Graphs.draw_empty())
        story.append(Graphs.draw_empty())
        story.append(Graphs.draw_empty())
        story.append(Dr)
        story.append(Graphs.draw_empty())
        story.append(Graphs.draw_empty())
        story.append(Graphs.draw_empty())
        story.append(Graphs.draw_empty())
        story.append(Graphs.draw_empty())
        text = name_+'在'+monthstr+'绿色电力的使用比例达到了<font color="red">' +format((data_['offset']/data_['electricity'])*100,'.2f') +'%</font>，相当于<font color="red">避免约'+format(data_['offset'],'.2f')+'吨二氧化碳排放</font>。'
        story.append(Graphs.draw_text(text))
    else:
        text = '由于'+name_+'未上传前两个月的活动数据或未提供完整的证明材料，本报告无法提供可信的碳排放趋势。'
        story.append(Graphs.draw_text(text))

    story.append(PageBreak())
    story.append(Graphs.draw_empty())
    story.append(Graphs.draw_empty())
    story.append(Graphs.draw_empty())
    story.append(Graphs.draw_empty())
    story.append(Graphs.draw_empty())
    story.append(Graphs.draw_empty())
    story.append(Graphs.draw_empty())
    text1 = '本研究报告仅供碳析（TanX）平台的注册客户使用。特别的，本平台不会因接收人收到本报告而视其为客户。在任何情况下，本报告中的排放信息并不构成对任何公司的建议或意见，碳析平台不对任何人因使用本报告中的内容所导致的损失负任何责任。在法律许可的情况下，碳析平台及其部分客户可能和报告中提到的公司进行交易活动，还可能为这些公司提供投资银行服务或其他服务。'
    text2 = '碳排放的测算是复杂且困难的过程，本报告估算碳排放所采用的信息为报告公司所提供的经营活动数据，证明材料和其他碳析平台认为可靠且已公开的信息，平台仅对公司提供材料进行初步核查。碳析平台力求但不能保证这些信息的准确性和完整性，也不保证报告内容不会发生任何变更，在不同时期，碳析可发出与本报告所载内容不同的更正报告。'
    text3 = '本报告的版权归碳析平台所有，未经书面许可，任何机构和个人不得以任何形式翻版、复制和发布。如引用、刊发、转载，需征得碳析平台的同意，并注明出处为碳析（TanX），且不得对本报告任何内容进行有悖原意的引用、删节和修改。'
    story.append(Graphs.draw_text(text1))
    story.append(Graphs.draw_empty())
    story.append(Graphs.draw_text(text2))
    story.append(Graphs.draw_empty())
    story.append(Graphs.draw_text(text3))
    ############################
    ############################
    doc.build(story,onFirstPage=myFirstPage, onLaterPages=myLaterPage)