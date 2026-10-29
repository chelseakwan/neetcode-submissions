class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # initialize dict for unique emails
        output = set()
        
        # for each email
        for email in emails:
            # split email on @
            local_name = email.split("@")[0].replace(".", "").split("+")[0]
            domain_name = email.split("@")[1]
        
            base_email = (local_name, domain_name)
            output.add(base_email)
        return len(output)