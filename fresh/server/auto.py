import os
import schedule
import time

# pip install schedule
# pip install os

# application 이동 필요
if __name__ == "__main__":
    schedule.every(2).weeks.do(os.system, "python excel.py prof")
    schedule.every(3).weeks.do(os.system, "python excel.py course_semester")
    schedule.every(1).weeks.do(os.system, "python excel.py qa")
    schedule.every().day.at("00:30:00").do(os.system, "python excel.py allcourse")
    schedule.every().day.at("00:00:00").do(os.system, "python drivedownload_coursesem.py")
    schedule.every().day.at("00:00:00").do(os.system, "python drivedownload_courses.py")
    schedule.every().day.at("00:00:00").do(os.system, "python drivedownload_courses2.py")
    schedule.every().day.at("00:00:00").do(os.system, "python drivedownload_professors.py")
    schedule.every().day.at("00:00:00").do(os.system, "python drivedownload_qa.py")
    schedule.every().day.at("00:00:00").do(os.system, "python drivedownload_qgpt.py")
    while True:
        schedule.run_pending()
        time.sleep(1)
