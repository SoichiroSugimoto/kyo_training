import os
import json
import boto3
import random
import datetime

from linebot import LineBotApi
from linebot.models import TextSendMessage, FlexSendMessage

from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute, MapAttribute

# qz0 = 'q0'
# qz1 = 'q1'
# qz2 = 'q2'
# qz3 = 'q3'
# qz4 = 'q4'
# qz5 = 'q5'
# qz6 = 'q6'
# qz7 = 'q7'
# qz8 = 'q8'
# qz9 = 'q9'

time = datetime.date.today()
random.seed(int(time.day))
qz0 = 'q' + str(random.randint(0, 9))
qz1 = 'q' + str(random.randint(10, 14))
qz2 = 'q' + str(random.randint(15, 19))
qz3 = 'q' + str(random.randint(20, 24))
qz4 = 'q' + str(random.randint(25, 30))
qz5 = 'q' + str(random.randint(32, 34))
qz6 = 'q' + str(random.randint(35, 41))
qz7 = 'q' + str(random.randint(43, 45))
qz8 = 'q' + str(random.randint(46, 50))
qz9 = 'q' + str(random.randint(51, 57))

# アクセストークン
access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
line_bot = LineBotApi(access_token)


# 問題毎のユーザスコアを格納するクラス
# UserScore モデルから参照
class ScoreMap(MapAttribute):
  q0 = NumberAttribute(null=True)
  q1 = NumberAttribute(null=True)
  q2 = NumberAttribute(null=True)
  q3 = NumberAttribute(null=True)
  q4 = NumberAttribute(null=True)
  q5 = NumberAttribute(null=True)
  q6 = NumberAttribute(null=True)
  q7 = NumberAttribute(null=True)
  q8 = NumberAttribute(null=True)
  q9 = NumberAttribute(null=True)

  q10 = NumberAttribute(null=True)
  q11 = NumberAttribute(null=True)
  q12 = NumberAttribute(null=True)
  q13 = NumberAttribute(null=True)
  q14 = NumberAttribute(null=True)
  q15 = NumberAttribute(null=True)
  q16 = NumberAttribute(null=True)
  q17 = NumberAttribute(null=True)
  q18 = NumberAttribute(null=True)
  q19 = NumberAttribute(null=True)

  q20 = NumberAttribute(null=True)
  q21 = NumberAttribute(null=True)
  q22 = NumberAttribute(null=True)
  q23 = NumberAttribute(null=True)
  q24 = NumberAttribute(null=True)
  q25 = NumberAttribute(null=True)
  q26 = NumberAttribute(null=True)
  q27 = NumberAttribute(null=True)
  q28 = NumberAttribute(null=True)
  q29 = NumberAttribute(null=True)

  q30 = NumberAttribute(null=True)
  q31 = NumberAttribute(null=True)
  q32 = NumberAttribute(null=True)
  q33 = NumberAttribute(null=True)
  q34 = NumberAttribute(null=True)
  q35 = NumberAttribute(null=True)
  q36 = NumberAttribute(null=True)
  q37 = NumberAttribute(null=True)
  q38 = NumberAttribute(null=True)
  q39 = NumberAttribute(null=True)

  q40 = NumberAttribute(null=True)
  q41 = NumberAttribute(null=True)
  q42 = NumberAttribute(null=True)
  q43 = NumberAttribute(null=True)
  q44 = NumberAttribute(null=True)
  q45 = NumberAttribute(null=True)
  q46 = NumberAttribute(null=True)
  q47 = NumberAttribute(null=True)
  q48 = NumberAttribute(null=True)
  q49 = NumberAttribute(null=True)

  q50 = NumberAttribute(null=True)
  q51 = NumberAttribute(null=True)
  q52 = NumberAttribute(null=True)
  q53 = NumberAttribute(null=True)
  q54 = NumberAttribute(null=True)
  q55 = NumberAttribute(null=True)
  q56 = NumberAttribute(null=True)
  q57 = NumberAttribute(null=True)
  q58 = NumberAttribute(null=True)
  q59 = NumberAttribute(null=True)

dynamodb = boto3.resource('dynamodb')
scores = dynamodb.Table('Score')

# ユーザスコアを格納するモデル
class UserScore(Model):
  class Meta:
    table_name = 'UserScore'
    region = 'ap-northeast-1'
    # aws_access_key_id = os.getenv('aws_access_key_id')
    # aws_secret_access_key = os.getenv('aws_secret_access_key')
  line_user_id = UnicodeAttribute(hash_key=True)
  scores = MapAttribute(of=ScoreMap)

def get_result(question, answer):
    question_info = scores.get_item(Key={"question_id": question})['Item']
    score = 0
    if question_info['answer'] == answer:
        score = int(question_info['score'])
    return score

def get_next_question(inserted_question):
    if inserted_question == qz0:
        next_question = scores.get_item(
            Key={"question_id": qz1}
        )['Item']['question']
    elif inserted_question == qz1:
        next_question = scores.get_item(
            Key={"question_id": qz2}
        )['Item']['question']
    elif inserted_question == qz2:
        next_question = scores.get_item(
            Key={"question_id": qz3}
        )['Item']['question']
    elif inserted_question == qz3:
        next_question = scores.get_item(
            Key={"question_id": qz4}
        )['Item']['question']
    elif inserted_question == qz4:
        next_question = scores.get_item(
            Key={"question_id": qz5}
        )['Item']['question']
    elif inserted_question == qz5:
        next_question = scores.get_item(
            Key={"question_id": qz6}
        )['Item']['question']
    elif inserted_question == qz6:
        next_question = scores.get_item(
            Key={"question_id": qz7}
        )['Item']['question']
    elif inserted_question == qz7:
        next_question = scores.get_item(
            Key={"question_id": qz8}
        )['Item']['question']
    elif inserted_question == qz8:
        next_question = scores.get_item(
            Key={"question_id": qz9}
        )['Item']['question']
    return FlexSendMessage(
        alt_text='Next Question',
        contents=json.loads(next_question)
    )

