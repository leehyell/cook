import sys
import sqlite3
import oracledb
import time
import re
from datetime import datetime
import bcrypt
import os
import hashlib

# 비밀번호 해싱
password = "test1234"
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


# 오라클 라이브러리 경로 설정
oracledb.init_oracle_client(lib_dir="C:\\project\\cook\\instantclient_11_2")

# 오라클 데이터베이스 연결
#각자 계정 연결
connect = oracledb.connect(user='', password='1234', dsn='localhost')
c = connect.cursor()  # 커서 생성

today = datetime.today()

##########usermember
#관리자/일반유저 미리 가입
#usermember/id/pw/name/tel1/tel2/tel3/jumin1/jumin2/email_id/email_domain/addr/detailaddr/streetaddr
###관리자
c.execute('insert into usermember (id,pw,name,tel1,tel2,tel3,jumin1,jumin2,email_id,email_domain,addr,streetaddr,detailaddr) ' +
          'values(:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13)'
          ,('admin',hashed_password.decode('utf-8'),'관리자','000','0000','0000','930210','1','admin','naver.com','16455','경기 수원시 팔달구 향교로2','3층 mbc 아카데미'))
###일반유저
c.execute('insert into usermember (id,pw,name,tel1,tel2,tel3,jumin1,jumin2,email_id,email_domain,addr,streetaddr,detailaddr) ' +
          'values(:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13)'
          ,('test1234',hashed_password.decode('utf-8'),'테스터','010','1234','5678','920505','2','test1234','naver.com','16455','경기 수원시 팔달구 향교로2','3층 mbc 아카데미'))

##########recipecategory
#메인, 서브 카테고리
c.execute('insert into recipecategory (categorynum, maincategory, subcategory) values(category_seq.nextval, :1, :2)',('한식', '탕/찌개'))
c.execute('insert into recipecategory (categorynum, maincategory, subcategory) values(category_seq.nextval, :1, :2)',('한식', '반찬'))
c.execute('insert into recipecategory (categorynum, maincategory, subcategory) values(category_seq.nextval, :1, :2)',('한식', '밥'))
c.execute('insert into recipecategory (categorynum, maincategory, subcategory) values(category_seq.nextval, :1, :2)',('일식', '밥'))
c.execute('insert into recipecategory (categorynum, maincategory, subcategory) values(category_seq.nextval, :1, :2)',('일식', '면'))
c.execute('insert into recipecategory (categorynum, maincategory, subcategory) values(category_seq.nextval, :1, :2)',('일식', '간식'))
c.execute('insert into recipecategory (categorynum, maincategory, subcategory) values(category_seq.nextval, :1, :2)',('중식', '면'))
c.execute('insert into recipecategory (categorynum, maincategory, subcategory) values(category_seq.nextval, :1, :2)',('중식', '밥'))
c.execute('insert into recipecategory (categorynum, maincategory, subcategory) values(category_seq.nextval, :1, :2)',('중식', '요리'))
c.execute('insert into recipecategory (categorynum, maincategory, subcategory) values(category_seq.nextval, :1, :2)',('양식', '면'))
c.execute('insert into recipecategory (categorynum, maincategory, subcategory) values(category_seq.nextval, :1, :2)',('양식', '밥'))
c.execute('insert into recipecategory (categorynum, maincategory, subcategory) values(category_seq.nextval, :1, :2)',('양식', '요리'))

##########ingredient
#####1. 치킨마요덮밥
##치킨(1),계란(2),깐양파(3),밥(4),마요네즈(5),진간장(6),설탕(7)
#1 치킨
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('야들리애 100% 닭다리 순살 후라이드 가라아게 치킨, 250g, 1개',8900,'치킨마요덮밥'))
#2 계란
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('곰곰 신선한 대란, 10구, 1개',3790,'치킨마요덮밥'))
#3 양파
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('국내산 친환경 깐양파, 300g, 1개',2980,'치킨마요덮밥'))
#4 밥
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('1인 가구 필수템 오뚜기 밥 210g, 1박스',15200,'치킨마요덮밥'))
#5 마요네즈
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('오뚜기 골드 마요네즈, 500g, 1개',4730,'치킨마요덮밥'))
#6 진간장
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('햇살담은 두번 달여 더 진한 진간장, 200ml, 2개',2520,'치킨마요덮밥'))
#7 설탕
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('큐원 갈색설탕, 1kg, 1개',2560,'치킨마요덮밥'))

#####2. 청국장
##청국장(8),된장(9),양파(3),김치(10),대파(11),멸치(12),물(13),다진마늘(14),두부(15)
#8 청국장
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('다담 청국장 양념, 530g, 1개',5200,'청국장'))
#9 된장
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('청정원순창 재래식 생된장, 1kg, 1개',4700,'청국장'))
#10 김치
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('곰 국내산 포기 김치, 4kg, 1개',20090,'청국장'))
#11 대파
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('곰곰 국내산 절단대파, 500g, 1개',2800,'청국장'))
#12 멸치
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('이어수산 통영 산지 직거래 국물용 멸치 (냉동), 500g, 1봉',9970,'청국장'))
#13 물
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('탐사수 무라벨, 2L, 12개',6790,'청국장'))
#14 다진마늘
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('곰곰 국산 다진마늘, 500g, 1개',6650,'청국장'))
#15 두부
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('풀무원 소가 찌개두부, 290g, 1개',1240,'청국장'))

#####3. 미역국
##미역(16),다진마늘(14),간장(6),된장(9),소금(17)
#16 미역
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('오뚜기 옛날 미역, 250g, 1개',7990,'미역국'))
#17 소금
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('청정원 천일염 가는소금, 500g, 1개',3590,'미역국'))

#####4. 김치찌개
##쌀뜰물(13),대파(11),청양고추(18),돼지고기목살(19),김치(10),국간장(20),고춧가루(21),다진마늘(14),새우젓(22),된장(9)
#18 청양고추
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('국내산 청양고추, 150g, 1개',1980,'김치찌개'))
#19 돼지 목살
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('포크밸리 1등급이상 돼지고기 찌개용 (냉장), 500g, 1팩',9990,'김치찌개'))
#20 국간장
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('청정원 햇살담은 국간장, 500ml, 1개',3090,'김치찌개'))
#21 고추가루
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('햇님마을 양념이 잘 어우러지는 국산 고춧가루 보통매운맛, 110g, 1개',6900,'김치찌개'))
#22 새우젓
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('일미식품 국내산 참새우젓, 1개, 200g',4800,'김치찌개'))

#####5. 제육볶음
##돼지고기 앞다리살(23),양파(3),청양고추(18),대파(11),고추장(24),고춧가루(21),다진마늘(14),설탕(7),매실액(25),간장(6),통깨(26),후추(27)
#23 돼지 앞다리살
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('곰곰 한돈 앞다리살 찌개용 (냉장), 500g, 1개',8660,'제육볶음'))
#24 고추장
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('순창궁 태양초 골드 고추장, 500g, 1개',3480,'제육볶음'))
#25 매실액
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('백설 리얼 매실청, 310ml, 1개',4530,'제육볶음'))
#26 통깨
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('오뚜기 옛날 볶음참깨, 200g, 1개',5480,'제육볶음'))
#27 후추
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('오뚜기 순후추, 100g, 1개',4640,'제육볶음'))

