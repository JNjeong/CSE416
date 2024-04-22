# pip install xlrd
# pip install openpyxl
# pip install pandas
# pip install pymysql

# https://devpouch.tistory.com/196

import pandas as pd
import sys
import pymysql
import math 

def checkNaN(element):
    return 'N/A' if math.isnan(element) else element


def db_save (field, dataset):
    sql_insert_courses="""insert into tb_course (course_name, course_fullname, course_credit, course_coordinator, course_info, course_prereq, course_outcome, course_requirement, course_sbc) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    sql_insert_prof = """insert into tb_prof (prof_name, prof_office, prof_contact, prof_email) values (%s,%s,%s,%s)"""

    if field == 'all':
        print('arg = all')
        for elem in [df_CSE, df_ESE, df_EST, df_MEC, df_BM, df_AMS, df_prof]:
            print('all')
            
    elif field == 'cse':
        for i in range(len(dataset[0])):
            course_elem = dataset[0].loc[i]
            cursor.execute(sql_insert_courses, 
                           (
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
        print('### LOG : successfully added to the database!!!')
        

    elif field == 'ese':
        for i in range(len(dataset[1])):
            course_elem = dataset[1].loc[i]
            cursor.execute(sql_insert_courses, 
                           (
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
        print('### LOG : successfully added to the database!!!')
        
        
    elif field == 'est':
        for i in range(len(dataset[2])):
            course_elem = dataset[2].loc[i]
            cursor.execute(sql_insert_courses, 
                           (
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
        print('### LOG : successfully added to the database!!!')
        

    elif field == 'mec':
        for i in range(len(dataset[3])):
            course_elem = dataset[3].loc[i]
            cursor.execute(sql_insert_courses, 
                           (
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
        print('### LOG : successfully added to the database!!!')
        

    elif field == 'bm':
        for i in range(len(dataset[4])):
            course_elem = dataset[4].loc[i]
            cursor.execute(sql_insert_courses, 
                           (
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
        print('### LOG : successfully added to the database!!!')
        
        
    elif field == 'ams':
        for i in range(len(dataset[5])):
            course_elem = dataset[5].loc[i]
            cursor.execute(sql_insert_courses, 
                           (
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
        print('### LOG : successfully added to the database!!!')
        
        
    elif field == 'prof':
        for i in range (len(dataset[6])):        
            prof_elem = dataset[6].loc[i]
            cursor.execute(sql_insert_prof,
                        (str(prof_elem['prof_name']).split('\n')[0],
                            str(prof_elem['prof_office']).split('\n')[0],
                            str(prof_elem['prof_contact']).split('\n')[0],
                            str(prof_elem['prof_email']).split('\n')[0])
                        )
        print('### LOG : successfully added to the database!!')

if __name__ == "__main__":

    course_list = 'courses.xlsx'
    prof_list = 'professors.xlsx'

    df_CSE = pd.read_excel(course_list, sheet_name='CSE')
    df_ESE = pd.read_excel(course_list, sheet_name='ESE')
    df_EST = pd.read_excel(course_list, sheet_name='EST')
    df_MEC = pd.read_excel(course_list, sheet_name='MEC')
    df_BM = pd.read_excel(course_list, sheet_name='BM')
    df_AMS = pd.read_excel(course_list, sheet_name='AMS')
    df_prof = pd.read_excel(prof_list)

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)

    # set up connection
    db = pymysql.connect(host='127.0.0.1', user='root', password='0000', db='mysql', charset='utf8')
    cursor = db.cursor()
    sql_select = 'select * from tb_courses'

    # result= cursor.fetchall() use this only select


    args = sys.argv
    if len(args) <= 1 :
        print('args = 0 ')
        # db saves all
    
    elif len(args) == 2 : 
        db_save(args[1], [df_CSE,df_ESE,df_EST,df_MEC,df_BM,df_AMS,df_prof])
        #cursor.execute('select * from tb_test;')
        #result = cursor.fetchall()
        #print(result)

    db.commit()
    db.close()
    


    #cursor.execute(sql)
        

        



    # print(df_CSE)
    # print(df_CSE['course_name'])
    # print(df_CSE[0:3])
