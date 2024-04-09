'''
    Problem: https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/
    Concepts: DFS, Recursion, Topological Sort
    performance: 88.95% runtime, 7.19% memory
'''
from typing import List
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n = len(recipes)
        recipesIngredientsMap = dict()
        for i in range(n):
            recipesIngredientsMap[recipes[i]] = ingredients[i]
        print(recipesIngredientsMap)
        visiting = set()

        @lru_cache(None)
        def isPossible(foodMat):
            # print(f'calling with {foodMat}')
            if foodMat in visiting:
                return False
            possible = True
            visiting.add(foodMat)
            if foodMat in supplies:
                possible = True
            elif foodMat in recipesIngredientsMap:
                for ingredient in recipesIngredientsMap[foodMat]:
                    if not isPossible(ingredient):
                        possible = False
                        break
            else:
                possible = False
            visiting.remove(foodMat)
            return possible
        return [recipe for recipe in recipes if isPossible(recipe)]