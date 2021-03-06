# SportManage
a Web system to manage athletic competition<br>
## 来自小组合作的软件工程大作业
个人开发计划：<br>
+ 4.28-5.5 完成Django框架搭建和前端页面设计
+ 5.10-5.20 开发项目基本功能
+ 5.20-6.1 根据需求分析补充项目细节
+ 6.1-6.5 完善项目各类文档信息
# 需求分析
## <br>1. 引言<br>
1.1. 编写目的<br>
1.2. 背景<br>
1.3. 参考资料<br>
## 2. 项目概述<br>
2.1. 面向的用户<br>
2.2. 实现目标<br>
2.3. 项目开发要求	<br>
2.4. 开发工具<br>
## 3. 系统描述<br>
3.1. 系统概述<br>
3.1.1.普通用户功能需求<br>
3.1.2.管理员功能需求<br>
3.2. 系统总体结构	<br>
3.3. 系统各部分功能模块<br>
## 4. 系统分析<br>
4.1. 用例图<br>
4.2. 活动图<br>
4.3. 时序图<br>
4.3.1.管理员时序图<br>
4.3.2.普通用户时序图<br>
4.4. 关系图<br>
## 5. 系统接口<br>
5.1. 用户接口<br>
5.2. 硬件接口<br>
## 6. 性能要求<br>
6.1. 精度要求<br>
6.2. 时间特征<br>
6.3. 灵活性<br>
## 7. 软件属性<br>
7.1. 系统安全性<br>
7.2. 可维护性<br>
## 8. 其他需求<br>
8.1. 数据库需求<br>
8.2. 系统操作要求	<br>
8.3. 故障及其处理	<br>
***
### 1.引言<br>
#### 1.1.编写目的<br>
基于Web的比赛对阵管理系统是典型的信息管理系统,本系统为各种比赛的组织者提供方便、快捷的方法，系统地对比赛进行合理的安排与管理，实现无纸化工作，节省大量人力和物力，随着科学技术的飞速发展与计算机技术的普遍应用，自动化的信息管理已深入各行各业，但由于传统信息管理方法的影响，目前国内比赛管理水平仍处于较低水平，主要存在以下问题。<br>
> 1.采用人工操作，不仅费时费力，而且容易出错。<br>
> 2.信息不集中，不便于人们查看，致使人们对比赛相关信息不了解。<br>
> 3.信息更新费时费力，也不能及时反映得分情况。<br>
> 4.对于比赛日程查询麻烦且不全面，不容易发现参赛队员的比赛时间冲突，给比赛进程带来麻烦。<br>
> 5.不能及时统计各项总分，不便于人们随时关注总体得分情况。<br>

基于Web的比赛对阵管理系统提供了强大的比赛系统管理功能，方便管理员对参赛队员成绩等信息的操作，采用比赛对阵管理系统后，参赛队员在比赛前在网络上输入个人信息即可，方便了运动员的报名，有错误时可以及时汇报修改。裁判员单独对各自的项目进行管理，保证了比赛的公正、公平。每个项目都有单独的帐号和密码对应，以保证成绩录入人员对自己管辖范围的唯一性。成绩查询界面中可以准确及时地查询到各项目、各运动员的个人信息、比赛成绩、排名、和团体加分等情况，同时为比赛安排裁判。系统开发完成后，可减少管理人员的数量，提高工作效率并保证数据的实时性、准确性、安全性、可靠性。<br>
#### 1.2.背景<br>
随着现代体育运动的不断发展，大型体育赛事的编排管理工作也越来越复杂精细化，为使体育竞赛项目能够高效、便捷、有序的进行，作为赛事的组织方就必须充分借助现代信息化手段，使用基于web的体育竞赛管理系统来统一管理体育赛事的各个环节。本文针对体育竞赛管理系统中最主要的数据库设计部分进行简要阐述。<br>
现代化的体育竞赛管理系统,利用计算机和网络技术使信息以数字化的形式在系统中存储和流动,软件系统管理各种设备自动地按照协议配合工作,使人们能够高效率地进行信息处理.传输和利用。本文体育竞赛管理系统实现了内外信息传递，比赛日程安排,比赛场地安排,赛事编排自动化等项目,极大的改变了传统的赛事以人工编排为主的工作方式,提高了工作管理效率。<br>
#### 1.3．参考资料<br>
[1]程嘉炎.球类运动竞赛法[M].北京:人民体育出版社,2004(1):50-110.<br>
[2]王珊,萨师煊.数据库系统概论[M].北京:高等教育出版社,2008(3):78-210.<br>
### 2.项目概述
#### 2.1.面向的用户<br>
赛事管理员主要是查询、录入和修改赛事信息，参赛队员、观众主要是查询、系统管理员主要维护系统和数据处理。<br>
#### 2.2.实现目标<br>
> (1)建立一个具有友好界面，操作简单的赛事管理系统。<br>
> (2)能够更好的管理、维护和保存赛事的相关信息。<br>
> (3)实现对参赛队员、裁判员信息录入，并建立完整的数据库，对所有的工作人员统一管理。<br>
> (4)管理员登陆本系统，可以查询、修改、更新系统数据，参赛队员和观众只能查询数据信息。<br>

