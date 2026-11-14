class Solution:

    def encode(self, strs: List[str]) -> str:
        return '_+[]'.join(strs) if strs else '!'
    def decode(self, s: str) -> List[str]:
        return s.split("_+[]") if s != '!' else []