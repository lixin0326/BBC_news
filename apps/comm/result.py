class Result:
    @staticmethod
    def get_success_result(data=None, status=200, msg='success'):
        return {
            'status': status,
            'msg': msg,
            'data': data
        }

    @staticmethod
    def get_error_result(status=404, msg='error'):
        return {
            'status': status,
            'msg': msg
        }