import requests

def send_line_notify(token, message):
    """
    發送 LINE Notify 訊息的函式

    :param token: LINE Notify 權杖
    :param message: 要發送的訊息
    """
    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    data = {
        "message": message
    }
    response = requests.post(url, headers=headers, data=data)
    return response.status_code

if __name__ == "__main__":
    # 請將 'YOUR_ACCESS_TOKEN' 替換為您的 LINE Notify 權杖
    access_token = 'FXVGdF2ffKqt85EWiSPGctGfLAIpzWBzyEseo18L4r3'
    message = '這是一個測試訊息'
    status_code = send_line_notify(access_token, message)
    if status_code == 200:
        print("訊息發送成功")
    else:
        print(f"訊息發送失敗，狀態碼：{status_code}")
