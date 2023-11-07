import time
import random
import requests
from fake_useragent import UserAgent as ua

requests.packages.urllib3.disable_warnings() 

class ProxyInformation:
    def __init__(self, timeout=5):
        """
        ProxyInformation is a tool to verify the information and status of a proxy server.

        Attributes:
            - timeout (int): The maximum time to wait for a response from the proxy server (default is 5 seconds).
            - myIP (str): The public IP address of the local machine.

        Methods:
            - check_proxy(proxy: str) -> dict:
                Verify the information and status of a proxy server.
            
        Example:
            checker = ProxyInformation(timeout=5)
            proxy_info = checker.check_proxy("103.88.35.200:1080")
            print(proxy_info)
        """
        self.myIP = self.__get_myip()
        self.timeout = timeout

    def __get_myip(self):
        """
        Get the public IP address of the local machine using ipinfo.io.

        Returns:
            str: The public IP address of the local machine.
        """
        ip = requests.get("https://ipinfo.io/json", headers={"User-Agent": ua().random}).json()["ip"]
        return ip
    
    def __geolocation(self, ip):
        """
        Get geolocation information for a given IP address using ipwhois.app.

        Args:
            ip (str): The IP address for which geolocation information is requested.

        Returns:
            str: The country of the IP address.
            str: The country code of the IP address.
        """
        info = requests.get(f"https://ipwhois.app/json/{ip}", headers={"User-Agent": ua().random}).json()

        country = info["country"]
        country_code = info["country_code"]
        return country, country_code

    def __get_info(self, proxy):
        """
        Get information and status of a proxy server.

        Args:
            proxy (str): The proxy server in the format "ip:port".

        Returns:
            dict: A dictionary containing information about the proxy server, including its status, response time, anonymity level, country, etc.
        """
        ip, port = proxy.split(":")

        result = {}
        protocols = ["http", "socks4", "socks5"]
        sites = ["https://ipinfo.io/json", "http://proxyjudge.us", "http://azenv.net"]

        for protocol in protocols:
            proxies = {
                "http": f"{protocol}://{proxy}",
                "https": f"{protocol}://{proxy}"
            }

            try:
                start = time.time()
                r = requests.get(random.choice(sites), headers={"User-Agent": ua().random}, proxies=proxies, timeout=self.timeout, verify=False)
                finish = time.time() - start

                result["ip"] = ip
                result["port"] = port
                result["protocol"] = protocol
                result["responseTime"] = finish

                if "HTTP_X_FORWARDED_FOR" in r.text:
                    result["anonymity"] = "Transparent"
                else:
                    if ip not in r.text and self.myIP not in r.text:
                        result["anonymity"] = "Elite"
                    if ip in r.text and self.myIP not in r.text:
                        result["anonymity"] = "Anonymous"

                country, country_code = self.__geolocation(ip)
                result["country"] = country
                result["country_code"] = country_code

                break
            except (requests.RequestException, ValueError):
                pass

        if result == {}:
            result["status"] = False
            
        return result
    
    def check_proxy(self, proxy):
        """
        Verify the information and status of a proxy server.

        Args:
            proxy (str): The proxy server in the format "ip:port".

        Returns:
            dict: A dictionary containing information about the proxy server, including its status, response time, anonymity level, country, etc.
        """
        return self.__get_info(proxy)