#####6. 잡채
##당면(28),소고기(29),양파(3),파프리카(30),당근(31),느타리버섯(32),시금치(33),다진마늘(14),소금(17),후춧가루(27),생강가루(34),식용유(35),간장(6),올리고당(36),참기름(37),통깨(26)
#28 당면
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('오뚜기 옛날 자른 당면, 500g, 1개',6150,'잡채'))
#29 소고기
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('곰곰 호주산 소고기 앞다리살 국거리용 (냉장), 300g, 1개',8700,'잡채'))
#30 파프리카
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('파프리카 혼합, 2개입, 1개',2790,'잡채'))
#31 당근
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('국내산 세척당근, 600g, 1개',4990,'잡채'))
#32 느타리버섯
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('국내산 무농약 느타리버섯, 200g, 1개',1430,'잡채'))
#33 시금치
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('국내산 시금치, 600g, 1개',6270,'잡채'))
#34 생강가루
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('내츄럴스파이스 생강분말, 35g, 1개',4200,'잡채'))
#35 식용유
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('해표 콩기름 식용유, 1.8L, 1개',4500,'잡채'))
#36 올리고당
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('청정원 요리 올리고당, 1.2kg, 1개',4980,'잡채'))
#37 참기름
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('오뚜기옛날 참기름, 500ml, 1개',7020,'잡채'))

#####7. 소불고기
##소불고기(38),식용유(35),물(13),후추(27),쪽파(39),간장(6),설탕(7),맛술(40),다진파(41),다진마늘(14),다진생강(42),참기름(37)
#38 소불고기
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('고기듬뿍 양념 소불고기 (냉장), 500g, 1개',9980,'소불고기'))
#39 쪽파
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('국내산 깐쪽파, 200g, 1개',3980,'소불고기'))
#40 청주
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('청정원 맛술, 830ml, 1개',3580,'소불고기'))
#41 다진 파
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('친정엄마꾸러미 뚝딱 대파 (냉동), 500g, 1개',4880,'소불고기'))
#42 다진 생강
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('곰곰 짜서쓰는 다진 생강, 300g, 1개',7730,'소불고기'))

#####8. 꼬막무침
##새꼬막(43),쪽파(39),소금(17),다진마늘(14),고춧가루(21),간장(6),설탕(7),식초(44),멸치액젓(45),참기름(37),참깨(46)
#43 새꼬막
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('우리바다좋은산지 벌교 출신 새꼬막, 1kg, 2봉',19380,'꼬막무침'))
#44 식초
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('오뚜기 사과식초, 360ml, 1개',1380,'꼬막무침'))
#45 멸치액젓
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('청정원 남해안 멸치액젓 골드, 500g, 1개',2300,'꼬막무침'))
#46 참깨
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('오뚜기 옛날 볶음참깨, 200g, 1개',5480,'꼬막무침'))

#####9. 비빔밥
##돼지고기목살(19),애호박(47),양파(3),당근(31),고추장(24),간장(6),설탕(7),깨소금(48),참기름(37),식초(44)
#47 애호박
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('국내산 애호박, 1개입, 1개',1580,'비빔밥'))
#48 깨소금
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('햇님마을 고소함이 가득한 우리집 깨소금, 1개, 100g',3800,'비빔밥'))

#####10. 김치볶음밥
#김치(10),설탕(7),간장(6),고춧가루(21),참기름(37),마요네즈(5),된장(9),파(39)
#추가 재료 없음

#####11. 간장계란밥
##밥(4),달걀(2),물(13),햄(49),다진대파(50),피자치즈(51),슬라이스치즈(52),간장(6),소금(17),후추(27)
#49 햄
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('롯데 의성마늘햄, 1kg, 1개',8440,'간장계란밥'))
#50 다진대파
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('대파 슬라이스, 150g, 1개',2190,'간장계란밥'))
#51 피자치즈
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('곰곰 모짜렐라 피자치즈, 1개, 1kg',10530,'간장계란밥'))
#52 슬라이스 치즈
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('곰곰 데일리 체다치즈 슬라이스, 396g, 1개',5990,'간장계란밥'))

#####12. 가지밥
##현미(53),가지(54),파(39),올리브유(55),간장(6),부추(56),다진마늘(14),고춧가루(21),설탕(7),참기름(37),통깨(26),간장(6)
#53 현미
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('국내산 현미, 5kg, 1개',12900,'가지밥'))
#54 가지
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('국내산 가지, 2개입, 1개',1980,'가지밥'))
#55 올리브유
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('백설 압착 올리브유, 500ml, 1개',11890,'가지밥'))
#56 부추
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('국내산 부추, 300g, 1개',2670,'가지밥'))

#####13. 탕수육
##돼지 안심(57),전분가루(58),계란(2),식용유(35),소금(17),후추(27),튀김유(59),양파(3),당근(31),귤(60),식초(44),간장(6),설탕(7)
#57 안심 돼지
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('돼지고기 안심, 500g, 1개',9000,'탕수육'))
#58 전분가루
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('전분가루, 1kg, 1개',5000,'탕수육'))
#59 튀김유
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('식용유, 1.8L, 1개',4500,'탕수육'))
#60 귤
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('귤, 5kg, 1개',15000,'탕수육'))

#####14. 동파육
##통삼겹(61),식용유(35),진간장(6),맛술(40),물엿(62),설탕(7),춘장(63),통후추(64),통마늘(65),양파(3),생강(66),대파(11),팔각(68)
#61 통삼겹
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('곰곰 한돈 삼겹살 수육용 (냉장), 1000g, 1개',25130,'동파육'))
#62 물엿
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('청정원 물엿, 700g, 1개',2720,'동파육'))
#63 춘장
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('진미 불맛춘장, 300g, 1개',2910,'동파육'))
#64 통후추
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('푸른빈 통흑후추, 200g, 1개',5360,'동파육'))
#65 통마늘
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('국내산 통마늘, 1kg, 1개',8980,'동파육'))
#66 생강
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('국내산 깐 생강, 50g, 1개',1610,'동파육'))
#68 팔각
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('한방선생 팔각, 100g, 1개',4990,'동파육'))

#####15. 짜장면
##식용유(35),다진생강(42),돼지고기(57),양파(3),주키니 호박(69),볶은 춘장(63),굴소스(72),설탕(7),MSG(64),양배추(65),전분물(58),중화면(66)
#69 주키니 호박
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('국내산 주키니호박, 1개입, 1개',2980,'짜장면'))

#####16. 해물짬뽕{
##홍합(67),오징어(68),흰다리새우(69),중화면(66),양파(3),애호박(47),양배추(65),사골곰탕(70),고추기름(71),다진마늘(14),굴소스(72),고춧가루(21),소금(17),후추,MSG(64),치킨파우더(73)
#67 홍합
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('바다자리 생물 홍합 (냉장), 3kg, 1개',11950,'해물짬뽕'))
#70 사골곰탕
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('비비고 사골곰탕, 500g, 6개',6040,'해물짬뽕'))
#71 고추기름
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('오뚜기옛날 고추맛 기름, 80ml, 3개',5880,'해물짬뽕'))
#73 치킨 파우더
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('이금기 치킨 파우더, 273g, 1개',6200,'해물짬뽕'))

#####17. 중화짬뽕
##물(13),치킨스톡(74),설탕(7),소금(17),진간장(6),식초(44),오이(75),계란(2),당근(31),새우(69),팽이버섯(76),생면(77),땅콩버터(78)
#74 치킨스톡
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('청정원 쉐프의 치킨스톡, 340g, 1개',5990,'중화짬뽕'))
#75 오이
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('국내산 백오이, 3개입, 1개',4490,'중화짬뽕'))
#76 팽이버섯
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('친환경 국내산 팽이버섯, 300g(150gx2개입), 1개',1100,'중화짬뽕'))
#77 생면
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('풀무원 풀스키친 생중화면, 1kg, 1개',7400,'중화짬뽕'))
#78 땅콩버터
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('스키피 수퍼 청크 피넛 버터, 462g, 1개',8900,'중화짬뽕'))

