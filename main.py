from  fastapi import FastAPI, Depends
from http_client import GETListsFood, GetFood
from model import ListFood, FoodMain
from myFilter import MyFilter
import uvicorn


app = FastAPI(
    title= "listFood"
)



def params_list(header: str = "chicken_breast"):
    return {"header": header}

def params_food(header: str = "52772"):
    return {"header": header}




@app.get("/foodList", response_model=list[ListFood])
async def get_food_list(params_list: dict = Depends(params_list)):
    
    listFood = GETListsFood(**params_list)
    
    return await listFood.getList()


@app.get("/mainFood",response_model= FoodMain )
async def get_food_main(params_food: dict = Depends(params_food)):
    
    listFood = GetFood(**params_food)
    
    result = await listFood.getFood()
    
    myFilter = MyFilter(result[0])
    
    return myFilter.myFilter()



if __name__ == "__main__":
    uvicorn.run("main:app", port = "0.0.0.0" , port=8000, reload=True)