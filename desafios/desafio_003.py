#Contar Pares

def count_evens(nums: list[int]):
    count = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            count = count+1
    return count

if __name__ == "__main__":
    print(count_evens([1, 2, 3, 4]))   # esperado 2
    print(count_evens([1]))            # esperado 0
    print(count_evens([2, 2, 2]))      # esperado 3
    print(count_evens([1, 3, 5]))      # esperado 0
    print(count_evens([-2, 0, 7]))     # esperado 2


