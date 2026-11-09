from src.steampie import generate_confirmation_key, generate_one_time_code


def test_generate_confirmation_key():
    identity_secret = "wiYRwKkTHobdDdSgppGbePf8aso="
    timestamp = 1794242760.2001884

    assert generate_confirmation_key(identity_secret, "list", timestamp) == "0/MQ1KDAMnEqUiPCmqvO7oueU9I="
    assert generate_confirmation_key(identity_secret, "accept", timestamp) == "Ot81Do966VNI0VteedWbhSTyeI0="
    assert generate_confirmation_key(identity_secret, "reject", timestamp) == "XyyM5PaFq7s0M2RE2T26RhqAmT8="
    assert generate_confirmation_key(identity_secret, "list") != "0/MQ1KDAMnEqUiPCmqvO7oueU9I="
    assert generate_confirmation_key(identity_secret, "accept") != "Ot81Do966VNI0VteedWbhSTyeI0="
    assert generate_confirmation_key(identity_secret, "reject") != "XyyM5PaFq7s0M2RE2T26RhqAmT8="


def test_generate_one_time_code():
    shared_secret = "LdDvyCO6bbyVXteuop6s6wFl0Zo="
    timestamp = 1794242760.2001884

    assert generate_one_time_code(shared_secret, timestamp) == "C525N"
    assert generate_one_time_code(shared_secret) != "C525N"
