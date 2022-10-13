from hashlib import sha256
import hmac

def main():
    serverSeed = "522be90560c64dd44480a1da68ae01d4fd344341646a13321abe14bcfc16615d"
    clientSeed = "f3nz1JkA2k"
    nonce = "6"
    cursor = 0  # 默认为0
    data = str(clientSeed) + ":" + str(nonce) + ":" + str(cursor)
    un = num(i=data,x=serverSeed)
    print("得出结果：",un)
def num(i,x):
    x = hmac_sha256(data=i, key=x)
    d = [x[0:2], x[2:4], x[4:6], x[6:8]]
    e = 0
    v = 0
    for i in d:
        v = v + 1
        inx = int(i, 16)
        if inx < 100:
            inx = -inx
        stn = "%.12f" % float(inx / (256 ** v))
        Set = stn.replace('-', '')
        e = e + float(Set)
    n = "%.12f" % e
    m = float(n) * 16777216
    num = 16777216 / int(m + 1) * 0.99
    return num

def hmac_sha256(key, data):
    key = key.encode('utf8')
    data = data.encode('utf8')
    encrypt_data = hmac.new(key, data, digestmod=sha256).hexdigest()
    return encrypt_data

if __name__ == '__main__':
    main()