#
# bar graph plot
#

from bokeh.io import output_file, show, save
from bokeh.plotting import figure

awscolor="#b3de69"
tkcolor="lightblue"

# XAVC300-1, XAVC300-2,XAVC150-1, XAVC150-2, HQX-1, HQX2
tk_w15lt = ['W15LT', [798,808, 605, 608, 179, 180]]
tk_w2000 = ['W2000', [1089, 1086, 817, 816, 271, 274]]
tk_w4000 = ['W4000', [538,535,516,514,146,148  ]]
tk_hdws4k3a = ['4K3A', [ 349, 348, 376, 376, 91, 91 ]]
aws_c5d4xlarge = ['c5d.4xlarge', [704,694,523,536,167,167]]
aws_r5d4xlarge = ['r5d.4xlarge', [762,968,612,720,232,232]]
aws_r5d8xlarge = ['r5d.8xlarge', [381, 402, 355, 363, 98, 104]]
aws_m5xlarge   = ['m5.xlarge', [3061, 3078, 2373, 2350, 777, 781]]
aws_m5d8xlarge   = ['m5d.8xlarge', [377, 359, 335, 333, 91, 99]]


label =[ tk_w15lt[0], tk_w2000[0], tk_w4000[0], tk_hdws4k3a[0], 
        aws_r5d4xlarge[0], aws_c5d4xlarge[0], aws_r5d8xlarge[0], aws_m5xlarge[0], 
        aws_m5d8xlarge[0] ]
data = [ tk_w15lt[1][0] , tk_w2000[1][0], tk_w4000[1][0], tk_hdws4k3a[1][0],
         aws_r5d4xlarge[1][0], aws_c5d4xlarge[1][0], aws_r5d8xlarge[1][0], aws_m5xlarge[1][0],
         aws_m5d8xlarge[1][0]]

fill_color = [tkcolor, tkcolor, tkcolor, tkcolor,
             awscolor, awscolor, awscolor, awscolor,
             awscolor ]


#sort
zip_lists = zip(data,label,fill_color)
zip_sort = sorted(zip_lists, reverse=True) 
data,label,fill_color = zip(*zip_sort) # zipを解除

#
p = figure(plot_height=240, title="XAVC 300Mbps, 4K export time", toolbar_location=None, y_range=label)
p.hbar(y=label, right=data, height=0.7, fill_color=fill_color )

p.xaxis.axis_label = "Processing time(sec)"
p.background_fill_color = "beige"
p.background_fill_alpha = 0.7

output_file("bars.html")
show(p)
