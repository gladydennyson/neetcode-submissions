class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_char = '#'

        encoded = ''
        strings = strs
        # print("strings", strings)
        
        for word in strings:
            encoded += str(len(word))
            encoded += encode_char
            encoded += word
        # print("encoded", encoded)
        return encoded


    def decode(self, s: str) -> List[str]:
        strings = []
        i = 0
        j = 0

        while i < len(s):
            j = i

            # read full length (can be multiple digits)
            while s[j] != '#':
                j += 1

            length = int(s[i:j])
            word = s[j + 1 : j + 1 + length]
            strings.append(word)

            # move pointer to next encoded chunk
            i = j + 1 + length

        return strings


