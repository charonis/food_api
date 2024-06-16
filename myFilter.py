class MyFilter: 
    
    def __init__(self, dictDate:dict) -> None:
        self.last_item = [ key for key, value in dictDate.items() if value != None and  value != "" and value != " "]
        self.dict_output = {"ingredients":{}, "measure": {}}
        self.dictDate = dictDate
        
        
    def lastKey(self):
        a = self.last_item
        
        a.reverse()
        
        for item in a:
            if item.find("Measure") != -1:
                return int(item[10:])
                

        
    
    def myFilter(self):
         
        index = self.lastKey()
         
        for key , value in self.dictDate.items():
            match key:
                case "strMeal":
                    self.dict_output["strMeal"] = value
                case "strInstructions":
                    self.dict_output["strInstructions"] = value
                case "strMealThumb":
                    self.dict_output["strMealThumb"] = value
                
        for number in range(1, index + 1):
            self.dict_output["ingredients"][f"strIngredient{number}"] = self.dictDate[f"strIngredient{number}"]
            
        for number in range(1, index + 1):
            self.dict_output["measure"][f"strMeasure{number }"] = self.dictDate[f"strMeasure{number}"]
        
                  
        
        return self.dict_output

