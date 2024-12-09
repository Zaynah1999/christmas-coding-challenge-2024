def isValid(self, s: str) -> bool:
        open_ = ['(', '[', '{']
        close_ = [')', ']','}']
        split_s = list(s)
        vals = [j in split_s for j in open_]
        if not any(vals) :
            return False
        for op, cl in zip(open_, close_):
            if op in s:
                if cl not in s:
                    return False