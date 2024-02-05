class Solution:
    def defangIPaddr(self, address: str) -> str:
         # Replace "." with "[.]"
        defanged_address = address.replace('.', '[.]')
        return defanged_address