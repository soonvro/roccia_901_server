from drf_spectacular.utils import OpenApiExample
from rest_framework import serializers


class ErrorResponseSerializer(serializers.Serializer):
    status_code = serializers.IntegerField()
    code = serializers.CharField()
    detail = serializers.CharField()


RANKING_WEEKS_RESPONSE_EXAMPLE = [
    OpenApiExample(
        "주차별 랭킹 목록 조회 성공 예시",
        summary="Weekly Rankings Response Example",
        description="주차별 랭킹 목록 조회 성공 시의 응답 예시입니다.",
        value={
            "message": "주차별 랭킹 목록 조회를 성공했습니다.",
            "data": {
                "weekly_rankings": [
                    {
                        "week": 1,
                        "ranking": [
                            {
                                "generation": "5기",
                                "level": "파랑색",
                                "location": "더클라임 홍대",
                                "profile_img": 6,
                                "rank": 1,
                                "score": 71.5,
                                "user_id": 28,
                                "username": "조동욱",
                            },
                            # ... other user rankings
                        ],
                    },
                    # ... other weeks
                ]
            },
        },
        response_only=True,
    )
]

RANKING_401_FAILURE_EXAMPLE = [
    OpenApiExample(
        "유효하지 않은 계정 예시",
        summary="Invalid Account",
        description="유효하지 않은 계정일 때의 응답 예시입니다.",
        value={"status_code": 401, "code": "invalid_account", "detail": "유효하지 않은 계정입니다."},
        response_only=True,
    )
]

RANKING_500_FAILURE_EXAMPLE = [
    OpenApiExample(
        "서버 내부 오류 예시",
        summary="Internal Server Error",
        description="서버 내부에서 발생한 오류일 때의 응답 예시입니다.",
        value={"status_code": 500, "code": "internal_server_error", "detail": "서버 내부에서 발생한 오류입니다."},
        response_only=True,
    )
]
