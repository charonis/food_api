from aiohttp import ClientSession
from conig import settings

        
class GETListsFood:
    
    def __init__(self, header: str):
        self.header = header
        
    async def getList(self):
        async with ClientSession() as session:
            async with session.get(f"{settings.URL_MAIN_COMPONENT}i={self.header}") as response:
                result =  await response.json()
                return result["meals"]
            
            
            
            
class GetFood:
    
    def __init__(self, header: str):
        self.header = header
        
    async def getFood(self):
        async with ClientSession() as session:
           async with session.get(f"{settings.URL_MAIN_FOOD}i={self.header}") as response:
                result = await response.json()
                return result["meals"]
            
            
