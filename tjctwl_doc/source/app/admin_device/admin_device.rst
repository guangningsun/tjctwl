管理员设备API设计
====================


管理员设备API
^^^^^^^^^^^^

- 设备情况

 获取设备主页信息

::

        get_admin_device_index_info

        参数：

        返回值：
          device_total_num - 设备总数
          connect_unit_num - 联网单位数
          health - 健康值（计算方法待定），如 97%
          normal_device_num - 正常设备个数
          offline_device_num - 离线设备个数
          alert_device_num - 报警设备个数
          breakdown_device_num - 故障设备个数

- 设备报警top5统计

 设备报警top5统计

::

        get_admin_device_top5

        参数：

        返回值：

- 设备总趋势数据

 获取设备总趋势数据，用于绘制统计图

::

        get_admin_device_trend_static

        参数：

        返回值：

- 隐患整改

 获取隐患整改统计信息

::

        get_admin_device_danger_static

        参数：

        返回值：
           danger_todo_num - 待整改个数
           danger_under_num - 整改中个数
           danger_done_num - 整改完毕个数
           danger_reject_num - 驳回个数
           danger_finish_num - 已完成个数
