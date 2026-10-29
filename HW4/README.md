# HW4 : todo 앱에 API 더하기
## 더한 것
- 설명 칸(note)을 API 로도 주고받게 했습니다.
- GET /api/todos/?done=true 로 완료한 것만 골라 받게 했습니다.
## 실행하는 법
pip install -r requirements.txt
flask --debug run
화면 http://127.0.0.1:5000/
문서 http://127.0.0.1:5000/api/docs
## 화면
### 1. 주소 여섯 줄이 모두 보이는 문서
<img width="1654" height="1070" alt="image" src="https://github.com/user-attachments/assets/bbba143a-5fc5-43c5-8bde-b310f03a0c65" />
### 2. note 를 넣어 만들었더니 201 이 온 모습
<img width="1596" height="564" alt="image" src="https://github.com/user-attachments/assets/c5cbf69a-7713-4f06-8504-c6f081e6f15d" />
### 3. 없는 번호를 불렀더니 404 가 온 모습
<img width="1608" height="466" alt="image" src="https://github.com/user-attachments/assets/3fd18a00-d8bb-494f-8ed9-ed2e8549db23" />
