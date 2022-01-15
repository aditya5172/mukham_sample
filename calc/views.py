from django.shortcuts import render
import numpy as np
import datetime
import pandas as pd
import datetime
import json
from json import dumps

from collections import OrderedDict
from fusionexport import ExportManager, ExportConfig

from django.http import HttpResponse
from django.http import JsonResponse

def home(request):
    return render(request,'home.html',{'name':'Kiran'})

def add(request):

    x={'Name': ['Vedavalli Perigisetty', 'Vedavalli Perigisetty', 'Vedavalli Perigisetty', 'Vedavalli Perigisetty', 'Vedavalli Perigisetty', 'Vedavalli Perigisetty', 'Vedavalli Perigisetty', 'Vedavalli Perigisetty', 'Vedavalli Perigisetty', 'Vedavalli Perigisetty', 'Vedavalli Perigisetty'], 'Date': [datetime.datetime(2021, 11, 24, 0, 0), datetime.datetime(2021, 11, 25, 0, 0), datetime.datetime(2021, 11, 26, 0, 0), datetime.datetime(2021, 11, 30, 0, 0), datetime.datetime(2021, 12, 1, 0, 0), datetime.datetime(2021, 12, 2, 0, 0), datetime.datetime(2021, 12, 3, 0, 0), datetime.datetime(2021, 12, 4, 0, 0), datetime.datetime(2021, 12, 14, 0, 0), datetime.datetime(2021, 12, 15, 0, 0), datetime.datetime(2021, 12, 30, 0, 0)], 'First Shift': [True, True, True, True, True, True, True, True, False, True, True], 'Time for First Shift': ['06:56:58', '04:06:33', '04:10:02', '03:52:22', '04:12:01', '04:26:40', '04:14:14', '05:47:21', np.nan, '04:14:32', '04:34:11'], 'Second Shift': [True, True, True, True, True, False, False, True, True, False, False], 'Time for Second Shift': ['11:42:41', '11:08:37', '11:00:48', '11:32:04', '11:46:06', np.nan, np.nan, '11:39:56', '11:33:20', np.nan, np.nan]}


    df2=pd.DataFrame(x)
    #print(df2.to_string())
    da={
        'Date':[],
        'First Shift':[],
        'Time for First Shift':[],
        'Second Shift':[],
        'Time for Second Shift':[]
    }

    def numberOfDays( y, m):
      leap = 0
      if y% 400 == 0:
         leap = 1
      elif y % 100 == 0:
         leap = 0
      elif y% 4 == 0:
         leap = 1
      if m==2:
         return 28 + leap
      list = [1,3,5,7,8,10,12]
      if m in list:
         return 31
      return 30

    m=0


    for i in range(0,len(df2)-1):
        if df2['Date'][i+1].month!=df2['Date'][i].month:
            ld=numberOfDays(df2['Date'][i].year,df2['Date'][i].month)
            da['Date'].append(df2['Date'][i])
            da['First Shift'].append(df2['First Shift'][i])
            da['Time for First Shift'].append(df2['Time for First Shift'][i])
            da['Second Shift'].append(df2['Second Shift'][i])
            da['Time for Second Shift'].append(df2['Time for Second Shift'][i])
            #print(df2['Date'][i].day+1,ld+1)
            for j in range(df2['Date'][i].day+1,ld+1):
                dd=datetime.date(df2['Date'][i].year,df2['Date'][i].month,j)

                da['Date'].append(dd)
                da['First Shift'].append(False)
                da['Time for First Shift'].append(np.nan)
                da['Second Shift'].append(False)
                da['Time for Second Shift'].append(np.nan)
            for j in range(1,df2['Date'][i+1].day):
                dd=datetime.date(df2['Date'][i+1].year,df2['Date'][i+1].month,j)

                da['Date'].append(dd)
                da['First Shift'].append(False)
                da['Time for First Shift'].append(np.nan)
                da['Second Shift'].append(False)
                da['Time for Second Shift'].append(np.nan)

        else:
            #print(df2['Date'][i+1].day-df2['Date'][i].day)

            if (df2['Date'][i+1].day-df2['Date'][i].day)>1:
                da2=df2['Date'][i+1].day
                da1=df2['Date'][i].day
                da['Date'].append(df2['Date'][i])
                da['First Shift'].append(df2['First Shift'][i])
                da['Time for First Shift'].append(df2['Time for First Shift'][i])
                da['Second Shift'].append(df2['Second Shift'][i])
                da['Time for Second Shift'].append(df2['Time for Second Shift'][i])
                #print(m,"yes")
                m=m+1
                for j in range(da1+1,da2):
                    dd=datetime.date(df2['Date'][i].year,df2['Date'][i].month,j)
                    #print(dd)
                    da['Date'].append(dd)
                    da['First Shift'].append(False)
                    da['Time for First Shift'].append(np.nan)
                    da['Second Shift'].append(False)
                    da['Time for Second Shift'].append(np.nan)
            else:
                da['Date'].append(df2['Date'][i])
                da['First Shift'].append(df2['First Shift'][i])
                da['Time for First Shift'].append(df2['Time for First Shift'][i])
                da['Second Shift'].append(df2['Second Shift'][i])
                da['Time for Second Shift'].append(df2['Time for Second Shift'][i])

    da['Date'].append(df2['Date'][i+1])
    da['First Shift'].append(df2['First Shift'][i+1])
    da['Time for First Shift'].append(df2['Time for First Shift'][i+1])
    da['Second Shift'].append(df2['Second Shift'][i+1])
    da['Time for Second Shift'].append(df2['Time for Second Shift'][i+1])
    df3=pd.DataFrame(da)
    #print(df3.to_string())

    def per(df4):
        p=0
        ab=0
        for i in range(0,len(df4)):
            if df4['First Shift'][i]:
                p=p+1
            elif df4['Second Shift'][i]:
                p=p+1
            else:
                ab=ab+1
        return p,ab
    p=0
    ab=0
    p,ab=per(df3)
    #print(p,ab)
    ddf={'Values':[p,ab],'Status':['Presnt','Absent']}
    ddf=pd.DataFrame(ddf)

    ax={'Present_Both_Shift':[],'Present_First_Shift':[],'Present_Second_Shift':[],'Absent_Both_Shift':[],'Absent_First_Shift':[],'Absent_Second_Shift':[]}
    def de(df4):
        xyz=df4['Date'][0]
        for i in range(0,len(df4),7):
            xxy=(df4['Date'][i]-xyz)/np.timedelta64(1,'D')
            xxx=int(xxy/7)+1
            pf=0
            ps=0
            af=0
            ab=0
            pb=0
            ass=0
            for j in range(i,i+7):
                if j>=len(df4):
                    break
                if df4['First Shift'][j] and df4['Second Shift'][j]:
                    pb=pb+1
                    continue
                elif not df4['First Shift'][j] and not df4['Second Shift'][j]:
                    ab=ab+1
                    continue
                if df4['First Shift'][j]:
                    pf=pf+1
                else:
                    af=af+1
                if df4['Second Shift'][j]:
                    ps=ps+1
                else:
                    ass=ass+1
            ax['Present_Both_Shift'].append(pb)
            ax['Absent_Both_Shift'].append(ab)
            ax['Present_First_Shift'].append(pf)
            ax['Present_Second_Shift'].append(ps)
            ax['Absent_First_Shift'].append(af)
            ax['Absent_Second_Shift'].append(ass)
        return ax
    ax=de(df3)
    #print(ax)
    ax=pd.DataFrame(ax)
    #ax=ax.transpose()
    #print(ax)

    json_records = ax.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)


    return render(request,'add.html',{'positivePercent':10,'negativePercent':30})
