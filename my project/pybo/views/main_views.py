from flask import Blueprint , render_template

from pybo.models import Question

# Blueprint: 라우팅 함수를 체계적으로 관리
bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    questions_list = Question.query.order_by(Question.create_date.desc()).all()

    return render_template('question/question_list.html', questions_list=questions_list)