#####18. 탄탄면
##생면(77).땅콩버터(78),사골육수(79),두반장(80),간장(6),라유(81),다진 파(41),다진마늘(14),다진고기-돼지고기목살(19),청경채(82),땅콩(83)
#79 사골육수
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('비비고 사골곰탕, 500g, 6개',6040,'탄탄면'))
#80 두반장
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('이금기 중화 두반장, 226g, 1개',3760,'탄탄면'))
#81 라유
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('모모야 약간 매운맛 라유 고추기름',6300,'탄탄면'))
#82 청경채
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('국내산 청경채, 300g, 1개',1920,'탄탄면'))
#83 땅콩
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('아산율림 국산 생땅콩, 250g, 1봉',9900,'탄탄면'))

#####19. 중식볶음밥
##대파(11),당근(31),계란(2),밥(4),식용유(35),소금(17)
#추가 재료 없음

#####20. 새우볶음밥
##계란(2),대파(11),냉동새우(69),진간장(6),참기름(37),통깨(26)
#추가 재료 없음

#####21. 스팸 돈부리 덮밥
##양파(3),계란(2),밥(4),간장(6),설탕(7),대파(11),맛술(40),참기름(37),후추(27),스팸(84)
#84 스팸
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('스팸 클래식, 340g, 3개',10630,'스팸 돈부리 덮밥'))

#####22. 규동 소고기 덮밥
##불고기용 소고기(38),계란(2),쪽파(39),양파(3),밥(4),모란봉 규동소스(85)
#85 모란봉 규동소스
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('이엔푸드 돈부리노타레 소스, 900ml, 1개',5660,'규동 소고기 덮밥'))

#####23. 돈코츠 라멘
##삼겹살(61),숙주나물(86),사골곰탕(70),소면(87),김(88),계란(2),소금(17),후추(27),다진마늘(14),쯔유(89),간장(6),맛술(40),쌈장(90)
#86 숙주나물
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('곰곰 아삭한 숙주나물, 300g, 1봉',1100,'돈코츠 라멘'))
#87 소면
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('오뚜기옛날 국수 소면, 900g, 1개',3190,'돈코츠 라멘'))
#88 김
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('광천김 도시락김, 5g, 16개',5990,'돈코츠 라멘'))
#89 쯔유
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('기꼬만 코이다시 혼쯔유, 500ml, 1개',6250,'돈코츠 라멘'))
#90 쌈장
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('해찬들 사계절 쌈장, 500g, 1개',2250,'돈코츠 라멘'))

#####24. 야끼소바
##### 불고기(38), 양파(3), 양배추(65), 숙주나물(86), 우동사리(91), 느타리버섯(32), 생강(66), 식용유(35), 간장(6), 맛술(40), 설탕(7), 스리랏차소스(92)
#91 우동 사리
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('풀무원 냉장_수타식 우동사리면 1인분, 210g, 1개',1380,'야끼소바'))
#92 스리라차
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('제이렉 스리라차 소스, 225ml, 1개',2990,'야끼소바'))

##### 25. 메밀소바
##### 메밀면(93), 메밀소바장국(94), 김(88), 와사비(95), 양파(3), 대파(11)
#93 메밀면
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('칠갑농산 메밀면, 400g, 1개',2780,'메밀소바'))
#94 메밀소바장국
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('오뚜기 메밀소바장국 소스, 360ml, 1개',2880,'메밀소바'))
#95 생와사비
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('청정원 생와사비, 40g, 1개',2980,'메밀소바'))

##### 26. 오코노미야키
##### 양배추(65), 베이컨(96), 계란(2), 튀김가루(97), 가쓰오부시(98), 데리야끼소스(99), 마요네즈(5), 식용유(35)
#96 베이컨
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('곰곰 담백한 베이컨, 130g, 1개',2150,'오코노미야키'))
#97 튀김가루
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('곰곰 바삭한 튀김가루, 1kg, 1개',2230,'오코노미야키'))
#98 기쓰오부시
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('석하 곱게깎은 가다랑어 가쓰오부시, 40g, 1개',5060,'오코노미야키'))
#99 데리야끼 소스
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('청정원 데리야끼 소스, 1개, 250g',3180,'오코노미야키'))

##### 27. 차왕무시
##### 칵테일 새우(100), 계란(2), 다시마(101), 소금(17), 우유(102)
#100 칵테일 새우
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('곰곰 냉동 흰다리 새우살, 300g(24~33미), 1개',5890,'차왕무시'))
#101 다시마
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('주일 완도 명품 자른 다시마, 1개, 50g',2380,'차왕무시'))
#102 우유
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('곰곰 신선한 우유, 900ml, 1개',2260,'차왕무시'))

##### 28. 당고
##### 건식 찹쌀가루(103), 소금(17), 진간장(6), 설탕(7), 맛술(40), 옥수수전분(104)
#103 건식 찹쌀가루
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('배대감 국산 찹쌀가루, 500g, 1개',4600,'당고'))
#104 옥수수 전분
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('배대감 옥수수전분, 350g, 1개',2180,'당고'))

###############recipe
##########한식
###탕/찌개
#####청국장
##청국장(8),된장(9),양파(3),김치(10),대파(11),멸치(12),물(13),다진마늘(14),두부(15)
c.execute('insert into recipe (recipeseq,food,category1,category2,image,ingredient,recipe,hits) values(recipe_seq.nextval,:1,:2,:3,:4,:5,:6,:7)',
          ('청국장','한식','탕/찌개','cheongukjang.jfif','8,9,3,10,11,12,13,14,15',
           '멸치와 물을 넣고 육수를 끓인다.<br>'+
           '물이 끓기 시작하면 멸치를 빼고 먹기 좋게 썰은 김치를 넣는다.<br>'+
           '양파도 먹기 좋은 크기로 잘라 넣는다.<br>'+
           '대파를 넣는다.<br>'+
           '다진마늘을 넣는다.<br>'+
           '된장을 한 스푼 떠서 풀어준다.<br>'+
           '끓을 때 청국장을 넣는다(기호에 맞게 조금씩 넣으면서 맛보는 거 추천).<br>'+
           '푹 끓어지면 두부를 넣어줍니다.<br>'+
           'EAT!',0))

#####미역국
##미역(16),다진마늘(14),간장(6),된장(9),소금(17)
c.execute('insert into recipe (recipeseq,food,category1,category2,image,ingredient,recipe,hits) values(recipe_seq.nextval,:1,:2,:3,:4,:5,:6,:7)',
          ('미역국','한식','탕/찌개','miyukguk.jfif','16,14,6,9,17',
           '미역을 물에 담궈 불려준다.<br>'+
           '불려진 미역을 잘라서 냄비에 넣고 참기름과 볶아준다.(미역이 물기가 없어 냄비에 달라 붙을 지경이 될 때까지)<br>'+
           '볶아진 미역에 물을 미역이 잠기기 않을 정도로 부어준다.<br>'+
           '다진마늘을 한 스푼정도 넣어준다.<br>'+
           '센 불에 끓여준다.<br>'+
           '물이 졸아들면 다시 물을 미역이 잠길 만큼 부어준다.<br>'+
           '간장 1티,되장 2/1티,소금(원하는 간만큼)을 넣어준다.<br>'+
           'EAT!',0))

