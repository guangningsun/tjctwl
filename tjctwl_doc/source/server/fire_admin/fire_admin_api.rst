巡检管理 API
^^^^^^^^^^^^

- 增加巡检计划

::

   add_check_plan
   参数：
       计划id
       公司部门名称
       上级部门名称
       创建时间
       创建人
       修改日期

   返回值：


- 删除巡检记录

::

   delete_check_plan
   参数：
      计划id
   
   返回值：



- 查询所有巡检记录

::

   get_check_plan
   
   参数：
    
   返回值：



- 修改巡检记录

::

   update_check_plan_by_id
   
   参数：
       计划id
       公司部门名称
       上级部门名称
       创建时间
       创建人
       修改日期
   
   返回值：



隐患整改 API
^^^^^^^^^^^^



- 新增隐患整改计划

::
  
  create_danger_check_plan
  参数：
  返回值：

- 删除隐患

::

  delete_danger_check_plan
  参数：
  返回值：

- 查询所有隐患

::

  get_all_danger_check_plan
  参数：
  返回值：

- 修改隐患记录

::

  modify_danger_check_plan
  参数：
  返回值：
  

维修保养 API
^^^^^^^^^^^^


- pass （待设备到位后开发）