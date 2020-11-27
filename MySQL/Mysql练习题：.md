Mysql练习题：
Student(S#,Sname,Sage,Ssex) 学生表

S#	Sanme	Sage	ssex
1001	aa	10	1
1002	Bb	20	1

SC(id#,S#,C#,score) 成绩表
Id#	S#	C#	score
1	1001	001	90
2	1001	002	95
3	1001	003	50
4	1002	001	95
5	1002	002	70

Course(C#,Cname) 课程表
C#	cname
001	java
002	Mysql
003	oracle

Teacher(T#,Tname) 教师表
CT(C#,T#) 课程+教师的关联表
USE test;

constraint c_id foreign key(tid)  references course(cid);
创建表时，添加外键。
alter table teacher add constraint t_c_id foreign key(tid)  references  course(cid);
创建表后添加外键。

CREATE TABLE Student(
  sid INT PRIMARY KEY AUTO_INCREMENT,
 s_cid int ,
constraint c_id foreign key(s_cid)  references course(cid),
  sname VARCHAR(50),
  sage INT,
  ssex VARCHAR(4)
);

INSERT INTO Student VALUES(1,2000,'张三1',25,'男');
INSERT INTO Student VALUES(2,2001,'张三2',29,'女');
INSERT INTO Student VALUES(3,2002,'张三3',30,'女');
INSERT INTO Student VALUES(4,2003,'张三4',15,'男');
INSERT INTO Student VALUES(5,2004,'张三5',5,'男');

INSERT INTO Student VALUES(1,2000,'张三1',25,'男'),
(2,2001,'张三2',29,'女'),
(3,2002,'张三3',30,'女'),
(4,2003,'张三4',15,'男'),
(5,2004,'张三5',5,'男');

CREATE TABLE Course(
  cid INT PRIMARY KEY AUTO_INCREMENT,
  cname VARCHAR(50)
);

INSERT INTO Course VALUES(2000,'java');
INSERT INTO Course VALUES(2001,'mysql');
INSERT INTO Course VALUES(2002,'oracle');
INSERT INTO Course VALUES(2003,'html');
INSERT INTO Course VALUES(2004,'javaEE');


INSERT INTO Course VALUES(2004,'javaEE'),
			(2003,'html'),
			(2002,'oracle'),
			(2001,'mysql'),
			(2000,'java');



CREATE TABLE sc(
  id INT PRIMARY KEY AUTO_INCREMENT,
  sid INT,
constraint sc_sid foreign key(sid)  references student(sid),
  cid INT,
constraint sc_cid foreign key(cid)  references course(cid),
  score DECIMAL(4,1)
);

INSERT INTO sc VALUES(1,1000,2000,90);
INSERT INTO sc VALUES(2,1000,2001,80);
INSERT INTO sc VALUES(3,1001,2000,85);
INSERT INTO sc VALUES(4,1002,2000,70);
INSERT INTO sc VALUES(5,1003,2003,100);
INSERT INTO sc VALUES(6,1002,2001,65);
INSERT INTO sc VALUES(7,1001,2001,85);

INSERT INTO sc VALUES(1,1000,2000,90),
(2,1000,2001,80),
(3,1001,2000,85),
(4,1002,2000,70),
(5,1003,2003,100),
(6,1002,2001,65),
(7,1001,2001,85);

CREATE TABLE Teacher(
  tid INT PRIMARY KEY AUTO_INCREMENT,
  tname VARCHAR(50),
constraint t_cid foreign key( tid)  references course(cid)
);

INSERT INTO Teacher VALUES(2001,'张老师');
INSERT INTO Teacher VALUES(2002,'李老师');
INSERT INTO Teacher VALUES(2003,'王老师');
INSERT INTO Teacher VALUES(2004,'赵老师');

INSERT INTO Teacher VALUES(2001,'张老师'),
(2002,'李老师'),
(2003,'王老师'),
(2004,'赵老师');

问题：
1、查询“1001”课程比“1002”课程成绩高的所有学生的学号；

2、查询平均成绩大于60分的同学的学号和平均成绩；

3、查询所有同学的学号、姓名、选课数、总成绩；

4、查询姓“李”的老师的个数；

5、查询没学过“叶平”老师课的同学的学号、姓名；
    
6、查询学过“001”并且也学过编号“002”课程的同学的学号、姓名；

7、查询学过“叶平”老师所教的所有课的同学的学号、姓名；

8、查询课程编号“002”的成绩比课程编号“001”课程低的所有同学的学号、姓名；

9、查询所有课程成绩小于60分的同学的学号、姓名；

10、查询没有学全所有课的同学的学号、姓名；
    
11、查询至少有一门课与学号为“1001”的同学所学相同的同学的学号和姓名；
    
12、查询至少学过学号为“001”同学所有一门课的其他同学学号和姓名；
    
13、把“SC”表中“叶平”老师教的课的成绩都更改为此课程的平均成绩；
     
14、查询和“1002”号的同学学习的课程完全相同的其他同学学号和姓名；
    
15、删除学习“叶平”老师课的SC表记录；
    
16、向SC表中插入一些记录，这些记录要求符合以下条件：没有上过编号“003”课程的同学学号、2号课的平均成绩；
    
17、按平均成绩从高到低显示所有学生的“数据库”、“企业管理”、“英语”三门的课程成绩，按如下形式显示： 学生ID,,数据库,企业管理,英语,有效课程数,有效平均分
    
18、查询各科成绩最高和最低的分：以如下形式显示：课程ID，最高分，最低分
    
19、按各科平均成绩从低到高和及格率的百分数从高到低顺序
     
20、查询如下课程平均成绩和及格率的百分数(用"1行"显示): 企业管理（001），马克思（002），OO&UML （003），数据库（004）
    
21、查询不同老师所教不同课程平均分从高到低显示
    
22、查询如下课程成绩第 3 名到第 6 名的学生成绩单：企业管理（001），马克思（002），UML （003），数据库（004）
    
23、统计列印各科成绩,各分数段人数:课程ID,课程名称,[100-85],[85-70],[70-60],[<60]
     

24、查询学生平均成绩及其名次
     

25、查询各科成绩前三名的记录:(不考虑成绩并列情况)
      
26、查询每门课程被选修的学生数

27、查询出只选修了一门课程的全部学生的学号和姓名

28、查询男生、女生人数
    ；
29、查询姓“张”的学生名单
    
30、查询同名同性学生名单，并统计同名人数

31、1981年出生的学生名单(注：Student表中Sage列的类型是datetime)
    
32、查询每门课程的平均成绩，结果按平均成绩升序排列，平均成绩相同时，按课程号降序排列
     
33、查询平均成绩大于85的所有学生的学号、姓名和平均成绩
    
34、查询课程名称为“数据库”，且分数低于60的学生姓名和分数
    
35、查询所有学生的选课情况；
    
36、查询任何一门课程成绩在70分以上的姓名、课程名称和分数；
    
37、查询不及格的课程，并按课程号从大到小排列
    
38、查询课程编号为003且课程成绩在80分以上的学生的学号和姓名；
    
39、求选了课程的学生人数
    
40、查询选修“叶平”老师所授课程的学生中，成绩最高的学生姓名及其成绩
    
41、查询各个课程及相应的选修人数
    
42、查询不同课程成绩相同的学生的学号、课程号、学生成绩 

43、查询每门功成绩最好的前两名
    
44、统计每门课程的学生选修人数（超过10人的课程才统计）。要求输出课程号和选修人数，查询结果按人数降序排列，查询结果按人数降序排列，若人数相同，按课程号升序排列  
    
45、检索至少选修两门课程的学生学号
    
46、查询全部学生都选修的课程的课程号和课程名
    
47、查询没学过“叶平”老师讲授的任一门课程的学生姓名
    
48、查询两门以上不及格课程的同学的学号及其平均成绩
    
49、检索“004”课程分数小于60，按分数降序排列的同学学号
    
50、删除“002”同学的“001”课程的成绩

