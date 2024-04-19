import psutil

def display_memory_usage():
    memory = psutil.virtual_memory()
    
    total_memory = memory.total
    
    available_memory = memory.available
    
    used_memory = memory.used
    

    memory_percent = memory.percent
    

    print("Total Memory:", total_memory / (1024 * 1024), "MB")
    print("Available Memory:", available_memory / (1024 * 1024), "MB")
    print("Used Memory:", used_memory / (1024 * 1024), "MB")
    print("Memory Usage Percentage:", memory_percent, "%")


display_memory_usage()
