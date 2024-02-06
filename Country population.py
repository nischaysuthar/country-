population = {
    "China": 143,
    "India": 136,
    "Usa": 32,
    "Pakistan": 21
}

def print_all():
    for country, p in population.items():
        print("\n population of",country,"is",p)

def add():
    country=input("\n Enter country name:")
    
    if country in population:
        print("\n Country already exist in dataset")
    
    p=int(input("\n Enter country population:"))
    population[country]=p
    print_all()
    
def remove():
    country = input("Enter country name to remove:")

    if country not in population:
        print("Country doesn't exist in our dataset. Terminating")
        
    del population[country]
    print_all()
    
def query():
    country = input("Enter country name to query:")
  
    if country not in population:
        print("Country doesn't exist in our dataset. Terminating")
        
    else:
        print("Population of",country,"is",population[country])
   

op=input("\n Enter operation:")

if op=="add":
    add()
elif op=="remove":
    remove()
elif op=="query":
    query()
else:
    print("\n invalid")

        
        