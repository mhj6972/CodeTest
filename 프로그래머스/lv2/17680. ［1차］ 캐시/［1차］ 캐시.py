def solution(cacheSize, cities):
    
    answer = 0
    n = len(cities)
    cache = []
    
    for i in range(n): # 대소문자 구분 안한다는 조건해결
        cities[i] = cities[i].lower()
        
    for city in cities:
        
        if city in cache: # cache hit
        	# used 되면 삭제 우선순위를 젤 뒤로 보냄
            cache.remove(city) 
            cache.append(city)
            answer += 1
        
        else: # cache miss
            cache.append(city)
            answer += 5
            
            # cache miss의 경우 값을 추가할 때 cacheSize가 초과되면 오래된 데이터는 삭제한다.
            if len(cache) == cacheSize + 1:
                cache.pop(0)
            
    return answer