CREATE TABLE tb_user (
	user_code INT PRIMARY KEY AUTO_INCREMENT ,
	user_studid INT NOT NULL UNIQUE,
	user_name VARCHAR(30) NOT NULL,
	user_id VARCHAR(30) NOT NULL UNIQUE,
	user_pw VARCHAR(30) NOT NULL,
	user_sbuemail VARCHAR(50) NOT NULL,
	user_email VARCHAR(50),
	user_auth INT
);

CREATE TABLE tb_usercourse (
	user_code INT,
	course_code INT,
	CONSTRAINT FOREIGN KEY (user_code) REFERENCES tb_user(user_code),
	CONSTRAINT FOREIGN KEY (course_code) REFERENCES tb_course_schedule(course_code)
);

CREATE TABLE tb_course_schedule (
	course_code INT PRIMARY KEY,
	course_date INT NOT NULL,
	course_start DATE NOT NULL,
	course_end DATE NOT NULL,
	course_room VARCHAR(10) NOT NULL,
	prof_code INT,
	course_number INT NOT NULL UNIQUE,
	CONSTRAINT FOREIGN KEY (prof_code) REFERENCES tb_prof(prof_code)
);

CREATE TABLE tb_course (
	course_code INT,
	course_name VARCHAR(10) NOT NULL,
	course_fullname VARCHAR(100) NOT NULL,
	course_credit INT NOT NULL,
	course_coordinator VARCHAR(30),
	course_info VARCHAR(100),
	course_requirement VARCHAR(200),
	course_outcome VARCHAR(300),
	course_sbc VARCHAR(30),
	
	
	CONSTRAINT FOREIGN KEY (course_code) REFERENCES tb_course_schedule(course_code)
);

CREATE TABLE tb_course_prereq (
	course_code_main INT,
	course_code_pre INT,
	CONSTRAINT FOREIGN KEY (course_code_main) REFERENCES tb_course_schedule(course_code),
	CONSTRAINT FOREIGN KEY (course_code_pre) REFERENCES tb_course_schedule(course_code)
);

CREATE TABLE tb_prof (
	prof_code INT PRIMARY KEY,
	prof_name VARCHAR(30) NOT NULL,
	prof_total_star DOUBLE DEFAULT 0,
	prof_star_cnt INT DEFAULT 0
);

CREATE TABLE tb_prof_comment (
	prof_code INT,
	course_code INT,
	user_code INT,
	comment VARCHAR(300),
	CONSTRAINT FOREIGN KEY (prof_code) REFERENCES tb_prof(prof_code),
	CONSTRAINT FOREIGN KEY (course_code) REFERENCES tb_course_schedule(course_code),
	CONSTRAINT FOREIGN KEY (user_code) REFERENCES tb_user(user_code)
);

CREATE TABLE tb_board (
	board_code INT PRIMARY KEY,
	board_title VARCHAR(200) NOT NULL,
	board_content TEXT,
	board_type VARCHAR(30)
);

CREATE TABLE tb_qa (
	qa_code INT PRIMARY KEY,
	qa_keyword VARCHAR(50) NOT NULL,
	qa_answer VARCHAR(200),
);

CREATE TABLE tb_qgpt(
	qpgt_code INT PRIMARY KEY,
	qpgt_keyword VARCHAR(50) NOT NULL,
	qpgt_question VARCHAR(300)
); 

select * from tb_user;
insert into tb_user ()