def update_score(user_score, answer):
    # 各設問に対するスコアを挿入する
    inserted_question = ''
    if user_score.scores[qz0] is None:
        score = get_result(qz0, answer)
        inserted_question = qz0
    elif user_score.scores[qz1] is None:
        score = get_result(qz1, answer)
        inserted_question = qz1
    elif user_score.scores[qz2] is None:
        score = get_result(qz2, answer)
        inserted_question = qz2
    elif user_score.scores[qz3] is None:
        score = get_result(qz3, answer)
        inserted_question = qz3
    elif user_score.scores[qz4] is None:
        score = get_result(qz4, answer)
        inserted_question = qz4
    elif user_score.scores[qz5] is None:
        score = get_result(qz5, answer)
        inserted_question = qz5
    elif user_score.scores[qz6] is None:
        score = get_result(qz6, answer)
        inserted_question = qz6
    elif user_score.scores[qz7] is None:
        score = get_result(qz7, answer)
        inserted_question = qz7
    elif user_score.scores[qz8] is None:
        score = get_result(qz8, answer)
        inserted_question = qz8
    elif user_score.scores[qz9] is None:
        score = get_result(qz9, answer)
        inserted_question = qz9

    # スコアを更新する
    if inserted_question != '':
        user_score.scores[inserted_question] = score
        user_score.save()

    if score == 0:
        result_msg = TextSendMessage(text='不正解です')
    else:
        result_msg = TextSendMessage(text='正解です')

    # 最終問題であれば結果を返す
    if inserted_question == qz9:
        result_data = UserScore.get(user_score.line_user_id)
        total_score = result_data.scores[qz0] + \
            result_data.scores[qz1] + result_data.scores[qz2] + \
            result_data.scores[qz3] + result_data.scores[qz4] + \
            result_data.scores[qz5] + result_data.scores[qz6] + \
            result_data.scores[qz7] + result_data.scores[qz8] + \
            result_data.scores[qz9]
        next_msg = TextSendMessage(
            text='以上で問題は終了です\n合計得点は{}点です'.format(total_score))
    else:
        next_msg = get_next_question(inserted_question)

    # 次の設問を返す
    return {
        'inserted_question': inserted_question,
        'score': score,
        'msg': [result_msg, next_msg]
    }


def lambda_handler(event, context):

  print("Received event: " + json.dumps(event, indent=2))

  # Webhookの接続確認用
  body = json.loads(event['body'])

  if len(body['events']) == 0:
      return {
          'statusCode': 200,
          'body': ''
      }

  print(body)
  user_id = body['events'][0]['source']['userId']

  event_type = body['events'][0]['type']
  message_text = body['events'][0]['message']['text'] if event_type == 'message' else ''

  if message_text == 'start'  or event_type == 'follow' :

    #「start」が入力された時に出題開始
    reply_token =  body['events'][0]['replyToken']
    # ユーザスコアが存在しない場合は作成する
    # iam:dynamodb:DescribeTable
    if not UserScore.exists():
      UserScore.create_table(read_capacity_units=1,
                            write_capacity_units=1, wait=True)

    # ユーザIDが存在しない場合は登録する
    UserScore(
                line_user_id=user_id,
                scores=ScoreMap(q0=None, q1=None, q2=None, q3=None, q4=None, q5=None, q6=None, q7=None, q8=None, q9=None,
                        q10=None, q11=None, q12=None, q13=None, q14=None, q15=None, q16=None, q17=None, q18=None, q19=None,
                        q20=None, q21=None, q22=None, q23=None, q24=None, q25=None, q26=None, q27=None, q28=None, q29=None,
                        q30=None, q31=None, q32=None, q33=None, q34=None, q35=None, q36=None, q37=None, q38=None, q39=None,
                        q40=None, q41=None, q42=None, q43=None, q44=None, q45=None, q46=None, q47=None, q48=None, q49=None,
                        q50=None, q51=None, q52=None, q53=None, q54=None, q55=None, q56=None, q57=None, q58=None, q59=None)
            ).save()

    # 最初の問題を取り出す
    first_question = scores.get_item(
                Key={"question_id": qz0}
            )['Item']['question']

    # クイズ開始のメッセージ
    greet_msg = "AWSにまつわる問題を用意しました。クイズを開始します。"
    print(greet_msg)

    greet_msg = TextSendMessage(
      text=greet_msg
    )

    # リプライトークンでFlexMessageを返信
    question_msg = FlexSendMessage(
        alt_text='First Question',
        contents=json.loads(first_question)
    )
    line_bot.reply_message(
        reply_token,
        [greet_msg, question_msg]
    )
    return {
        'statusCode': 200,
        'body': json.dumps('Init Success!')
    }
  elif event_type == 'unfollow':
      # ブロックされた時にはデータを削除する
      UserScore.get(user_id).delete()
      return {
          'statusCode': 200,
          'body': json.dumps('Delete Success!')
      }
  else:

    reply_token =  body['events'][0]['replyToken']
    # 2問目以降
    user_score = UserScore.get(user_id)

    # 入力チェック
    if message_text.isnumeric():

      # 問題に対するスコアを取得
      # ユーザスコアを更新
      # 正解 or 不正解を 返す
      result = update_score(user_score, message_text)

      print('Question: {}\nScore: {}'.format(
      result['inserted_question'], result['score']))

      msg_obj = result['msg']

      line_bot.reply_message(
          reply_token,
          msg_obj
      )

    else:
      print("数値を入力してください。")