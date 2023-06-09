# payhere_assignment

Django version : 4.2

DB : mysql 5.7

DB diagram

<img width="821" alt="image" src="https://user-images.githubusercontent.com/69445075/233576794-9ee761d6-b945-472a-945b-d6e3251de41f.png">

## JWT 토큰 발급 api

access 토큰과 refresh 토큰 발급 
/api/token/

<img width="1337" alt="image" src="https://user-images.githubusercontent.com/69445075/234506525-3a64a925-c0fa-4142-895c-243e01c6c260.png">

access 토큰 리프레시  
/api/token/refresh

<img width="1375" alt="image" src="https://user-images.githubusercontent.com/69445075/234506634-df1cf069-6476-46f3-af33-b0374d5c4147.png">

## 기능 api 

### 회원가입 

POST /caffe/signup 

body { "username": phone, "password": password } 

### 상품 리스트 

GET /caffe/(int:page)/ access token 필요

<img width="1702" alt="image" src="https://user-images.githubusercontent.com/69445075/234546218-e255d607-d7c2-4fd2-a254-75dd126ec01e.png">


### 상품 검색 

GET /caffe/(int:page)/(string:keyword)/ access token 필요

### 상품 등록 

POST /caffe/ access token 필요

body { "category": "coffee", "price":3000, "origin_price":300, "name": "아이스 카페라떼", "info": "ice latte", "barcode":"!!!|||11||", "big_size":false }

### 상품 수정 

PUT /caffe/(int:pk)/ access token 필요

body { "category": "coffee", "price":3000, "origin_price":300, "name": "아이스 카페라떼", "info": "ice latte", "barcode":"!!!|||11||", "big_size":false }

### 상품 상세 정보 

GET /caffe/(int:pk)/ access token 필요

### 상품 삭제 

DELETE /caffe/(int:pk)/ access token 필요


## DB 마이그레이션 후 

<img width="598" alt="image" src="https://user-images.githubusercontent.com/69445075/234509019-1188e145-4b55-4e20-91a0-865b8c28182f.png">


## Serializer 확인 

python manage.py shell

<img width="614" alt="-optanaconda3Libpython3 9site-packagesrest frameworkserializers py ir" src="https://user-images.githubusercontent.com/69445075/233790345-4b23c618-24c4-4615-b376-071097fa45ed.png">

<img width="637" alt="In  2  s2 - ProductSerializer()" src="https://user-images.githubusercontent.com/69445075/233790361-2d40537e-6d4c-47cb-9ab5-ba862b08e81e.png">
