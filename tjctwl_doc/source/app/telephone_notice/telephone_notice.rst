火警电话通知API设计
====================


火警电话通知API
^^^^^^^^^^^^^^^

- 获取电话短信通知设备列表

 获取电话短信通知列表

::

  get_device_tel_sms_notice_info

  参数：
    user_id

  返回值：
    device_tel_sms_notice_info_list - 设备电话短信通知设置状态列表
    --------------
    device_tel_sms_notice_info:
      device_sn - 设备ID
      address - 地址
      location - 安装位置
      tele_notice - 是否打开电话通知
      sms_notice - 是否打开短信通知

- 修改电话短信通知

 修改电话短信通知

::

  update_device_tel_sms_notice

  参数：
    device_sn - 设备ID
    tele_notice - 是否打开电话通知
    sms_notice - 是否打开短信通知
  返回值：
