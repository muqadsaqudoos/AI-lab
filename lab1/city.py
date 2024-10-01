class CityData:
    def __init__(self,city,outConCount,outCons):
        self.city = city
        self.outConCount = outConCount
        self.outCons = outCons
        self.visited = False
        self.predecessor = -1 

def get_cities(file):
    cities = []
    with open(file,'r') as file:
        num_of_cities = int(file.readline().strip())
        for _ in range(num_of_cities):
            city_info = file.readline().strip().split(" ")
            city = city_info[1].strip(",")
            outConCount = int(city_info[2])
            if outConCount >0:
                outCons = list(map(int,city_info[3:]))

            else:
                outCons = []

            cities.append(CityData(city,outConCount,outCons))

    return cities


def dfs(cities, source, destination):
    if source.city == destination:
        return [source.city]
    
    source.visited = True
    
    for out_connections in source.outCons:
        if cities[out_connections].visited == False:
            cities[out_connections].predecessor = source.city

            path = dfs(cities, cities[out_connections], destination)

            if path:
                return [source.city] + path
            
    return None

def index(c,cities):
    for i,city in enumerate(cities):
        if city.city == c:
            return i
    return -1

def main():
    a = input("Please enter filename storing a network: ")
    cities = get_cities(a)

    while True:
        source = input("Enter the name of starting city: ")
        destination = input("Enter the name of destination: ")

        source_index = index(source,cities)
        destination_index = index(destination,cities)

        if source_index == -1:
            print(f"{source} is not a valid city, please re-enter.")
            continue
        if destination_index == -1:
            print(f"{source} is not a valid city, please re-enter.")
            continue

        path = dfs(cities, cities[source_index] , destination)

        if path:
            print(" -> ".join(path))
            break

        else:
            print(f"there is not path from {source} to {destination}, please re-enter option: ")
            continue

main()

