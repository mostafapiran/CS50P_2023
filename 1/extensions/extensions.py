x = {
    "gif"  : "image/gif",
    "jpg"  : "image/jpeg",
    "jpeg" : "image/jpeg",
    "png"  : "image/png",
    "pdf"  : "application/pdf",
    "txt"  : "text/plain",
    "zip"  : "application/zip"
}

a = input("File Name: ").strip().lower()

if a.rfind(".") != -1:
    i = int(a.rindex(".")) +1
    b = a[i:]
    if b not in x:
        print("application/octet-stream")
    else:
        print(x[b])
else:
    print("application/octet-stream")


