import math
# k번째 순열을 찾는 함수
def find_kth_permutation(n, k):
    numbers = list(range(1, n + 1))  # 1부터 n까지의 숫자 리스트 생성
    k -= 1  # 0-based indexing으로 변환
    result = []

    for i in range(n, 0, -1):
        fact = math.factorial(i - 1)  # 현재 자릿수의 블록 크기 계산
        index = k // fact  # k를 블록 크기로 나눈 몫이 현재 자릿수의 숫자 인덱스
        result.append(numbers.pop(index))  # 해당 숫자를 결과에 추가하고 리스트에서 제거
        k %= fact  # k를 블록 크기로 나눈 나머지를 갱신

    return result  # k번째 순열 반환

# 주어진 순열이 몇 번째인지 찾는 함수
def find_permutation_index(n, perm):
    numbers = list(range(1, n + 1))  # 1부터 n까지의 숫자 리스트 생성
    index = 0

    for i in range(n):
        pos = numbers.index(perm[i])  # 현재 숫자가 남은 숫자 리스트에서 몇 번째인지 확인
        index += pos * math.factorial(n - i - 1)  # 위치 * 해당 자릿수의 블록 크기를 더함
        numbers.pop(pos)  # 해당 숫자를 리스트에서 제거

    return index + 1  # 1-based indexing으로 결과 반환

# 첫 번째 입력: N
N = int(input())

# 두 번째 입력: 문제 유형과 데이터
data = list(map(int, input().split()))

if data[0] == 1:
    # 문제 유형 1: k번째 순열 출력
    print(*find_kth_permutation(N, data[1]))
elif data[0] == 2:
    # 문제 유형 2: 주어진 순열의 인덱스 출력
    print(find_permutation_index(N, data[1:]))
