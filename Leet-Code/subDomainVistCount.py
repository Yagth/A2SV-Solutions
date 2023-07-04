from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cpdomainsNew = defaultdict(int)
        for domain in cpdomains:
            tempList = domain.split(" ")
            count = int(tempList[0])
            domainLevels = tempList[1].split(".")[::-1]
            domainLevel = domainLevels[0]
            cpdomainsNew[domainLevel] += count

            for i in range(1, len(domainLevels)):
                domainLevel = domainLevels[i] + "." + domainLevel
                cpdomainsNew[domainLevel] += count
        
        answer = []
        for key, count in cpdomainsNew.items():
            answer.append(str(count)+" "+key)
        return answer