#####김치찌개
##쌀뜨물(13),대파(11),청양고추(18),돼지고기목살(19),김치(10),국간장(20),고춧가루(21),다진마늘(14),새우젓(22),된장(9)
c.execute('insert into recipe (recipeseq,food,category1,category2,image,ingredient,recipe,hits) values(recipe_seq.nextval,:1,:2,:3,:4,:5,:6,:7)',
          ('김치찌개','한식','탕/찌개','kimchizzigae.jfif','13,11,18,19,10,20,21,14,22,9',
           '2번째나 3번째 쌀뜨물을 준비한다.<br>'+
           '돼지고기 목살,대파,김치를 먹기 좋은 사이즈로 썰어준다.<br>'+
           '냄비에 쌀뜨물 700ml를 넣어준다.<br>'+
           '돼지고기목살을 넣어준다.<br>'+
           '된장을 1/2스푼 넣어준다.<br>'+
           '김치를 넣어준다.<br>'+
           '끓기 시작하면 다진마늘 한 스푼을 넣어준다.<br>'+
           '고춧가루와 국간장을 한 스푼을 넣어준다.<br>'+
           '간을 보며 새우젓을 넣어준다.<br>'+
           '청양고추와 대파를 넣고 끓여준다.<br>'+
           'EAT!',0))

###반찬
#####제육볶음
##돼지고기 앞다리살(23),양파(3),청양고추(18),대파(11),고추장(24),고춧가루(21),다진마늘(14),설탕(7),매실액(25),간장(6),통깨(26),후추(27)
c.execute('insert into recipe (recipeseq,food,category1,category2,image,ingredient,recipe,hits) values(recipe_seq.nextval,:1,:2,:3,:4,:5,:6,:7)',
          ('제육볶음','한식','반찬','jaeyuk.jfif','23,3,18,11,24,21,14,7,25,6,26,27',
           '재료를 준비한다.<br>'+
           '고추장(3큰술),고춧가루(2큰술),다진마늘(1큰술),설탕(2큰술),간장(1큰술),통깨(약간),후추(약간)을 모두 넣고 섞어준다.<br>'+
           '대파와 청양고추는 어슷썰어주고 양파는 먹기 좋은 크기로 잘라준다.<br>'+
           '돼지고기는 한 입 크기로 썰어준다.<br>'+
           '만들어둔 양념장에 고기를 버무려준다.<br>'+
           '바로 볶아도 되고 냉장고에 30분정도 두어 숙성시켜준다.<br>'+
           '팬에 식용유 2큰술과 대파를 넣고 강불로 3분정도 볶아 파기름을 내준다.<br>'+
           '양념한 고기를 넣어준다.<br>'+
           '중볼로 볶아 고기를 완전히 익혀준다.<br>'+
           '양파와 청양고추를 넣어준다.<br>'+
           '마지막으로 통깨를 뿌려준다.<br>'+
           'EAT!',0))

#####잡채
##당면(28),소고기(29),양파(3),파프리카(30),당근(31),느타리버섯(32),시금치(33),다진마늘(14),소금(17),후춧가루(27),생강가루(34),식용유(35),간장(6),올리고당(36),참기름(37),통깨(26)
c.execute('insert into recipe (recipeseq,food,category1,category2,image,ingredient,recipe,hits) values(recipe_seq.nextval,:1,:2,:3,:4,:5,:6,:7)',
          ('잡채','한식','반찬','jabchae.jfif','28,29,3,30,31,32,33,14,17,27,34,35,6,36,37,26',
           '소고기는 다진마늘 0.5,후춧가루,소금,생강가루 적당량을 넣어 고기의 밑간을 해준다.<br>'+
           '잡채에 넣을 채소 당근,파프리카,양파를 채썰어주고 느타리 버섯은 가닥가닥 떼어 준비한다.<br>'+
           '시금치는 물에 씻어 물기를 빼고 준비한다.<br>'+
           '달군 팬에 식용유를 두르고 양파와 소금,후춧가루를 조금씩 넣어 볶아준다.<br>'+
           '같은 방법으로 소금,후춧가루로 간을 하고 느타리버섯을 볶아준다.<br>'+
           '시금치 역시 소금 간을 하고 살짝 볶아준다.<br>'+
           '마지막으로 밑간을 해놓은 소고기를 볶아준다.<br>'+
           '각각 재료를 볶아 준비해준다.<br>'+
           '냄비에 물을 담고 물이 팔팔 끓으면 당면을 넣고 10-11분 정도 삶아준다.<br>'+
           '삶아낸 당면은 찬물에 행군다.<br>'+
           '팬에 식용유 2,간장5,올리고당2를 넣고 삶아놓은 당면을 넣는다.<br>'+
           '물기가 사라질 때까지 볶아준다.<br>'+
           '볶아놓은 당면은 한 김 식히고 볶아놓았던 야채로 모두 한 곳에 넣고 참기름2,통깨1을 넣어 버무려준다.<br>'+
           'EAT!',0))

#####소불고기
##소불고기(38),식용유(35),물(13),후추(27),쪽파(39),간장(6),설탕(7),맛술(40),다진파(41),다진마늘(14),다진생강(42),참기름(37)
c.execute('insert into recipe (recipeseq,food,category1,category2,image,ingredient,recipe,hits) values(recipe_seq.nextval,:1,:2,:3,:4,:5,:6,:7)',
          ('소불고기','한식','반찬','sobulgogi.jfif','38,35,13,27,39,6,7,40,41,14,42,37',
           '불고기를 먹기 좋은 크기로 썬다.<br>'+
           '양념장을 만든다(간장3t,물2t,설탕2t,청주2t,다진파1t,다진마늘1t,다진생각1/4t,참기름약간).<br>'+
           '불고기에 양념장을 넣고 잘 섞는다.<br>'+
           '팬에 약간의 기름을 두르고 불고기를 익힌다.<br>'+
           '고기가 타지 않도록 중간마다 물을 넣는다.<br>'+
           '후추를 약간 뿌린다.<br>'+
           '구운 고기 위에 쪽파를 뿌린다.<br>'+
           'EAT!',0))

#####꼬막무침
##새꼬막(43),쪽파(39),소금(17),다진마늘(14),고춧가루(21),간장(6),설탕(7),식초(44),멸치액젓(45),참기름(37),참깨(46)
c.execute('insert into recipe (recipeseq,food,category1,category2,image,ingredient,recipe,hits) values(recipe_seq.nextval,:1,:2,:3,:4,:5,:6,:7)',
          ('꼬막무침','한식','반찬','ggomakmuchim.jfif','43,39,17,14,21,6,7,44,45,37,46',
           '소금 1스푼을 넣고 꼬막을 깨끗하게 닦아준다.<br>'+
           '끓는물에 소금 1스푼 넣고 꼬막을 삶아준다.<br>'+
           '꼬막이 입을 벌리면 건져낸다.<br>'+
           '건져낸 꼬막은 흐르는 찬물에 닦아준다.<br>'+
           '껍질을 분리한다.<br>'+
           '껍질은 벗긴 꼬막은 물에 다시 씻고 물기를 빼준다.<br>'+
           '쪽파를 채썰어준다.<br>'+
           '물기를 뺀 꼬막에 준비된 양념과 쪽파를 넣어준다.(다진마늘1스푼,고춧가루2스푼,간장2스푼,설탕1.5스푼,식초0.5스푼,멸치액젓1스푼,참기름0.5스푼)<br>'+
           'EAT!',0))

###밥
#####비빔밥
##돼지고기목살(19),애호박(47),양파(3),당근(31),고추장(24),간장(6),설탕(7),깨소금(48),참기름(37),식초(44)
c.execute('insert into recipe (recipeseq,food,category1,category2,image,ingredient,recipe,hits) values(recipe_seq.nextval,:1,:2,:3,:4,:5,:6,:7)',
          ('비빔밥','한식','밥','bibimbab.jfif','19,47,3,31,24,6,7,48,37,44',
           '양파,당근,애호박을 채썰어서 준비한다.<br>'+
           '비빔밥에 비벼먹을 양념장을 준비한다.(고추장2T,간장2T,설탕1.5T,깨소금,참기름,식초1T)<br>'+
           '먼저 당근을 소금 1꼬집 넣고 색깔이 나게 볶아준다.<br>'+
           '애호박도 똑같이 볶아준다.<br>'+
           '양파는 간장 1T 넣고 중불에 오래 볶아준다.<br>'+
           '소금,후추로 밑간을 해놓은 채썰어준 돼지고기를 볶아준다.<br>'+
           '밥 위에 볶아놓은 야채와 고기를 올리고 반숙 계란후라이와 양념장을 올려준다.<br>'+
           'EAT!',0))

