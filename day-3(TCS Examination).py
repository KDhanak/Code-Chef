# cook your dish here
def whatIsTheRank():
    T = int(input("Please enter the number of test cases: "))
    results = []

    for _ in range(T):
        dDSA, dTOC, dDM = map(int, input(
            "Score of Dragon in DSA, TOC, DM respectively(seperate by single space): ").split())
        sDSA, sTOC, sDM = map(int, input(
            "Score of SLOTH in DSA, TOC, DM respectively(seperate by single space): ").split())

        dSUM = dDSA + dTOC + dDM
        sSUM = sDSA + sTOC + sDM

        result = ""

        if dSUM > sSUM:
            result = "DRAGON"
        elif dSUM == sSUM:
            if dDSA > sDSA:
                result = "DRAGON"
            elif dDSA == sDSA:
                if dTOC > sTOC:
                    result = "DRAGON"
                elif dTOC == sTOC:
                    result = "TIE"
                else:
                    result = "SLOTH"
            else:
                result = "SLOTH"
        else:
            result = "SLOTH"

        results.append(result)
    return results


if __name__ == "__main__":
    results = whatIsTheRank()
    for res in results:
        print(res)
