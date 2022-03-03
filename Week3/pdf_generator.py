from reportlab.platypus import SimpleDocTemplate, Paragraph, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie

report = SimpleDocTemplate("report.pdf")

fruit = {
    "elderberries": 1,
    "figs": 1,
    "apples": 2,
    "durians": 3,
    "bananas": 5,
    "cherries": 8,
    "grapes": 13
}

styles = getSampleStyleSheet()

report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])

table_data = []
for k, v in fruit.items():
    table_data.append([k, v])

table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]

report_table = Table(data=table_data, style=table_style, hAlign="LEFT")

report_pie = Pie()
report_pie.data = []
report_pie.labels = []

for fruit_name in sorted(fruit):
    report_pie.data.append(fruit[fruit_name])
    report_pie.labels.append(fruit_name)

report_chart = Drawing(width=400, height=400)
report_chart.add(report_pie)
print(report_pie.data)

report.build([report_title, report_table])