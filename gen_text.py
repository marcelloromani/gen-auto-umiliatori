from random import randint
from typing import List
from urllib.parse import quote

# TODO: move this out of the code
GENDER_O_A_VALUES = ['o', 'a']
WHAT_I_DIDNT_HAVE = [
    'il supergreenpass',
    'la laurea in fisica',
    'la laurea in ingegneria navale',
    'il certificato antivertigini',
]
WHAT_UNDER_MY_RESP = [
    'un figlio',
    'tre gattini',
    'due coccodrilli ed un orangotango',
    'due gatti con la demenza senile e una moglie disturbata',
]


def random_from_list(values: List[str]) -> str:
    idx = randint(0, len(values) - 1)
    return values[idx]


def render_template():
    gender_o_a = random_from_list(GENDER_O_A_VALUES)
    what_i_didnt_have = random_from_list(WHAT_I_DIDNT_HAVE)
    what_under_my_resp = random_from_list(WHAT_UNDER_MY_RESP)

    # TODO: use proper templating library
    msg = f"""Ero stat{gender_o_a} assunt{gender_o_a} per un lavoro nuovo, mi sono presentat{gender_o_a} sul posto e sono stat{gender_o_a} respint{gender_o_a} e umiliat{gender_o_a} perché non avevo {what_i_didnt_have}. Ora sono senza lavoro e con {what_under_my_resp} a carico.

Io non dimenticherò.
"""

    silly_hashtag = "respintieumiliati"

    tweet_text = f"{msg} #{silly_hashtag}"
    tweetme_href = "https://twitter.com/intent/tweet?text={}".format(quote(tweet_text))

    html_text = "".join([f"<p>{line.strip()}</p>" for line in msg.split("\n")])
    html_text = f"{html_text}<p><a href=\"https://twitter.com/search?q=%23{silly_hashtag}\">#{silly_hashtag}</a>"
    html_text = f"{html_text}<p><a href=\"{tweetme_href}\">Tuitta anche tu il tuo sdegno!</a></p>"

    return html_text


def handler(event, context):
    body = render_template()
    return {
        "statusCode": 200,
        "body": body,
        "headers": {"Content-Type": "text/html;charset=UTF-8"},
    }


if __name__ == "__main__":
    print(render_template())
