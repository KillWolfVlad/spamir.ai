from request_boost import boosted_requests


def check_users(user_ids: list[str]) -> list[dict]:
    urls = [f"https://api.cas.chat/check?user_id={x}" for x in user_ids]

    results = boosted_requests(
        urls=urls,
        no_workers=len(user_ids),
        max_tries=99,
        after_max_tries="assert",
        timeout=10,
        verbose=False,
        parse_json=True,
    )

    return results
