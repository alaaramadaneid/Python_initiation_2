import shutil

def check_disk_space():
    total, used, free = shutil.disk_usage("/")

    total_gb = total / (2**30)  
    used_gb = used / (2**30)
    free_gb = free / (2**30)

    print("Total Disk Space:", total_gb, "GB")
    print("Used Disk Space:", used_gb, "GB")
    print("Free Disk Space:", free_gb, "GB")

check_disk_space()