#####김치볶음밥
##김치(10),설탕(7),간장(6),고춧가루(21),참기름(37),마요네즈(5),된장(9),파(39)
c.execute('insert into recipe (recipeseq,food,category1,category2,image,ingredient,recipe,hits) values(recipe_seq.nextval,:1,:2,:3,:4,:5,:6,:7)',
          ('김치볶음밥','한식','밥','kimchibab.jfif','10,7,6,21,37,5,9,39',
           '김치를 잘게 썬다.<br>'+
           '김치에 양념을 넣고 잘 비벼준다.(고춧가루1스푼,설탕1스푼,진간장1스푼,참기름2스푼,마요네즈1스푼,된장1/3스푼,다진대파2큰술)<br>'+
           '식용유 3스푼을 붓고 달군 팬에 재료를 고루 펴서 부어준다.<br>'+
           '뚜껑을 열고 수분이 거의 남지않은 꾸덕한 상태가 되면 밥 2공기를 넣고 볶는다.<br>'+
           '흰밥이 보이지 않을 정도로 고루 섞어준다.<br>'+
           '밥을 펴 뚜껑을 덮고 센 불에 20-30초간 둔다.<br>'+
           'EAT!',0))

#간장계란밥
##밥(4),달걀(2),물(13),햄(49),다진대파(50),피자치즈(51),슬라이스치즈(52),간장(6),소금(17),후추(27)
c.execute('insert into recipe (recipeseq,food,category1,category2,image,ingredient,recipe,hits) values(recipe_seq.nextval,:1,:2,:3,:4,:5,:6,:7)',
          ('간장계란밥','한식','밥','ganjangbab.jfif','4,2,13,49,50,51,52,6,17,27',
           '햄,대파는 다져서 준비한다.<br>'+
           '전자레인지용 그릇에 달걀을 풀고, 물,후추,소금을 넣고 섞는다.(달걀1개,물100ml,소금후추 약간).<br>'+
           '달걀 물에 밥,햄,대파,간장(1/2T)를 넣어 잘 섞는다.<br>'+
           '랩을 덮어 구멍을 뚫은 후 전자레인지에 3분간 익힌다.<br>'+
           '전자레인지에서 꺼낸 후 잘 섞는다.<br>'+
           '달걀밥 위에 피자치즈를 올리고 슬라이스 치즈를 올려 전자레인지에 3분간 더 익혀준다.<br>'+
           'EAT!',0))

#####가지밥
##현미(53),가지(54),파(39),올리브유(55),간장(6),부추(56),다진마늘(14),고춧가루(21),설탕(7),참기름(37),통깨(26),간장(6)
c.execute('insert into recipe (recipeseq,food,category1,category2,image,ingredient,recipe,hits) values(recipe_seq.nextval,:1,:2,:3,:4,:5,:6,:7)',
          ('가지밥','한식','밥','gajibab.jfif','53,54,39,55,6,56,14,21,7,37,26,6',
           '가지를 손질해서 원하는 만큼 어슷 썰어준다.<br>'+
           '팬을 달구기 전에 올리브유 4큰술과 다진파 1컵을 넣은 후 중불에서 파를 노릇하게 볶아준다.<br>'+
           '파향이 올라오면 가지를 넣고 볶는다.<br>'+
           '가지가 숨이 죽을 쯤 간장 3큰술을 팬 가장자리에 눌리듯 넣어 볶는다.<br>'+
           '30분 정도 불린 현미쌀 2컵에 물을 평상시 밥하는 양보다 80%정도 넣고 볶은 가지를 올린 후 밥을 지어준다.<br>'+
           '밥이 지어질 동안 양념장을 준비한다.(다진부추1/2컵,다진파1/2컵,고춧가루2큰술,다진마늘1/2큰술 통깨 적당량,간장(재료들이 되직하게 섞일 정도)).<br>'+
           '매운 맛을 원하면 매운고추를 다져서 넣어준다.<br>'+
           '설탕은 간을 보며 넣어주고 참기름을 넣어준다.<br>'+
           '가지밥이 완성되면 양념장을 적당이 얹어 비빈다.<br>'+
           'EAT!',0))


##########중식
###요리
#####탕수육
##돼지 안심(57),전분가루(58),계란(2),식용유(35),소금(17),후추(27),튀김유(59),양파(3),당근(31),귤(60),식초(44),간장(6),설탕(7)
c.execute('insert into recipe (recipeseq,food,category1,category2,image,ingredient,recipe,hits) values(recipe_seq.nextval,:1,:2,:3,:4,:5,:6,:7)',
          ('음식이름','중식','요리','tangsuyuk.jpg','57,58,2,35,17,27,59,3,31,60,44,6,7',
           '전분가루가 충분히 잠기도록 물을 붓고 1시간이상 기다린다.<br>'+
           '전분가루 위의 물을 따라낸 후 계란과 식용유 5스푼과 섞어준다.(마요네즈 질감처럼 될 때까지)<br>'+
           '탕수육 크기로 썬 돼지고기를 섞는다.(취향에 따라 고기에 소금, 후추로 간 해주기)<br>'+
           '기름을 충분히 두른 팬을 올리고 160~180도(튀김을 넣었을 때 부르르 끓어오르는 온도)가 되면 고기를 넣고 1차로 튀긴다.<br>'+
           '2차로 튀긴 후, 엉겨 붙지 않게 탕수육을 넓게 펴 놓는다.<br>'+
           '<탕수육 소스 만들기>다른 냄비에 튀길 때 사용한 식용유 세 스푼을 넣고 채 썬 양파와 어슷썰기한 당근을 넣는다.<br>'+
           '물, 간장, 설탕, 식초를 넣고 끓이다가 전분물을 조금씩 넣어 농도를 맞춰준다.<br>'+
           '.<br>'+
           'EAT!',0
        ))

#####동파육
##통삼겹(61),식용유(35),진간장(6),맛술(40),물엿(62),설탕(7),춘장(63),통후추(64),통마늘(65),양파(3),생강(66),대파(11),팔각(68)
c.execute('insert into recipe (recipeseq,food,category1,category2,image,ingredient,recipe,hits) values(recipe_seq.nextval,:1,:2,:3,:4,:5,:6,:7)',
          ('동파육','중식','면','dongpayuk.jpg','61,35,6,40,62,7,63,64,65,3,66,11,68',
           '삼겹살을 정사각형 모양으로 자른 뒤 비계에 십자모양으로 칼집을 낸다.<br>'+
           '프라이팬에 식용유를 두르고 삽겹살을 여섯방면 골고루 구워준다.(속까지 익히지 않아도 OK)<br>'+
           '삼겹살을 구운 냄비에 물 3컵과 함께 나머지 재료를 털어 넣어준다.<br>'+
           '(춘장은 잘 풀어주고 양파는 껍질째 넣는다. 팔각은 없다면 패스)<br>'+
           '약불에서 뚜껑 덮고 1시간 30분동안 졸인다.(남은 양념은 삶은 계란이나 메추리알을 담가 장조림으로 먹어도 좋다.)<br>'+
           'EAT!',0
        ))