#### 2.3.项目开发要求<br>
> (1)项目开发规范统一、模块划分。<br>
> (2)程序优化、安全并要有良好的可扩展性。<br>
> (3)用户界面简洁明了、操作简单实用。<br>
> (4)与用户保持良好的沟通，及时根据用户新的需求改善系统功能。<br>
#### 2.4.开发工具<br>
### 3.系统描述<br>
#### 3.1.系统概述<br>
##### 3.1.1.普通用户功能需求<br>
要设计一个优秀的运动会赛事编排管理系统，就必须首先明确用户对系统的要求。赛事编排管理系统的功能为：方便用户报名参加比赛，查询个人赛项成绩。普通用户是系统的服务对象，也是系统的主要参与者。一个赛事编排管理系统的好坏主要是由普通用户来评判的。因此，对于普通用户该系统需满足以下几方面需求：<br>
> 1.用户管理：目前可提供用户自定义报名。<br>
> 2.成绩查询：该用户可以对所有人、所有班级、比赛项目的成绩进行查询。<br>
> 3.赛程查询：对整个赛事的赛项进行查看，并得知赛项的详细内容，如比赛规则，参赛人数，比赛时间等。<br>
##### 3.1.2.管理员功能需求:<br>
管理员是一个软件系统的管理者，需要处理各种信息的增添、修改、删除，也要对用户的信息进行维护，在本软件中，管理员可以实现以下功能：<br>
> 1.查看赛事的信息。<br>
> 2.可删除和更新用户信息。<br>
> 3.能处理已存在用户报名参加比赛。<br>
> 4.可以对赛项进行编制处理和增删改。<br>
> 5.可以按模块中的内容精确查询。<br>
> 6.可以对赛项的赛程进行时间，分组等进行设置和增删改。<br>
> 7.可以对比赛选手进行增删改。<br>
> 8.可以对选手的成绩进行增删改。<br>
> 9.可以进行软件登陆身份验证。<br>
#### 3.2系统总体结构
![输入图片说明](https://images.gitee.com/uploads/images/2020/0427/150348_db55efe1_7473443.png "总体图.png")<br>
#### 3.3系统各部分功能模块<br>
> + 注    册  录入用户数据到用户数据表，设置用户权限。<br>
> + 登    录  读取用户数据表，自动区分管理员与运动员，自动跳转到各自第一功能模块。<br>
> + 报    名  读取用户信息，用户先选择报名的赛事，选择分队、比赛项目。在提交时对比当前服务器时间和赛事报名时间，若在报名时间内则判断 项目个数。报名数据保存在运动员数据表中。否则报名失败。<br>
> + 成绩查询  读取成绩数据表，显示用户所参加赛事名称及比赛项目的成绩、排名。<br>
> + 赛程查询  读取用户所报项目，按一定规则限制条件进行查询。可以分学号、姓名等进行查询。<br>
> + 赛事管理  管理员添加赛事名称，确定报名时间及比赛（开始）时间。提交时保存数据到赛事数据表，并提示进行赛程编排。<br>
> + 选手管理  查询报名参与运动会运动员的学号，返回该运动员报名的具体信息，无匹配结果，则返回提示查无此人。管理员可以对已报名的运动员信息进行删除与修改。对运动员信息的修改与删除必须使用管理员的密码校验，防止非管理员恶意更改运动员信息。此功能仅管理员可以使用，普通用户无法访问该页面。<br>
> + 赛程管理  管理员可手动进行所有赛程编排、管理，也可以读取系统预设中的赛程表。结果保存至赛程数据表中。<br>
> + 用户管理  读取所需要普通用户的信息，管理员可以实现对普通用户一些基本资料的修改。<br>
> + 成绩录入  选择赛事，显示所有比赛项目的前8名。选择赛程，录入运动员的成绩保存至成绩数据表。<br>
数据项分析<br>
通过对系统功能模块的分析，设计数据项如下：<br>
> + 用户信息：姓名、性别、学号、系别、赛事等级，参赛时间，赛事性质，
赛事名称。<br>
> + 赛项信息：赛事ID、赛事名称、规则、赛事性质，赛事时间、报名时间。<br>
> + 运动员信息：参赛项目、报名时间、姓名、学号、系别、性别，修改参赛项目，赛事性质，比赛结果，比赛时间，修改比赛结果。<br>
> + 赛程信息：赛事名称、参赛项目、赛事性质、比赛时间、参赛运动员。<br>
> + 成绩管理：姓名、学号、性别、赛事名称、参赛项目、性质、排名。<br>
> + 管理员信息包括：管理员账号，密码。<br>

## 拟根据我SRTP的项目demo，用Python3+Django Web框架和前端设计语言完成此项目的设计
