class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique_mails = set()
        for email in emails:
            i = 0
            forward = ''
            while email[i] != '@' and email[i] != '+':
                if email[i] != '.':
                    forward += email[i]
                i+= 1
            forward += email[email.index('@'):]
            unique_mails.add(forward)
        return len(unique_mails)