###면
#####짜장면
##식용유(35),다진생강(42),돼지고기(57),양파(3),주키니 호박(69),볶은 춘장(63),굴소스(72),설탕(7),MSG(64),양배추(65),전분물(58),중화면(66)
c.execute('insert into recipe (recipeseq,food,category1,category2,image,ingredient,recipe,hits) values(recipe_seq.nextval,:1,:2,:3,:4,:5,:6,:7)',
          ('짜장면','중식','면','jjajangmyun.jpg','35,42,57,3,69,63,72,7,64,65,58,66',
           '웍에 기름을 넉넉히 두르고 다진 생강, 고기, 큼직히 썬 양파, 호박을 넣고 볶아준다.<br>'+
           '고기가 반쯤 익었다싶으면 설탕, msg를 넣고 더 볶아준다.<br>'+
           '큼직히 썬 양배추도 넣고 볶아준다.<br>'+
           '굴소스, 춘장을 넣고 볶다가 전분물로 농도를 맞춰준다.<br>'+
           '중화면을 삶아 짜장을 올린다.<br>'+
           'EAT!',0
        ))

#####해물짬뽕
##홍합(67),오징어(68),흰다리새우(69),중화면(66),양파(3),애호박(47),양배추(65),사골곰탕(70),고추기름(71),다진마늘(14),굴소스(72),고춧가루(21),소금(17),후추,MSG(64),치킨파우더(73)
c.execute('insert into recipe (recipeseq,food,category1,category2,image,ingredient,recipe,hits) values(recipe_seq.nextval,:1,:2,:3,:4,:5,:6,:7)',
          ('해물짬뽕','중식','면','haemuljjambbong.jpg','67,68,69,66,3,47,65,70,71,14,72,21,17,64,73',
           '끓는물에 중화면을 4분정도 삶아 찬물에 헹궈둔다.(강불)<br>'+
           '고추기름에 다진마늘을 약불에 볶다가 마늘이 노릇해지면 적당한 크기로 썬 양파, 애호박, 양배추를 넣어 중불에서 볶아준다.(약불→중불)<br>'+
           '채소의 숨이 죽으면 적당한 크기로 썬 오징어와 새우, 고춧가루, 굴소스, msg, 치킨파우더(없으면 패스)를 넣는다.<br>'+
           '오징어가 반즈음 익으면 사골곰탕육수를 넣고 바로 깨끗이 씻은 홍합을 넣고 소금, 후추로 간한다.(사골곰탕 육수를 넣어주면 더 맛있음)<br>'+
           '면을 국물에 30초 정도 토렴해준 뒤 그릇에 담고 위에 국물을 부어준다.<br>'+
           'EAT!',0
        ))

#####중화짬뽕
##물(13),치킨스톡(74),설탕(7),소금(17),진간장(6),식초(44),오이(75),계란(2),당근(31),새우(69),팽이버섯(76),생면(77),땅콩버터(78)
c.execute('insert into recipe (recipeseq,food,category1,category2,image,ingredient,recipe,hits) values(recipe_seq.nextval,:1,:2,:3,:4,:5,:6,:7)',
          ('중화짬뽕','중식','면','junghwajjambbong.jpg','74,7,17,6,44,78,2,31,69,76,77,78',
           '생수, 치킨스톡, 설탕, 소금, 진간장, 식초를 섞어 냉동실 둬 차갑게 한다.(살얼음이 껴도 OK)<br>'+
           '고명을 준비한다.(계란지단은 계란을 잘 풀어 프라이팬에 식용유를 두르고 최대한 약불에 익히기)<br>'+
           '새우를 면 끓는물에 새우색이 변할 때까지 데친다.<br>'+
           '면을 4분정도 삶고 찬물로 헹군 후 물기를 털어준다.(중화면이 없다면 칼국수 생면도 OK)<br>'+
           '뜨거운 면수 1스푼에 땅콩 버터 한스푼을 푼다.<br>'+
           '냉동실에 있던 육수를 붓고, 위에 고명과 땅콩버터 푼 것을 올려준다.<br>'+
           'EAT!',0
        ))

#####탄탄면
##생면(77).땅콩버터(78),사골육수(79),두반장(80),간장(6),라유(81),다진 파(41),다진마늘(14),다진고기-돼지고기목살(19),청경채(82),땅콩(83)
c.execute('insert into recipe (recipeseq,food,category1,category2,image,ingredient,recipe,hits) values(recipe_seq.nextval,:1,:2,:3,:4,:5,:6,:7)',
          ('탄탄면','중식','면','tantanmyun.jpg','78,79,80,6,81,41,14,19,82,83',
           '라유(고추기름)을 두르고 다진 파, 다진 마늘, 다진고기, 간장 반스푼, 두반장 반스푼을 넣고 볶는다.(다진파, 다진 마늘은 반 남기기)<br>'+
           '면 삶을 물이 끓으면 6등분한 청경채를넣어 3초 데치고 꺼낸다.<br>'+
           '면을 3-4분정도 삶고 익으면 찬물에 헹군다.<br>'+
           '사골육수를 1/4만 붓고 땅콩버터, 고명 만들고 남은 파, 마늘, 두반장, 간장을 넣고 잘 풀어준다.<br>'+
           '나머지 육수를 넣고 끓인다.<br>'+
           '면에 육수를 넣고 청경채, 고기토핑, 견과류 부신거, 쨔사이(없으면 패스)를 올린다.<br>'+
           'EAT!',0
        ))

###밥
#####중식볶음밥
##대파(11),당근(31),계란(2),밥(4),식용유(35),소금(17)
c.execute('insert into recipe (recipeseq,food,category1,category2,image,ingredient,recipe,hits) values(recipe_seq.nextval,:1,:2,:3,:4,:5,:6,:7)',
          ('중식볶음밥','중식','밥','jungsikbab.jpg','11,31,2,4,35,17',
           '당근은 1~2 센치 간격으로 세조각 썰어서 잘게 다진다.(밥은 고슬하게)<br>'+
           '식용유 8스푼을 냄비에 붓고 중~강불로 예열한다.<br>'+
           '계란 2개를 투입한다.<br>'+
           '계란이 익기전에 휙휙 저어준다.(스크램블)<br>'+
           '계란이 익으면 밥을 넣고 볶는다.(가스불 화력에 따라 중/강불 조절)<br>'+
           '볶아진 밥에 소금 세꼬집을 뿌린다.<br>'+
           '틈틈히 볶아주면서 야채를 투입한다.<br>'+
           '야채가 익을 때 까지 볶아준다.<br>'+
           '+) 취향에 따라 계란후라이를 올린다.<br>'+
           'EAT!',0
        ))

#####새우볶음밥
##계란(2),대파(11),냉동새우(69),진간장(6),참기름(37),통깨(26)
c.execute('insert into recipe (recipeseq,food,category1,category2,image,ingredient,recipe,hits) values(recipe_seq.nextval,:1,:2,:3,:4,:5,:6,:7)',
          ('새우볶음밥','중식','밥','saeubab.jpg','2,11,69,6,37,26',
           '팬에 올리브 기름을 살짝 두르고 파를 볶아 파기름을 준비한다.<br>'+
           '볶은 파를 한쪽으로 치우고 계란 2개를 올린다.<br>'+
           '계란은 스크램블로 만든다.<br>'+
           '스크램블이 완성이 되었다면 볶은 파와 섞어준다.<br>'+
           '프라이팬 모퉁이에 새우를 볶아준다.<br>'+
           '새우와 파와 스크램블을 함께 섞어주고 간을 맞추기 위해서 간장으로 간을 맞춰준다.<br>'+
           '간이 골고루 배도록 잘 섞어준다.<br>'+
           '고소함을 더해 주기 위해서 참기름도 1t 추가한다.<br>'+
           '그릇에 담아 위에 통깨를 살짝 뿌린다.<br>'+
           'EAT!',0
        ))


