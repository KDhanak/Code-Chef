# cook your dish here
def canWithdraw():
    T = int(input("Please provide the number of test cases: "))
    results = []

    for _ in range(T):
        N, K = map(int, input(
            "Please enter the number of people N and total initial money in ATM with a space in between: ").split())
        amounts = list(map(int, input(
            "PLease provide N number of money requirements with a space between: ").split()))
        result = ''

        for amount in amounts:
            if K >= amount:
                K -= amount
                result += "1"
            else:
                result += "0"

        results.append(result)
    return results


if __name__ == "__main__":
    results = canWithdraw()
    for res in results:
        print(res)
