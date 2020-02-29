管理员施工安装API设计
====================


管理员施工安装API
^^^^^^^^^^^^

施工绑定只能一次绑定一个业主信息，绑定多个业主的话需要再次进行绑定操作。
客户端扫码后，或者输入设备编码后，马上查询当前设备信息，如果没有该设备的绑定信息的话，进行绑定操作，有的话就把信息展示，只能添加业主信息。

- 安装设备列表

 获取安装设备列表信息

::

        get_admin_install_list

        参数：
          start_index - 设备起始索引，传 "0" 表示从第一个开始查
          num - 步长，即每次查询的个数，用于分页查询 (默认 20)
          device_sn - 设备编码（条件查询，可选）

        返回值：
        install_info_list - 安装设备列表信息
        --------------
        install_info:
          id - 施工id
          date - 施工时间
          device_status - 设备状态
          img_url - 设备图片
          device_sn - 设备编码
          device_name - 设备名称
          worker - 施工人员
          device_type - 设备型号
          owner_name - 业主姓名
          ower_tel - 业主电话
          address - 地址
          location - 安装位置
          map_location - 地图位置
          install_photo - 安装图片

- 添加施工安装设备

 添加施工安装设备

::

   add_install

   参数：
      device_sn - 设备编码
      device_name - 设备名称
      device_type - 设备型号
      owner_name - 业主姓名
      ower_tel - 业主电话
      address - 地址
      location - 安装位置
      map_location - 地图位置
      install_photo - 安装图片
      date - 安装时间

   返回值：

- 更新施工安装设备

  更新施工安装设备，重装

::

  update_install

  参数：
     id - 施工id
     device_sn - 设备编码
     device_name - 设备名称
     owner_name - 业主姓名
     ower_tel - 业主电话
     address - 地址
     location - 安装位置
     map_location - 地图位置
     install_photo - 安装图片
     date - 安装时间

  返回值：

- 查询施工安装设备

  通过设备code查询施工安装设备

::

  get_install_by_device_sn

  参数：
     device_sn - 设备编码

  返回值：
    id - 施工id
    date - 施工时间
    device_status - 设备状态
    img_url - 设备图片
    device_sn - 设备编码
    device_name - 设备名称
    worker - 施工人员
    device_type - 设备型号
    owner_name - 业主姓名
    ower_tel - 业主电话
    address - 地址
    location - 安装位置
    map_location - 地图位置
    install_photo - 安装图片
