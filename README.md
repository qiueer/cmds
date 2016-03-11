MPort
=========================================
Port Monitor

【配置文件】
-------------------------------------------
    1) #开头的行为注释行
    2) 全局配置
      [system] -- 为section，system为section名，section名必须为system
      groups  -- system section下必须包含groups配置项，用于指定使用哪些组
    3) 除了system section外其他section
      以[esf list]为例，esf为section名，用在groups参数，可以随意取，但不能包含空格（tab），list为section类型，保持list不变即可
      esf section下每一行都是监控配置项，其中hosts为主机列表，主机列表之间通过,分割；port端口；module模块名；mails告警接收人列表，以，分割；

【用法示例】
--------------------------------------------
    1) -f参数，指定配置文件路径，同时相对路径、绝对路径
      cd ${your_script_dir}
      python mport.py -f ${your_conf_file_path}

    2)-f参数同1)所述；-g参数，指定使用配置文件中哪些组
      cd ${your_script_dir}
      python mport.py -f ${your_conf_file_path} -g ${your_groups}

    3)-f参数同1)所述；-g参数，指定使用配置文件中哪些组；-i install将该脚本安装到crontab
      cd ${your_script_dir}
      python mport.py -f ${your_conf_file_path} -g ${your_groups} -i 

【crontab定时任务】-- 参考
-------------------------
    */1 * * * * cd /home/qiujqin/monitors/port_monitor && python mport.py  -f etc/dest/esf.conf -g production >/tmp/mport.py.log 2>&1

【如何使用】 -- 示例
---------------------------------
    #配置邮件服务器等信息
    cp  etc/config.py.example  etc/config.py
    vi etc/config.py
    
    #添加/配置需要监控的主机或IP、端口、模块、告警接收人等
    cd etc/conf/dest
    cp monitor.conf.example monitor.conf
    vi monitor.conf
    
    #测试、使用，以及安装
    python  mport.py -f etc/conf/dest/monitor.conf
    python  mport.py -f etc/conf/dest/monitor.conf -i
