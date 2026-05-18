from fastapi.responses import HTMLResponse
from fastapi import APIRouter, Form
from db import get_db, UserDB
from sqlalchemy.orm import Session
from pydantic import BaseModel

router = APIRouter()
class User(BaseModel):
    name: str
    age: int

@router.get("/", response_class=HTMLResponse)
def root():
    return """
    <html>
        <body>
            <h1>나의 첫 웹 페이지</h1>
            <p>FastAPI가 HTML을 반환했습니다.</p>

            <hr>

            <h2>기능 선택</h2>

            <h2>나만의 질의응답기 with local LLM</h2>
            <form action="/ask" method="post">
                <p> 
                    프롬포트 : <input type="text" name="prompt">
                </p>
                <button type="submit">질문하기</button>
            <form>

           <h2>덧셈</h2>
            <form action="/add" method="get">
            <p>
                a: <input type="number" name="a" value="10">
            </p>
            <p>
                b: <input type="number" name="b" value="20">
            </p>
            <button type="submit">덧셈 실행</button>
            </form>
            <hr>

            <h2>뺼셈</h2>
            <form action="/minus" method="get">
            <p>
                a: <input type="number" name="a" value="10">
            </p>
            <p>
                b: <input type="number" name="b" value="20">
            </p>
            <button type="submit">뺼셈 실행</button>
            </form>

           

            <hr>

            <h2>사용자 등록</h2>
            <form action="/register" method="post">
                <p>이름: <input type="text" name="name" value="sdkim"></p>
                <p>나이: <input type="text" name="age" value="20"></p>
                <button type="submit">사용자 등록</button>
            </form>

            <hr>

            <h2>사용자 로그인</h2>
            <form action="/login" method="get">
                <p>이름: <input type="text" name="name" value="sdkim"></p>
                <p>비밀번호: <input type="text" name="password" value="1234"></p>
                <button type="submit">사용자 로그인</button>
            </form>

            <hr>

            <h2>비밀번호 수정</h2>
            <form action="/modify" method="get">
                <p>이름: <input type="text" name="name" value="sdkim"></p>
                <p>새 비밀번호: <input type="text" name="newpassword" value="4321"></p>
                <button type="submit">비밀번호 수정</button>
            </form>
        </body>
    </html>
    """



@router.get("/add")
def add(a: int, b: int):
    
    result = a + b
    return {"result": result}

@router.get("/minus")
def minus(a: int, b: int):
  
    result = a - b
    return { "result": result}

    result = a + b
    return {"result": result}


@app.get("/minus")
def minus(a: int, b: int):

    # Check if b is zero and return error message if true
    if b == 0:
        return {"error": "Cannot divide by zero"}
    else:
    result = a - b


        return {"result": result}
