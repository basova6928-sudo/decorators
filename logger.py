import datetime

def logger(old_function):
    
    def new_function(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        all_args = list(args) + [f"{k}={v}" for k, v in kwargs.items()]
        args_str = ", ".join(map(str, all_args))
        result = old_function(*args, **kwargs)
        log_entry = f"{timestamp} | {old_function.__name__} | args={args_str} | return={result}\n"
        with open('main.log', 'a') as f:
            f.write(log_entry)
        return result
    return new_function


def logger_path(path):
    
    def __logger(old_function):
        def new_function(*args, **kwargs):
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            all_args = list(args) + [f"{k}={v}" for k, v in kwargs.items()]
            args_str = ", ".join(map(str, all_args))
            result = old_function(*args, **kwargs)
            log_entry = f"{timestamp} | {old_function.__name__} | args={args_str} | return={result}\n"
            with open(path, 'a') as f:
                f.write(log_entry)
            return result
        return new_function
    return __logger
