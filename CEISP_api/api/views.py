from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.contrib.auth import authenticate, login
from account.models import EnterpriseUser as User
from account.models import Scope1emissions
from account.models import Scope2emissions
from account.models import Scope3emissions
from account.models import offset
#from django.contrib.auth.models import User
from account.models import Account
from .serializers import AccountSerializer,UsersSerializer,Scope1emissionsSerializer,Scope2emissionsSerializer,Scope3emissionsSerializer,offsetSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly
from rest_framework import status
from django.db.models import Q
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.utils import timezone
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import roleTokenObtainPairSerializer
import logging
import json

from reportlab_fc.data2pdf import data2pdf

logging.basicConfig(
    format='%(asctime)s - %(pathname)s[%(lineno)d] - %(levelname)s: %(message)s',
    level=logging.INFO)
logger = logging.getLogger(__name__)

#测试用api
@api_view(['GET','POST','OPTIONS'])
#@permission_classes((IsAuthenticated,))
def get_accounts(request):
    if request.method == 'OPTIONS':
        return Response({'Msg':'ok'},status=status.HTTP_200_OK)
    if request.method == 'GET':
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE','OPTIONS'])
#@permission_classes((IsAuthenticated,))
def get_account_detail(request, id):
    if request.method == 'OPTIONS':
        return Response({'Msg':'ok'},status=status.HTTP_200_OK)
    try:
        account = Account.objects.get(pk=id)
        if request.method == 'GET':
            serializer = AccountSerializer(account)
            return Response(serializer.data,status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            serializer = AccountSerializer(account, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            account.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    except:
        return Response({'DEBUG_ERROR':'No such id'}, status=status.HTTP_400_BAD_REQUEST)

#登录(实际上没有啥用)
@api_view(['GET','POST','OPTIONS'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JWTAuthentication,))
def user_login(request):
    if request.method == 'OPTIONS':
        return Response({'Msg':'ok'},status=status.HTTP_200_OK)
    logger.error('request')
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)

    if username is None or password is None:
        return Response({'ERROR': '请求参数错误'},status=status.HTTP_400_BAD_REQUEST)

    is_login = authenticate(request, username=username, password=password)
    if is_login is None:
        return Response({'ERROR': '账号或密码错误'},status=status.HTTP_400_BAD_REQUEST)

    #return Response({'token': token},status=status.HTTP_200_OK)
    return Response({'token': 666},status=status.HTTP_200_OK)

#公司主页信息展示
@api_view(['GET','OPTIONS'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JWTAuthentication,))
def get_emission_info(request):
    if request.method == 'OPTIONS':
        return Response({'Msg':'ok'},status=status.HTTP_200_OK)
    user = request.user
    try:
        user_scope1 = user.scope1.all().order_by('-year', '-month')[0]
        year = user_scope1.year
        month = user_scope1.month
    except:
        res_info = {'Enterprise_Name':user.Enterprise_Name,
        'Enterprise_Intro':user.Enterprise_Intro,
        'Enterprise_Legalperson':user.Enterprise_Legalperson,
        'username':user.username,
        'email':user.email,}
        return Response(res_info,status=status.HTTP_202_ACCEPTED)
    user_scope2 = user.scope2.get(year=year,month=month)
    user_scope3 = user.scope3.get(year=year,month=month)
    user_offset = user.offset.get(year=year,month=month)
    response_data_show = month_data_to_dict(user_scope1,user_scope2,user_scope3,user_offset)
    response_data = {
        'Enterprise_Name':user.Enterprise_Name,
        'Enterprise_Intro':user.Enterprise_Intro,
        'Enterprise_Legalperson':user.Enterprise_Legalperson,
        'username':user.username,
        'email':user.email,
        'show_data':response_data_show}
    return Response(response_data,status=status.HTTP_200_OK)

##########################################################
#以下是可用api
##########################################################

# 登录获取token
class roleTokenObtainPairView(TokenObtainPairView):
    serializer_class = roleTokenObtainPairSerializer

# 注册
@api_view(['GET', 'POST','OPTIONS'])
@permission_classes((AllowAny,))
def register(request):
    if request.method == 'POST':
# 获取参数
        user_name = request.POST.get('Tel', None)
        pwd = request.POST.get('pwd',None)
        mail = request.POST.get('mail','')
		# 用户已存在
        if User.objects.filter(username=user_name):
            return Response({'Error':'用户已存在'}, status=status.HTTP_202_ACCEPTED)
        if User.objects.filter(email=mail):
            return Response({'Error':'用户已存在'}, status=status.HTTP_202_ACCEPTED)
        # 用户不存在
        else:
        #使用User内置方法创建用户
            userinfo = {'username':user_name,
                    'email':mail,
                    'password':pwd,
                    'Enterprise_Name':request.POST.get('EnterpriseName',''),
                    'is_staff':1,
                    'is_active':1,
                    'is_superuser':0}
            user = User.objects.create_user(**userinfo)
            return Response({'Msg':'Register successfully'}, status=status.HTTP_201_CREATED)
    elif request.method == 'OPTIONS':
        return Response({'Msg':'ok'},status=status.HTTP_200_OK)
    return Response({'ERROR':'error'}, status=status.HTTP_400_BAD_REQUEST)


# 修改公司信息
@api_view(['POST','OPTIONS'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JWTAuthentication,))
def user_changeinfo(request):
    if request.method == 'OPTIONS':
        return Response({'Msg':'ok'},status=status.HTTP_200_OK)
    user = request.user
    intro = request.POST.get('Enterprise_Intro', None)
    logger.error(str(request.POST))
    legalperson = request.POST.get('Enterprise_Legalperson', None)
    if intro:
        user.Enterprise_Intro = intro
    if legalperson:
        user.Enterprise_Legalperson = legalperson
        logger.info('changed')
    user.save()
    return Response({'msg':'修改完成'},status=status.HTTP_202_ACCEPTED)

#Scope1
@api_view(['POST','OPTIONS'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JWTAuthentication,))
def Scope1upload(request):
    if request.method == 'OPTIONS':
        return Response({'Msg':'ok'},status=status.HTTP_200_OK)
    user = request.user
    data = request.data.copy()
    #检查是否已经录入
    year_ = request.POST.get('year', None)
    month_ = request.POST.get('month', None)
    if user.scope1.filter(year=year_,month=month_):
        return Response({'Error':'Recorded!'}, status=status.HTTP_202_ACCEPTED)
    data.update({'Enterprise':user.username})
    serializer = Scope1emissionsSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Scope2
@api_view(['POST','OPTIONS'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JWTAuthentication,))
def Scope2upload(request):
    if request.method == 'OPTIONS':
        return Response({'Msg':'ok'},status=status.HTTP_200_OK)
    user = request.user
    data = request.data.copy()
    #检查是否已经录入
    year_ = request.POST.get('year', None)
    month_ = request.POST.get('month', None)
    if user.scope2.filter(year=year_,month=month_):    
        return Response({'Error':'Recorded!'}, status=status.HTTP_202_ACCEPTED)
    data.update({'Enterprise':user.username})
    serializer = Scope2emissionsSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Scope3
@api_view(['POST','OPTIONS'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JWTAuthentication,))
def Scope3upload(request):
    if request.method == 'OPTIONS':
        return Response({'Msg':'ok'},status=status.HTTP_200_OK)
    user = request.user
    data = request.data.copy()
    #检查是否已经录入
    year_ = request.POST.get('year', None)
    month_ = request.POST.get('month', None)
    if user.scope3.filter(year=year_,month=month_):
        return Response({'Error':'Recorded!'}, status=status.HTTP_202_ACCEPTED)
    data.update({'Enterprise':user.username})
    serializer = Scope3emissionsSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#减排信息录入
@api_view(['POST','OPTIONS'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JWTAuthentication,))
def offsetupload(request):
    if request.method == 'OPTIONS':
        return Response({'Msg':'ok'},status=status.HTTP_200_OK)
    user = request.user
    data = request.data.copy()
    #检查是否已经录入
    year_ = request.POST.get('year', None)
    month_ = request.POST.get('month', None)
    if user.offset.filter(year=year_,month=month_):
        return Response({'Error':'Recorded!'}, status=status.HTTP_202_ACCEPTED)
    data.update({'Enterprise':user.username})
    serializer = offsetSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 月度排放信息汇总函数（非api）
def month_data_to_dict(user_scope1,user_scope2,user_scope3,user_offset):
    is_certified_all = user_scope1.is_certified and user_scope2.is_certified and user_scope3.is_certified and user_offset.is_certified
    is_certified_part = user_scope1.is_certified or user_scope2.is_certified or user_scope3.is_certified or user_offset.is_certified
    if is_certified_all:
        is_certified = 'all'
    elif not is_certified_part:
        is_certified = 'none'
    else:
        is_certified = 'part'
    response_data = {'fixburn':format(user_scope1.fixburn,'.2f'),
                     'movingburn':format(user_scope1.movingburn,'.2f'),
                     'emission1':format(user_scope1.emission1,'.2f'),
                     'electricity':format(user_scope2.electricity,'.2f'),
                     'heating':format(user_scope2.heating,'.2f'),
                     'emission2':format(user_scope2.emission2,'.2f'),
                     'commuting':format(user_scope3.commuting,'.2f'),
                     'travel':format(user_scope3.travel,'.2f'),
                     'emission3':format(user_scope3.emission3,'.2f'),
                     'emission_all':format(user_scope1.emission1+user_scope2.emission2+user_scope3.emission3,'.2f'),
                     'offset':format(user_offset.offset,'.2f'),
                     'output':user_offset.output_wyuan,
                     'certified':is_certified,
                     'year':user_scope1.year,
                     'month':user_scope1.month}
    return response_data

def month_data_to_dict_float(user_scope1,user_scope2,user_scope3,user_offset):
    is_certified_all = user_scope1.is_certified and user_scope2.is_certified and user_scope3.is_certified and user_offset.is_certified
    is_certified_part = user_scope1.is_certified or user_scope2.is_certified or user_scope3.is_certified or user_offset.is_certified
    if is_certified_all:
        is_certified = 'all'
    elif not is_certified_part:
        is_certified = 'none'
    else:
        is_certified = 'part'
    response_data = {'fixburn':user_scope1.fixburn,
                     'movingburn':user_scope1.movingburn,
                     'emission1':user_scope1.emission1,
                     'electricity':user_scope2.electricity,
                     'heating':user_scope2.heating,
                     'emission2':user_scope2.emission2,
                     'commuting':user_scope3.commuting,
                     'travel':user_scope3.travel,
                     'emission3':user_scope3.emission3,
                     'emission_all':user_scope1.emission1+user_scope2.emission2+user_scope3.emission3,
                     'offset':user_offset.offset,
                     'output':user_offset.output_wyuan,
                     'certified':is_certified,
                     'year':user_scope1.year,
                     'month':user_scope1.month}
    return response_data

#公司信息提醒
@api_view(['GET','OPTIONS'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JWTAuthentication,))
def get_massage(request):
    if request.method == 'OPTIONS':
        return Response({'Msg':'ok'},status=status.HTTP_200_OK)
    user = request.user
    response_data = {}
    
    date = timezone.localdate()
    emission_reminders = []
    for i in range(5):
        month = date.month - 1 - i
        year = date.year
        if month <= 0:
            month = month+12
            year = year -1
        try:
            monthinfo1 =  user.scope1.all().get(year=year,month=month)
            monthinfo2 =  user.scope2.all().get(year=year,month=month)
            if monthinfo1.file1 == 'nofile' or monthinfo2.file2 == 'nofile':
                emission_reminders.append('您还未上传'+str(year)+'年'+str(month)+'月排放数据的证明文件，请尽快上传，否则将影响公司的碳排放认证。')
        except:
            emission_reminders.append('您还未录入'+str(year)+'年'+str(month)+'月的排放数据，请尽快录入。')
    response_data.update({'emissions':emission_reminders})
    #公司介绍和法人信息
    info_reminders = []
    if user.Enterprise_Intro == '':
        info_reminders.append('您还未填写企业介绍信息，请尽快填写。')
    if user.Enterprise_Legalperson == '':
        info_reminders.append('您还未填写企业法人信息，请尽快填写。')
    response_data.update({'info':info_reminders})

    return Response(response_data,status=status.HTTP_200_OK)

# 公司信息筛选器（银行接口）
@api_view(['POST','OPTIONS'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JWTAuthentication,))
def get_info_all(request):
    if request.method == 'OPTIONS':
        return Response({'Msg':'ok'},status=status.HTTP_200_OK)
    user = request.user
    if user.is_Enterprise:
        return Response({'ERROR':'无权限！'},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
    today_ = timezone.localdate()
    #上上个月信息
    month_ = today_.month - 2
    year_ = today_.year
    if month_ <= 0:
        month_ = month_ + 12
        year_ = year_ - 1
    # 获取页码（默认第一页）
    page = int(request.POST.get('page',1))
    #pagelength = int(request.POST.get('pagelength',100))
    pagelength = 1000
    # 获取年月（默认上上个月）
    month = request.POST.get('month')
    year = request.POST.get('year')
    if month == 'null':
        month = month_
    else:
        month = int(month)
    if year == 'null':
        year = year_
    else:
        year = int(year)
    # 获取筛选器（默认没有筛选器）
    certified_ = request.POST.get('certified')
    # 获取排序器（默认排序器是总排放量高到低）
    sortkey_ = request.POST.get('sortkey')
    if sortkey_ == '':
        sortkey_ = 'emission_all'
    ascending_ = request.POST.get('ascending')
    if ascending_ == 'true':
        ascending_bool = True
    else:
        ascending_bool = False
    # 搜索
    searchkey_ = request.POST.get('searchkey')
    if searchkey_ == '':
        searchkey_ = None
    EnModel_all = User.objects.filter(is_Enterprise = True)
    user_data_list = []
    logger.error(str(request.POST))
    #logger.error(certified_)
    #logger.error(type(certified_))
    #logger.error(type(year))
    #logger.error(year)
    for EnModel in EnModel_all:
        try:
            user_scope1 = EnModel.scope1.get(year=year,month=month)
            user_scope2 = EnModel.scope2.get(year=year,month=month)
            user_scope3 = EnModel.scope3.get(year=year,month=month)
            user_offset = EnModel.offset.get(year=year,month=month)
            user_data = month_data_to_dict(user_scope1,user_scope2,user_scope3,user_offset)
            if searchkey_:
                if not (searchkey_ in EnModel.Enterprise_Name):
                    continue
            user_data.update({'Enterprise_name':EnModel.Enterprise_Name,
                              'username':EnModel.username})
            user_data_list.append(user_data)
        except:
            continue
    if certified_ == 'true':
        filtered_user_data_list = list(filter(lambda x: x['certified']=='all',user_data_list))
        sorted_user_data_list = sorted(filtered_user_data_list, key=lambda x: x[sortkey_],reverse = not ascending_bool)
    else:
        sorted_user_data_list = sorted(user_data_list, key=lambda x: x[sortkey_],reverse=not ascending_bool)
    num = len(sorted_user_data_list)
    if num == 0:
        page_max = 0
        final_data = []
    else: 
        page_max = (num // pagelength) + bool(num % pagelength)
        final_data = sorted_user_data_list[pagelength*(page-1):pagelength*page]
    response_data = {'page_max':page_max,
                     'data_num':num,
                     'data':final_data}
    return Response(response_data,status=status.HTTP_200_OK)

# 公司详情页
@api_view(['POST','OPTIONS'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JWTAuthentication,))
def get_enterprise_info(request):
    if request.method == 'OPTIONS':
        return Response({'Msg':'ok'},status=status.HTTP_200_OK)
    user = request.user
    if user.is_Enterprise:
        EnModel = user
    else:
        username_ = str(request.POST.get('username'))
        EnModel=User.objects.get(username = username_)
    month = request.POST.get('month')
    year = request.POST.get('year')
    user_scope1 = EnModel.scope1.get(year=year,month=month)
    user_scope2 = EnModel.scope2.get(year=year,month=month)
    user_scope3 = EnModel.scope3.get(year=year,month=month)
    user_offset = EnModel.offset.get(year=year,month=month)
    response_data_show = month_data_to_dict(user_scope1,user_scope2,user_scope3,user_offset)
    intro_ = EnModel.Enterprise_Intro
    if intro_ == '':
        intro_ = '该公司暂未填写介绍'
    response_data = {
        'Enterprise_Name':EnModel.Enterprise_Name,
        'Enterprise_Intro':intro_,
        'Enterprise_Legalperson':EnModel.Enterprise_Legalperson,
        'username':EnModel.username,
        'email':EnModel.email,
        'show_data':response_data_show}
    return Response(response_data,status=status.HTTP_200_OK)

# 报告下载
@api_view(['POST','OPTIONS'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JWTAuthentication,))
def get_enterprise_report(request):
    if request.method == 'OPTIONS':
        return Response({'Msg':'ok'},status=status.HTTP_200_OK)
    user = request.user
    if user.is_Enterprise:
        EnModel = user
    else:
        username_ = request.POST.get('username')
        EnModel = User.objects.get(username = username_)
    month = int(request.POST.get('month'))
    year = int(request.POST.get('year'))
    user_scope1 = EnModel.scope1.get(year=year,month=month)
    user_scope2 = EnModel.scope2.get(year=year,month=month)
    user_scope3 = EnModel.scope3.get(year=year,month=month)
    user_offset = EnModel.offset.get(year=year,month=month)
    response_data_show = month_data_to_dict_float(user_scope1,user_scope2,user_scope3,user_offset)
    if response_data_show['certified'] != 'all':
        return Response({'ERROR':'排放数据未获得认证，无法生成报告'},status=status.HTTP_202_ACCEPTED)
    history_data = []
    for i in range(5):
        month_h = month - 1 - i
        year_h = year
        if month_h <= 0:
            year_h = year -1
            month_h = month_h + 12
        try:
            user_scope1_h = EnModel.scope1.get(year=year_h,month=month_h)
            user_scope2_h = EnModel.scope2.get(year=year_h,month=month_h)
            user_scope3_h = EnModel.scope3.get(year=year_h,month=month_h)
            user_offset_h = EnModel.offset.get(year=year_h,month=month_h)
            history_data.append(month_data_to_dict_float(user_scope1_h,user_scope2_h,user_scope3_h,user_offset_h))
        except:
            break
    history_num = len(history_data)
    intro_ = EnModel.Enterprise_Intro
    if intro_ == '':
        intro_ = '该公司暂未填写介绍'
    response_data = {
        'Enterprise_Name':EnModel.Enterprise_Name,
        'Enterprise_Intro':intro_,
        'Enterprise_Legalperson':EnModel.Enterprise_Legalperson,
        'username':EnModel.username,
        'email':EnModel.email,
        'show_data':response_data_show,
        'history_num':history_num,
        'history_data':history_data,
    }
    usermonthstr = str((int(response_data['username'])*1000000 + response_data_show['year']*100 + response_data_show['month'])*5)
    with open("./reportlab_fc/info.json", "r") as f:
        old_data = json.load(f)
    if not old_data.get(usermonthstr):
        data2pdf(response_data)
        #重新读取
        with open("./reportlab_fc/info.json", "r") as f:
            old_data = json.load(f)
    randomstr = old_data.get(usermonthstr)
    y_m = str(response_data_show['year']*100+response_data_show['month'])
    url = '/report/'+usermonthstr+randomstr+'/'+y_m+'report.pdf'
    return Response({'loc':url},status=status.HTTP_200_OK)

# 历史数据接口
@api_view(['POST','OPTIONS'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JWTAuthentication,))
def get_history(request):
    if request.method == 'OPTIONS':
        return Response({'Msg':'ok'},status=status.HTTP_200_OK)
    user = request.user
    if user.is_Enterprise:
        EnModel = user
    else:
        username_ = request.POST.get('username')
        EnModel=User.objects.get(username = username_)
    # 获取页码（默认第一页）
    page = int(request.POST.get('page',1))
    pagelength = int(request.POST.get('pagelength',10))
    #logger.error(username_)
    user_scope1_list = EnModel.scope1.all().order_by('-year', '-month')
    user_scope2_list = EnModel.scope2.all().order_by('-year', '-month')
    user_scope3_list = EnModel.scope3.all().order_by('-year', '-month')
    user_offset_list = EnModel.offset.all().order_by('-year', '-month')
    response_data_history = []
    for i in range(len(user_scope1_list)):
        user_scope1 = user_scope1_list[i]
        user_scope2 = user_scope2_list[i]
        user_scope3 = user_scope3_list[i]
        user_offset = user_offset_list[i]
        response_data_history.append(month_data_to_dict(user_scope1,user_scope2,user_scope3,user_offset))
    num = len(response_data_history)
    if num == 0:
        page_max = 0
        final_data = []
    else: 
        page_max = (num // pagelength) + bool(num % pagelength)
        final_data = response_data_history[pagelength*(page-1):pagelength*page]
    response_data = {
        'history_num':num,
        'history_page_max':page_max,
        'history_data':final_data,
    }
    return Response(response_data,status=status.HTTP_200_OK)
