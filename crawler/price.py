import websocket


def on_message(ws, message):
    print(message)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    print("### opened ###")


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://sim-quotesdk.mktdata.cn/quote",
                                header={
                                    'Pragma': 'no-cache',
                                    'Origin': 'http://www.cninfo.com.cn',
                                    'Accept-Language': 'zh-CN,zh;q=0.9',
                                    'Sec-WebSocket-Key': '81zlRxAPYhYcwYcwL0motw==',
                                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
                                    'Upgrade': 'websocket',
                                    'Cache-Control': 'no-cache',
                                    'Sec-WebSocket-Protocol': 'ncloud',
                                    'Connection': 'Upgrade',
                                    'Sec-WebSocket-Version': '13',
                                    'Sec-WebSocket-Extensions': 'permessage-deflate; client_max_window_bits'
                                },
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
