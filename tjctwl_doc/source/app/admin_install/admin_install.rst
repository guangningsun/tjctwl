管理员施工安装API设计
====================


管理员施工安装API
^^^^^^^^^^^^

- 安装设备列表

 获取安装设备列表信息

::

        get_admin_install_list

        参数：
          start_index - 设备起始索引，传 "0" 表示从第一个开始查
          num - 步长，即每次查询的个数，用于分页查询 (默认 20)
          device_code - 设备编码（条件查询，可选）

        返回值：
        install_info_list - 安装设备列表信息
        --------------
        install_info:
          status - 施工状态
          date - 施工时间
          device_status - 设备状态
          img_url - 设备图片
          device_code - 设备编码
          device_name - 设备名称
          worker - 施工人员

- 添加施工安装设备

 添加施工安装设备

::

   add_install

   参数：
      device_code - 设备编码
      device_name - 设备名称
      device_type - 设备型号
      owner_name - 业主姓名
      ower_tel - 业主电话
      address - 地址
      detailed_address - 详细地址
      location - 安装位置
      map_location - 地图位置
      install_photo - 安装图片

   返回值：

- 更新施工安装设备

  更新施工安装设备，重装

::

  update_install

  参数：
     device_code - 设备编码
     device_name - 设备名称
     device_type - 设备型号
     owner_name - 业主姓名
     ower_tel - 业主电话
     address - 地址
     detailed_address - 详细地址
     location - 安装位置
     map_location - 地图位置
     install_photo - 安装图片

  返回值：