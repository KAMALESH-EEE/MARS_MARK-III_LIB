class DS:
    Id='01_'
    def check():
        print(DS.Id+'C_')
        i_data=input()
        datas=i_data.split('_')
        if(datas[0]=='01' and datas[1]=='s'):
            return True
        else:
            return False
        
    def stop():
        data=DS.Id+'0_'+'0_'
        print(data)

    def forward():
        data=DS.Id+'0_'+'1_'
        print(data)
    
    def reverse():
        data=DS.Id+'0_'+'2_'
        print(data)

    def left():
        data=DS.Id+'-90_'+'1_'
        print(data)

    def right():
        data=DS.Id+'90_'+'1_'
        print(data)

    def move(deg,di):
        data=DS.Id+str(deg)+'_'+str(di)+'_'
        print(data)


class SM:
    Id='03_'

    def check():
        print(SM.Id+'C_')
        i_data=input()
        datas=i_data.split('_')
        if(datas[0]=='03' and datas[1]=='s'):
            return True
        else:
            return False

    def DHT():
        data=SM.Id+'1_'
        print(data)
        i_data=input()
        datas = i_data.split('_')
        if datas[0] == '03':
            return datas[1:3]
        else:
            return None,None
        
