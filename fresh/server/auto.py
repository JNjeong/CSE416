import os
import schedule
import time

# pip install schedule

if __name__ == "__main__":
    schedule.every(2).weeks.do(os.system, "python excel.py prof")
    schedule.every(3).weeks.do(os.system, "python excel.py course_semester")
    schedule.every(1).weeks.do(os.system, "python excel.py qa")
    schedule.every().day.at("00:00:00").do(os.system, "python excel.py allcourse")
    while True:
        schedule.run_pending()
        time.sleep(1)
