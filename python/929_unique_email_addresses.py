class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen_emails = set()
        for email in emails:
            local, domain = email.split('@')
            new_local = ''
            for c in local:
                if c == '+':
                    break
                elif c != '.':
                    new_local += c
            seen_emails.add(new_local + '@' + domain)
        return len(seen_emails)