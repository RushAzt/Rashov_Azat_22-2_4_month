def get_user_from_request(reqquest):
    return reqquest.user if not reqquest.user.is_anonymous else None