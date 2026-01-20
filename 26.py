class Logger:
    log_count = 0

    @classmethod
    def log(cls, message):
        cls.log_count += 1
        print(f"{cls.__name__} Log #{cls.log_count}: {message}")

class FileLogger(Logger):
    pass

Logger.log("系统启动。")
FileLogger.log("打开文件。")
Logger.log("出错！")
FileLogger.log("关闭文件。")