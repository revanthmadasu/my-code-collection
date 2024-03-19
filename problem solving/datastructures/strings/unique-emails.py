'''
    problem: https://leetcode.com/problems/unique-email-addresses
    concepts: string
    performance: 58.17% runtime, 74.85% memory
'''
from typing import List
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emailsMap = dict()
        for email in emails:
            localName, domain = email.split('@')
            localName = localName.replace('.','')
            if '+' in localName:
                localName = localName[:localName.index('+')]
            # print(f'email: {email} -> {localName+domain}')
            emailsMap[localName+'@'+domain] = True
        return len(emailsMap)
            