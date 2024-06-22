from aiohttp import ClientSession

        
class GETListsFood:
    
    def __init__(self, header: str):
        self.header = header
        
    async def getList(self):
        async with ClientSession() as session:
            async with session.get(f"https://www.themealdb.com/api/json/v1/1/filter.php?i={self.header}") as response:
                result =  await response.json()
                return result["meals"]
            
            
            
            
class GetFood:
    
    def __init__(self, header: str):
        self.header = header
        
    async def getFood(self):
        async with ClientSession() as session:
           async with session.get(f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={self.header}") as response:
                result = await response.json()
                return result["meals"]
            
            
