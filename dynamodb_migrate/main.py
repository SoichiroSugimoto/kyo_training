import json
import random
from score_model import Score

if not Score.exists():
  Score.create_table(read_capacity_units=1,
                    write_capacity_units=1, wait=True)

with open('flex_messages.json', 'r',encoding="utf-8") as f:
    flex_messages = json.load(f)

# index = random.randrange(59)
# cnt = 0

# スコア情報を挿入する

Score(question_id='q0', question=json.dumps(flex_messages['q0']),
      answer='3', score=1).save()
Score(question_id='q1', question=json.dumps(flex_messages['q1']),
      answer='1', score=1).save()
Score(question_id='q2', question=json.dumps(flex_messages['q2']),
      answer='4', score=1).save()
Score(question_id='q3', question=json.dumps(flex_messages['q3']),
      answer='2', score=1).save()
Score(question_id='q4', question=json.dumps(flex_messages['q4']),
      answer='2', score=1).save()
Score(question_id='q5', question=json.dumps(flex_messages['q5']),
      answer='3', score=1).save()
Score(question_id='q6', question=json.dumps(flex_messages['q6']),
      answer='1', score=1).save()
Score(question_id='q7', question=json.dumps(flex_messages['q7']),
      answer='3', score=1).save()
Score(question_id='q8', question=json.dumps(flex_messages['q8']),
      answer='1', score=1).save()
Score(question_id='q9', question=json.dumps(flex_messages['q9']),
      answer='4', score=1).save()
Score(question_id='q10', question=json.dumps(flex_messages['q10']),
      answer='1', score=1).save()
Score(question_id='q11', question=json.dumps(flex_messages['q11']),
      answer='3', score=1).save()
Score(question_id='q12', question=json.dumps(flex_messages['q12']),
      answer='2', score=1).save()
Score(question_id='q13', question=json.dumps(flex_messages['q13']),
      answer='2', score=1).save()
Score(question_id='q14', question=json.dumps(flex_messages['q14']),
      answer='4', score=1).save()
Score(question_id='q15', question=json.dumps(flex_messages['q15']),
      answer='3', score=1).save()
Score(question_id='q16', question=json.dumps(flex_messages['q16']),
      answer='4', score=1).save()
Score(question_id='q17', question=json.dumps(flex_messages['q17']),
      answer='2', score=1).save()
Score(question_id='q18', question=json.dumps(flex_messages['q18']),
      answer='4', score=1).save()
Score(question_id='q19', question=json.dumps(flex_messages['q19']),
      answer='3', score=1).save()
Score(question_id='q20', question=json.dumps(flex_messages['q20']),
      answer='4', score=1).save()
Score(question_id='q21', question=json.dumps(flex_messages['q21']),
      answer='2', score=1).save()
Score(question_id='q22', question=json.dumps(flex_messages['q22']),
      answer='3', score=1).save()
Score(question_id='q23', question=json.dumps(flex_messages['q23']),
      answer='1', score=1).save()
Score(question_id='q24', question=json.dumps(flex_messages['q24']),
      answer='3', score=1).save()
Score(question_id='q25', question=json.dumps(flex_messages['q25']),
      answer='1', score=1).save()
Score(question_id='q26', question=json.dumps(flex_messages['q26']),
      answer='2', score=1).save()
Score(question_id='q27', question=json.dumps(flex_messages['q27']),
      answer='4', score=1).save()
Score(question_id='q28', question=json.dumps(flex_messages['q28']),
      answer='3', score=1).save()
Score(question_id='q29', question=json.dumps(flex_messages['q29']),
      answer='4', score=1).save()
Score(question_id='q30', question=json.dumps(flex_messages['q30']),
      answer='1', score=1).save()
Score(question_id='q31', question=json.dumps(flex_messages['q31']),
      answer='1', score=1).save()
Score(question_id='q32', question=json.dumps(flex_messages['q32']),
      answer='3', score=1).save()
Score(question_id='q33', question=json.dumps(flex_messages['q33']),
      answer='2', score=1).save()
Score(question_id='q34', question=json.dumps(flex_messages['q34']),
      answer='4', score=1).save()
Score(question_id='q35', question=json.dumps(flex_messages['q35']),
      answer='2', score=1).save()
Score(question_id='q36', question=json.dumps(flex_messages['q36']),
      answer='2', score=1).save()
Score(question_id='q37', question=json.dumps(flex_messages['q37']),
      answer='3', score=1).save()
Score(question_id='q38', question=json.dumps(flex_messages['q38']),
      answer='2', score=1).save()
Score(question_id='q39', question=json.dumps(flex_messages['q39']),
      answer='2', score=1).save()
Score(question_id='q40', question=json.dumps(flex_messages['q40']),
      answer='2', score=1).save()
Score(question_id='q41', question=json.dumps(flex_messages['q41']),
      answer='3', score=1).save()
Score(question_id='q42', question=json.dumps(flex_messages['q42']),
      answer='1', score=1).save()
Score(question_id='q43', question=json.dumps(flex_messages['q43']),
      answer='1', score=1).save()
Score(question_id='q44', question=json.dumps(flex_messages['q44']),
      answer='2', score=1).save()
Score(question_id='q45', question=json.dumps(flex_messages['q45']),
      answer='3', score=1).save()
Score(question_id='q46', question=json.dumps(flex_messages['q46']),
      answer='1', score=1).save()
Score(question_id='q47', question=json.dumps(flex_messages['q47']),
      answer='4', score=1).save()
Score(question_id='q48', question=json.dumps(flex_messages['q48']),
      answer='4', score=1).save()
Score(question_id='q49', question=json.dumps(flex_messages['q49']),
      answer='4', score=1).save()
Score(question_id='q50', question=json.dumps(flex_messages['q50']),
      answer='1', score=1).save()
Score(question_id='q51', question=json.dumps(flex_messages['q51']),
      answer='2', score=1).save()
Score(question_id='q52', question=json.dumps(flex_messages['q52']),
      answer='3', score=1).save()
Score(question_id='q53', question=json.dumps(flex_messages['q53']),
      answer='4', score=1).save()
Score(question_id='q54', question=json.dumps(flex_messages['q54']),
      answer='3', score=1).save()
Score(question_id='q55', question=json.dumps(flex_messages['q55']),
      answer='2', score=1).save()
Score(question_id='q56', question=json.dumps(flex_messages['q56']),
      answer='1', score=1).save()
Score(question_id='q57', question=json.dumps(flex_messages['q57']),
      answer='2', score=1).save()
Score(question_id='q58', question=json.dumps(flex_messages['q58']),
      answer='3', score=1).save()
Score(question_id='q59', question=json.dumps(flex_messages['q59']),
      answer='4', score=1).save()

print('Done!')
