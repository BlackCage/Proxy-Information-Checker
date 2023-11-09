import time
import random
import requests
import concurrent.futures

requests.packages.urllib3.disable_warnings()

class ProxyInformation:
    def __init__(self, timeout=5):
        """
        Initializes the ProxyInformation class.

        Parameters:
            - timeout (int): The maximum time to wait for a response from the proxy server (default is 5 seconds).
        """
        self.myIP = self.__get_myip()
        self.timeout = timeout

    def __get_myip(self):
        """
        Gets the public IP address of the local machine using ipify.org.

        Returns:
            str: The public IP address of the local machine.
        """
        try:
            ip = requests.get("https://api.ipify.org?format=json").json()["ip"]
            return ip
        except requests.RequestException:
            return None

    def __geolocation(self, ip):
        """
        Gets geolocation information for a given IP address using reallyfreegeoip.org.

        Args:
            ip (str): The IP address for which geolocation information is requested.

        Returns:
            str: The country name of the IP address.
            str: The country code of the IP address.
        """
        try:
            info = requests.get(f"https://reallyfreegeoip.org/json/{ip}").json()
            country_name = info["country_name"]
            country_code = info["country_code"]
            return country_name, country_code
        except requests.RequestException:
            return None, None

    def __test_protocol(self, proxy, protocol, sites):
        """
        Tests a proxy server for a specific protocol.

        Args:
            proxy (str): The proxy server in the format "ip:port".
            protocol (str): The protocol to test (e.g., "http", "socks4", "socks5").
            sites (list): List of websites to test the proxy against.

        Returns:
            dict: A dictionary containing information about the proxy server, including its status, response time, anonymity level, country, etc.
        """
        proxies = {"http": f"{protocol}://{proxy}", "https": f"{protocol}://{proxy}"}

        try:
            start = time.time()
            r = requests.get(random.choice(sites), proxies=proxies, timeout=self.timeout, verify=False)
            finish = time.time() - start

            info = {
                "ip": proxy.split(":")[0],
                "port": proxy.split(":")[1],
                "protocol": protocol,
                "responseTime": finish
            }

            if "HTTP_X_FORWARDED_FOR" in r.text:
                info["anonymity"] = "Transparent"
            else:
                ip, myIP = proxy.split(":")[0], self.myIP
                if ip not in r.text and myIP not in r.text:
                    info["anonymity"] = "Elite"
                if ip in r.text and myIP not in r.text:
                    info["anonymity"] = "Anonymous"

            country, country_code = self.__geolocation(ip)
            info.update({
                "country": country,
                "country_code": country_code
            })

            return info
        except (requests.RequestException, ValueError):
            return None

    def __get_info(self, proxy):
        """
        Gets information and status of a proxy server by testing multiple protocols.

        Args:
            proxy (str): The proxy server in the format "ip:port".

        Returns:
            dict: A dictionary containing information about the proxy server, including its status, response time, anonymity level, country, etc.
        """
        result = {"status": False}

        protocols = ["http", "socks4", "socks5"]
        sites = ["https://ipinfo.io/json", "http://proxyjudge.us", "http://azenv.net"]

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(self.__test_protocol, proxy, protocol, sites) for protocol in protocols]

        for future in concurrent.futures.as_completed(futures):
            info = future.result()
            if info:
                result = {"status": True, "info": info}
                break

        return result

    def check_proxy(self, proxy):
        """
        Verifies the information and status of a proxy server by testing multiple protocols.

        Args:
            proxy (str): The proxy server in the format "ip:port".

        Returns:
            dict: A dictionary containing information about the proxy server, including its status, response time, anonymity level, country, etc.
        """
        return self.__get_info(proxy)