##########일식
###밥
#####치킨마요덮밥
##치킨(1),계란(2),깐양파(3),밥(4),마요네즈(5),진간장(6),설탕(7)
c.execute('insert into recipe (recipeseq,food,category1,category2,image,ingredient,recipe,hits) values(recipe_seq.nextval,:1,:2,:3,:4,:5,:6,:7)',
          ('치킨마요덮밥','일식','밥','chickenmayo.jpg','1,2,3,4,5,6,7',
           '계란 2개를 풀어 계란물을 만든다.<br>'+
           '팬에 기름을 두르고 계란물을 붓는다.<br>'+
           '젓가락을 이용해 에그 스크램블을 만든다.<br>'+
           '준비된 밥에 스크램블을 올린다.<br>'+
           '치킨을 구워준다.<br>'+
           '치킨이 구워지는 동안 양파 반개를 썰어준다.<br>'+
           '치킨이 다 구워지면 가위를 이용하여 먹기 좋게 잘라준다.<br>'+
           '팬에 기름을 두르고 양파를 볶아준다.<br>'+
           '양파가 투명해질때 간장 1스푼, 설탕 0.5스푼을 넣고 마저 볶아준다.<br>'+
           '밥위에 볶음 양파, 치킨을 올리고 마요네즈를 뿌린다.<br>'+
           'EAT!',0))
#####스팸 돈부리 덮밥
##양파(3),계란(2),밥(4),간장(6),설탕(7),대파(11),맛술(40),참기름(37),후추(27),스팸(84)
c.execute('insert into recipe (recipeseq,food,category1,category2,image,ingredient,recipe,hits) values(recipe_seq.nextval,:1,:2,:3,:4,:5,:6,:7)',
          ('스팸 돈부리 덮밥','일식','밥','spamdonburi.jpg','3,2,4,6,7,11,40,37,27,84',
           '스팸을 1cm 두께로 자른다.<br>'+
           '스팸을 팬에 넣고 중불에 노릇노릇하게 익을 때까지 굽는다.<br>'+
           '잘게 다진 양파 0.5개와 대파 0.5개를 넣고 투명해질 때까지 볶는다.<br>'+
           '계란 2개에 소금과 후추를 넣고 풀어준다.<br>'+
           '팬에 기름을 두르고 젓가락을 이용하여 스크램블을 만든다.<br>'+
           '작은 그릇에 간장 2큰술, 설탕 1큰술, 맛술 2큰술, 참기름 0.5큰술을 넣고 섞는다.<br>'+
           '소스를 스팸 볶음에 넣고 끓여준다.<br>'+
           '밥을 그릇에 담는다.<br>'+
           '밥 위에 스팸 볶음과 스크램블 에그를 올린 후 소스를 뿌려준다.<br>'+
           'EAT!',0))
#####규동 소고기 덮밥
##불고기용 소고기(38),계란(2),쪽파(39),양파(3),밥(4),모란봉 규동소스(85)
c.execute('insert into recipe (recipeseq,food,category1,category2,image,ingredient,recipe,hits) values(recipe_seq.nextval,:1,:2,:3,:4,:5,:6,:7)',
          ('규동 소고기 덮밥','일식','밥','gyudong.jpg','38,2,39,3,4,85',
           '양파 0.5개는 길게, 쪽파 2줄은 잘게 썰어 준다.<br>'+
           '소고기는 먹기 좋은 크기로 썰어준다.<br>'+
           '규동소스 30g에 물 50g을 희석하여 소스를 만든다.<br>'+
           '팬에 소고기를 굽는다.<br>'+
           '소고기가 거의 다 구워졌으면 양파를 넣고 같이 살짝만 볶아준다.<br>'+
           '물에 희석시킨 규동소스를 붓고 섞어준 후 센 불에서 끓여준다.<br>'+
           '소스가 조금 남을때까지 졸인 후 밥 위에 얹는다.<br>'+
           'EAT!',0))

### 면
##### 돈코츠 라멘
##### 삼겹살(61),숙주나물(86),사골곰탕(70),소면(87),김(88),계란(2),대파(11),소금(17),후추(27),다진마늘(14),쯔유(89),간장(6),맛술(40),쌈장(90)
c.execute('insert into recipe (recipeseq,food,category1,category2,image,ingredient,recipe,hits) values(recipe_seq.nextval,:1,:2,:3,:4,:5,:6,:7)',
          ('돈코츠 라멘','일식','면','doncozramen.jpg','61,86,70,87,88,2,11,17,27,14,89,6,40,90',
           '끓는 물에 삼겹살을 잠길정도로 넣는다.<br>'+
           '맛술 2큰술, 쯔유 1큰술, 간장 1큰술을 넣는다.<br>'+
           '뚜껑을 덮고 중불로 졸여준다.<br>'+
           '냄비에 물과 소금을 넣고 달걀을 2개 넣어 9~10분 정도 삶아 반숙으로 준비한다.<br>'+
           '달군 후라이팬에 김 2장을 앞뒤로 구워준다.<br>'+
           '김을 먹기 좋은 사이즈로 잘라준다.<br>'+
           '고명으로 올릴 대파도 잘게 썰어준다.<br>'+
           '끓는 물에 소면을 삶아준다.(찬물을 부어가며 끓인다.)<br>'+
           '냄비에 사골 곰탕 500g 2팩을 넣고 끓인다.<br>'+
           '국물이 끓으면 쌈장 1작은술을 넣고 소금과 후추로 간을 해준다.<br>'+
           '그릇에 다진 마늘 1큰술, 숙주 한줌을 넣어준다.<br>'+
           '그 위에 소면 → 육수 → 대파 → 고기 → 계란 → 김 순으로 올려준다.<br>'+
           'EAT!',0))

##### 야끼소바
##### 불고기 200g (38), 양파1/4(3),양배추1/2주먹(65),숙주나물150g(86),우동사리 200g(91),느타리버섯(32), 생강 엄지 한마디(66), 식용유(35), 간장1T(6),맛술1/2T(40), 설탕1/2T(7), 스리랏차소스3T(92)
c.execute('insert into recipe (recipeseq,food,category1,category2,image,ingredient,recipe,hits) values(recipe_seq.nextval,:1,:2,:3,:4,:5,:6,:7)',
          ('야끼소바','일식','면','yakisoba.jpg','38,3,65,86,91,32,66,35,6,40,7,92',
           '양파 1/4개, 양배추 1/2주먹을 채썰고 숙주나물 150g, 느타리버섯을 다듬는다.<br>'+
           '우동사리 200g을 끓는 물에 2분 삶아준다.<br>'+
           '식용유로 달군 팬에 생강을 넣어 향을 입힌다.<br>'+
           '불고기 200g을 먼저 팬에 넣어 볶는다.<br>'+
           '고기가 익어갈 때 센 불로 손질한 야채들을 넣고 볶아준다.<br>'+
           '야채가 익었다면 면을 넣어준다.<br>'+
           '간장 1T, 맛술 0.5T, 설탕 0.5T를 섞어 넣어 간을 맞춘다.<br>'+
           '스리라차 소스 3T를 넣고 30초간 더 볶아준다.<br>'+
           '+) 반숙 계란후라이를 올려 먹기<br>'+
           'EAT!',0))

