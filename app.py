from flask import Flask, request

app = Flask(__name__)

@app.route('/capture', methods=['GET'])
def capture():
    # GET 요청의 "flag" 매개변수를 가져와 로그에 기록합니다.
    flag = request.args.get('flag')
    if flag:
        print(f"Captured FLAG: {flag}")
        # 플래그를 파일에 저장할 수도 있음
        with open("captured_flags.txt", "a") as file:
            file.write(f"{flag}\n")
        return "FLAG captured successfully", 200
    return "No flag received", 400

# 서버 실행
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)