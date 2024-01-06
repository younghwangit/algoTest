A, B = input().split()
def compare(A, B):
    if A > B:
        print(">")
    elif A < B:
        print("<")
    elif A == B:
        print("==")
compare(int(A), int(B))