##### 메밀소바
##### 메밀면(93), 메밀소바장국(94), 김(88), 와사비(95), 양파(3), 대파(11)
c.execute('insert into recipe (recipeseq,food,category1,category2,image,ingredient,recipe,hits) values(recipe_seq.nextval,:1,:2,:3,:4,:5,:6,:7)',
          ('메밀소바','일식','면','memilsoba.jpg','93,94,88,95,3,11',
           '장국 1: 물 6 비율로 메밀장국을 만든다.<br>'+
           '냄비에 물 800ml를 넣고 끓을 때 면을 넣어 40초간 끓여준다.<br>'+
           '해면된 면을 3~4번 찬물에 헹구고 체에 받쳐 물기를 뺀다.<br>'+
           '만들어둔 장국에 면을 넣는다.<br>'+
           '면 위에 김, 와사비, 양파, 대파를 기호껏 넣는다..<br>'+
           'EAT!',0))

### 간식
##### 오코노미야키
##### 양배추(65), 베이컨(96), 계란(2), 튀김가루(97), 가쓰오부시(98), 데리야끼소스(99), 마요네즈(5), 식용유(35)
c.execute('insert into recipe (recipeseq,food,category1,category2,image,ingredient,recipe,hits) values(recipe_seq.nextval,:1,:2,:3,:4,:5,:6,:7)',
          ('오코노미야키','일식','간식','okonomiyaki.jpg','65,96,2,97,98,99,5,35',
           '양배추 200g을 채 썰어 물로 행군 후 물기를 빼준다.<br>'+
           '물기가 빠진 양배추에 튀김가루 2컵(400ml), 계란 1개를 넣어 준다.<br>'+
           '베이컨 130g을 취향껏 잘라 넣어주고 물을 100ml정도 넣어준다.<br>'+
           '물을 조금씩 넣어주며 점도를 조절해 준다.<br>'+
           '팬에 식용유를 두르고 달궈지면 반죽을 넣고 구워준다.<br>'+
           '다 익은 오코노미야키를 접시에 담는다.<br>'+
           '오코노미야키 윗 면에 데리야키 소스, 마요네즈를 골고루 발라주고 가쓰오부시를 올려준다.<br>'+
           'EAT!',0))

##### 차왕무시
##### 칵테일 새우(100), 계란(2), 다시마(101), 소금(17), 우유(102)
c.execute('insert into recipe (recipeseq,food,category1,category2,image,ingredient,recipe,hits) values(recipe_seq.nextval,:1,:2,:3,:4,:5,:6,:7)',
          ('차왕무시','일식','간식','chawangmusi.jpg','100,2,101,17,102',
           '칵테일 새우 4개 정도 찬물로 해동시켜 뜨거운 물에 10초간 담군다.<br>'+
           '물에 다시마 4개를 넣고 끓여 육수를 만든다.<br>'+
           '계란 4개를 채망에 걸러 알을 제거한다.<br>'+
           '우유 2T, 맛술 1T, 소금 0.5T, 육수 1컵을 넣고 다시 섞어 용기에 담는다.<br>'+
           '찜기에 물을 넣고 끓인다.<br>'+
           '물이 끓으려 할 때, 그릇을 넣어주고 거즈로 덮은 후 찜기 뚜껑을 닫는다.<br>'+
           '중불로 5~6분 정도 찌고 뚜껑을 열어 칵테일 새우를 넣어준다.<br>'+
           '다시 거즈와 뚜껑을 닫고 5분 정도 쪄준다.<br>'+
           'EAT!',0))

##### 당고
##### 건식 찹쌀가루(103), 소금(17), 진간장(6), 설탕(7), 맛술(40), 옥수수전분(104)
c.execute('insert into recipe (recipeseq,food,category1,category2,image,ingredient,recipe,hits) values(recipe_seq.nextval,:1,:2,:3,:4,:5,:6,:7)',
          ('당고','일식','간식','dango.jpg','103,17,6,7,40,104',
           '건식 찹쌀가루 200g을 담고 소금 0.3T를 넣는다.<br>'+
           '뜨거운 물을 조금씩 부어 질지 않게 식을 떄까지 숟가락으로 섞는다.<br>'+
           '손으로 치대면서 매끈해 질 때까지 반죽해준다.<br>'+
           '일정한 크기로 조금씩 떼어내어 동글하게 빚어준다.<br>'+
           '끓는 물에 동그랗게 빚은 찹쌀반죽을 넣고 저어가며 익혀준다.<br>'+
           '찹쌀반죽이 위로 뜨면 2~3분 더 익힌 후 꺼내준다.<br>'+
           '얼음물에 반죽을 1~2분 정도 식힌 후 채에 받쳐 물기를 빼준다.<br>'+
           '물기가 빠지면 꼬지에 4알씩 꽂아준다.<br>'+
           '팬에 식용유를 두르고 앞뒤로 노릇하게 구워준다.<br>'+
           '소스 만들기: 냄비에 간장 20g, 설탕 40g, 물 100g, 맛술 30g, 옥수수 전분 10g을 넣어준다. <br>'+
           '거품기로 저어서 전분을 풀어준 후 중불에서 계속 저으면서 끓인다.<br>'+
           '소스가 투명해지고 약간 걸쭉해지면 불을 끈다.<br>'+
           '숟가락으로 소스를 떠서 앞뒤로 발라준다.<br>'+
           'EAT!',0))

##########양식
###면
###밥
#####요리
##음식이름
##재료
#c.execute('insert into recipe (recipeseq,food,category1,category2,image,ingredient,recipe,hits) values(recipe_seq.nextval,:1,:2,:3,:4,:5,:6,:7)',
#          ('음식이름','양식','2차 카테고리','음식사진src','재료시퀀스번호만나열,필수',
#           '.<br>'+
#           'EAT!',0))#EAT은 항상 붙이기


##########cookcommunity
##공지사항
c.execute('insert into cookcommunity (community_num, community_id, community_title, community_content, community_date, community_update_date, community_readcnt)' +
          'values(community_num_seq.nextval, :1, :2, :3, :4, :5, :6)',('admin','오픈 공지','오픈 예상 날짜는 2024년 12월 9일입니다! 많관부!',today,today,0))
c.execute('insert into cookcommunity (community_num, community_id, community_title, community_content, community_date, community_update_date, community_readcnt)' +
          'values(community_num_seq.nextval, :1, :2, :3, :4, :5, :6)',('admin','레시피 공지','원하는 레시피가 없다면? 커뮤니티 타이틀에 [건의]를 붙여 글을 올려주세요.',today,today,0))
c.execute('insert into cookcommunity (community_num, community_id, community_title, community_content, community_date, community_update_date, community_readcnt)' +
          'values(community_num_seq.nextval, :1, :2, :3, :4, :5, :6)',('admin','게시판 공지','타인을 향한 악의적인 댓글, 비방, 욕설 등의 게시글, 댓글은 별도의 경고 없이 유저 차단 조치 합니다.',today,today,0))
##자유게시판
c.execute('insert into cookcommunity (community_num, community_id, community_title, community_content, community_date, community_update_date, community_readcnt)' +
          'values(community_num_seq.nextval, :1, :2, :3, :4, :5, :6)',('test1234','오늘 뭐 먹지?','제곧내',today,today,0))
##자유게시판 댓글
c.execute('insert into cookcomment (comment_num, comment_id, comment_content, comment_date, comment_update_date, community_num, indent, step)' +
          'values(comment_num_seq.nextval, :1, :2, :3, :4, :5, :6, :7)',('admin','이걸 위해 나온게 바로! 뭐 먹지? 랜덤 뽑기 기능입니다! 많관부♥',today,today,10004,0,1))
c.execute('insert into cookcomment (comment_num, comment_id, comment_content, comment_date, comment_update_date, community_num, indent, step)' +
          'values(comment_num_seq.nextval, :1, :2, :3, :4, :5, :6, :7)',('test1234','ㅋㅋㅋㅋㅋㅋㅋ셀프홍보다!!!',today,today,10004,10001,0))

connect.commit()
print('완료')