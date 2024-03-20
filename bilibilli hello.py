import requests
url = 'https://api.live.bilibili.com/msg/send' 

headers={
    'origin': 'https://live.bilibili.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    'cookie':"buvid3=2CEFCDD4-CFD0-62FA-03CF-6987AC30258282605infoc; b_nut=1706582983; _uuid=7B710E9DB-6A41-7103A-B5B8-47778B1081FFE99278infoc; hit-dyn-v2=1; buvid_fp_plain=undefined; SESSDATA=f5c3fdc8%2C1722136707%2Cf9a4e%2A12CjCUBYedNECx-eU2JaBFiCaHpOUP7eN_041ld8O9cwZ1NgTq2wyh184QYx7g-UpJygMSVjdEUGlWNUtkdjdZd2k3QzMwV2NiakdjQlJkWnZlNTR1RWV4Z0RmTGdwQVZMWFdlWUJZZ0dFSFlYblF1QnRYV3p2bFllTWg3Z1VRbE1lQkNxbWxnZmhnIIEC; bili_jct=c84e3f38982d3eb1156dfebb7e181ff5; DedeUserID=272821847; DedeUserID__ckMd5=5b82c3a0642ba28f; sid=6pulm97c; LIVE_BUVID=AUTO9817065847381573; CURRENT_FNVAL=4048; rpdid=|(u))|kYkJJl0J'u~|YY|lRJm; CURRENT_QUALITY=80; enable_web_push=DISABLE; header_theme_version=CLOSE; buvid4=6737C565-DA63-402E-9988-7EA2CC23243782605-024013002-MK6BGhp8PAZvP%2BlvKwV44g%3D%3D; fingerprint=46dde2f6d652c566bb7051c0214992cf; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDgyNTcxOTYsImlhdCI6MTcwNzk5NzkzNiwicGx0IjotMX0.KneUMTcrTN55v7x68y50seqgLFmu_BNCjjUliBWtYyA; bili_ticket_expires=1708257136; home_feed_column=5; browser_resolution=1920-919; buvid_fp=d0d8d83a5e3fe6ee1f8a5756bd8a4ca3; bp_video_offset_272821847=898678269832855592; b_lsid=3A4D4BD9_18DB20EECA8; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1707813881,1707980331,1708065075,1708090367; PVID=8; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1708090533"} # type: ignore

data = {
'bubble': '0',
'msg': '阿枯晚上好',
'color': '5816798',
'mode': '1',
'fontsize': '25',
'rnd': '1708090481',
'roomid': '21669627',
'csrf': 'c84e3f38982d3eb1156dfebb7e181ff5',
'csrf_token': 'c84e3f38982d3eb1156dfebb7e181ff5'
}


result =  requests.post(url=url, headers=headers, data=data).text      
print("result:", result)       