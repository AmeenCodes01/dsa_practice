#failed interview task :((

def getReqStatus(requests):
    res = {}
    ans= []
    success = "{status: 200, message: OK}"
    err = "{status: 429, message: Too many requests}"
    
    for i,req in enumerate(requests):
        if req not in res:
            res[req]=[i,1]
            ans.append(success)
        else:
            #if exist, check diff. --> condition
        
            t = (i - res[req][0])
            
            if t<=5:
                if res[req][1]<2:
                    res[req]=[i,res[req][1]+1]
                    ans.append(success)
                else:
                    ans.append(err)
            elif t >5 and t <= 30:
                if res[req][1]<5:
                    res[req]=[i,res[req][1]+1]
                    ans.append(success)
                else:
                    ans.append(err)
            else:
                if t > 30:
                    res[req][1]=0
                    
                           
    print(ans)
reqs = ['www.eeebebb.com', 'www.acaaaed.com', 'www.dccbece.com', 'www.cdddcca.com', 'www.cddbadc.com', 'www.cddbadc.com', 'www.bdddabd.com', 'www.cccbeae.com', 'www.cccbeae.com', 'www.cddbadc.com', 'www.cddbadc.com', 'www.eabbaac.com', 'www.eeebebb.com', 'www.cdddcca.com', 'www.abecadb.com', 'www.cdddcca.com', 'www.bdddabd.com', 'www.acaaaed.com', 'www.cdddcca.com', 'www.eabbaac.com', 'www.dccbece.com', 'www.ebaacbd.com', 'www.bdddabd.com', 'www.ebaacbd.com', 'www.abecadb.com', 'www.abecadb.com', 'www.abecadb.com', 'www.eeebebb.com', 'www.eeebebb.com', 'www.ebaacbd.com', 'www.cdddcca.com', 'www.ebaacbd.com', 'www.cdddcca.com', 'www.cdddcca.com', 'www.bdddabd.com', 'www.cdddcca.com', 'www.cdddcca.com', 'www.acaaaed.com', 'www.dccbece.com', 'www.acaaaed.com', 'www.bdddabd.com', 'www.cccbeae.com', 'www.cccbeae.com', 'www.bdddabd.com', 'www.dccbece.com', 'www.bdddabd.com', 'www.abecadb.com', 'www.ebaacbd.com', 'www.acaaaed.com', 'www.cddbadc.com', 'www.bdddabd.com', 'www.cccbeae.com', 'www.ebaacbd.com', 'www.eabbaac.com', 'www.dccbece.com', 'www.abecadb.com', 'www.dccbece.com', 'www.abecadb.com', 'www.ebaacbd.com', 'www.cddbadc.com', 'www.abecadb.com', 'www.abecadb.com', 'www.eabbaac.com', 'www.ebaacbd.com', 'www.abecadb.com', 'www.ebaacbd.com', 'www.eabbaac.com', 'www.cddbadc.com', 'www.cdddcca.com', 'www.cddbadc.com', 'www.acaaaed.com', 'www.bdddabd.com', 'www.cccbeae.com', 'www.acaaaed.com', 'www.cddbadc.com', 'www.ebaacbd.com', 'www.cdddcca.com', 'www.acaaaed.com', 'www.eabbaac.com', 'www.eeebebb.com', 'www.cdddcca.com', 'www.eabbaac.com', 'www.acaaaed.com', 'www.acaaaed.com', 'www.eeebebb.com', 'www.eabbaac.com', 'www.eeebebb.com', 'www.eeebebb.com', 'www.bdddabd.com', 'www.ebaacbd.com', 'www.cddbadc.com', 'www.eeebebb.com', 'www.cccbeae.com', 'www.dccbece.com', 'www.cdddcca.com', 'www.cccbeae.com', 'www.bdddabd.com', 'www.acaaaed.com', 'www.eabbaac.com', 'www.cdddcca.com', 'www.cccbeae.com', 'www.acaaaed.com', 'www.dccbece.com', 'www.dccbece.com', 'www.abecadb.com', 'www.bdddabd.com', 'www.acaaaed.com', 'www.abecadb.com', 'www.ebaacbd.com', 'www.cddbadc.com', 'www.abecadb.com', 'www.cddbadc.com', 'www.cddbadc.com', 'www.eeebebb.com', 'www.abecadb.com', 'www.acaaaed.com', 'www.ebaacbd.com', 'www.bdddabd.com', 'www.cddbadc.com', 'www.bdddabd.com', 'www.eeebebb.com', 'www.cddbadc.com', 'www.cdddcca.com', 'www.eabbaac.com', 'www.cdddcca.com', 'www.cddbadc.com', 'www.cdddcca.com', 'www.cddbadc.com', 'www.cddbadc.com', 'www.bdddabd.com', 'www.abecadb.com', 'www.eeebebb.com', 'www.eeebebb.com', 'www.eeebebb.com', 'www.acaaaed.com', 'www.cccbeae.com', 'www.abecadb.com', 'www.bdddabd.com', 'www.cddbadc.com', 'www.eabbaac.com', 'www.cddbadc.com', 'www.ebaacbd.com', 'www.eeebebb.com', 'www.cdddcca.com', 'www.cdddcca.com', 'www.dccbece.com', 'www.eabbaac.com', 'www.abecadb.com', 'www.eabbaac.com', 'www.cdddcca.com', 'www.cccbeae.com', 'www.ebaacbd.com', 'www.eabbaac.com', 'www.cccbeae.com', 'www.eeebebb.com', 'www.ebaacbd.com', 'www.ebaacbd.com', 'www.eabbaac.com', 'www.acaaaed.com', 'www.cddbadc.com', 'www.cccbeae.com', 'www.acaaaed.com', 'www.eabbaac.com', 'www.cddbadc.com', 'www.bdddabd.com', 'www.ebaacbd.com', 'www.dccbece.com', 'www.cdddcca.com', 'www.cccbeae.com', 'www.cccbeae.com', 'www.acaaaed.com', 'www.dccbece.com', 'www.cccbeae.com', 'www.abecadb.com', 'www.acaaaed.com', 'www.dccbece.com', 'www.bdddabd.com', 'www.acaaaed.com', 'www.eabbaac.com', 'www.acaaaed.com', 'www.eabbaac.com', 'www.eeebebb.com', 'www.eeebebb.com', 'www.cddbadc.com', 'www.cddbadc.com', 'www.eabbaac.com', 'www.bdddabd.com', 'www.eeebebb.com', 'www.cdddcca.com', 'www.bdddabd.com', 'www.cccbeae.com', 'www.eeebebb.com', 'www.ebaacbd.com', 'www.eeebebb.com', 'www.cdddcca.com', 'www.cdddcca.com', 'www.eeebebb.com', 'www.cdddcca.com', 'www.acaaaed.com', 'www.cddbadc.com', 'www.ebaacbd.com', 'www.ebaacbd.com', 'www.bdddabd.com', 'www.eeebebb.com', 'www.cddbadc.com', 'www.acaaaed.com', 'www.eabbaac.com', 'www.cddbadc.com', 'www.cdddcca.com', 'www.acaaaed.com', 'www.eabbaac.com', 'www.eeebebb.com', 'www.cdddcca.com', 'www.bdddabd.com', 'www.abecadb.com', 'www.ebaacbd.com', 'www.eabbaac.com', 'www.abecadb.com', 'www.dccbece.com', 'www.cccbeae.com', 'www.acaaaed.com', 'www.abecadb.com', 'www.eabbaac.com', 'www.ebaacbd.com', 'www.dccbece.com', 'www.dccbece.com', 'www.acaaaed.com', 'www.eabbaac.com', 'www.cccbeae.com', 'www.eabbaac.com', 'www.ebaacbd.com', 'www.eabbaac.com', 'www.cddbadc.com', 'www.ebaacbd.com', 'www.eabbaac.com', 'www.acaaaed.com', 'www.eabbaac.com', 'www.eeebebb.com', 'www.dccbece.com', 'www.bdddabd.com', 'www.cccbeae.com', 'www.eeebebb.com', 'www.cddbadc.com', 'www.abecadb.com', 'www.ebaacbd.com', 'www.cdddcca.com', 'www.cdddcca.com', 'www.bdddabd.com', 'www.cddbadc.com', 'www.cddbadc.com', 'www.cddbadc.com', 'www.ebaacbd.com', 'www.ebaacbd.com', 'www.eeebebb.com', 'www.ebaacbd.com', 'www.eabbaac.com', 'www.cdddcca.com', 'www.ebaacbd.com', 'www.eeebebb.com', 'www.cddbadc.com', 'www.bdddabd.com', 'www.abecadb.com', 'www.bdddabd.com', 'www.bdddabd.com', 'www.cdddcca.com', 'www.cddbadc.com', 'www.eabbaac.com', 'www.acaaaed.com', 'www.eabbaac.com', 'www.dccbece.com', 'www.eabbaac.com', 'www.ebaacbd.com', 'www.cddbadc.com', 'www.eabbaac.com', 'www.eabbaac.com', 'www.dccbece.com', 'www.acaaaed.com', 'www.eabbaac.com', 'www.eeebebb.com', 'www.cdddcca.com', 'www.cdddcca.com', 'www.cddbadc.com', 'www.dccbece.com', 'www.ebaacbd.com', 'www.acaaaed.com', 'www.cdddcca.com', 'www.cddbadc.com', 'www.dccbece.com', 'www.acaaaed.com', 'www.cddbadc.com', 'www.ebaacbd.com', 'www.cddbadc.com', 'www.eeebebb.com', 'www.cccbeae.com', 'www.acaaaed.com', 'www.eeebebb.com', 'www.ebaacbd.com', 'www.cccbeae.com', 'www.cddbadc.com', 'www.acaaaed.com', 'www.cccbeae.com', 'www.eeebebb.com', 'www.bdddabd.com', 'www.cccbeae.com', 'www.cccbeae.com', 'www.eeebebb.com', 'www.bdddabd.com', 'www.eeebebb.com', 'www.cccbeae.com', 'www.eeebebb.com', 'www.cdddcca.com', 'www.bdddabd.com', 'www.cccbeae.com', 'www.eeebebb.com', 'www.eabbaac.com', 'www.eeebebb.com', 'www.eeebebb.com', 'www.eeebebb.com', 'www.acaaaed.com', 'www.cddbadc.com', 'www.acaaaed.com', 'www.eeebebb.com', 'www.cdddcca.com', 'www.bdddabd.com', 'www.cddbadc.com', 'www.cddbadc.com', 'www.dccbece.com', 'www.bdddabd.com', 'www.cccbeae.com', 'www.abecadb.com', 'www.cddbadc.com', 'www.eabbaac.com', 'www.dccbece.com']
res= ["a","b","a","a","c","d","e","f","a"]
getReqStatus(res)
