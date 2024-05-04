from rest_framework import permissions, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from config.exceptions import UserNotExistException
from mypage.serializers import MypageSerializer


class MypageAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request: Request) -> Response:
        user = request.user
        if not user:
            raise UserNotExistException()

        serializer = MypageSerializer(user)

        return Response(
            # fmt: off
            data={
                "detail": "마이페이지 조회를 성공했습니다.",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK
            # fmt: on
        )
