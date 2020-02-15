# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
import json
import time
from AppModel.models import *
from django.db.models import Avg, Count, Min, Sum
import xlrd
import uuid
from collections import OrderedDict
import hashlib
import urllib
import random
import logging
import requests
import base64
from django.http import JsonResponse

logger = logging.getLogger(__name__)


# 内部方法，用于获取当前时间戳
# done
def _get_timestamp():
    return int(round(time.time()*1000))


# 内部方法用于返回json消息
# done
def _generate_json_message(flag, message):
    if flag:
        return HttpResponse("{\"error\":0,\"msg\":\""+message+"\"}",
                            #content_type="application/x-www-form-urlencoded",
                            content_type='application/json',
                            )
    else:
        return HttpResponse("{\"error\":1,\"msg\":\""+message+"\"}",
                            #content_type="application/x-www-form-urlencoded",
                            content_type='application/json',
                            )


# 内部方法用于将对象返回值转换成json串
# done
def _generate_json_from_models(response_list):
    return HttpResponse(json.dumps(response_list),
                        #content_type="application/x-www-form-urlencoded",
                        content_type='application/json',
                        )
#                      content_type="application/json")



def user_login(request):
    # import pdb;pdb.set_trace()
    if request.POST:
        context = {}
        login_username = request.POST['username']
        login_password = request.POST['password']
        try:
            if login_username:
                user_info = UserInfo.objects.get(username=login_username)
            if user_info is not None:
                if user_info.password == login_password:
                    dict_tmp = {}
                    dict_tmp.update(user_info.__dict__)
                    dict_tmp.pop("_state", None)
                    res_data = {"error": 0, "msg": dict_tmp}
                    return _generate_json_from_models(res_data)

                else:
                    return _generate_json_message(False, "username or password doesn`t match")
        except:
            return _generate_json_message(False, "login false")


def remove_payment_class(request):
    context = {}
    try:
        payment_class_ids = request.POST['payment_class_ids']
        for payment_class_id in class_ids.split(","):
            payment_class_info = PaymentClassInfo.objects.get(payment_class_id=payment_class_id)
            payment_class_info.delete()
        return _generate_json_message(True, "Remove payment class Success")
    except:
        return _generate_json_message(True, "Remove payment class Success")


def get_all_payment_class_info(request):
    list_response = []
    list_payment_class = PaymentClassInfo.objects.all()
    for res in list_payment_class:
        dict_tmp = {}
        dict_tmp.update(res.__dict__)
        dict_tmp.pop("_state", None)
        list_response.append(dict_tmp)
    return _generate_json_from_models(list_response)



# 初始化登录界面
def init_web(request):
    return render(request, '/admin')


