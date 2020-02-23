用户设备API设计
====================


用户设备API
^^^^^^^^^^^^

- 设备情况

 获取设备主页信息

::

        get_user_device_index_info

        参数：
          user_id - 用户id
        返回值：
          device_total_num - 设备总数
          normal_device_num - 正常设备个数
          offline_device_num - 离线设备个数
          alert_device_num - 报警设备个数
          breakdown_device_num - 故障设备个数
          notic - 通知
          normal_device_list - 正常设备列表
          offline_device_list - 离线设备列表
          alert_device_list - 报警设备列表
          breakdown_device_list - 故障设备列表
          ----------------
          device_info:
            code - 设备编码
            name - 设备名称
            model - 设备型号
            address - 地址
            location - 安装位置
            signal - 信号强度
            battery - 电量
            image - 设备图片

- 添加设备

 添加设备

::

   user_opt_device/{user_id}/

   请求方式:
      PUT
   参数：
      device_sn - 设备编码
      name - 设备名称
      address - 地址
      location - 安装位置

      tel_notic - 是否启用电话通知(暂时不用)
      sms_notic - 是否启用短信通知(暂时不用)

   返回值：

- 查看设备状态

 查看设备状态

::

  get_device_detail

  参数：
     device_sn - 设备编码
     user_id

  返回值：
    device_info:
     code - 设备编码
     name - 设备名称
     model - 设备型号
     IMEI - IMEI号
     ICCID - ICCID号
     address - 地址
     location - 安装位置
     signal - 信号强度
     battery - 电量
     image - 设备图片

- 删除设备

  删除设备

::

  user_opt_device/{user_id}/

  请求方式:
     PUT

  参数：
    device_sn - 设备编码

  返回值：

- 修改设备信息

 修改设备信息

::

  update_device_info

  参数：
    code - 设备编码
    name - 设备名称
    address - 地址
    location - 安装位置

  返回值：
