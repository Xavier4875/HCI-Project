import asyncio
import info
from tapo import ApiClient

async def main():
    client = ApiClient(
        info.USERNAME,
        info.PASSWORD
    )

    bulb = await client.p100(
        info.IP
    )

    switch = input("Do you want the light on (yes/no): ")

    while switch != "stop":
        if switch == "yes":
            # Turn ON
            await bulb.on()
            print("Bulb turned ON")

        await asyncio.sleep(2)

        if switch == "no":
            await bulb.off()
            print("Bulb turned OFF")

        switch = input("Do you want the light on (yes/no): ")

    await bulb.on()

asyncio.run(main())




