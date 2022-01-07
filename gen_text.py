from random import randint
from typing import List

GENDER_O_A_VALUES = ['o', 'a']
WHAT_I_DIDNT_HAVE = ['il supergreenpass', 'la laurea in fisica', 'la laurea in ingegneria navale']
WHAT_UNDER_MY_RESP = ['un figlio', 'tre gattini', 'due coccodrilli ed un orangotango']


def random_from_list(values: List[str]) -> str:
    idx = randint(0, len(values) - 1)
    return values[idx]


def render_template():
    gender_o_a = random_from_list(GENDER_O_A_VALUES)
    what_i_didnt_have = random_from_list(WHAT_I_DIDNT_HAVE)
    what_under_my_resp = random_from_list(WHAT_UNDER_MY_RESP)

    return f"""
    Ero stat{gender_o_a} assunt{gender_o_a} per un lavoro nuovo, mi sono presentat{gender_o_a} sul posto e sono stat{gender_o_a} respint{gender_o_a} e umiliat{gender_o_a} perché non avevo {what_i_didnt_have}. Ora sono senza lavoro e con {what_under_my_resp} a carico.

    Io non dimenticherò.
    """


def handler(event, context):
    body = render_template()
    return {
        "statusCode": 200,
        "body": body,
        "headers": {"Content-Type": "text/plain;charset=UTF-8"},
    }


if __name__ == "__main__":
    print(render_template())
