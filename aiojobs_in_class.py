import aiojobs
import asyncio


async def coro():
    while True:
        print("func coro!!")
        await asyncio.sleep(1)


class Job:
    async def init_scheduler(self):
        self.scheduler = await aiojobs.create_scheduler()

    async def add_job(self, job):
        await self.scheduler.spawn(job)

    async def close(self):
        await self.scheduler.close()


async def main():
    job = Job()
    await job.init_scheduler()
    await job.add_job(coro())
    await asyncio.sleep(5)
    await job.close()

asyncio.get_event_loop().run_until_complete(main())
