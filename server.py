import socket
import cv2

# #需要一直监听树莓派有没有数据传过来
# server = socket.socket()
# server.bind(('192.168.43.179',6969)) #绑定要监听端口
# server.listen(5) #监听
#
# print("我要开始等电话了")
#
# while True:
#     conn, addr = server.accept()  # 等电话打进来
#
#     # conn就是客户端连过来而在服务器端为其生成的一个连接实例
#     print(conn, addr)
#     print("电话来了")
#
#     count = 0
#
#     while True:
#         data = conn.recv(1024)
#
#         print("recv:",data)
#
#         if data==1:
#             GetVideoFromPI()
#
#         if not data:
#             print("client has lost...")
#             break
#         conn.send(data.upper())
#
#         count+=1
#         if count >10:
#             print('count %',count)
#             break
#
# server.close()
def GetVideoFromPI():
    #直接访问树莓派摄像头
    #stream_addr2:视频文件路径  'rtsp://192.168.1.115:9554/webcam'
    stream_addr2 ='D:\dino.mp4'
    cap = cv2.VideoCapture(stream_addr2)

    while (True):
        ret, frame = cap.read()
        cv2.imshow('capture', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return

GetVideoFromPI()