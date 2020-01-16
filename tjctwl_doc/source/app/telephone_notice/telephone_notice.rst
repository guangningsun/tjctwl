火警电话通知API设计
====================


火警电话通知API
^^^^^^^^^^^^^^^

- 获取电话号码列表

 获取电话号码列表

::

   get_telephone_list

   参数：

   返回值：
   telephone_list - 电话号码列表

- 添加电话号码

 添加电话号码

::

   add_telephone

   参数：
      telephone - 电话号码

   返回值：

- 删除电话号码

  删除电话号码

::

  delete_telephone
  参数：
     telephone - 电话号码

  返回值：

- 修改电话号码

 修改电话号码

::

  update_telephone
  参数：
     telephone - 电话号码

  返回值：

- 获取电话短信通知设备列表

 获取电话短信通知列表

::

  get_device_tel_sms_notice_info

  参数：

  返回值：
    device_tel_sms_notice_info_list - 设备电话短信通知设置状态列表
    --------------
    device_tel_sms_notice_info:
      device_id - 设备ID
      address - 地址
      location - 安装位置
      tele_notice - 是否打开电话通知
      sms_notice - 是否打开短信通知

- 修改电话短信通知

 修改电话短信通知

::

  update_device_tel_sms_notice

  参数：
    device_id - 设备ID
    tele_notice - 是否打开电话通知
    sms_notice - 是否打开短信通知
  返回值：
