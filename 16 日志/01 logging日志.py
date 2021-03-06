import logging
""" 日志级别 """
# debug info warning error critical
# 日志等级说明:
# DEBUG:程序调试bug时使用
# INFO∶程序正常运行时使用
# WARNING∶程序未按预期运行时使用﹐但并不是错误﹐如:用户登录密码错误ERROR︰程序出错误时使用﹐如:IO操作失败
# CRITICAL︰特别严重的问题﹐导致程序不能再继续运行时使用﹐如:磁盘空间为空﹐一般很少使用默认的是WARNING等级﹐当在WARNING或WARNING之上等级的才记录日志信息·
# 日志等级从低到高的顺序是:DEBUG< INFO < WARNING < ERROR < CRITICAL

""" logging日志的使用 """
# 输出到控制台
logging.debug('这是一个 debug 级别的日志信息')
logging.info('这是一个 info 级别的日志信息')
logging.warning('这是一个 warning 级别的日志信息')
logging.error('这是一个 error 级别的日志信息')
logging.critical('这是一个 critical 级别的日志信息')
只有大于等于warning才会显示
print('###############')
""" 设置日志配置信息 """
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(threadName)s:%(levelname)s %(message)s',
    filename="logging.txt",
    filemode='a',
    encoding='utf8'
)  # 必须先配置,这样直接运行会有bug
# 设置logging日志的配置信息
# #level表示设置级别
# %( asctime)s表示当前时问
# %( filename)s表示程序文件名
# %( lineno)d 表示行号
# % ( levelname)s表示日志级别
# #% ( message)s表示日志信息

logging.debug('这是一个 debug 级别的日志信息')
logging.info('这是一个 info 级别的日志信息')
logging.warning('这是一个 warning 级别的日志信息')
logging.error('这是一个 error 级别的日志信息')
logging.critical('这是一个 critical 级别的日志信息')
