class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        modified_str = s.replace('-','').upper()
        result = ""
        counter = 0
        for i in modified_str[::-1]:
            result += i
            counter += 1
            if counter % k == 0 and counter < len(modified_str):
                result += '-'
        return result[::-1]