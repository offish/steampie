from typing import Any, get_args, get_origin, get_type_hints, is_typeddict


def check_typed_item_dict(item: Any | object, typed_dict: type, hints: dict[str, Any]):
    assert isinstance(item, dict), f"expected dict, got {type(item)}"

    missing = typed_dict.__required_keys__ - item.keys()
    assert not missing, f"{typed_dict.__name__}: missing keys {sorted(missing)}"

    extra = item.keys() - hints.keys()
    assert not extra, f"{typed_dict.__name__}: unexpected keys {sorted(extra)}"

    for key, value in item.items():
        expected = hints[key]

        if get_origin(expected) is list:
            assert isinstance(value, list), f"{key}: expected list, got {type(value)}"

            (inner,) = get_args(expected)

            if is_typeddict(inner):
                check_typed_dict(value, inner)

        elif is_typeddict(expected):
            check_typed_dict(value, expected)

        else:
            message = f"{typed_dict.__name__}.{key}: expected {expected}, got {type(value).__name__}"
            assert isinstance(value, expected), message


def check_typed_dict(data: object, typed_dict: type) -> None:
    items = data if isinstance(data, list) else [data]
    hints = get_type_hints(typed_dict)

    for item in items:
        check_typed_item_dict(item, typed_dict, hints)
