def solution(brown, yellow):
    total = brown + yellow
    
    # 전체 카펫의 크기에서 가능한 모든 가로, 세로 값을 찾아봅니다.
    for height in range(1, total + 1):
        if total % height == 0:
            width = total // height
            # 가로가 세로보다 크거나 같은 조건을 만족해야 하므로, 이 조건을 추가합니다.
            if width >= height:
                # (width - 2) * (height - 2)가 yellow와 같아야 중앙에 노란색 격자가 존재할 수 있습니다.
                if (width - 2) * (height - 2) == yellow:
                    return [width, height]


