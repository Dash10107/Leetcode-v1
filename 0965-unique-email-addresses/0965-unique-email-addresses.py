class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans = set()
        for email in emails:
            local, domain = email.split('@')
            name = local.split('+')[0]
            name = name.replace('.','')
            ans.add((name+'@'+domain))
        return len(ans)
