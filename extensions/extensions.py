ext = {
        'jpg':'image/jpeg',
        'jpeg':'image/jpeg',
        'png':'image/png',
        'gif':'image/gif',
        'pdf':'application/pdf',
        'txt':'text/plain',
        'zip':'application/zip'
        }

def end(t):
    if t.lower().strip().split('.')[-1] in ext:
        return ext[t.lower().strip().split('.')[-1]]
    else:
        return 'application/octet-stream'

#if it works, it works

print((end(input('File type: '))))


