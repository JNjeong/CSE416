# pip install xlrd
# pip install openpyxl
# pip install pandas
# pip install pymysql

# https://devpouch.tistory.com/196

import pandas as pd
import sys
import pymysql
import math

"""

def res_convert_to_array(ret_db):
    ret_db = str(ret_db)
    ret_db = ret_db.replace('((', '')
    ret_db = ret_db.replace('))', '')
    ret_db = ret_db.split(', ')
    return ret_db


db = pymysql.connect(host='127.0.0.1', user='root', password='0000', db='mysql', charset='utf8')
cursor = db.cursor()
sql_select = 'select * from tb_courses where course_name = %s'
cursor.execute(sql_select)
res = cursor.fetchall()
res = res_convert_to_array(res)
"""



def res_convert_to_array(ret_db):
    ret_db = str(ret_db)
    ret_db = ret_db.replace('((', '')
    ret_db = ret_db.replace('))', '')
    ret_db = ret_db.split(', ')
    return ret_db

def nan_converter(*args):
    if args == 'nan':
        return ' '
    else : return args

def db_save (field, datasets):
    sql_insert_courses="""insert into tb_course (course_name, course_fullname, course_credit, course_coordinator, course_info, course_prereq, course_outcome, course_requirement, course_sbc) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    sql_insert_prof = """insert into tb_prof (prof_name, prof_office, prof_contact, prof_email) values (%s,%s,%s,%s)"""
    sql_insert_qa = """insert into tb_qa (qa_keyword, qa_answer) values (%s,%s)"""
    sql_insert_course_semester = """insert into tb_course_schedule (course_code, course_date, course_start, course_end, course_room, course_prof, course_number) values (%s,%s,%s,%s,%s,%s,%s)"""
    sql_insert_temp_courses= """insert into tb_course (course_name, course_fullname, course_credit, course_sbc) values (%s,%s,%s,%s)"""
    sql_select_course = """select * from tb_course where course_name=%s"""
    sql_select_prof = """select * from tb_prof where prof_name=%s"""
    sql_select_qa = """select * from tb_qa where qa_keyword=%s"""
    sql_select_course_code = """select course_code from tb_course where course_name = %s"""
    sql_update_courses = """update tb_course set course_fullname=%s, course_credit=%s, course_coordinator=%s, course_info=%s, course_prereq=%s, course_outcome=%s, course_requirement=%s, course_sbc=%s where course_name=%s"""
    sql_update_prof = """update tb_prof set prof_office=%s, prof_contact=%s, prof_email=%s where prof_name=%s"""
    sql_update_qa = """update tb_qa set qa_answer=%s where qa_keyword=%s"""
    sql_delete_course_semester = """delete from tb_course_schedule"""
    

    if field == 'allcourse':
        datasets_courses = datasets[2:len(datasets)-2]
        for dataset in datasets_courses:
            for i in range(len(dataset)):
                course_elem = dataset.loc[i]
                cursor.execute(sql_select_course, (str(course_elem['course_name']).split('\n')[0]))
                course_result = cursor.fetchall()
                course_result = res_convert_to_array(course_result)

                if len(course_result) <= 1:
                    cursor.execute(sql_insert_courses, (
                        str(course_elem['course_name']).split('\n')[0],
                        str(course_elem['course_fullname']).split('\n')[0],
                        str(course_elem['course_credit']).split('\n')[0],
                        str(course_elem['course_coordinator']).split('\n')[0],
                        str(course_elem['course_info']).split('\n')[0],
                        str(course_elem['course_prereq']).split('\n')[0],
                        str(course_elem['course_outcome']).split('\n')[0],
                        str(course_elem['course_requirement']).split('\n')[0],
                        str(course_elem['course_sbc']).split('\n')[0]
                    ))
                else : 
                    cursor.execute(sql_update_courses,(
                        str(course_elem['course_fullname']).split('\n')[0],
                        str(course_elem['course_credit']).split('\n')[0],
                        str(course_elem['course_coordinator']).split('\n')[0],
                        str(course_elem['course_info']).split('\n')[0],
                        str(course_elem['course_prereq']).split('\n')[0],
                        str(course_elem['course_outcome']).split('\n')[0],
                        str(course_elem['course_requirement']).split('\n')[0],
                        str(course_elem['course_sbc']).split('\n')[0],
                        str(course_elem['course_name']).split('\n')[0]
                    ))

    elif field =='course_semester':
        cursor.execute(sql_delete_course_semester)
        cursor.fetchall()
        for n in range(len(datasets[0])):
            dataset = datasets[0][n]
            for i in range(1, len(dataset)):
                course_semester_elem = dataset.loc[i]
                if n == 0:
                    course_name = (str(course_semester_elem[1])+str(course_semester_elem[3]))
                elif n == 1 or n == 2: 
                    course_name = (str(course_semester_elem[1])+str(course_semester_elem[4]))
                elif n == 3 :
                    course_name = (str(course_semester_elem[1])+str(course_semester_elem[2]))
                    
                cursor.execute(sql_select_course_code, (course_name.split('.')[0]))
                course_semester_code_result = cursor.fetchall()
                
                if len(course_semester_code_result) <= 0:
                    if n==0 : 
                        cursor.execute(sql_insert_temp_courses, (
                            nan_converter((str(course_semester_elem[1])+str(course_semester_elem[3]).split('.')[0])),
                            nan_converter(str(course_semester_elem[4])), 
                            nan_converter(str(course_semester_elem[9])), 
                            nan_converter(str(course_semester_elem[5]))
                            ))
                    elif n==1:
                        cursor.execute(sql_insert_temp_courses, (
                            nan_converter((str(course_semester_elem[1])+str(course_semester_elem[4]).split('.')[0])), 
                            nan_converter(str(course_semester_elem[5])), 
                            nan_converter(str(course_semester_elem[9])), 
                            nan_converter(str(course_semester_elem[6]))
                            ))
                    elif n==2:
                        cursor.execute(sql_insert_temp_courses, (
                            nan_converter((str(course_semester_elem[1])+str(course_semester_elem[4]).split('.')[0])), 
                            nan_converter(str(course_semester_elem[5])), 
                            nan_converter(str(course_semester_elem[9])), 
                            nan_converter(str(course_semester_elem[6]))
                            )) 
                    elif n==3:
                        cursor.execute(sql_insert_temp_courses, (
                            nan_converter((str(course_semester_elem[1])+str(course_semester_elem[2]).split('.')[0])), 
                            nan_converter(str(course_semester_elem[4])), 
                            nan_converter(str(course_semester_elem[9])), 
                            nan_converter(str(course_semester_elem[6]))
                            ))

                elif len(course_semester_code_result) > 0 :
                    if str(course_semester_elem[0]) == 'nan' : continue
                    cursor.execute(sql_insert_course_semester , (
                        str(course_semester_code_result[0][0]),
                        str(course_semester_elem[10]),
                        str(course_semester_elem[11]),
                        str(course_semester_elem[12]),
                        str(course_semester_elem[13]),
                        str(course_semester_elem[14]),
                        str(course_semester_elem[0])
                    ))

    elif field == 'qa':
        for i in range(len(datasets[1])):
            qa_elem = datasets[1].loc[i]
            print('@@@@@@@', qa_elem)
            cursor.execute(sql_select_qa, (str(qa_elem['qa_keyword']).split('\n')[0]))
            qa_result = cursor.fetchall()
            qa_result = res_convert_to_array(qa_result)
            print('##########', qa_result)
            if len(qa_result) <= 1:
                cursor.execute(sql_insert_qa, (
                    str(qa_elem['qa_keyword']).split('\n')[0],
                    str(qa_elem['qa_answer']).split('\n')[0]
                ))
            else :
                cursor.execute(sql_update_qa,(
                    str(qa_elem['qa_answer']).split('\n')[0],
                    str(qa_elem['qa_keyword']).split('\n')[0]
                ))
    elif field == 'prof':
        for i in range (len(datasets[len(datasets)-1])):        
            prof_elem = datasets[len(datasets)-1].loc[i]
            cursor.execute(sql_select_prof, (str(prof_elem['prof_name']).split('\n')[0]))
            prof_result = cursor.fetchall()
            prof_result = res_convert_to_array(prof_result)
            if len(prof_result) <= 1:
                cursor.execute(sql_insert_prof,(
                    str(prof_elem['prof_name']).split('\n')[0],
                    str(prof_elem['prof_office']).split('\n')[0],
                    str(prof_elem['prof_contact']).split('\n')[0],
                    str(prof_elem['prof_email']).split('\n')[0]
                ))
            else : 
                cursor.execute(sql_update_prof, (
                    str(prof_elem['prof_office']).split('\n')[0],
                    str(prof_elem['prof_contact']).split('\n')[0],
                    str(prof_elem['prof_email']).split('\n')[0],
                    str(prof_elem['prof_name']).split('\n')[0]
                ))
            
    else : 
        if field == 'cse': dataset = datasets[2]
        elif field == 'ese': dataset = datasets[3]
        elif field == 'est': dataset = datasets[4]
        elif field == 'mec': dataset = datasets[5]
        elif field == 'bm': dataset = datasets[6]    
        elif field == 'ams': dataset = datasets[7]
        elif field == 'car': dataset = dataset[8]
        elif field == 'chi': dataset = dataset[9]
        elif field == 'phy': dataset = dataset[10]
        elif field == 'kor': dataset = dataset[11]
        elif field == 'mat': dataset = dataset[12]
        elif field == 'geo': dataset = dataset[13]
        elif field == 'esg': dataset = dataset[14]
        elif field == 'pol': dataset = dataset[15]
        elif field == 'soc': dataset = dataset[16]
        elif field == 'arh': dataset = dataset[17]
        elif field == 'his': dataset = dataset[18]
        elif field == 'phi': dataset = dataset[19]
        elif field == 'sus': dataset = dataset[20]
        elif field == 'eco': dataset = dataset[21]
        elif field == 'com': dataset = dataset[22]
        elif field == 'atm': dataset = dataset[23]
        elif field == 'ars': dataset = dataset[24]
        elif field == 'mus': dataset = dataset[25]
        elif field == 'spn': dataset = dataset[26]
        elif field == 'flm': dataset = dataset[27]
        elif field == 'elp': dataset = dataset[28]

        
        for i in range(len(dataset)):
            course_elem = dataset.loc[i]
            
            cursor.execute(sql_select_course, (str(course_elem['course_name']).split('\n')[0]))
            course_result=cursor.fetchall()
            course_result = res_convert_to_array(course_result)
            print(course_result)
            if len(course_result) <= 1:
                cursor.execute(sql_insert_courses, (
                    str(course_elem['course_name']).split('\n')[0],
                    str(course_elem['course_fullname']).split('\n')[0],
                    str(course_elem['course_credit']).split('\n')[0],
                    str(course_elem['course_coordinator']).split('\n')[0],
                    str(course_elem['course_info']).split('\n')[0],
                    str(course_elem['course_prereq']).split('\n')[0],
                    str(course_elem['course_outcome']).split('\n')[0],
                    str(course_elem['course_requirement']).split('\n')[0],
                    str(course_elem['course_sbc']).split('\n')[0]
                ))
            else :
                cursor.execute(sql_update_courses, (
                    str(course_elem['course_fullname']).split('\n')[0],
                    str(course_elem['course_credit']).split('\n')[0],
                    str(course_elem['course_coordinator']).split('\n')[0],
                    str(course_elem['course_info']).split('\n')[0],
                    str(course_elem['course_prereq']).split('\n')[0],
                    str(course_elem['course_outcome']).split('\n')[0],
                    str(course_elem['course_requirement']).split('\n')[0],
                    str(course_elem['course_sbc']).split('\n')[0],
                    str(course_elem['course_name']).split('\n')[0]
                ))


if __name__ == "__main__":

    course_list = 'courses.xlsx'
    course_list2 = 'courses2.xlsx'
    prof_list = 'professors.xlsx'
    course_semester = 'course_semester.xlsx'
    qa_list = 'qa.xlsx'

    df_COURSE_SEMSETER1 = pd.read_excel(course_semester, sheet_name='Table 1')
    df_COURSE_SEMSETER2 = pd.read_excel(course_semester, sheet_name='Table 2')
    df_COURSE_SEMSETER3 = pd.read_excel(course_semester, sheet_name='Table 3')
    df_COURSE_SEMSETER4 = pd.read_excel(course_semester, sheet_name='Table 4')
    df_COURSE_SEMESTERS = [df_COURSE_SEMSETER1,df_COURSE_SEMSETER2,df_COURSE_SEMSETER3,df_COURSE_SEMSETER4]
    df_QA = pd.read_excel(qa_list, sheet_name='QA')

    df_CSE = pd.read_excel(course_list, sheet_name='CSE')
    df_ESE = pd.read_excel(course_list, sheet_name='ESE')
    df_EST = pd.read_excel(course_list, sheet_name='EST')
    df_MEC = pd.read_excel(course_list, sheet_name='MEC')
    df_BM = pd.read_excel(course_list, sheet_name='BM')
    df_AMS = pd.read_excel(course_list, sheet_name='AMS')

    df_CAR = pd.read_excel(course_list, sheet_name ='CAR')
    df_CHI = pd.read_excel(course_list, sheet_name ='CHI')
    df_PHY = pd.read_excel(course_list, sheet_name ='PHY')
    df_KOR = pd.read_excel(course_list, sheet_name ='KOR')
    df_MAT = pd.read_excel(course_list, sheet_name ='MAT')
    df_GEO = pd.read_excel(course_list, sheet_name ='GEO')
    df_ESG = pd.read_excel(course_list, sheet_name ='ESG')
    df_POL = pd.read_excel(course_list, sheet_name ='POL')
    df_SOC = pd.read_excel(course_list, sheet_name ='SOC')
    df_ARH = pd.read_excel(course_list2, sheet_name ='ARH')
    df_HIS = pd.read_excel(course_list2, sheet_name ='HIS')
    df_PHI = pd.read_excel(course_list2, sheet_name ='PHI')
    df_SUS = pd.read_excel(course_list2, sheet_name ='SUS')
    df_ECO = pd.read_excel(course_list2, sheet_name ='ECO')
    df_COM = pd.read_excel(course_list2, sheet_name ='COM')
    df_ATM = pd.read_excel(course_list2, sheet_name ='ATM')
    df_ARS = pd.read_excel(course_list2, sheet_name ='ARS')
    df_MUS = pd.read_excel(course_list2, sheet_name ='MUS')
    df_SPN = pd.read_excel(course_list2, sheet_name ='SPN')
    df_FLM = pd.read_excel(course_list2, sheet_name ='FLM')
    df_ELP = pd.read_excel(course_list2, sheet_name ='ELP')
    df_prof = pd.read_excel(prof_list)

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)

    # set up connection
    db = pymysql.connect(host='127.0.0.1', user='root', password='0000', db='mysql', charset='utf8')
    cursor = db.cursor()
    sql_select = 'select * from tb_courses'

    # result= cursor.fetchall() use this only select


    args = sys.argv
    if len(args) < 2 :
        print("Please enter one of following options(allcourse, course_semester, qa, cse, ese, est, mec, bm, ams, car, chi, phy, cor, mat, geo, esg, pol, soc, arh, his, phi, sus, eco, com atm, ars, mus, spn, flm, elp, prof).")
        print("※all course automatically insert or update all courses listed above.")
    

    elif len(args) == 2 : 
        db_save(args[1], [df_COURSE_SEMESTERS, df_QA, df_CSE,df_ESE,df_EST,df_MEC,df_BM,df_AMS,df_CAR, df_CHI, df_PHY, df_KOR, df_MAT, df_GEO, df_ESG, df_POL, df_SOC, df_ARH, df_HIS, df_PHI, df_SUS, df_ECO, df_COM, df_ATM, df_ARS, df_MUS, df_SPN, df_FLM, df_ELP, df_prof])

    db.commit()
    db.close()
    

