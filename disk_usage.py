import shutil

def check_disk_usage(disk, min_absolute, min_percent):
    # return True if there is enough free disk space, False otherwise.
    du = shutil.disk_usage()
    percent_free = 100 * du.free / du.total
    gigabyte_free = du.free / 2**30
    if precent_free < min_percent or gigabyte_free < min_percent:
        return False
    return True

if not check_disk_usage('F:/',23,30):
    print ('Error: Not enough disk space')
    return 1
print ('Everything ok!')
return 0
