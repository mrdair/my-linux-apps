import requests, json, time, re
time.sleep(10)

###find
while True:
    try:
        ip = requests.get("http://ident.me").text
        print(ip)
        if re.match("^\d+\.\d+\.\d+\.\d+$", ip):
            break
    except:
        time.sleep(10)
        pass

###find id record
headers = {
    'X-Auth-Email': 'mohammadrezadavidabadi@gmail.com',
    'X-Auth-Key': 'df602084bb625e82ab3c20475d91bd88cae74',
    'Content-Type': 'application/json',
}

params = (
    ('type', 'A'),
    ('name', 'raspberry_pi_4.mrda.ir'),
)
response = requests.get('https://api.cloudflare.com/client/v4/zones/ce242c17a93fdcd3266bd54e009fe75f/dns_records', headers=headers, params=params)
id = json.loads(response.text)["result"][0]["id"]
old_ip = json.loads(response.text)["result"][0]["content"]
print(old_ip)
if not ip==old_ip:
    while True:
        try:
            ###delte id record
            response = requests.delete(
                str('https://api.cloudflare.com/client/v4/zones/ce242c17a93fdcd3266bd54e009fe75f/dns_records/' + id),
                headers=headers)
            break
        except:
            time.sleep(5)
    while True:
        try:
            ###create new record
            data = '{"type":"A","name":"raspberry_pi_4.mrda.ir","content":"' + ip + '","ttl":1, "proxied":false}'
            response = requests.post(
                'https://api.cloudflare.com/client/v4/zones/ce242c17a93fdcd3266bd54e009fe75f/dns_records', headers=headers,
                data=data)
            break
        except:
            time.sleep(5)
else:
    print("same ip")

print(ip)
